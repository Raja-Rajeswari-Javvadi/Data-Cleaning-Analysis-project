import pandas as pd
from sqlalchemy import create_engine
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("student_performance.csv")

# Display the first few rows
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Check data types
print(df.dtypes)

# Clean column names: lowercase and replace spaces with underscores
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
print("\nRenamed Columns:\n", df.columns.tolist())  # Check the exact column names

# Check unique grades
print("\nUnique Grades:\n", df['grade'].unique())

# Calculate average score from all subjects
df['average_score'] = df[['mathematics', 'english', 'science', 'history', 'geography', 'physicaleducation']].mean(axis=1)

# Categorize attendance
df['attendance_category'] = df['attendancerate'].apply(
    lambda x: 'Excellent' if x >= 90 else ('Good' if x >= 85 else 'Needs Improvement')
)

# Create an in-memory SQLite engine
engine = create_engine('sqlite://', echo=False)

# Load DataFrame into SQL table
df.to_sql('students', con=engine, index=False, if_exists='replace')

# Query: Average score by grade
avg_score_query = pd.read_sql("""
SELECT grade, ROUND(AVG(average_score), 2) AS avg_score
FROM students
GROUP BY grade
ORDER BY avg_score DESC
""", engine)

print("\nAverage Score by Grade:\n", avg_score_query)

# Plot: Average score by grade
sns.set(style="whitegrid")
sns.barplot(data=avg_score_query, x='grade', y='avg_score', palette='Set2')
plt.title("Average Score by Grade")
plt.ylabel("Average Score")
plt.xlabel("Grade")
plt.tight_layout()
plt.show()
