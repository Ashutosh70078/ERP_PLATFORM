"""
=============================================================================
NIET SMART UNIVERSITY ERP PLATFORM - OS CONCEPTS SIMULATOR (CCSE0353A)
Course: Operating Systems | Faculty: Mr. Praveen Kr Tomar
Team 52: Krish Kumar, Ashutosh Kumar, Govind Kumar, Suman Kumar, Preety Kumari
=============================================================================

[EXPLAINABILITY FOR VIVA]:
Faculty sir agar pooche: "Yeh toh normal web application hai, isme Operating
System ka concept kahan laga hai?", toh aap is module ko open karke explain
karenge:
1. CPU Scheduling (Preety Kumari & Krish Kumar):
   ERP par aane wale student requests (leave, bonafide) ko hum CPU processes
   maante hain aur FCFS aur Round Robin algorithm se schedule karke dikhate hain.
2. Process Synchronization / Mutex Lock (Ashutosh Kumar):
   Shared resource (e.g. Lab System ya Library Book) par race condition rokne
   ke liye Mutex Lock ka simulation.
3. Memory Management / LRU Cache (Suman Kumar Gorain & Govind Kumar):
   Student profiles baar-baar fetch hone par RAM cache mein Page Hit vs Page Fault
   ka demonstration.
4. Security & Access Control (Ashutosh Kumar):
   Role-Based Protection Matrix (Read, Write, Execute rights for Admin/Faculty/Student).
=============================================================================
"""

from collections import deque
import copy

# -----------------------------------------------------------------------------
# 1. CPU SCHEDULING SIMULATOR (FCFS & ROUND ROBIN)
# -----------------------------------------------------------------------------
def simulate_fcfs(processes):
    """
    First-Come, First-Served (FCFS) Scheduling Algorithm.
    Non-preemptive algorithm: The process that arrives first is executed first.
    Formula:
    - Turnaround Time (TAT) = Completion Time (CT) - Arrival Time (AT)
    - Waiting Time (WT) = Turnaround Time (TAT) - Burst Time (BT)
    """
    if not processes:
        return {"schedule": [], "avg_wt": 0, "avg_tat": 0, "gantt": []}

    procs = copy.deepcopy(processes)
    # Sort by arrival time
    procs.sort(key=lambda x: x["at"])

    current_time = 0
    gantt_chart = []
    total_wt = 0
    total_tat = 0

    for p in procs:
        if current_time < p["at"]:
            # CPU is idle
            gantt_chart.append({"pid": "IDLE", "start": current_time, "end": p["at"]})
            current_time = p["at"]

        start_time = current_time
        end_time = start_time + p["bt"]
        current_time = end_time

        p["ct"] = end_time
        p["tat"] = p["ct"] - p["at"]
        p["wt"] = p["tat"] - p["bt"]

        total_wt += p["wt"]
        total_tat += p["tat"]

        gantt_chart.append({
            "pid": p["pid"],
            "title": p.get("title", p["pid"]),
            "start": start_time,
            "end": end_time
        })

    n = len(procs)
    return {
        "schedule": procs,
        "avg_wt": round(total_wt / n, 2),
        "avg_tat": round(total_tat / n, 2),
        "gantt": gantt_chart
    }


def simulate_round_robin(processes, time_quantum=2):
    """
    Round Robin (RR) Scheduling Algorithm.
    Preemptive algorithm designed especially for time-sharing systems.
    Each process gets a small unit of CPU time (time quantum), usually 10-100 ms.
    """
    if not processes:
        return {"schedule": [], "avg_wt": 0, "avg_tat": 0, "gantt": [], "quantum": time_quantum}

    procs = copy.deepcopy(processes)
    procs.sort(key=lambda x: x["at"])

    n = len(procs)
    remaining_bt = {p["pid"]: p["bt"] for p in procs}
    proc_dict = {p["pid"]: p for p in procs}

    current_time = 0
    ready_queue = deque()
    arrived = set()
    gantt_chart = []
    completed = 0

    # Add processes that arrive at time 0
    for p in procs:
        if p["at"] <= current_time and p["pid"] not in arrived:
            ready_queue.append(p["pid"])
            arrived.add(p["pid"])

    while completed < n:
        if not ready_queue:
            # CPU is idle, advance to the next arriving process
            next_proc = min([p for p in procs if p["pid"] not in arrived], key=lambda x: x["at"])
            gantt_chart.append({"pid": "IDLE", "start": current_time, "end": next_proc["at"]})
            current_time = next_proc["at"]
            for p in procs:
                if p["at"] <= current_time and p["pid"] not in arrived:
                    ready_queue.append(p["pid"])
                    arrived.add(p["pid"])
            continue

        curr_pid = ready_queue.popleft()
        exec_time = min(time_quantum, remaining_bt[curr_pid])

        start_time = current_time
        end_time = current_time + exec_time
        current_time = end_time
        remaining_bt[curr_pid] -= exec_time

        gantt_chart.append({
            "pid": curr_pid,
            "title": proc_dict[curr_pid].get("title", curr_pid),
            "start": start_time,
            "end": end_time
        })

        # Check for new arrivals during this execution window
        for p in procs:
            if p["at"] <= current_time and p["pid"] not in arrived:
                ready_queue.append(p["pid"])
                arrived.add(p["pid"])

        # If current process still has remaining time, push it back
        if remaining_bt[curr_pid] > 0:
            ready_queue.append(curr_pid)
        else:
            completed += 1
            proc_dict[curr_pid]["ct"] = current_time
            proc_dict[curr_pid]["tat"] = proc_dict[curr_pid]["ct"] - proc_dict[curr_pid]["at"]
            proc_dict[curr_pid]["wt"] = proc_dict[curr_pid]["tat"] - proc_dict[curr_pid]["bt"]

    total_wt = sum(p["wt"] for p in procs)
    total_tat = sum(p["tat"] for p in procs)

    return {
        "schedule": procs,
        "avg_wt": round(total_wt / n, 2),
        "avg_tat": round(total_tat / n, 2),
        "gantt": gantt_chart,
        "quantum": time_quantum
    }


# -----------------------------------------------------------------------------
# 2. PROCESS SYNCHRONIZATION & MUTEX LOCK SIMULATOR
# -----------------------------------------------------------------------------
class MutexSimulator:
    """
    Simulates a Mutex (Mutual Exclusion) Lock for shared university resources.
    Prevents Race Conditions when multiple student sessions try to book the
    same lab workstation or borrow the last copy of a library book simultaneously.
    """
    def __init__(self, resource_name="AI GPU Lab Workstation #01"):
        self.resource_name = resource_name
        self.is_locked = False
        self.locked_by = None
        self.wait_queue = []
        self.logs = []

    def acquire(self, process_id, user_name):
        if not self.is_locked:
            self.is_locked = True
            self.locked_by = f"{user_name} ({process_id})"
            msg = f"[LOCK ACQUIRED] {user_name} entered Critical Section for '{self.resource_name}'. Mutex locked."
            self.logs.append(msg)
            return True, msg
        else:
            entry = f"{user_name} ({process_id})"
            if entry not in self.wait_queue:
                self.wait_queue.append(entry)
            msg = f"[BLOCKED] Critical Section is BUSY! {user_name} was placed in Semaphore Waiting Queue."
            self.logs.append(msg)
            return False, msg

    def release(self, process_id, user_name):
        if not self.is_locked:
            return False, "Lock is not currently held."
        
        rel_msg = f"[LOCK RELEASED] {self.locked_by} left Critical Section."
        self.logs.append(rel_msg)

        if self.wait_queue:
            next_user = self.wait_queue.pop(0)
            self.locked_by = next_user
            msg = f"{rel_msg} Woke up next waiting process: {next_user} acquired the lock."
            self.logs.append(msg)
            return True, msg
        else:
            self.is_locked = False
            self.locked_by = None
            msg = f"{rel_msg} Resource '{self.resource_name}' is now FREE (UNLOCKED)."
            self.logs.append(msg)
            return True, msg

    def get_state(self):
        return {
            "resource": self.resource_name,
            "is_locked": self.is_locked,
            "locked_by": self.locked_by,
            "wait_queue": list(self.wait_queue),
            "logs": self.logs[-6:]  # last 6 logs
        }

# Global mutex instance for demo
GLOBAL_MUTEX = MutexSimulator("NIET High-Performance AI Server Workstation")


# -----------------------------------------------------------------------------
# 3. MEMORY MANAGEMENT (LRU CACHE SIMULATOR)
# -----------------------------------------------------------------------------
class LRUCacheSimulator:
    """
    Least Recently Used (LRU) Page Replacement / Memory Cache Simulator.
    Simulates memory management where recently accessed student records
    stay in fast RAM cache (capacity = 4 frames).
    Demonstrates Page Hit vs Page Fault (Cache Miss).
    """
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.cache = []  # Stores items in order of access
        self.hits = 0
        self.misses = 0
        self.history = []

    def access(self, item_key, item_name):
        if item_key in self.cache:
            # HIT
            self.hits += 1
            self.cache.remove(item_key)
            self.cache.append(item_key)
            status = "HIT (Found in Fast RAM)"
        else:
            # MISS / PAGE FAULT
            self.misses += 1
            if len(self.cache) >= self.capacity:
                evicted = self.cache.pop(0)  # Evict least recently used
                status = f"MISS (Page Fault - Evicted {evicted} to Disk)"
            else:
                status = "MISS (Page Fault - Loaded from Disk)"
            self.cache.append(item_key)

        total = self.hits + self.misses
        hit_ratio = round((self.hits / total) * 100, 1) if total > 0 else 0

        self.history.append({
            "key": item_key,
            "name": item_name,
            "status": status,
            "frames": list(self.cache),
            "hit_ratio": hit_ratio
        })
        return status, hit_ratio

    def get_state(self):
        total = self.hits + self.misses
        hit_ratio = round((self.hits / total) * 100, 1) if total > 0 else 0
        return {
            "capacity": self.capacity,
            "current_frames": list(self.cache),
            "hits": self.hits,
            "misses": self.misses,
            "hit_ratio": hit_ratio,
            "history": self.history[-5:]
        }

# Global LRU instance for demo
GLOBAL_LRU_CACHE = LRUCacheSimulator(capacity=4)
# Initialize with some active students
GLOBAL_LRU_CACHE.access("0261dcsa007", "Ashutosh Jitendra Singh")
GLOBAL_LRU_CACHE.access("0261dscai010", "Krish Kumar")
GLOBAL_LRU_CACHE.access("0261dcsai003", "Govind Kumar")


# -----------------------------------------------------------------------------
# 4. OS SECURITY & PROTECTION MATRIX (ACCESS CONTROL)
# -----------------------------------------------------------------------------
def get_access_control_matrix():
    """
    Returns the Protection Domain Matrix (ACL).
    Shows OS protection domains mapped to ERP user roles.
    R = Read, W = Write, X = Execute, - = Denied
    """
    return [
        {"object": "Student Master Records", "admin": "R / W / X", "faculty": "R only", "student": "R (Own Only)"},
        {"object": "Attendance Register", "admin": "R / W", "faculty": "R / W", "student": "R only"},
        {"object": "Sessional & Exam Marks", "admin": "R / W", "faculty": "R / W", "student": "R only"},
        {"object": "Campus Notices & Circulars", "admin": "R / W / X", "faculty": "R / W", "student": "R only"},
        {"object": "Fee Account & Gateway", "admin": "R / W", "faculty": "Denied (-)", "student": "R / Pay"},
        {"object": "OS Engine & Kernel Monitor", "admin": "Full Control", "faculty": "View Queue", "student": "Submit Job"}
    ]
