#  A/B Testing – Web UI Improvement

This project simulates an A/B testing scenario using Python and Excel to analyze the impact of a new website UI on user conversion rates.

---

##  Objective

To determine whether the new website design (Group B) performs better than the original design (Group A) in terms of user conversions, using statistical testing.

---

##  Project Files

| File | Description |
|------|-------------|
| `ab_testing.py` | Python script to simulate visitor data and perform hypothesis testing |
| `ab_test_data.csv` | Generated dataset of 10,000 website visitors split into Group A and Group B |
| `A-B Test Results.xlsx` | Excel file showing summarized metrics and final analysis dashboard |
| `Screenshots/` | Before/After screenshots of Excel dashboard and terminal output |

---

##  Tools & Libraries

- Python (Pandas, NumPy, Statsmodels)
- Microsoft Excel / Google Sheets
- A/B Testing
- Z-Test for Proportions

---

##  Methodology

1. **Simulated 10,000 visitors** randomly assigned to Group A and Group B.
2. Assigned conversion rates:
   - Group A: 10%
   - Group B: 12%
3. **Calculated conversion counts** and performed a **Z-test for proportions**.
4. Created a **summary dashboard in Excel** showing:
   - Total Conversions
   - Total Visitors
   - Conversion Rates
   - Statistical Significance (P-value)

---

##  Results

- **Z-statistic:** `-3.1358`  
- **P-value:** `0.0017`  
-  Result: Statistically significant improvement in Group B

---

##  Screenshots

- Terminal Output of Hypothesis Test
- Excel Summary Dashboard
- Before/After snapshots of Excel analysis

---

##  What I Learned

- How to simulate A/B test data using Python
- How to apply hypothesis testing for conversion analysis
- How to present test results using Excel dashboards
- Importance of statistical significance in decision-making

---

##  Future Improvements

- Use real-world data from analytics tools (e.g., Google Optimize, Mixpanel)
- Try Chi-Square Test for independence
- Create interactive dashboards with Power BI or Tableau


