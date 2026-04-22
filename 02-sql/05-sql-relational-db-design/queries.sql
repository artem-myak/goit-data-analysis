-- STEP 1: Database Schema Creation (DDL)
-- Creating tables with Primary Keys and defining structure

CREATE TABLE departments_miakenkyi (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL
);

CREATE TABLE jobs_miakenkyi (
    job_id INT PRIMARY KEY,
    job_title VARCHAR(50) NOT NULL
);

CREATE TABLE employees_miakenkyi (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    department_id INT NOT NULL,
    job_id INT NOT NULL
);

-- STEP 2: Data Population (DML)
-- Inserting records into departments, jobs, and employees

INSERT INTO departments_miakenkyi VALUES
    (1, 'Engineering'),
    (2, 'Sales'),
    (3, 'HR'),
    (4, 'Marketing');

INSERT INTO jobs_miakenkyi VALUES
    (1, 'Data Analyst'),
    (2, 'Backend Engineer'),
    (3, 'Sales Manager');

INSERT INTO employees_miakenkyi VALUES
    (1, 'Alice', 'Johnson', 3, 1),
    (2, 'Bob', 'Smith', 1, 2),
    (3, 'Carol', 'Diaz', 2, 3);

-- STEP 3: Data Modification
-- Updating a specific record and deleting an entry

UPDATE employees_miakenkyi 
SET last_name = 'Jackson' 
WHERE employee_id = 2;

DELETE FROM employees_miakenkyi 
WHERE first_name = 'Carol';

-- STEP 4: Data Retrieval and Analysis
-- INNER JOIN to fetch employee details with department and job titles

SELECT 
    e.first_name, 
    e.last_name, 
    j.job_title, 
    d.department_name
FROM employees_miakenkyi e
JOIN departments_miakenkyi d ON e.department_id = d.department_id
JOIN jobs_miakenkyi j ON e.job_id = j.job_id;

-- LEFT JOIN to show all departments including those without employees

SELECT 
    dm.department_name, 
    em.first_name, 
    em.last_name
FROM departments_miakenkyi dm
LEFT JOIN employees_miakenkyi em ON dm.department_id = em.department_id;

-- STEP 5: Cleanup
-- Removing tables using CASCADE to handle dependencies

DROP TABLE departments_miakenkyi CASCADE;
DROP TABLE jobs_miakenkyi CASCADE;
DROP TABLE employees_miakenkyi CASCADE;