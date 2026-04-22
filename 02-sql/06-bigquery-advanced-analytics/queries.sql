-- Завдання 1: Робота з STRUCT та тимчасовими таблицями
-- Створюємо тимчасову таблицю temp_logs зі структурованим полем details
CREATE TEMP TABLE temp_logs AS
SELECT 
    user_id,
    STRUCT(event_name AS event, screen) AS details
FROM `homework_bigquery.event_logs`;

-- Виводимо окремо вкладені поля details.event та details.screen
SELECT
    user_id,
    details.event,
    details.screen
FROM temp_logs;


-- Завдання 2: Фільтрація за унікальними користувачами та датою
-- Рахуємо кількість унікальних користувачів з подією 'purchase' за останні 3 дні
SELECT COUNT(DISTINCT user_id) AS count_users
FROM `homework_bigquery.event_logs`
WHERE event_name = 'purchase'
  AND _PARTITIONDATE BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 2 DAY) AND CURRENT_DATE();


-- Завдання 3: Побудова масиву дій користувача через ARRAY_AGG
SELECT 
    user_id,
    DATE(event_time) AS event_date,
    ARRAY_AGG(event_name) AS events_per_day
FROM `homework_bigquery.event_logs`
GROUP BY user_id, event_date;


-- Завдання 4: Ручне створення STRUCT та витягування вкладених полів
WITH manual_struct AS (
  SELECT 
    user_id,
    STRUCT(event_name AS event, screen AS location) AS info
  FROM `homework_bigquery.event_logs`
)
SELECT 
    user_id AS uid,
    info.location AS location
FROM manual_struct;


-- Завдання 5 та 6: Запланований запит (Scheduled Query)
-- Оцінка обсягу: запит обробляє приблизно 430 B
INSERT INTO `homework_bigquery.daily_unique_users` (rep_date, count_users)
SELECT 
    CURRENT_DATE() AS rep_date,
    COUNT(DISTINCT user_id) AS count_users
FROM `homework_bigquery.event_logs`
WHERE event_name = 'purchase'
  AND _PARTITIONDATE >= '2024-01-01';


-- Завдання 7: Розгортання масиву через UNNEST
WITH users_events_per_day AS (
  SELECT 
    user_id,
    DATE(event_time) AS event_date,
    ARRAY_AGG(event_name) AS events_per_day
  FROM `homework_bigquery.event_logs`
  GROUP BY user_id, event_date
)
-- Розгортаємо масив для аналізу унікальних подій
SELECT 
    user_id,
    event_date,
    event_name
FROM users_events_per_day
CROSS JOIN UNNEST(events_per_day) AS event_name;