from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def create_marks_file():
    file_path = "/tmp/student_marks.txt"
    content = """Math,80
Science,75
English,90
Python,95
"""
    with open(file_path, "w") as f:
        f.write(content)

    print("Marks file created successfully")


def read_marks_file():
    file_path = "/tmp/student_marks.txt"
    with open(file_path, "r") as f:
        for line in f:
            print(line.strip())


def calculate_total():
    file_path = "/tmp/student_marks.txt"
    total = 0

    with open(file_path, "r") as f:
        for line in f:
            subject, marks = line.strip().split(",")
            total += int(marks)

    print(f"Total Marks = {total}")

    with open("/tmp/total_marks.txt", "w") as f:
        f.write(str(total))


def percentage_calculation():
    total_file = "/tmp/total_marks.txt"

    with open(total_file, "r") as f:
        total = int(f.read().strip())

    percentage = (total / 400) * 100  # 4 subjects, each out of 100
    percentage = int(percentage)

    print(f"Percentage = {percentage}")

    with open("/tmp/percentage.txt", "w") as f:
        f.write(str(percentage))


def generate_result():
    total_file = "/tmp/total_marks.txt"
    percentage_file = "/tmp/percentage.txt"
    result_file = "/tmp/result.txt"

    with open(total_file, "r") as f:
        total = int(f.read().strip())

    with open(percentage_file, "r") as f:
        percentage = int(f.read().strip())

    if total >= 200:
        result_status = "PASS"
    else:
        result_status = "FAIL"

    with open(result_file, "w") as f:
        f.write("Student Result Summary\n")
        f.write(f"Total Marks = {total}\n")
        f.write(f"Percentage = {percentage}\n")
        f.write(f"Result = {result_status}\n")

    print("Result file generated successfully")


with DAG(
    dag_id="student_marks_result_dag",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    create_marks_file_task = PythonOperator(
        task_id="create_marks_file",
        python_callable=create_marks_file
    )

    read_marks_file_task = PythonOperator(
        task_id="read_marks_file",
        python_callable=read_marks_file
    )

    calculate_total_task = PythonOperator(
        task_id="calculate_total",
        python_callable=calculate_total
    )

    percentage_calculation_task = PythonOperator(
        task_id="percentage_calculation",
        python_callable=percentage_calculation
    )

    generate_result_task = PythonOperator(
        task_id="generate_result",
        python_callable=generate_result
    )

    create_marks_file_task >> read_marks_file_task >> calculate_total_task >> percentage_calculation_task >> generate_result_task
    
    
    
    
    
    