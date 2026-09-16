"""
=============================================================================
NIET SMART UNIVERSITY ERP PLATFORM - DATA STORE (MOCK DATABASE LAYER)
Course: Operating Systems (CCSE0353A) | Faculty: Mr. Praveen Kr Tomar
Team 52: Krish Kumar, Ashutosh Kumar, Govind Kumar, Suman Kumar, Preety Kumari
=============================================================================

[EXPLAINABILITY FOR VIVA / TEACHER]:
Yeh file hamara "Data Layer" (Database Simulation) hai.
Abhi humne isse clean Python Dictionaries aur Lists mein banaya hai taaki:
1. Code samajhna aur viva mein explain karna sabse easy ho.
2. Jab hum baad mein MySQL ya SQLite se connect karenge, toh sirf is file ke
   functions ke andar SQL queries (e.g. SELECT, INSERT, UPDATE) likhni padengi.
   Frontend aur routes ko touch bhi nahi karna padega!
=============================================================================
"""

import datetime

# -----------------------------------------------------------------------------
# 1. STUDENTS DATA (Pre-loaded with Team Members & Sample Records)
# -----------------------------------------------------------------------------
STUDENTS = {
    "0261dcsa007": {
        "roll_no": "0261dcsa007",
        "name": "Ashutosh Jitendra Singh",
        "email": "ashutosh.singh@niet.co.in",
        "password": "student123",
        "branch": "B.Tech CSE (AI)",
        "semester": 3,
        "section": "C",
        "academic_year": "2026-2027",
        "overall_attendance": 86.5,
        "cgpa": 8.92,
        "fee_status": "Paid",
        "fee_amount": 82500,
        "fee_paid": 82500,
        "transaction_id": "NIET2026TXN98124",
        "role_in_project": "Security & Reliability Specialist",
        "subjects": [
            {"code": "CCSE0353A", "name": "Operating Systems", "faculty": "Mr. Praveen Kr Tomar", "attended": 28, "total": 30, "sessional_1": 28, "sessional_2": 29},
            {"code": "CCSE0301A", "name": "Data Structures & Algorithms", "faculty": "Dr. Rajesh Sharma", "attended": 26, "total": 30, "sessional_1": 27, "sessional_2": 28},
            {"code": "CCSE0302A", "name": "Database Management Systems", "faculty": "Prof. Neha Gupta", "attended": 25, "total": 30, "sessional_1": 26, "sessional_2": 27},
            {"code": "CCSE0304A", "name": "Artificial Intelligence Foundations", "faculty": "Dr. Amit Verma", "attended": 27, "total": 30, "sessional_1": 29, "sessional_2": 29},
            {"code": "CCSE0305A", "name": "Computer Organization & Architecture", "faculty": "Prof. Sanjay Singh", "attended": 24, "total": 30, "sessional_1": 25, "sessional_2": 26}
        ],
        "library_issued": [
            {"title": "Operating System Concepts (Silberschatz)", "issue_date": "2026-08-15", "due_date": "2026-09-25", "fine": 0},
            {"title": "Artificial Intelligence: A Modern Approach", "issue_date": "2026-08-20", "due_date": "2026-09-30", "fine": 0}
        ]
    },
    "0261dscai010": {
        "roll_no": "0261dscai010",
        "name": "Krish Kumar",
        "email": "krish.kumar@niet.co.in",
        "password": "student123",
        "branch": "B.Tech CSE (AI)",
        "semester": 3,
        "section": "C",
        "academic_year": "2026-2027",
        "overall_attendance": 91.2,
        "cgpa": 9.15,
        "fee_status": "Paid",
        "fee_amount": 82500,
        "fee_paid": 82500,
        "transaction_id": "NIET2026TXN98112",
        "role_in_project": "Team Leader & System Analyst",
        "subjects": [
            {"code": "CCSE0353A", "name": "Operating Systems", "faculty": "Mr. Praveen Kr Tomar", "attended": 29, "total": 30, "sessional_1": 29, "sessional_2": 30},
            {"code": "CCSE0301A", "name": "Data Structures & Algorithms", "faculty": "Dr. Rajesh Sharma", "attended": 28, "total": 30, "sessional_1": 28, "sessional_2": 29},
            {"code": "CCSE0302A", "name": "Database Management Systems", "faculty": "Prof. Neha Gupta", "attended": 27, "total": 30, "sessional_1": 28, "sessional_2": 28},
            {"code": "CCSE0304A", "name": "Artificial Intelligence Foundations", "faculty": "Dr. Amit Verma", "attended": 28, "total": 30, "sessional_1": 30, "sessional_2": 29},
            {"code": "CCSE0305A", "name": "Computer Organization & Architecture", "faculty": "Prof. Sanjay Singh", "attended": 25, "total": 30, "sessional_1": 27, "sessional_2": 28}
        ],
        "library_issued": [
            {"title": "Modern Operating Systems (Tanenbaum)", "issue_date": "2026-08-10", "due_date": "2026-09-20", "fine": 0}
        ]
    },
    "0261dcsai003": {
        "roll_no": "0261dcsai003",
        "name": "Govind Kumar",
        "email": "govind.kumar@niet.co.in",
        "password": "student123",
        "branch": "B.Tech CSE (AI)",
        "semester": 3,
        "section": "C",
        "academic_year": "2026-2027",
        "overall_attendance": 78.4,
        "cgpa": 8.40,
        "fee_status": "Paid",
        "fee_amount": 82500,
        "fee_paid": 82500,
        "transaction_id": "NIET2026TXN98135",
        "role_in_project": "Modern OS & Documentation Specialist",
        "subjects": [
            {"code": "CCSE0353A", "name": "Operating Systems", "faculty": "Mr. Praveen Kr Tomar", "attended": 24, "total": 30, "sessional_1": 25, "sessional_2": 26},
            {"code": "CCSE0301A", "name": "Data Structures & Algorithms", "faculty": "Dr. Rajesh Sharma", "attended": 23, "total": 30, "sessional_1": 24, "sessional_2": 25},
            {"code": "CCSE0302A", "name": "Database Management Systems", "faculty": "Prof. Neha Gupta", "attended": 24, "total": 30, "sessional_1": 25, "sessional_2": 25},
            {"code": "CCSE0304A", "name": "Artificial Intelligence Foundations", "faculty": "Dr. Amit Verma", "attended": 25, "total": 30, "sessional_1": 26, "sessional_2": 27},
            {"code": "CCSE0305A", "name": "Computer Organization & Architecture", "faculty": "Prof. Sanjay Singh", "attended": 22, "total": 30, "sessional_1": 23, "sessional_2": 24}
        ],
        "library_issued": [
            {"title": "Linux Kernel Development (Robert Love)", "issue_date": "2026-08-18", "due_date": "2026-09-28", "fine": 0}
        ]
    },
    "0261dcsai012": {
        "roll_no": "0261dcsai012",
        "name": "Suman Kumar Gorain",
        "email": "suman.gorain@niet.co.in",
        "password": "student123",
        "branch": "B.Tech CSE (AI)",
        "semester": 3,
        "section": "C",
        "academic_year": "2026-2027",
        "overall_attendance": 72.0,  # Below 75% for Shortage Alert Demonstration!
        "cgpa": 7.85,
        "fee_status": "Due",
        "fee_amount": 82500,
        "fee_paid": 50000,
        "transaction_id": "NIET2026TXN98150",
        "role_in_project": "Performance & Optimization Specialist",
        "subjects": [
            {"code": "CCSE0353A", "name": "Operating Systems", "faculty": "Mr. Praveen Kr Tomar", "attended": 21, "total": 30, "sessional_1": 23, "sessional_2": 24},
            {"code": "CCSE0301A", "name": "Data Structures & Algorithms", "faculty": "Dr. Rajesh Sharma", "attended": 22, "total": 30, "sessional_1": 22, "sessional_2": 23},
            {"code": "CCSE0302A", "name": "Database Management Systems", "faculty": "Prof. Neha Gupta", "attended": 21, "total": 30, "sessional_1": 23, "sessional_2": 24},
            {"code": "CCSE0304A", "name": "Artificial Intelligence Foundations", "faculty": "Dr. Amit Verma", "attended": 23, "total": 30, "sessional_1": 25, "sessional_2": 25},
            {"code": "CCSE0305A", "name": "Computer Organization & Architecture", "faculty": "Prof. Sanjay Singh", "attended": 21, "total": 30, "sessional_1": 22, "sessional_2": 23}
        ],
        "library_issued": []
    },
    "0261dcsai011": {
        "roll_no": "0261dcsai011",
        "name": "Preety Kumari",
        "email": "preety.kumari@niet.co.in",
        "password": "student123",
        "branch": "B.Tech CSE (AI)",
        "semester": 3,
        "section": "C",
        "academic_year": "2026-2027",
        "overall_attendance": 88.0,
        "cgpa": 8.70,
        "fee_status": "Paid",
        "fee_amount": 82500,
        "fee_paid": 82500,
        "transaction_id": "NIET2026TXN98177",
        "role_in_project": "Linux & Scheduling Specialist",
        "subjects": [
            {"code": "CCSE0353A", "name": "Operating Systems", "faculty": "Mr. Praveen Kr Tomar", "attended": 27, "total": 30, "sessional_1": 28, "sessional_2": 29},
            {"code": "CCSE0301A", "name": "Data Structures & Algorithms", "faculty": "Dr. Rajesh Sharma", "attended": 26, "total": 30, "sessional_1": 27, "sessional_2": 27},
            {"code": "CCSE0302A", "name": "Database Management Systems", "faculty": "Prof. Neha Gupta", "attended": 26, "total": 30, "sessional_1": 27, "sessional_2": 28},
            {"code": "CCSE0304A", "name": "Artificial Intelligence Foundations", "faculty": "Dr. Amit Verma", "attended": 27, "total": 30, "sessional_1": 28, "sessional_2": 29},
            {"code": "CCSE0305A", "name": "Computer Organization & Architecture", "faculty": "Prof. Sanjay Singh", "attended": 26, "total": 30, "sessional_1": 26, "sessional_2": 27}
        ],
        "library_issued": [
            {"title": "Operating Systems: Three Easy Pieces (Arpaci-Dusseau)", "issue_date": "2026-08-25", "due_date": "2026-09-30", "fine": 0}
        ]
    }
}

# -----------------------------------------------------------------------------
# 2. FACULTY DATA
# -----------------------------------------------------------------------------
FACULTY = {
    "faculty": {
        "username": "faculty",
        "name": "Mr. Praveen Kr Tomar",
        "designation": "Assistant Professor & Course Coordinator",
        "department": "Artificial Intelligence & CSE",
        "subject_assigned": "Operating Systems (CCSE0353A)",
        "email": "praveen.tomar@niet.co.in",
        "password": "fac123",
        "sections": ["Batch C", "Batch D"],
        "schedule": [
            {"day": "Monday", "time": "09:30 AM - 10:30 AM", "room": "Block B - Room 302", "subject": "Operating Systems Lecture"},
            {"day": "Tuesday", "time": "11:30 AM - 01:30 PM", "room": "OS Lab - Lab 5", "subject": "Linux / Shell Programming Lab"},
            {"day": "Wednesday", "time": "02:00 PM - 03:00 PM", "room": "Block B - Room 302", "subject": "Operating Systems Lecture"},
            {"day": "Friday", "time": "10:30 AM - 11:30 AM", "room": "Block B - Room 302", "subject": "Process Scheduling Tutorial"}
        ]
    }
}

# -----------------------------------------------------------------------------
# 3. ADMIN DATA
# -----------------------------------------------------------------------------
ADMIN = {
    "username": "admin",
    "name": "Prof. Director Academics",
    "email": "admin.erp@niet.co.in",
    "password": "admin123",
    "role": "Super Admin"
}

# -----------------------------------------------------------------------------
# 4. CAMPUS NOTICES & CIRCULARS
# -----------------------------------------------------------------------------
NOTICES = [
    {
        "id": 1,
        "title": "Operating Systems Capstone Project Review-1 Schedule (CCSE0353A)",
        "category": "Academic",
        "date": "2026-09-17",
        "pinned": True,
        "content": "All Group 52 students are hereby informed that PBL Review-1 will be held in OS Lab. Topics: Process Scheduling, Synchronization, Memory Management, and ERP demo."
    },
    {
        "id": 2,
        "title": "Mandatory 75% Attendance Requirement for Sessional & University Exams",
        "category": "Important",
        "date": "2026-09-15",
        "pinned": True,
        "content": "As per AKTU and NIET Autonomous guidelines, students with attendance below 75% will be debarred from appearing in Sessional-2 and End Semester examinations."
    },
    {
        "id": 3,
        "title": "Central Library Extended Timings for Mid-Term Preparation",
        "category": "Library",
        "date": "2026-09-12",
        "pinned": False,
        "content": "NIET Central Library will remain open till 9:00 PM on all working days to assist students in preparing for mid-term tests and research projects."
    },
    {
        "id": 4,
        "title": "Hackathon 2026 Internal Hackathon Registrations Open",
        "category": "Events",
        "date": "2026-09-10",
        "pinned": False,
        "content": "Teams interested in presenting AI, OS, or Web Development solutions are invited to register at the Innovation Cell before 25th September."
    }
]

# -----------------------------------------------------------------------------
# 5. STUDENT SERVICE REQUESTS (Mapped to OS Scheduling Queue)
# -----------------------------------------------------------------------------
STUDENT_REQUESTS = [
    {
        "id": "REQ-101",
        "roll_no": "0261dcsa007",
        "student_name": "Ashutosh Jitendra Singh",
        "request_type": "Bonafide Certificate",
        "reason": "Required for National Scholarship Application",
        "status": "Pending",
        "timestamp": "2026-09-16 10:15 AM",
        "os_burst_time": 4  # Simulated CPU burst time for processing in OS queue
    },
    {
        "id": "REQ-102",
        "roll_no": "0261dcsai012",
        "student_name": "Suman Kumar Gorain",
        "request_type": "Medical Leave Approval",
        "reason": "Suffering from Viral Fever for 3 days",
        "status": "Approved",
        "timestamp": "2026-09-15 02:40 PM",
        "os_burst_time": 6
    },
    {
        "id": "REQ-103",
        "roll_no": "0261dscai010",
        "student_name": "Krish Kumar",
        "request_type": "Library Card Re-Issue",
        "reason": "Lost previous card during college fest",
        "status": "Approved",
        "timestamp": "2026-09-14 11:30 AM",
        "os_burst_time": 2
    },
    {
        "id": "REQ-104",
        "roll_no": "0261dcsai011",
        "student_name": "Preety Kumari",
        "request_type": "Railway Concession Form",
        "reason": "Travel to hometown during semester break",
        "status": "Pending",
        "timestamp": "2026-09-16 04:20 PM",
        "os_burst_time": 5
    }
]

# -----------------------------------------------------------------------------
# 6. CENTRAL LIBRARY CATALOG
# -----------------------------------------------------------------------------
LIBRARY_BOOKS = [
    {"isbn": "978-0133591620", "title": "Operating System Concepts", "author": "Silberschatz, Galvin, Gagne", "copies_total": 20, "copies_available": 14, "shelf": "Rack OS-01"},
    {"isbn": "978-0130340740", "title": "Modern Operating Systems", "author": "Andrew S. Tanenbaum", "copies_total": 15, "copies_available": 8, "shelf": "Rack OS-02"},
    {"isbn": "978-0136042594", "title": "Artificial Intelligence: A Modern Approach", "author": "Stuart Russell, Peter Norvig", "copies_total": 25, "copies_available": 18, "shelf": "Rack AI-04"},
    {"isbn": "978-0262033848", "title": "Introduction to Algorithms (CLRS)", "author": "Cormen, Leiserson, Rivest, Stein", "copies_total": 30, "copies_available": 12, "shelf": "Rack CS-09"},
    {"isbn": "978-0072465631", "title": "Database System Concepts", "author": "Korth, Sudarshan", "copies_total": 18, "copies_available": 11, "shelf": "Rack DB-03"}
]

# -----------------------------------------------------------------------------
# 7. TIME TABLE (SECTION C - 3rd SEM B.TECH CSE-AI)
# -----------------------------------------------------------------------------
TIMETABLE = [
    {"day": "Monday", "p1": "OS (CCSE0353A)", "p2": "DSA (CCSE0301A)", "p3": "DBMS (CCSE0302A)", "p4": "Lunch", "p5": "AI Foundations", "p6": "COA"},
    {"day": "Tuesday", "p1": "DSA (CCSE0301A)", "p2": "DBMS (CCSE0302A)", "p3": "OS Lab (Lab 5)", "p4": "Lunch", "p5": "OS Lab (Lab 5)", "p6": "AI Tutorial"},
    {"day": "Wednesday", "p1": "OS (CCSE0353A)", "p2": "COA", "p3": "AI Foundations", "p4": "Lunch", "p5": "DBMS Lab (Lab 4)", "p6": "DBMS Lab (Lab 4)"},
    {"day": "Thursday", "p1": "AI Foundations", "p2": "DSA Lab (Lab 2)", "p3": "DSA Lab (Lab 2)", "p4": "Lunch", "p5": "OS Tutorial", "p6": "Soft Skills"},
    {"day": "Friday", "p1": "COA", "p2": "OS (CCSE0353A)", "p3": "DSA (CCSE0301A)", "p4": "Lunch", "p5": "Mini Project PBL", "p6": "Mini Project PBL"}
]


# =============================================================================
# DATA ACCESS FUNCTIONS (EASY TO CONNECT TO SQL/DBMS LATER)
# =============================================================================

def get_student(roll_no):
    """Retrieve single student by roll number."""
    return STUDENTS.get(roll_no.strip())

def get_all_students():
    """Retrieve list of all students."""
    return list(STUDENTS.values())

def add_student(data):
    """
    Add a new student to the system.
    Later in DBMS: `INSERT INTO students (roll_no, name, ...) VALUES (...)`
    """
    roll = data.get("roll_no", "").strip()
    if not roll or roll in STUDENTS:
        return False, "Roll number already exists or is empty!"
    
    STUDENTS[roll] = {
        "roll_no": roll,
        "name": data.get("name", "Student"),
        "email": data.get("email", f"{roll}@niet.co.in"),
        "password": data.get("password", "student123"),
        "branch": data.get("branch", "B.Tech CSE (AI)"),
        "semester": int(data.get("semester", 3)),
        "section": data.get("section", "C"),
        "academic_year": "2026-2027",
        "overall_attendance": float(data.get("attendance", 85.0)),
        "cgpa": float(data.get("cgpa", 8.0)),
        "fee_status": data.get("fee_status", "Paid"),
        "fee_amount": 82500,
        "fee_paid": 82500 if data.get("fee_status") == "Paid" else 40000,
        "transaction_id": f"NIET2026TXN{len(STUDENTS)+100}",
        "role_in_project": data.get("role_in_project", "Student Scholar"),
        "subjects": [
            {"code": "CCSE0353A", "name": "Operating Systems", "faculty": "Mr. Praveen Kr Tomar", "attended": 25, "total": 30, "sessional_1": 25, "sessional_2": 26},
            {"code": "CCSE0301A", "name": "Data Structures & Algorithms", "faculty": "Dr. Rajesh Sharma", "attended": 24, "total": 30, "sessional_1": 25, "sessional_2": 25}
        ],
        "library_issued": []
    }
    return True, "Student added successfully!"

def delete_student(roll_no):
    """
    Delete a student from records.
    Later in DBMS: `DELETE FROM students WHERE roll_no = %s`
    """
    if roll_no in STUDENTS:
        del STUDENTS[roll_no]
        return True, "Student deleted successfully!"
    return False, "Student not found!"

def mark_attendance(roll_no, status):
    """
    Toggle or update attendance for student.
    status: 'Present' or 'Absent'
    """
    student = STUDENTS.get(roll_no)
    if not student:
        return False, "Student not found"
    
    # Update OS subject attendance as a demo
    for subj in student["subjects"]:
        if subj["code"] == "CCSE0353A":
            subj["total"] += 1
            if status == "Present":
                subj["attended"] += 1
            # Recalculate overall
            total_classes = sum(s["total"] for s in student["subjects"])
            total_attended = sum(s["attended"] for s in student["subjects"])
            student["overall_attendance"] = round((total_attended / total_classes) * 100, 1)
            break
    return True, f"Attendance marked {status} for {student['name']}"

def update_marks(roll_no, subject_code, sessional_1, sessional_2):
    """Update sessional marks for student."""
    student = STUDENTS.get(roll_no)
    if not student:
        return False, "Student not found"
    for subj in student["subjects"]:
        if subj["code"] == subject_code:
            subj["sessional_1"] = int(sessional_1)
            subj["sessional_2"] = int(sessional_2)
            return True, f"Marks updated for {student['name']}"
    return False, "Subject not found"

def get_notices():
    """Get all notices (pinned first)."""
    return sorted(NOTICES, key=lambda x: not x["pinned"])

def add_notice(title, category, content):
    """Add a new campus notice."""
    new_id = len(NOTICES) + 1
    today = datetime.date.today().strftime("%Y-%m-%d")
    NOTICES.insert(0, {
        "id": new_id,
        "title": title,
        "category": category,
        "date": today,
        "pinned": False,
        "content": content
    })
    return True, "Notice published successfully!"

def get_student_requests():
    """Get all service requests."""
    return STUDENT_REQUESTS

def add_student_request(roll_no, student_name, request_type, reason):
    """Submit a student service request."""
    req_id = f"REQ-{len(STUDENT_REQUESTS) + 101}"
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
    import random
    burst = random.randint(2, 8)
    STUDENT_REQUESTS.insert(0, {
        "id": req_id,
        "roll_no": roll_no,
        "student_name": student_name,
        "request_type": request_type,
        "reason": reason,
        "status": "Pending",
        "timestamp": now_str,
        "os_burst_time": burst
    })
    return True, f"Application {req_id} submitted successfully for administrative approval."

def update_request_status(req_id, new_status):
    """Approve or reject a request."""
    for req in STUDENT_REQUESTS:
        if req["id"] == req_id:
            req["status"] = new_status
            return True, f"Request {req_id} updated to {new_status}"
    return False, "Request not found"

def get_system_stats():
    """Overall statistics for the Admin Dashboard."""
    total_students = len(STUDENTS)
    avg_att = round(sum(s["overall_attendance"] for s in STUDENTS.values()) / max(total_students, 1), 1)
    shortage_count = sum(1 for s in STUDENTS.values() if s["overall_attendance"] < 75.0)
    pending_fees = sum(1 for s in STUDENTS.values() if s["fee_status"] != "Paid")
    pending_requests = sum(1 for s in STUDENT_REQUESTS if s["status"] == "Pending")
    
    return {
        "total_students": total_students,
        "avg_attendance": avg_att,
        "attendance_shortage_count": shortage_count,
        "pending_fees_count": pending_fees,
        "pending_requests_count": pending_requests,
        "total_notices": len(NOTICES),
        "total_faculty": len(FACULTY)
    }
