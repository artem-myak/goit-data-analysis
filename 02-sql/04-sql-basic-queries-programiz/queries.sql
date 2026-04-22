-- 1. Customers from USA
SELECT * FROM Customers 
WHERE country = 'USA';

-- 2. Customers older than 25
SELECT first_name, last_name, age 
FROM Customers 
WHERE age > 25;

-- 3. Age categorization using CASE WHEN
SELECT first_name, last_name, age, country,
CASE
    WHEN age < 24 THEN 'Young'
    WHEN age BETWEEN 24 AND 30 THEN 'Adult'
    WHEN age > 30 THEN 'Senior'
END AS age_group
FROM Customers;

-- 4. Customers whose first name starts with 'J'
SELECT first_name, last_name, age, country
FROM Customers
WHERE first_name LIKE 'J%';

-- 5. Concatenating first and last name into full_name
SELECT TRIM(first_name) || ' ' || TRIM(last_name) AS full_name
FROM Customers;

-- 6. Last name and its length
SELECT last_name, 
  LENGTH(last_name) AS lastname_length
FROM Customers;

-- 7. Name in UPPER case and surname in LOWER case
SELECT UPPER(first_name) AS new_first_name,
  LOWER(last_name) AS new_last_name
FROM Customers;

-- 8. Filtering by last name length (exactly 3 characters) and handling nulls
SELECT first_name, last_name, age,
  COALESCE(country, 'No data') AS right_country
FROM Customers
WHERE LENGTH(last_name) = 3;

-- 9. Orders with amount > 500, sorted descending
SELECT item, amount
FROM Orders
WHERE amount > 500
ORDER BY amount DESC;

-- 10. Join Shippings and Customers to show delivery status
SELECT c.first_name, c.last_name, s.status
FROM Customers AS c
JOIN Shippings AS s ON c.customer_id = s.customer;