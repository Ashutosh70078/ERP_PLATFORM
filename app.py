"""
=============================================================================
NIET SMART UNIVERSITY ERP PLATFORM - MAIN CONTROLLER (app.py)
Course: Operating Systems (CCSE0353A) | Faculty: Mr. Praveen Kr Tomar
Team 52: Krish Kumar, Ashutosh Kumar, Govind Kumar, Suman Kumar, Preety Kumari
=============================================================================

[EXPLAINABILITY FOR VIVA / PRESENTATION]:
Yeh Flask application hamara main server controller hai:
1. Har URL route ke liye ek clear function likha hai (e.g. @app.route('/login'))
2. Sessions ka use kiya hai user authentication aur role-based security ke liye.
3. Templates render karte waqt data_store.py aur os_simulator.py se data pass kiya hai.
4. Hosting ke liye os.environ.get("PORT", 5000) use kiya hai taaki Render/Railway par chal sake.
=============================================================================
"""

import os
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import data_store
import os_simulator

app = Flask(__name__)
# Secret key for session management & security
app.secret_key = os.environ.get("SECRET_KEY", "niet_smart_erp_secret_key_2026_group52")


# -----------------------------------------------------------------------------
# HELPER FUNCTIONS (AUTHENTICATION & ACCESS CONTROL)
# -----------------------------------------------------------------------------
def is_logged_in():
    return "user" in session

def get_current_user():
    return session.get("user")

def get_current_role():
    return session.get("role")


# -----------------------------------------------------------------------------
# ROUTE 1: HOME LANDING PAGE
# -----------------------------------------------------------------------------
@app.route("/")
def index():
    """
    Public landing page showing NIET institutional details,
    PBL project info (Group 52, Faculty: Mr. Praveen Kr Tomar),
    and quick login access cards.
    """
    notices = data_store.get_notices()[:3]
    stats = data_store.get_system_stats()
    return render_template("index.html", notices=notices, stats=stats)


# -----------------------------------------------------------------------------
# ROUTE 2: LOGIN (ROLE-BASED AUTHENTICATION)
# -----------------------------------------------------------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Handles user login for all three roles:
    1. Admin (admin / admin123)
    2. Faculty (faculty / fac123)
    3. Student (0261dcsa007 / student123)
    """
    if request.method == "POST":
        role = request.form.get("role")
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        # Check Admin Login
        if role == "admin":
            if username == data_store.ADMIN["username"] and password == data_store.ADMIN["password"]:
                session["user"] = data_store.ADMIN["name"]
                session["username"] = data_store.ADMIN["username"]
                session["role"] = "admin"
                flash("Welcome to NIET Admin Portal!", "success")
                return redirect(url_for("admin_dashboard"))
            else:
                flash("Invalid Admin username or password!", "danger")

        # Check Faculty Login
        elif role == "faculty":
            fac = data_store.FACULTY.get(username)
            if fac and fac["password"] == password:
                session["user"] = fac["name"]
                session["username"] = fac["username"]
                session["role"] = "faculty"
                flash(f"Welcome {fac['name']} to Faculty Portal!", "success")
                return redirect(url_for("faculty_dashboard"))
            else:
                flash("Invalid Faculty credentials!", "danger")

        # Check Student Login
        elif role == "student":
            student = data_store.get_student(username)
            if student and student["password"] == password:
                session["user"] = student["name"]
                session["username"] = student["roll_no"]
                session["role"] = "student"
                # Update OS memory LRU cache for demonstration
                os_simulator.GLOBAL_LRU_CACHE.access(student["roll_no"], student["name"])
                flash(f"Welcome {student['name']}!", "success")
                return redirect(url_for("student_dashboard"))
            else:
                flash("Invalid Student Roll Number or Password!", "danger")

    return render_template("login.html")


# -----------------------------------------------------------------------------
# ROUTE 3: LOGOUT
# -----------------------------------------------------------------------------
@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out safely.", "info")
    return redirect(url_for("login"))


# -----------------------------------------------------------------------------
# ROUTE 4: STUDENT PORTAL (DASHBOARD)
# -----------------------------------------------------------------------------
@app.route("/dashboard/student")
def student_dashboard():
    """
    Student Dashboard showing:
    - Overall attendance percentage with 75% rule warning
    - Sessional Marks & Grades
    - Timetable
    - Fee Status & Receipt modal
    - Library issued books
    - Service request submission form
    """
    if not is_logged_in() or get_current_role() != "student":
        flash("Please log in as a Student to access this page.", "warning")
        return redirect(url_for("login"))

    roll_no = session.get("username")
    student = data_store.get_student(roll_no)
    if not student:
        # Fallback to Ashutosh's account if session is somehow generic
        student = data_store.get_student("0261dcsa007")

    notices = data_store.get_notices()
    my_requests = [r for r in data_store.get_student_requests() if r["roll_no"] == student["roll_no"]]

    return render_template(
        "student_dashboard.html",
        student=student,
        timetable=data_store.TIMETABLE,
        notices=notices,
        my_requests=my_requests,
        library_books=data_store.LIBRARY_BOOKS
    )


# -----------------------------------------------------------------------------
# ROUTE 5: STUDENT SERVICE REQUEST (SUBMIT JOB TO OS QUEUE)
# -----------------------------------------------------------------------------
@app.route("/student/submit-request", methods=["POST"])
def submit_student_request():
    if not is_logged_in() or get_current_role() != "student":
        return redirect(url_for("login"))

    roll_no = session.get("username")
    student = data_store.get_student(roll_no)
    req_type = request.form.get("request_type")
    reason = request.form.get("reason")

    success, msg = data_store.add_student_request(roll_no, student["name"], req_type, reason)
    flash(msg, "success")
    return redirect(url_for("student_dashboard"))


# -----------------------------------------------------------------------------
# ROUTE 6: FACULTY PORTAL (DASHBOARD)
# -----------------------------------------------------------------------------
@app.route("/dashboard/faculty")
def faculty_dashboard():
    """
    Faculty Dashboard showing:
    - Assigned subjects & Lecture schedule
    - Batch C Attendance register with 1-click update
    - Sessional marks updating interface
    - List of students with low attendance alert (<75%)
    """
    if not is_logged_in() or get_current_role() != "faculty":
        flash("Please log in as Faculty to access this page.", "warning")
        return redirect(url_for("login"))

    faculty = data_store.FACULTY.get("faculty")
    students = data_store.get_all_students()
    notices = data_store.get_notices()

    return render_template(
        "faculty_dashboard.html",
        faculty=faculty,
        students=students,
        notices=notices
    )


@app.route("/faculty/mark-attendance", methods=["POST"])
def faculty_mark_attendance():
    if not is_logged_in() or get_current_role() != "faculty":
        return redirect(url_for("login"))

    roll_no = request.form.get("roll_no")
    status = request.form.get("status")  # 'Present' or 'Absent'

    success, msg = data_store.mark_attendance(roll_no, status)
    flash(msg, "success" if success else "danger")
    return redirect(url_for("faculty_dashboard"))


@app.route("/faculty/update-marks", methods=["POST"])
def faculty_update_marks():
    if not is_logged_in() or get_current_role() != "faculty":
        return redirect(url_for("login"))

    roll_no = request.form.get("roll_no")
    subject_code = request.form.get("subject_code", "CCSE0353A")
    s1 = request.form.get("sessional_1", 0)
    s2 = request.form.get("sessional_2", 0)

    success, msg = data_store.update_marks(roll_no, subject_code, s1, s2)
    flash(msg, "success" if success else "danger")
    return redirect(url_for("faculty_dashboard"))


# -----------------------------------------------------------------------------
# ROUTE 7: ADMIN PORTAL (DASHBOARD)
# -----------------------------------------------------------------------------
@app.route("/dashboard/admin")
def admin_dashboard():
    """
    Super Admin Dashboard:
    - High-level KPIs (Total students, average attendance, fees, pending requests)
    - Add New Student & Delete Student
    - Publish campus notices
    - Service Request approvals (Leave, Bonafide)
    - Link to OS Concept Simulator
    """
    if not is_logged_in() or get_current_role() != "admin":
        flash("Please log in as Admin to access this page.", "warning")
        return redirect(url_for("login"))

    stats = data_store.get_system_stats()
    students = data_store.get_all_students()
    notices = data_store.get_notices()
    requests = data_store.get_student_requests()

    return render_template(
        "admin_dashboard.html",
        stats=stats,
        students=students,
        notices=notices,
        requests=requests
    )


@app.route("/admin/add-student", methods=["POST"])
def admin_add_student():
    if not is_logged_in() or get_current_role() != "admin":
        return redirect(url_for("login"))

    data = {
        "roll_no": request.form.get("roll_no"),
        "name": request.form.get("name"),
        "branch": request.form.get("branch", "B.Tech CSE (AI)"),
        "semester": request.form.get("semester", 3),
        "section": request.form.get("section", "C"),
        "attendance": request.form.get("attendance", 85.0),
        "cgpa": request.form.get("cgpa", 8.5),
        "fee_status": request.form.get("fee_status", "Paid"),
        "role_in_project": request.form.get("role_in_project", "Student Scholar")
    }
    success, msg = data_store.add_student(data)
    flash(msg, "success" if success else "danger")
    return redirect(url_for("admin_dashboard"))


@app.route("/admin/delete-student/<roll_no>", methods=["POST"])
def admin_delete_student(roll_no):
    if not is_logged_in() or get_current_role() != "admin":
        return redirect(url_for("login"))

    success, msg = data_store.delete_student(roll_no)
    flash(msg, "info" if success else "danger")
    return redirect(url_for("admin_dashboard"))


@app.route("/admin/add-notice", methods=["POST"])
def admin_add_notice():
    if not is_logged_in() or get_current_role() != "admin":
        return redirect(url_for("login"))

    title = request.form.get("title")
    category = request.form.get("category", "General")
    content = request.form.get("content")

    success, msg = data_store.add_notice(title, category, content)
    flash(msg, "success")
    return redirect(url_for("admin_dashboard"))


@app.route("/admin/request-action/<req_id>/<action>", methods=["POST"])
def admin_request_action(req_id, action):
    if not is_logged_in() or get_current_role() != "admin":
        return redirect(url_for("login"))

    new_status = "Approved" if action == "approve" else "Rejected"
    success, msg = data_store.update_request_status(req_id, new_status)
    flash(msg, "info")
    return redirect(url_for("admin_dashboard"))


# -----------------------------------------------------------------------------
# ROUTE 8: OPERATING SYSTEMS INTERNALS & CONCEPTS DASHBOARD (CCSE0353A)
# -----------------------------------------------------------------------------
@app.route("/os-monitor")
def os_monitor():
    """
    Live interactive simulation of Operating Systems concepts applied to the ERP:
    1. CPU Scheduling (FCFS & Round Robin) of student service requests.
    2. Process Synchronization / Mutex Lock on shared college resources.
    3. Memory Cache (LRU page replacement) with Hit Ratio.
    4. Access Control / Security Matrix.
    """
    # Convert student requests to OS process queue format
    requests = data_store.get_student_requests()
    processes = []
    for idx, r in enumerate(requests):
        processes.append({
            "pid": f"P{idx+1} ({r['id']})",
            "title": f"{r['student_name']} - {r['request_type']}",
            "at": idx * 2,  # Simulated arrival time
            "bt": r.get("os_burst_time", 4)  # Simulated burst time
        })

    # Run FCFS
    fcfs_result = os_simulator.simulate_fcfs(processes)
    # Run Round Robin with quantum = 3
    quantum = int(request.args.get("quantum", 3))
    rr_result = os_simulator.simulate_round_robin(processes, time_quantum=quantum)

    # Mutex lock state
    mutex_state = os_simulator.GLOBAL_MUTEX.get_state()

    # LRU Cache state
    cache_state = os_simulator.GLOBAL_LRU_CACHE.get_state()

    # Access Control Matrix
    acl_matrix = os_simulator.get_access_control_matrix()

    return render_template(
        "os_internals.html",
        fcfs=fcfs_result,
        rr=rr_result,
        quantum=quantum,
        mutex=mutex_state,
        cache=cache_state,
        acl=acl_matrix,
        students=data_store.get_all_students()
    )


# -----------------------------------------------------------------------------
# ROUTE 9: OS INTERACTIVE ACTIONS (MUTEX & CACHE DEMOS)
# -----------------------------------------------------------------------------
@app.route("/os/mutex/acquire", methods=["POST"])
def mutex_acquire():
    user_name = request.form.get("user_name", "Student Thread")
    proc_id = request.form.get("proc_id", "T-1")
    success, msg = os_simulator.GLOBAL_MUTEX.acquire(proc_id, user_name)
    flash(msg, "success" if success else "warning")
    return redirect(url_for("os_monitor"))


@app.route("/os/mutex/release", methods=["POST"])
def mutex_release():
    user_name = request.form.get("user_name", "Current Lock Holder")
    proc_id = request.form.get("proc_id", "T-1")
    success, msg = os_simulator.GLOBAL_MUTEX.release(proc_id, user_name)
    flash(msg, "info")
    return redirect(url_for("os_monitor"))


@app.route("/os/cache/access", methods=["POST"])
def cache_access():
    roll_no = request.form.get("roll_no")
    student = data_store.get_student(roll_no)
    name = student["name"] if student else "Unknown"
    status, hit_ratio = os_simulator.GLOBAL_LRU_CACHE.access(roll_no, name)
    flash(f"RAM Cache Request for {name} ({roll_no}) -> {status}. Hit Ratio: {hit_ratio}%", "info")
    return redirect(url_for("os_monitor"))


# -----------------------------------------------------------------------------
# APPLICATION ENTRYPOINT (DEPLOYMENT READY)
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # Uses PORT environment variable if provided by Render / Railway / Heroku,
    # otherwise defaults to local port 5000.
    port = int(os.environ.get("PORT", 5000))
    print(f"\n=======================================================")
    print(f" NIET Smart University ERP Platform Started!")
    print(f" Course: Operating Systems (CCSE0353A) | Group 52")
    print(f" Faculty: Mr. Praveen Kr Tomar")
    print(f" Open your browser at: http://127.0.0.1:{port}")
    print(f"=======================================================\n")
    app.run(host="0.0.0.0", port=port, debug=True)
