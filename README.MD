# Vision-Based Smart Attendance System

## Introduction
The Vision-Based Smart Attendance System is an innovative and efficient solution for managing student attendance using computer vision and database integration. This project uses eye image detection and comparison techniques to register students and mark their attendance. It eliminates manual processes and enhances reliability and accuracy in attendance tracking.

## Features
- *Student Registration*: Captures and stores student details with an eye image in the database.
- *Attendance Marking*: Identifies students by comparing real-time and stored eye images using SSIM.
- *Database Integration*: Maintains records of students and their attendance securely in SQLite.
- *Real-Time Image Capture*: Uses a webcam for on-the-spot eye image detection.
- *Error Handling*: Robust exception handling for smooth operation and error recovery.
- *Console-Based Interface*: Easy-to-use text-based menu for user interactions.
- *Automated Logging*: Tracks and updates attendance with timestamps automatically.

## Applications
- *Educational Institutions*: For tracking student attendance in classrooms or during exams.
- *Corporate Environments*: For managing employee attendance and office entry/exit logs.
- *Events*: For checking in participants at conferences, seminars, and other events.

## Team Members
1. Pawar Nikita Rajendra
2. Telore Maheshwari Shivaji
3. Pawar Rohan Sunil
4. Deshmukh Rohan Ravindra

## Project Phases
1. *Requirement Gathering & Analysis*  
   Focuses on understanding user needs and defining both functional and non-functional requirements. This helps set a clear direction for the project.

2. *System Design*  
   The system architecture, user interface, database schema, and algorithm design are developed to ensure the entire system structure is planned before implementation.

3. *Hardware and Software Setup*  
   Necessary equipment (such as cameras) is configured, and software libraries for image processing and recognition are installed.

4. *Eye Detection and Recognition Model Development*  
   Eye detection is implemented using models like Haar Cascades or MTCNN, and recognition is built using deep learning techniques.

5. *Integration and Development of Attendance Management*  
   The eye recognition system is integrated with the attendance logging mechanism, and the user interface is created for admin use.

6. *Testing*  
   Rigorous testing, including unit testing, integration testing, load testing, and user acceptance testing, ensures reliability, performance, and usability.

## Requirements

### Hardware Requirements
- *Camera*: High-resolution camera for real-time image capture.
- *System*: A computer or server with adequate processing power (e.g., Intel i5 or higher) to run image processing and recognition algorithms.
- *Storage*: Minimum 500 GB for storing attendance logs and images.

### Software Requirements
- *Operating System*: Windows, macOS, or Linux (Ubuntu preferred).
- *Programming Language*: Python 3.8 or higher.
- *Libraries and Frameworks*:
  - OpenCV: For image processing.
  - Dlib: For eye detection and feature extraction.
  - NumPy: For numerical computations.
  - Scikit-image: For advanced image preprocessing and analysis.
- *Database*: SQLite3 for storing attendance logs and user data.

## Steps to Run the Program
1. *Clone the Repository*  
   Download or clone the project repository:
   ```bash
   git clone <https://github.com/nikitapawar5121/Vision-Based-Smart-Attendance-System.git>
   cd Vision-Based-Smart-Attendance-System
2. Install Required Libraries
•	Ensure Python is installed on your system, then install the required libraries:
pip install -r requirements.txt

3. Configure the Database
•	Set up the SQLite3 database:
o	Ensure the attendance.db file exists or create it.
o	Use the following SQL commands to initialize the tables (if needed):
CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT,    eye_encoding BLOB);
CREATE TABLE attendance (id INTEGER PRIMARY KEY, user_id INTEGER,   timestamp TEXT);
4. Add EYE Data
•	Run the script to register users by capturing their eye data:
      python add_user.py
5. Run the Program
•	Start the attendance system:
python main.py
6. View Attendance Records
•	Use the admin panel (if available) or directly query the database:
sqlite3 attendance.db
SELECT * FROM attendance
7. Stop the Program
•	Press Ctrl + C in the terminal to stop the system.


# Attendance Management System - Future Scope

## IoT Integration

- **Multi-factor Attendance Verification**:  
  - Combine the system with IoT devices such as RFID tags or smart cards for multi-factor attendance verification.
  - Use smart devices to automatically detect if the student is present within the classroom vicinity.

## Mobile App for Attendance Management

- **Real-Time Attendance View**:  
  - Develop a mobile application that allows teachers and administrators to view attendance records in real time.
  
- **Report Generation**:  
  - Teachers and administrators can generate attendance reports directly from the mobile app.
# Attendance Management System - Future Scope

This project aims to improve attendance management through innovative features like IoT integration, a mobile app for real-time attendance tracking, and a robust database management system. Below are the key components of the future scope of the system.

## IoT Integration

- **Multi-factor Attendance Verification**:  
  - Combine the system with IoT devices such as RFID tags or smart cards for multi-factor attendance verification.
  - Use smart devices to automatically detect if the student is present within the classroom vicinity.

## Mobile App for Attendance Management

- **Real-Time Attendance View**:  
  - Develop a mobile application that allows teachers and administrators to view attendance records in real time.
  
- **Report Generation**:  
  - Teachers and administrators can generate attendance reports directly from the mobile app.

- **Attendance Pattern Notifications**:  
  - Get notifications for irregular attendance patterns, helping administrators track and manage attendance more efficiently.

## Database Management

- **Time Management in Database**:  
  - Implement a time management feature in the SQLite database, recording timestamps of student attendance in a table format.

## Technologies Used

- **IoT Devices**: RFID Tags, Smart Cards
- **Mobile Application**: Android/iOS (for future integration)
- **Database**: SQLite

## Future Goals

- Extend the system with more IoT devices.
- Build and deploy the mobile app for real-time tracking and reporting.
- Optimize the database structure for scalability and efficiency.

Feel free to contribute, report bugs, or suggest improvements!


## Database Management

- **Time Management in Database**:  
  - Implement a time management feature in the SQLite database, recording timestamps of student attendance in a table format.

## Technologies Used

- **IoT Devices**: RFID Tags, Smart Cards
- **Mobile Application**: Android/iOS (for future integration)
- **Database**: SQLite

## Future Goals

- Extend the system with more IoT devices.
- Build and deploy the mobile app for real-time tracking and reporting.
- Optimize the database structure for scalability and efficiency.

Feel free to contribute, report bugs, or suggest improvements!




