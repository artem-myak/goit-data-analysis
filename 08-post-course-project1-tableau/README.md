# Coffee Sales & Financial Performance Analysis ☕📈

## 📌 Project Overview
This project presents a comprehensive analysis of a coffee retail network's performance data (2011-2014). The goal was to transform raw sales data into a strategic tool for executive decision-making, focusing on customer trends, market distribution, and financial health.

The analysis is presented as a two-page interactive dashboard built in **Tableau**, optimized for professional aesthetics and actionable business insights.

> **🔗 [View Interactive Dashboard on Tableau Public](https://public.tableau.com/shared/22C3PDHN6?:display_count=n&:origin=viz_share_link)**

---

## 📊 Key Business Questions Addressed
* **Market Presence:** Which countries and product categories drive the highest revenue and profit?
* **Financial Health:** What is the trend of **ARPPU** (Average Revenue Per Paying User) and overall profitability?
* **Growth Stability:** How do current monthly sales compare to the 12-month moving average?
* **Risk Identification:** Are there significant downward trends where profit margins fall below critical thresholds?

---

## 🛠 Technical Features & Implementation

### 1. Advanced Data Visualization
* **Dual Axis Charts:** Combined Profit and ARPPU to visualize the correlation between volume and per-user value.
* **Variance Analysis (MoM):** Bar charts showing Month-over-Month sales changes with Red/Blue color coding.
* **Trend Analysis:** Integrated Linear Regression trend lines and **12-month Moving Averages** to smooth out seasonality.

### 2. Complex Calculations
* **LOD Expressions & Table Calcs:** Implementation of advanced formulas for ARPPU, Profit Margin %, and Variance.
* **Conditional Logic:** Created a KPI-based coloring system for margin monitoring:
    * 🟢 **Green:** High Profitability (>10.5%)
    * 🟡 **Yellow:** Target Range (9.5% - 10.5%)
    * 🔴 **Red:** Low Profitability (<9.5%)

### 3. UX/UI Optimization
* **Executive Design:** Clean, distraction-free interface with a consistent color palette and typography.
* **Interactive Navigation:** Seamless switching between *Market Overview* and *Financial Trends* using dashboard actions.
* **Global Filtering:** Synchronized filters across all dashboards for deep-dive analysis by Roast and Coffee type.

---

## 💡 Key Analytical Insights
* **Negative Convergence:** Identified a parallel decline in both **Total Profit** and **ARPPU** over the final fiscal year, signaling a potential issue with customer loyalty or a shift toward cheaper products.
* **Profitability Benchmarking:** The business consistently operates in the "Yellow Zone" (approx. 10% margin). While stable, this suggests thin margins that are highly sensitive to operational cost increases.
* **Market Opportunity:** Specific roast types showed high resilience in the UK market compared to the USA, providing a template for regional strategy optimization.

---

## 📂 Project Structure
* `/images` — Screenshots of the final dashboards.
* `project1.twbx` — Tableau Workbook file.
* `README.md` — Project documentation and summary.

---

### 🛠 Tools Used
**Tableau Desktop** | **MS Excel** | **Data Modeling** | **Business Intelligence**
