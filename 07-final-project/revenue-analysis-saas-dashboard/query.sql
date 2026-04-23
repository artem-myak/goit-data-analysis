WITH user_monthly_revenue AS 
(
    SELECT 
        gp.user_id,
        gp.game_name,
        DATE_TRUNC('month', gp.payment_date) AS payment_month,
        SUM(gp.revenue_amount_usd) AS total_revenue,
        gpu.age,
        gpu."language" 
    FROM project.games_payments gp
    LEFT JOIN project.games_paid_users gpu 
    ON gp.user_id = gpu.user_id 
    GROUP BY 1, 2, 3, 5, 6 
),

revenue_lag AS 
(
    SELECT 
        *,
        LAG(payment_month) OVER(PARTITION BY user_id ORDER BY payment_month) AS previous_paid_month,
        LEAD(payment_month) OVER(PARTITION BY user_id ORDER BY payment_month) AS next_paid_month,
        DATE(payment_month + INTERVAL '1 month') AS next_calendar_month,
        DATE(payment_month - INTERVAL '1 month') AS prev_calendar_month,
        LAG(total_revenue) OVER(PARTITION BY user_id ORDER BY payment_month) AS previous_revenue,
        LEAD(total_revenue) OVER(PARTITION BY user_id ORDER BY payment_month) AS future_revenue
    FROM user_monthly_revenue
),

mrr_metrics AS
(
    SELECT 
        *,
        CASE WHEN previous_paid_month IS NULL 
            THEN total_revenue ELSE 0 END AS new_mrr,
        CASE WHEN previous_paid_month IS NULL 
            THEN 1 ELSE 0 END AS new_paid_users,
        1 AS paid_users,
        CASE WHEN (previous_paid_month = prev_calendar_month) AND (total_revenue > previous_revenue)
            THEN total_revenue - previous_revenue ELSE 0 END AS expansion_mrr,
        CASE WHEN (previous_paid_month = prev_calendar_month) AND (total_revenue < previous_revenue)
            THEN previous_revenue - total_revenue ELSE 0 END AS contraction_mrr,
        CASE WHEN (next_paid_month IS NULL) OR (next_paid_month != next_calendar_month)
            THEN total_revenue ELSE 0 END AS churned_revenue,
        CASE WHEN (next_paid_month IS NULL) OR (next_paid_month != next_calendar_month)
            THEN 1 ELSE 0 END AS churned_users,
        CASE WHEN (next_paid_month IS NULL) OR (next_paid_month != next_calendar_month)
            THEN next_calendar_month END AS churn_month             
    FROM revenue_lag
)

SELECT * FROM mrr_metrics;