create table Employees (
	Name varchar(255),
	Position varchar(255),
	Department varchar(255),
	Salary int);

insert into Employees (Name, Position, Department, Salary) values ('Ivan', 'Administrator', 'Admin', 12000);
insert into Employees (Name, Position, Department, Salary) values ('Andrey', 'Accountant', 'Finance', 9500);
insert into Employees (Name, Position, Department, Salary) values ('Kate', 'Assistant', 'Admin', 6500);
insert into Employees (Name, Position, Department, Salary) values ('Michail', 'Courier', 'Finance', 5000);
insert into Employees (Name, Position, Department, Salary) values ('Oleg', 'Manager', 'Admin', 10000);

select * from Employees;

update Employees set position = 'Pre-Assistant' where   name = 'Michail';

alter table Employees add column HireDate date;

update Employees set HireDate = '05.02.2020' where name = 'Ivan';
update Employees set HireDate = '18.05.2022' where name = 'Kate';
update Employees set HireDate = '15.07.2025' where name = 'Andrey';
update Employees set HireDate = '01.02.1995' where name = 'Michail';
update Employees set HireDate = '08.08.2025' where name = 'Oleg';

select * from Employees where position = 'Manager';

select * from Employees where position = 'Manager';

select * from Employees where Salary > 7000;

select * from Employees where department = 'Admin';

select avg(Salary) from Employees; 

drop table Employees