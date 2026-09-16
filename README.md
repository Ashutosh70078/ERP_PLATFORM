# NIET Smart University ERP Platform (Operating Systems Capstone Project)

**Institution:** Noida Institute of Engineering and Technology (NIET, Greater Noida)  
**Department:** Department of Artificial Intelligence  
**Program & Branch:** B.Tech CSE (AI) | 3rd Semester | Batch C (Academic Year 2026-2027)  
**Course Name & Code:** Operating Systems (`CCSE0353A` / `CCSE0303A`)  
**Faculty / Course Coordinator:** Mr. Praveen Kr Tomar  
**Team / Group:** Group 52  

### Group Members & Project Roles:
1. **Krish Kumar** (`0261dscai010`) - Team Leader & System Analyst
2. **Ashutosh Jitendra Singh** (`0261dcsa007`) - Security & Reliability Specialist
3. **Govind Kumar** (`0261dcsai003`) - Modern OS & Documentation Specialist
4. **Suman Kumar Gorain** (`0261dcsai012`) - Performance & Optimization Specialist
5. **Preety Kumari** (`0261dcsai011`) - Linux & Scheduling Specialist

---

## 🚀 Overview

The **NIET Smart University ERP Platform** is a web-based educational ERP application built using **Python (Flask)**, **HTML5**, and **Vanilla CSS3**. 

Beyond conventional university activities (Attendance, Marks, Notices, Timetable, Fees, Library), this platform solves a primary academic objective of the **Operating Systems Course (CCSE0353A)**: **mapping theoretical OS concepts directly into operational software features**.

---

## 🔬 Operating Systems (OS) Concepts Mapping

| OS Concept | Real ERP Feature | Team Member Responsible |
| :--- | :--- | :--- |
| **Process Scheduling (FCFS & Round Robin)** | Student service requests (Bonafide, Leave) enter a CPU Ready Queue and are scheduled with dynamic Gantt charts and TAT/WT metrics. | **Preety Kumari** & **Krish Kumar** |
| **Process Synchronization & Mutex Lock** | Prevents Race Conditions when concurrent threads attempt to reserve the same High-Performance AI Lab Workstation or single-copy library book. | **Ashutosh Kumar** |
| **Memory Management & LRU Cache** | Simulates physical RAM page frames (Capacity = 4 frames) showing Page Hit vs. Page Fault (Cache Miss) when student profiles are accessed. | **Suman Kumar Gorain** & **Govind Kumar** |
| **Security & Access Control Matrix (ACL)** | Role-Based Access Control enforcing User Mode vs. Kernel Mode privilege separation across Admin, Faculty, and Student users. | **Ashutosh Kumar** |

---

## 🔑 Demo Login Credentials

For quick evaluation during viva, 1-click fill buttons are present on `/login`:

- **Student Portal**:
  - Roll No: `0261dcsa007` (Ashutosh) or `0261dscai010` (Krish)
  - Password: `student123`
- **Faculty Portal**:
  - Username: `faculty` (Mr. Praveen Kr Tomar)
  - Password: `fac123`
- **Super Administrator Console**:
  - Username: `admin`
  - Password: `admin123`

---

## 🛠️ Installation & Local Execution

### 1. Prerequisites
- Python 3.10+ installed.

### 2. Setup Virtual Environment
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux / Mac:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Platform
```bash
python app.py
```
Open your browser and navigate to: `http://127.0.0.1:5000`

---

## ☁️ Free Cloud Hosting Deployment

The repository is pre-configured with `Procfile`, `runtime.txt`, and dynamic port binding (`os.environ.get("PORT", 5000)`).

### Deploying to Render.com (Free Tier):
1. Push this folder to a GitHub repository.
2. Log in to [Render.com](https://render.com) and click **New + Web Service**.
3. Connect your GitHub repository.
4. Set:
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Click **Deploy Web Service**. Your website will be live in 2 minutes!

### Deploying to PythonAnywhere.com:
1. Create a free account on [PythonAnywhere](https://www.pythonanywhere.com).
2. Upload the project files into the Files tab.
3. In the Web tab, choose Flask / Python 3.10 and point WSGI configuration to `app.py`.

---

## 🗄️ Future DBMS / SQL Integration

All database queries and mutations are isolated inside **`data_store.py`**. 

To connect MySQL or SQLite in future phases:
1. Open `data_store.py`.
2. Replace Python dictionary operations with SQL queries:
   ```python
   # Example:
   # cursor.execute("SELECT * FROM students WHERE roll_no = %s", (roll_no,))
   ```
3. Frontend and routes require **zero** changes!
