CREATE DATABASE UniversityDB;
USE UniversityDB;
CREATE TABLE Student (
RegnNo BIGINT PRIMARY KEY,
RollNo BIGINT,
FirstName VARCHAR(50),
LastName VARCHAR(50),
Dept VARCHAR(50),
Course VARCHAR(50),
Specialisation VARCHAR(50),
Semester INT,
Marks INT,
City VARCHAR(50),
State VARCHAR(50),
EmailID VARCHAR(50)
);
CREATE TABLE Faculty (
EmployeeID INT PRIMARY KEY,
Designation VARCHAR(50),
Department VARCHAR(50),
Salary INT,
DateOfJoining DATE,
Subject VARCHAR(50),
DateOfBirth DATE,
NumOfGuidedPhDs INT,
Name VARCHAR(100)
);
CREATE TABLE Fees (
TransactionID INT PRIMARY KEY,
RegnNo BIGINT,StudentName VARCHAR(100),
Course VARCHAR(50),
Semester INT,
DateOfPayment DATE,
TypeOfFees VARCHAR(50),
AmountPaid DECIMAL(10, 2),
PaymentMethod VARCHAR(50)
);
ALTER TABLE Fees
ADD CONSTRAINT FK_Student_RegnNo
FOREIGN KEY (RegnNo)
REFERENCES Student(RegnNo);
ALTER TABLE Student
ADD Gender VARCHAR(10),
ADD DateOfBirth DATE,
ADD SGPA DECIMAL(3, 2);
ALTER TABLE Faculty
ADD HighestQualification VARCHAR(50);
INSERT INTO Student (RegnNo, RollNo, FirstName, LastName, Dept, Course, Specialisation, Semester, Marks, City,
State, EmailID, Gender, DateOfBirth, SGPA)
VALUES
(221000120111, 10000222034, 'Arindam', 'Biswas', 'Computer Science', 'B.Tech.', 'Machine Learning', 3, 90,
'Krishnanagar', 'West Bengal', 'arindambiswas260@gmail.com', 'Male', '2000-09-09', 9.5),
(221000120107,10000222056,'Saikat','Mitra','Electronics and
Telecommunication','Diploma','Robotics',5,89,'Hyderabad','Andrapradesh','mitrasaikat420@gmail.com','Male','2001-
9-28',9.0),
(221000120136,10000222062,'Sarmistha','Raul','Computer Science','B.sc.','Data Science',1,91,'New
Delhi','Delhi','raulsarmistha740@gmail.com','Female','2002-03-12',9.2),
(221000120122, 10000222034, 'Souvik', 'Mondal', 'Computer Science', 'B.sc.', 'Data Science', 3, 90, 'Patna', 'Bihar',
NULL, 'Male', '2000-10-03', 9.5),
(221000120116, 10000222039, 'Sananda','Paul','Information Technology', 'B.Tech',
'DSA',3,87,'Bhagalpur','Bihar','paulsanansa@gmail.com','Female','2001-11-25',9.0);INSERT INTO Faculty (EmployeeID, Designation, Department, Salary, DateOfJoining, Subject, DateOfBirth,
NumOfGuidedPhDs, HighestQualification, Name)
VALUES
(101, 'Professor', 'Computer Science', 80000, '2010-08-20', 'Database Management', '1970-12-10', 10, 'Ph.D. in
Computer Science','Souvik Mondal'),
(102, 'Associate Professor', 'Information Technology', 70000, '2015-05-10', 'Data Structure And Algorithm', '1980-06-
25', 8, 'Ph.D. in Computer Science','Snehangshu Biswas'),
(103,'Assistant Professor','Information Technology',50000,'2010-06-11','Operating System','2000-12-29',5,'Ph.D. in
Computer Science','Subham Kundu'),
(104, 'Associate Professor', 'Computer Science', 80000, '2010-08-29', 'Database Management', '1970-12-19', 11,
'Ph.D. in Computer Science','Debomita Saha'),
(105,'Assistant Professor','Geoinformatics',55000,'2009-06-04','Database Management','1985-01-26',7,'Ph.D in Data
Science','Misti Roy');
INSERT INTO Fees (TransactionID, RegnNo, StudentName, Course, Semester, DateOfPayment, TypeOfFees,
AmountPaid, PaymentMethod)
VALUES
(1,221000120111,'Arindam Biswas', 'B.Tech', 5, '2023-01-15', 'Tuition Fees', 5000, 'Credit Card'),
(2,221000120107,'Saikat Mitra', 'Diploma', 5, '2023-02-20', 'Tuition Fees', 5500, 'Cash'),
(3,221000120116,'Sananda Paul','B.Tech',3,'2023-03-12','Semester Fees',30000,'Net Banking'),
(4,221000120111,'Arindam Biswas', 'B.Tech', 5, '2023-03-02', 'Exam Fees', 1200, 'UPI'),
(5,221000120111, 'Arindam Biswas', 'B.Tech', 5, '2023-03-09', 'Semester Fees', 30000, 'Credit Card');
RENAME TABLE Faculty TO Staff;
SET SQL_SAFE_UPDATES = 0;
UPDATE StaffSET Designation = 'Associate Professor'
WHERE Designation = 'Assistant Professor' AND YEAR(CURDATE()) - YEAR(DateOfJoining) >= 8;
SET SQL_SAFE_UPDATES = 1;
SELECT * FROM Staff;
SELECT * FROM Fees;
SELECT FirstName, LastName
FROM Student
WHERE Course = 'B.sc.' AND Specialisation = 'Data Science';
SELECT *
FROM Staff
WHERE Name LIKE '%a';
SELECT RegnNo, RollNo, FirstName, LastName
FROM Student
WHERE EmailID IS NULL OR EmailID = '';
ALTER TABLE Student
ADD CONSTRAINT CHK_SemesterRange CHECK (Semester BETWEEN 1 AND 8);
DELIMITER //
CREATE TRIGGER before_insert_Staff
BEFORE INSERT ON Staff FOR EACH ROW
BEGINDECLARE staff_age INT;
SET staff_age = YEAR(CURDATE()) - YEAR(NEW.DateOfBirth);
IF staff_age > 65 THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = 'Age constraint violated: Staff member is over 65 years old';
END IF;
END//
CREATE TRIGGER before_update_Staff
BEFORE UPDATE ON Staff FOR EACH ROW
BEGIN
DECLARE staff_age INT;
SET staff_age = YEAR(CURDATE()) - YEAR(NEW.DateOfBirth);
IF staff_age > 65 THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = 'Age constraint violated: Staff member is over 65 years old';
END IF;
END//
DELIMITER ;
SELECT *
FROM Staff
ORDER BY YEAR(CURDATE()) - YEAR(DateOfJoining) DESC;
SELECT Designation, AVG(Salary) AS AverageSalary
FROM Staff
GROUP BY Designation;
SELECT SUM(AmountPaid) AS TotalFeesReceived
FROM Fees;SELECT FirstName, LastName, RegnNo
FROM Student
WHERE State = 'Bihar'
ORDER BY FirstName, LastName;
SELECT f.TypeOfFees, f.StudentName, f.RegnNo, MIN(f.DateOfPayment) AS FirstPaymentDate
FROM Fees f
JOIN (
SELECT TypeOfFees, MIN(DateOfPayment) AS MinPaymentDate
FROM Fees
GROUP BY TypeOfFees
) minDates ON f.TypeOfFees = minDates.TypeOfFees AND f.DateOfPayment = minDates.MinPaymentDate
GROUP BY f.TypeOfFees, f.StudentName, f.RegnNo;
SELECT Name, DateOfJoining, Designation
FROM Staff
ORDER BY NumOfGuidedPhDs DESC;
SELECT PaymentMethod, COUNT(*) AS NumberOfPayments, SUM(AmountPaid) AS TotalFeesPaid
FROM Fees
GROUP BY PaymentMethod;
SELECT *
FROM Fees
WHERE YEAR(DateOfPayment) = 2023 AND MONTH(DateOfPayment) = 3;SELECT Dept, COUNT(*) AS NumberOfStudents
FROM Student
GROUP BY Dept;
SELECT Name, DateOfJoining
FROM Staff
WHERE Department = 'Geoinformatics'
ORDER BY DateOfJoining;
SET SQL_SAFE_UPDATES = 0;
UPDATE Staff
SET Salary = Salary + 3000
WHERE Department = 'Information Technology';
SET SQL_SAFE_UPDATES = 1;
SELECT Name, (YEAR(CURDATE()) - YEAR(DateOfJoining)) AS WorkExperience
FROM Staff
WHERE Salary < (SELECT AVG(Salary) FROM Staff);
SELECT RegnNo, RollNo, FirstName, LastName, Dept, SGPA
FROM Student s1
WHERE SGPA = (SELECT MAX(SGPA) FROM Student s2 WHERE s1.Dept = s2.Dept);
SELECT FirstName, LastName, DeptFROM Student
WHERE RegnNo NOT IN (SELECT RegnNo FROM Fees)
ORDER BY Dept, FirstName, LastName;
SELECT DISTINCT Dept
FROM Student
WHERE Dept NOT IN (SELECT DISTINCT Department FROM Staff);
SELECT Name
FROM Staff
WHERE DateOfBirth > (SELECT MIN(DateOfBirth) FROM Student);
SELECT s.FirstName, s.LastName, s.RollNo, s.Dept, f.AmountPaid
FROM Student s
JOIN Fees f ON s.RegnNo = f.RegnNo
ORDER BY f.AmountPaid DESC
LIMIT 1;
SELECT Dept, 'Student' AS Category, COUNT(*) AS Count
FROM Student
GROUP BY Dept
UNION
SELECT Department AS Dept, 'Staff' AS Category, COUNT(*) AS Count
FROM Staff
GROUP BY Department;
