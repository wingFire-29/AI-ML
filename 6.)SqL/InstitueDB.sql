Create Database if not exists institute;

use institute;

Create Table Teacher(
	id INT Primary key,
    name VarChar(50),
    Sub Varchar(50),
    Salary Int(50)
);

INSERT INTO Teacher
(id,name,Sub,Salary)
Values
(23,"Ajay","Math",45000),
(21,"Parag","DL",60000),
(22,"Pranay","Java",50000),
(33,"Shubham","Javascript",55000),
(19,"Ritika","English",40000);

Select * From Teacher;

-- salaries above 50K
Select * From Teacher
Where salary>50000;

-- change col name salries to CTC
Alter Table Teacher
Change Column Salary CTC INT;

Alter Table Teacher
Change Column CTC Salary INT;
SET SQL_SAFE_UPDATES = 0;

Update Teacher
SET Salary=Salary + Salary*0.25;