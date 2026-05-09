from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime 

def create_employee_file():
    file="/tmp/employees.txt"
    content= """Rahul,45000
Sneha,52000
Amit,61000
Priya,47000
Kiran,39000"""
    with open(file , "w") as f:
        f.write(content)
    print("Employee file created successfully")
        
def read_employee_data():
    file="/tmp/employees.txt"
    with open(file, "r") as f:
        for line in f:
            print(line.strip())
            
def  calculate_salary_expense():
    file="/tmp/employees.txt"
    total=0
    with open(file, "r") as f:
        for line in f:
            name, sal= line.strip().split(",")
            total += int(sal)
            
    print(f"Total Salary: {total}")
    
    with open("/tmp/total_sal.txt", "w") as f:
        f.write(str(total))
        
def find_highest_salary():
    file="/tmp/employees.txt"
    high_sal=0
    high_emp=""
    with open(file, "r") as f:
        for line in f:
            name, sal= line.strip().split(",")
            sal= int(sal)
            
            if sal > high_sal:
                high_sal= sal
                high_emp = name

    print(f"Highest Salary = {high_sal}")
    print(f"Employee = {high_emp}")
    
def generate_salary_report():
    tot_file= "/tmp/total_sal.txt"
    report_file="/tmp/salary_report.txt"
    
    with open(tot_file, "r") as f:
        total= int(f.read().strip())
    content= f"""Employee Salary Report
Total Employees = 5
Total Salary Expense = {total}
Status = Processed Successfully"""

    with open(report_file, "w") as f:
        f.write(content)
    print("Salary report generated successfully") 
    
    
with DAG (
    dag_id = "Employee_salary_report_dag",
    schedule= "@daily",
    start_date = datetime(2025,1,1),
    catchup= False
    ) as dag:
    create_employee_file_task = PythonOperator(
    task_id = "create_employee_file",
    python_callable= create_employee_file)
        
    read_employee_data_task = PythonOperator(
    task_id = "read_employee_data",
    python_callable= read_employee_data)
        
    calculate_salary_expense_task = PythonOperator(
    task_id = "calculate_salary_expense",
    python_callable= calculate_salary_expense)
        
    find_highest_salary_task = PythonOperator(
    task_id = "find_highest_salary",
    python_callable= find_highest_salary)
        
    generate_salary_report_task = PythonOperator(
    task_id = "generate_salary_report",
    python_callable= generate_salary_report)
     
    create_employee_file_task >> read_employee_data_task >> calculate_salary_expense_task >> find_highest_salary_task >> generate_salary_report_task
    

    
    