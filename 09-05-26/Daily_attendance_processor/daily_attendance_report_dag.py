from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_attendance_file():
    file="/tmp/attendance.txt"
    content="""Aarav,Present
Priya,Present
Rahul,Absent
Sneha,Present
Kiran,Absent
Ananya,Present
Vikram,Present
Meera,Absent
Farhan,Present
Divya,Present"""

    with open(file, "w") as f:
        f.write(content)
        
    print("Attendance content written successfully")

def read_attendance_file():
    file="/tmp/attendance.txt"
    with open(file, "r") as f:
        for line in f:
            print(line.strip())

def count_total_students():
    file="/tmp/attendance.txt"
    total=0
    with open(file, "r") as f:
        for line in f:
            if line.strip():
                total+=1
    print(f"Total Students= {total}")
    
    with open("/tmp/total_students.txt", "w") as f:
        f.write(str(total))
        
def count_present_students():
    file="/tmp/attendance.txt"
    present_count=0
    with open(file, "r") as f:
        for line in f:
            name, att = line.strip().split(",")
            if att == "Present":
                present_count+=1
    print(f"Present Students = {present_count}")
    with open("/tmp/present_students.txt", "w") as f:
        f.write(str(present_count))

def count_absent_students():
    file="/tmp/attendance.txt"
    absent_count=0
    with open(file, "r") as f:
        for line in f:
            name, att = line.strip().split(",")
            if att == "Absent":
                absent_count+=1
    print(f"Absent Students = {absent_count}")
    with open("/tmp/absent_students.txt", "w") as f:
        f.write(str(absent_count))
        
def calculate_attendance_percentage():
    total_file="/tmp/total_students.txt"
    present_file="/tmp/present_students.txt"
    total=0
    present=0
    percentage=0
    with open(total_file, "r") as f:
        total=int(f.read().strip()) 
    
    with open(present_file, "r" ) as f:
        present= int(f.read().strip())
    percentage= int((present/total) * 100)
    
    print(f"Attendance Percentage = {percentage}")
    
    with open("/tmp/attendance_percentage.txt", "w") as f:
        f.write(str(percentage))

def list_absent_students():
    file_path = "/tmp/attendance.txt"
    absent_list = []

    with open(file_path, "r") as f:
        for line in f:
            name, status = line.strip().split(",")
            if status == "Absent":
                absent_list.append(name)

    print("Absent Students List")
    for student in absent_list:
        print(student)

    with open("/tmp/absent_list.txt", "w") as f:
        for student in absent_list:
            f.write(student + "\n")
        
def generate_attendance_report():
    file="/tmp/attendance_report.txt"
    
    with open("/tmp/total_students.txt", "r") as f:
        total= int(f.read().strip())
        
    with open("/tmp/present_students.txt", "r") as f:
        present= int(f.read().strip())
    
    with open("/tmp/absent_students.txt", "r") as f:
        absent= int(f.read().strip())
        
    with open("/tmp/attendance_percentage.txt", "r") as f:
        percentage= int(f.read().strip())
    
    status = "Good" if percentage >= 75 else "Needs Improvement"

    report_file = "/tmp/attendance_report.txt"
    content = f"""Daily Attendance Report
Total Students = {total}
Present Students = {present}
Absent Students = {absent}
Attendance Percentage = {percentage}%
Status = {status}
"""

    with open(report_file, "w") as f:
        f.write(content)

    print("Attendance report generated successfully")
    
with DAG(
    dag_id="daily_attendance_report_dag",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    create_attendance_file_task = PythonOperator(
        task_id="create_attendance_file",
        python_callable=create_attendance_file
    )

    read_attendance_file_task = PythonOperator(
        task_id="read_attendance_file",
        python_callable=read_attendance_file
    )

    count_total_students_task = PythonOperator(
        task_id="count_total_students",
        python_callable=count_total_students
    )

    count_present_students_task = PythonOperator(
        task_id="count_present_students",
        python_callable=count_present_students
    )

    count_absent_students_task = PythonOperator(
        task_id="count_absent_students",
        python_callable=count_absent_students
    )

    calculate_attendance_percentage_task = PythonOperator(
        task_id="calculate_attendance_percentage",
        python_callable=calculate_attendance_percentage
    )

    list_absent_students_task = PythonOperator(
        task_id="list_absent_students",
        python_callable=list_absent_students
    )

    generate_attendance_report_task = PythonOperator(
        task_id="generate_attendance_report",
        python_callable=generate_attendance_report
    )

    create_attendance_file_task >> read_attendance_file_task >> count_total_students_task >> count_present_students_task >> count_absent_students_task >> calculate_attendance_percentage_task >> list_absent_students_task >> generate_attendance_report_task
    
    
    
    
    