create database if not exists personal_expense_monitoring;
use personal_expense_monitoring;

create table users(
user_id int auto_increment primary key,
f_name varchar(50) not null,
l_name varchar(50) not null,
email varchar(150) not null,
password varchar(200) not null );

create table categories(
category_id int auto_increment primary key,
category_name varchar(100) unique not null,
category_type enum("income", "expense") not null );

create table expenses(
expense_id int auto_increment primary key,
user_id int not null,
category_id int not null,
payment_mode enum("cash", "card", "UPI"),
amount decimal(10, 2) not null,
expense_date date not null
);

insert into users(f_name, l_name, email, password) values
("Rahul", "Sharma", "rahul@gmail.com", "rahul123"),
("Anjana", "Arora", "anjana@gmail.com", "anjana456"),
("John", "Doe", "john@gmail.com", "john123"),
("Nikitha", "Ramesh", "nikitha@gmail.com", "nikitha456"),
("Sebastian", "Paul", "sebastian@gmail.com", "sebastian123");


insert into categories(category_name, category_type) values
("Food", "expense"),
("Rent", "expense"),
("Salary", "income"),
("Travel", "expense"),
("Medical", "expense"),
("Shopping", "expense");

insert into expenses(user_id, category_id, payment_mode, amount, expense_date) values
(1, 1, "UPI", 500.00, "2026-05-01"),
(1, 2, "cash", 10000.00, "2026-05-02"),
(1, 4, "card", 2500.00, "2026-05-05"),
(2, 1, "UPI", 300.00, "2026-05-04"),
(3, 5, "cash", 50.00, "2026-05-07"),
(4, 6, "UPI", 1300.00, "2026-05-06"),
(5, 3, "cash", 50000.00, "2026-05-02");

select * from users;

select * from categories;

select * from expenses;

update expenses set payment_mode="card" where expense_id = 1;

update expenses set  expense_date = "2026-05-01" where expense_id = 4;

update users set l_name= "Luther" where user_id = 5;

delete from users where user_id= 5;

delete from expenses where expense_id = 5;
