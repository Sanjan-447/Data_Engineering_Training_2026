CREATE DATABASE company_training;

USE company_training;

CREATE TABLE employees (
emp_id INT PRIMARY KEY,
emp_name VARCHAR(100),
department VARCHAR(50),
city VARCHAR(50)
);

INSERT INTO employees VALUES
(1, 'Rohan Mehta', 'IT', 'Hyderabad'),
(2, 'Sneha Iyer', 'IT', 'Bangalore'),
(3, 'Kiran Patel', 'Finance', 'Mumbai'),
(4, 'Ananya Das', 'HR', NULL),
(5, 'Rahul Sharma', 'IT', 'Delhi'),
(6, NULL, 'Marketing', 'Chennai');

CREATE TABLE projects (
project_id INT PRIMARY KEY,
emp_id INT,
project_name VARCHAR(100),
project_budget DECIMAL(12,2),
project_status VARCHAR(50)
);

INSERT INTO projects VALUES
(101, 1, 'AI Chatbot', 120000, 'Active'),
(102, 1, 'ML Prediction', 90000, 'Active'),
(103, 2, 'Data Warehouse', 150000, 'Active'),
(104, 3, 'Financial Dashboard', 80000, 'Completed'),
(105, NULL, 'Website Revamp', 60000, 'Pending'),
(106, 8, 'Mobile App', 100000, 'Active');

-- exercise 1

select e.emp_name, p.project_name, p.project_budget from employees  e inner join projects p on e.emp_id=p.emp_id; 

-- exercise 2 

select e.emp_name, p.project_name from employees e left join projects p on e.emp_id=p.emp_id;

-- exercise 3

select p.* from projects p left join employees e on p.emp_id= e.emp_id; 

-- exercise 4

select e.emp_id, e.emp_name, p.project_name from employees e left join projects p on e.emp_id=p.emp_id
union 
select e.emp_id, e.emp_name, p.project_name from employees e right join projects p on e.emp_id=p.emp_id;  

-- exercise 5 

select e.emp_name, p.project_name from employees e cross join projects p;

-- exercise 6

select p.project_name from projects p join employees e on p.emp_id=e.emp_id where e.department='IT';

-- exercise 7

select project_name from projects where project_budget > 100000;   

-- exercise 8

select e.emp_name, p.project_name from employees e join projects p on e.emp_id=p.emp_id where e.city='Hyderabad'; 

-- exercise 9
select e.emp_name, count(p.project_name) as total_projects from employees e join projects p on e.emp_id=p.emp_id group by e.emp_name;

-- exercise 10
select e.emp_name, sum(p.project_budget) as total_budget from employees e join projects p on e.emp_id=p.emp_id group by e.emp_name; 
 
 -- exercise 11
 select e.department, avg(p.project_budget) as average_budget from employees e join projects p on e.emp_id=p.emp_id group by e.department;
 
 -- exercise 12
 select e.department, count(p.project_name) as total_projects from employees e join projects p on e.emp_id=p.emp_id group by e.department;
 
-- exercise 13
select e.department, sum(p.project_budget) as total_budget from employees e join projects p on e.emp_id=p.emp_id group by e.department;

-- exercise 14
select city, count(emp_name) as total_employees from employees group by city;

-- exercise 15
select e.emp_name from employees e join projects p on e.emp_id=p.emp_id group by e.emp_name having count(p.project_name)>1; 

-- exercise 16
select e.department from  employees e join projects p on e.emp_id=p.emp_id group by e.department having sum(p.project_budget) > 150000;

--  exercise 17
select e.emp_name from employees e join projects p on e.emp_id=p.emp_id group by e.emp_name having sum(p.project_budget) > 100000;

-- capstone query

select e.emp_name, e.department, sum(p.project_budget) as total_project_budget from employees e join projects p on e.emp_id=p.emp_id group by e.emp_name, e.department having total_project_budget > 100000 order by total_project_budget desc; 