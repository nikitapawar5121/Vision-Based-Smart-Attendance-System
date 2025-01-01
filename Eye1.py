import cv2
import os
import sqlite3
from datetime import datetime
from skimage.metrics import structural_similarity as ssim
import numpy as np
import time

# Create database and tables for storing attendance and student data
def initialize_database():
    try:
        conn = sqlite3.connect("student_records.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                roll_no TEXT NOT NULL UNIQUE,
                image_path TEXT NOT NULL
            )"""
        )
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS attendance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_name TEXT NOT NULL,
                roll_no TEXT NOT NULL,
                date TEXT NOT NULL,
                status TEXT NOT NULL
            )"""
        )
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        conn.close()

# Save student data to the database
def add_student_to_database(name, roll_no, image_path):
    try:
        conn = sqlite3.connect("student_records.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, roll_no, image_path) VALUES (?, ?, ?)", (name, roll_no, image_path))
        conn.commit()
        print(f"Student {name} (Roll No: {roll_no}) registered successfully.")
    except sqlite3.IntegrityError:
        print(f"Error: A student with Roll No {roll_no} is already registered.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        conn.close()

# Mark attendance in the database
def mark_attendance(student_name, roll_no, status):
    try:
        conn = sqlite3.connect("student_records.db")
        cursor = conn.cursor()
        date = datetime.now().strftime("%Y-%m-%d")
        cursor.execute("INSERT INTO attendance (student_name, roll_no, date, status) VALUES (?, ?, ?, ?)", (student_name, roll_no, date, status))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        conn.close()

# Capture an eye image using the webcam with a 3-second countdown
def capture_eye_image(filename):
    try:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            raise RuntimeError("Failed to open webcam.")
        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
        
        print("Starting eye capture... Please stay still.")
        for i in range(3, 0, -1):  # Countdown
            print(f"Capturing in {i}...")
            time.sleep(1)
        
        ret, frame = cap.read()
        if not ret:
            raise RuntimeError("Failed to capture frame from webcam.")
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
        if len(eyes) > 0:
            x, y, w, h = eyes[0]
            eye_region = gray[y:y + h, x:x + w]
            cv2.imwrite(filename, eye_region)
            print(f"Eye image saved as {filename}.")
        else:
            print("No eye detected. Please try again.")
    except Exception as e:
        print(f"Error capturing eye image: {e}")
    finally:
        cap.release()

# Compare two images using SSIM
def compare_images(img1_path, img2_path):
    try:
        img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)
        if img1 is None or img2 is None:
            raise FileNotFoundError(f"One or both images not found: {img1_path}, {img2_path}")
        img1 = cv2.resize(img1, (100, 100))
        img2 = cv2.resize(img2, (100, 100))
        score, _ = ssim(img1, img2, full=True)
        return score
    except FileNotFoundError as e:
        print(e)
        return 0
    except Exception as e:
        print(f"Error comparing images: {e}")
        return 0

# Main Attendance System
def attendance_system():
    initialize_database()
    while True:
        try:
            print("\nWelcome to Vision-Based Attendance System.")
            print("1. Register Student")
            print("2. Mark Attendance")
            print("3. Exit")
            choice = input("Enter your choice (1/2/3): ")
            
            if choice == "1":
                name = input("Enter student name: ")
                roll_no = input("Enter student roll number: ")
                filename = f"images/{roll_no}.jpg"
                os.makedirs("images", exist_ok=True)
                capture_eye_image(filename)
                add_student_to_database(name, roll_no, filename)
            
            elif choice == "2":
                filename = "temp_eye.jpg"
                capture_eye_image(filename)
                conn = sqlite3.connect("student_records.db")
                cursor = conn.cursor()
                cursor.execute("SELECT name, roll_no, image_path FROM students")
                students = cursor.fetchall()
                conn.close()
                
                matched = False
                for student_name, roll_no, image_path in students:
                    similarity = compare_images(filename, image_path)
                    if similarity > 0.8:  # Threshold for matching
                        print(f"Attendance marked for {student_name} (Roll No: {roll_no}).")
                        mark_attendance(student_name, roll_no, "Present")
                        matched = True
                        break
                
                if not matched:
                    print("No match found. Student not registered.")
                    mark_attendance("Unknown", "Unknown", "Absent")
                os.remove(filename)
            
            elif choice == "3":
                print("Exiting the system. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    attendance_system()