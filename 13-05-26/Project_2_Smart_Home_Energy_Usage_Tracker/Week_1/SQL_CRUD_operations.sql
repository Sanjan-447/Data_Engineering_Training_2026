create database if not exists smart_home_energy;
use smart_home_energy;

create table rooms(
room_id int auto_increment primary key,
room_name varchar(100) not null);

create table devices(
device_id int auto_increment primary key,
room_id int not null,
device_name varchar(100) not null,
device_type varchar(50) not null,
status enum("on", "off") default "off",
power_rating_watts decimal(10,2),
foreign key (room_id) references rooms(room_id) );


create table energy_logs(
log_id int auto_increment primary key,
device_id int not null,
timestamp datetime not null,
energy_kwh decimal(10,2) not null,
foreign key (device_id) references devices(device_id) );

insert into rooms(room_name) values
("Living Room"),
("Bedroom"),
("Kitchen"),
("Study Room");

insert into devices(room_id, device_name, device_type, status, power_rating_watts) values
(1, "Smart TV", "Entertainment", "OFF", 180),
(1, "Air Conditioner", "Cooling", "ON", 1500),
(2, "Ceiling Fan", "Cooling", "ON", 75),
(2, "Smart Light", "Lighting", "OFF", 15),
(3, "Refrigerator", "Appliance", "ON", 300),
(3, "Microwave Oven", "Appliance", "OFF", 1200),
(4, "Laptop Charger", "Electronics", "ON", 90),
(4, "WiFi Router", "Networking", "ON", 20);

insert into energy_logs(device_id, timestamp, energy_kwh) values
(2, "2026-05-01 09:00:00", 1.20),
(2, "2026-05-01 13:00:00", 1.10),
(2, "2026-05-01 18:00:00", 1.35),
(1, "2026-05-01 20:00:00", 0.15),
(1, "2026-05-02 21:00:00", 0.18),
(3, "2026-05-01 10:00:00", 0.05),
(3, "2026-05-01 15:00:00", 0.06),
(3, "2026-05-02 11:00:00", 0.05),
(5, "2026-05-01 08:00:00", 0.40),
(5, "2026-05-01 12:00:00", 0.42),
(5, "2026-05-02 08:00:00", 0.41),
(5, "2026-05-02 20:00:00", 0.45),
(7, "2026-05-01 09:30:00", 0.08),
(7, "2026-05-01 17:30:00", 0.09),
(7, "2026-05-02 09:30:00", 0.08),
(8, "2026-05-01 00:00:00", 0.02),
(8, "2026-05-01 06:00:00", 0.02),
(8, "2026-05-02 00:00:00", 0.02),
(2, "2026-06-01 10:00:00", 1.50),
(2, "2026-06-01 15:00:00", 1.45),
(5, "2026-06-01 08:00:00", 0.48),
(5, "2026-06-01 20:00:00", 0.50),
(2, "2026-07-01 12:00:00", 2.50),
(5, "2026-07-01 08:00:00", 0.60);

select * from rooms;

select * from devices;

select * from energy_logs;

select r.*, d.*, e.*  from rooms r join devices d 
on r.room_id = d.room_id join energy_logs e
on d.device_id = e.device_id ;


update devices set status = "ON" where device_id =1;

update devices set status = "OFF" where device_id =2;

delete from devices where device_id = 4;

update energy_logs set energy_kwh = 1.40 where log_id = 1;

delete from energy_logs where log_id = 6;