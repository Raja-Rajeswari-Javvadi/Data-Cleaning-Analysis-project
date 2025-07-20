# Student Performance Data Analysis 📊

This project involves data cleaning, transformation, and analysis of student academic performance using **Python**, **Pandas**, **SQL (SQLite)**, and **Seaborn**.

## 📌 Objective
To extract meaningful insights from a student dataset containing grades, subject scores, and attendance rates.

## 💻 Tools & Technologies
- Python
- Pandas, NumPy
- SQL (via SQLite in-memory)
- Seaborn, Matplotlib
- VS Code

## 📊 Key Features
- Cleaned and transformed student data
- Calculated average scores across 6 subjects
- Categorized students based on attendance rate
- SQL queries for grade-wise average analysis
- Visualized insights using Seaborn

## 🔍 Sample SQL Query
```sql
SELECT grade, ROUND(AVG(average_score), 2) AS avg_score
FROM students
GROUP BY grade
ORDER BY avg_score DESC;
