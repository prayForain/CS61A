-- Disc 12 SQL
-- pass-test

CREATE TABLE IF NOT EXISTS  records AS
    SELECT "Ben Bitdiddle" AS name, "Computer" AS division, "Wizard" AS title,
        60000 AS salary, "Oliver Warbucks" AS supervisor UNION
    SELECT "Alyssa P Hacker", "Computer", "Programmer", 40000, "Ben Bitdiddle" UNION
    SELECT "Cy D Fect", "Computer", "Programmer", 35000, "Ben Bitdiddle" UNION
    SELECT "Lem E Tweakit", "Computer", "Technician", 25000, "Ben Bitdiddle" UNION
    SELECT "Louis Reasoner", "Computer", "Programmer Trainee", 30000, "Alyssa P Hacker" UNION
    SELECT "Oliver Warbucks", "Administration", "Big Wheel", 150000, "Oliver Warbucks" UNION
    SELECT "Eben Scrooge", "Accounting", "Chief Accountant", 75000, "Oliver Warbucks" UNION
    SELECT "Robert Cratchet", "Accounting", "Scrivener", 18000, "Eben Scrooge" UNION
    SELECT "Lana Lambda", "Administration", "Executive Director", 610000, "Lana Lambda";

CREATE TABLE IF NOT EXISTS  meetings AS
    SELECT "Accounting" AS division, "Monday" AS day, "9am" AS time UNION
    SELECT "Computer", "Wednesday", "4pm" UNION
    SELECT "Administration", "Monday", "11am" UNION
    SELECT "Administration", "Wednesday", "4pm";

CREATE TABLE IF NOT EXISTS  courses AS
    SELECT "John DeNero" AS professor , "CS 61A" AS course , "Fa17" AS semester UNION
    SELECT "Paul Hilfinger"           , "CS 61A"           , "Fa17" UNION
    SELECT "Paul Hilfinger"           , "CS 61A"           , "Sp17" UNION
    SELECT "John DeNero"              , "Data 8"           , "Sp17" UNION
    SELECT "Josh Hug"                 , "CS 61B"           , "Sp17" UNION
    SELECT "Satish Rao"               , "CS 70 "           , "Sp17" UNION
    SELECT "Nicholas Weaver"          , "CS 61C"           , "Sp17" UNION
    SELECT "Gerald Friedland"         , "CS 61C"           , "Sp17" UNION
    SELECT "John DeNero"              , "CS 61A"           , "Fa16" UNION
    SELECT "Paul Hilfinger"           , "CS 61B"           , "Fa16";

-- 2.1
SELECT name from records where supervisor = "Oliver Warbucks";
    
-- 2.2
SELECT * from records where name = supervisor;

-- 2.3
SELECT name from records where salary > 50000 order by name;

-- 3.1
SELECT day, time from records as a, meetings
    where a.supervisor = "Oliver Warbucks";

-- 3.2
SELECT a.name, b.name from records as a, records as b
    where a.name < b.name and a.division = b.division;

-- 3.4
SELECT a.name from records as a, records as b
    where a.supervisor = b.name and a.division <> b.division;

-- 4.1
SELECT supervisor, sum(salary) from records group by supervisor;

-- 4.2
SELECT b.day from records as a, meetings as b
    where a.division = b.division group by b.day having count(a.name) < 5;

-- 4.3
SELECT a.division, a.name, b.name  from records as a, records as b
    where a.division = b.division and a.name < b.name and a.salary + b.salary < 100000;

-- 5.1
CREATE TABLE num_taught AS
    SELECT professor, course, count(semester) as times from courses
        group by professor, course;

-- 5.2
SELECT a.professor, b.professor, a.course from num_taught as a, num_taught as b
    where a.professor < b.professor and a.course = b.course and a.times = b.times;

-- 5.3
SELECT a.professor, b.professor from courses as a, courses as b
    where a.course = b.course and a.semester = b.semester and a.professor < b.professor
        group by a.professor, b.professor having count(a.course) > 1;
