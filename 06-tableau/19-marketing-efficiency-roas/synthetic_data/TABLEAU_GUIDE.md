# Tableau Analytics Guide for Synthetic E-Commerce Data

## Quick Start

### Importing Data into Tableau

1. Open Tableau Desktop
2. Connect to Data → Text File
3. Import the three CSV files:
   - `user_events.csv`
   - `transactions.csv`
   - `marketing_spend.csv`

## Data Relationships Setup

Create the following relationships in Tableau:

```
user_events.user_id = transactions.user_id
DATE(user_events.event_timestamp) = marketing_spend.date
transactions.order_date = marketing_spend.date
```

## Analytics Dashboards

### 1. Conversion Funnel Analysis

**Data Source:** `user_events.csv`

**Calculated Fields:**

```tableau
// Count by Event Type
IF [event_type] = 'page_view' THEN 1 ELSE 0 END
IF [event_type] = 'product_viewed' THEN 1 ELSE 0 END
IF [event_type] = 'add_to_cart' THEN 1 ELSE 0 END
IF [event_type] = 'initiate_checkout' THEN 1 ELSE 0 END
IF [event_type] = 'purchase' THEN 1 ELSE 0 END

// Conversion Rate
SUM([Purchases]) / SUM([Page Views])
```

**Visualizations:**
- Funnel chart showing progression from page_view → purchase
- Conversion rates between each step
- Drop-off analysis by session

**Expected Results:**
- Page Views: 5,451
- Product Viewed: 3,835 (70.4%)
- Add to Cart: 1,756 (32.2%)
- Initiate Checkout: 625 (11.5%)
- Purchase: 396 (7.3%)

---

### 2. Cohort Analysis

**Data Sources:** `user_events.csv` + `transactions.csv`

**Calculated Fields:**

```tableau
// Cohort Month (Account Creation)
DATETRUNC('month', [event_timestamp]) WHERE [event_type] = 'account_created'

// Months Since Signup
DATEDIFF('month', [Cohort Month], [order_date])

// Cohort Size
COUNTD([user_id]) WHERE [event_type] = 'account_created'

// Retention Rate
COUNTD([user_id] WITH PURCHASES) / [Cohort Size]
```

**Visualizations:**
- Cohort retention matrix (heatmap)
- Revenue by cohort over time
- Average orders per cohort
- Customer lifetime value trend

**Key Insights:**
- 148 out of 200 users (74%) made at least one purchase
- Average 10.2 orders per purchasing user
- Track monthly cohorts over 24 months

---

### 3. ROAS (Return on Ad Spend) Analysis

**Data Sources:** `marketing_spend.csv` + `transactions.csv`

**Calculated Fields:**

```tableau
// Total Revenue
SUM([total_amount] - [discount_amount])

// Total Ad Spend
SUM([spend_amount])

// ROAS
[Total Revenue] / [Total Ad Spend]

// Revenue by Channel
SUM([total_amount]) WHERE [acquisition_channel] = 'paid_search'
```

**Visualizations:**
- ROAS by channel (bar chart)
- Spend vs Revenue scatter plot
- Daily ROAS trend line
- Channel mix pie chart

**Expected Metrics:**
- Total Revenue: $985,908.87 (net of discounts)
- Total Spend: $10,517,908.21
- Overall ROAS: 0.09 (or 9%)
- Best performing channels can be identified

**Breakdown by Channel:**
- Paid Search: $4,244,363.99
- Paid Social: $3,465,347.90
- Social Media: $2,027,100.19
- Email: $416,900.41
- Referral: $243,800.58
- Organic: $120,395.14

---

### 4. CAC (Customer Acquisition Cost)

**Data Sources:** `marketing_spend.csv` + `user_events.csv`

**Calculated Fields:**

```tableau
// New Users
COUNTD([user_id]) WHERE [event_type] = 'account_created'

// CAC
[Total Ad Spend] / [New Users]

// CAC by Channel
SUM([spend_amount]) / COUNTD([user_id] WHERE [event_type] = 'account_created')
```

**Visualizations:**
- CAC by channel (horizontal bar)
- CAC trend over time (line chart)
- CAC vs LTV comparison
- Country comparison

**Analysis:**
- 200 total users acquired
- Calculate CAC per channel
- Compare paid vs organic acquisition costs

---

### 5. Customer Lifetime Value (CLV)

**Data Source:** `transactions.csv`

**Calculated Fields:**

```tableau
// Average Order Value
SUM([total_amount]) / COUNTD([order_id])

// Orders per Customer
COUNTD([order_id]) / COUNTD([user_id])

// Customer Lifetime Value
[Average Order Value] * [Orders per Customer]

// Purchase Frequency
COUNTD([order_id]) / COUNTD([user_id])
```

**Visualizations:**
- CLV distribution histogram
- Repeat purchase rate
- Average time between orders
- Top customers by revenue

**Expected Metrics:**
- Average Order Value: $679.31
- Average Orders per User: 10.2
- Estimated CLV: $6,929.36

---

### 6. Churn Analysis

**Data Sources:** `user_events.csv` + `transactions.csv`

**Calculated Fields:**

```tableau
// Days Since Last Purchase
DATEDIFF('day', MAX([order_date]), TODAY())

// At Risk (No purchase in 90+ days)
IF [Days Since Last Purchase] > 90 THEN 'At Risk' ELSE 'Active' END

// Churn Rate
COUNT([At Risk Users]) / COUNTD([user_id])
```

**Visualizations:**
- Churn rate by cohort
- Time to second purchase (histogram)
- Reactivation campaigns targeting
- Customer status segmentation

**Segments:**
- Active: Recent purchase (< 30 days)
- At Risk: No purchase (30-90 days)
- Churned: No purchase (> 90 days)

---

### 7. Product Performance

**Data Source:** `transactions.csv`

**Calculated Fields:**

```tableau
// Revenue by Category
SUM([total_amount]) BY [product_category]

// Quantity Sold
SUM([quantity])

// Average Unit Price
AVG([unit_price])

// Discount Impact
SUM([discount_amount]) / SUM([total_amount])
```

**Visualizations:**
- Revenue by category (tree map)
- Top products by revenue (bar chart)
- Discount analysis
- Order status breakdown

**Category Distribution:**
- Electronics: 267 orders
- Beauty: 260 orders
- Books: 258 orders
- Home: 251 orders
- Clothing: 251 orders
- Sports: 220 orders

---

### 8. Marketing Performance Dashboard

**Data Source:** `marketing_spend.csv`

**Calculated Fields:**

```tableau
// CTR (Click-Through Rate)
SUM([clicks]) / SUM([impressions])

// CPC (Cost Per Click)
SUM([spend_amount]) / SUM([clicks])

// CPM (Cost Per Thousand Impressions)
(SUM([spend_amount]) / SUM([impressions])) * 1000
```

**Visualizations:**
- Daily spend trend (area chart)
- CTR by channel (line chart)
- Impressions and clicks (dual axis)
- Geographic performance map

**Expected Metrics:**
- Total Impressions: 10.5 billion
- Total Clicks: 314.7 million
- Overall CTR: 3.00%
- 731 days of data (2 years)

---

## Dashboard Filters

Create the following filters for interactive exploration:

1. **Date Range Filter**
   - Field: `event_timestamp`, `order_date`, or `date`
   - Type: Date range slider

2. **Channel Filter**
   - Field: `acquisition_channel`
   - Type: Multi-select dropdown

3. **Product Category Filter**
   - Field: `product_category`
   - Type: Multi-select checkbox

4. **Country Filter**
   - Field: `country`
   - Type: Single select

5. **User Segment Filter**
   - Field: Custom calculated field for user segments
   - Type: Multi-select

---

## Advanced Analytics

### 1. Time-Series Forecasting

Use Tableau's built-in forecasting on:
- Daily revenue trends
- User acquisition rate
- Order volume

### 2. Clustering Analysis

Segment users by:
- Purchase frequency
- Average order value
- Product category preferences
- Time between purchases

### 3. Statistical Analysis

- Correlation between marketing spend and revenue
- Seasonality analysis (Q4 has higher spend)
- Day of week patterns

---

## Sample Calculated Fields

```tableau
// Overall Conversion Rate
COUNTD([user_id] WHERE [event_type] = 'purchase') /
COUNTD([user_id] WHERE [event_type] = 'account_created')

// Revenue per Session
SUM([total_amount]) / COUNTD([session_id])

// Average Days to First Purchase
AVG(DATEDIFF('day',
    MIN([event_timestamp] WHERE [event_type] = 'account_created'),
    MIN([order_date])))

// Repeat Purchase Rate
COUNTD([user_id] WHERE COUNTD([order_id]) > 1) / COUNTD([user_id])

// Order Status Rate
COUNTD([order_id] WHERE [order_status] = 'completed') / COUNTD([order_id])
```

---

## Tips for Best Results

1. **Date Alignment**: Ensure dates are properly formatted as date fields in Tableau
2. **Relationships**: Use relationships instead of joins for better performance
3. **LOD Expressions**: Use Level of Detail calculations for complex aggregations
4. **Parameters**: Create parameters for dynamic thresholds (e.g., churn days, CAC targets)
5. **Actions**: Add dashboard actions for drill-down analysis
6. **Tooltips**: Enhance tooltips with relevant calculated fields
7. **Color Coding**: Use consistent color schemes for metrics (green for good, red for concerning)

---

## Expected Dashboard KPIs

### Executive Summary Dashboard

| Metric | Value |
|--------|-------|
| Total Users | 200 |
| Conversion Rate | 74% |
| Total Revenue | $1,023,723.92 |
| Average Order Value | $679.31 |
| Total Orders | 1,507 |
| Marketing Spend | $10,517,908.21 |
| Overall ROAS | 0.09 (9%) |
| Customer Lifetime Value | $6,929.36 |

### Funnel Metrics

| Stage | Count | Conversion Rate |
|-------|-------|-----------------|
| Page Views | 5,451 | 100% |
| Product Viewed | 3,835 | 70.4% |
| Add to Cart | 1,756 | 32.2% |
| Checkout | 625 | 11.5% |
| Purchase | 396 | 7.3% |

---

## Troubleshooting

**Issue:** Dates not joining correctly
- **Solution:** Use DATETRUNC to normalize dates to day level

**Issue:** Duplicate counts
- **Solution:** Use COUNTD instead of COUNT for unique counts

**Issue:** Performance issues
- **Solution:** Create extracts instead of live connections, add filters

**Issue:** Missing values
- **Solution:** Handle nulls with IFNULL or ZN functions

---

## Next Steps

1. Import all three CSV files into Tableau
2. Set up data relationships
3. Create calculated fields for key metrics
4. Build individual worksheets for each analysis
5. Combine into dashboards with filters
6. Add interactivity with actions
7. Share with stakeholders

Happy analyzing!
