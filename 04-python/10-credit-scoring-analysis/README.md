# Credit Scoring Model: Application Rating System

## Project Overview
This project implements a simplified credit scoring engine using Python and Pandas. The goal was to process loan applications, enrich them with industry-specific data, and calculate a multi-criteria reliability rating for each applicant.

## Key Technical Operations:
* **Data Cleansing:** Handled duplicates in applicant IDs and implemented strategic null-filling (zero-fill for ratings, text-fill for education levels).
* **Data Merging:** Combined application data with industry risk scores using relational joins.
* **Complex Scoring Logic:** Developed a 100-point rating system based on 6 distinct criteria:
    * Demographics (Age, Marital Status).
    * Geography (Location-based weights).
    * Timing (Weekday vs. Weekend application submission).
    * External Credit Ratings & Industry Risk Scores.
* **Advanced Pandas Techniques:** Utilized boolean masking and vectorization for efficient rating calculation (avoiding slow loops).
* **Time-Series Aggregation:** Grouped successful applications by submission week to analyze average quality trends.

## Deliverables
* `Credit_Scoring_Assignment.ipynb`: Complete Jupyter Notebook with the scoring engine implementation.

🔗 **Live Version:** [Google Colab/Jupyter Link](https://colab.research.google.com/drive/1hXdw429oGRnMdFfFVoTaM7X3z4Q5tIaL?usp=sharing)

Note: This project was completed as part of the GoIT Data Analysis course.
