import pandas as pd

# Create the DataFrame with the given data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'HR'],
    'Salary': [45000, 54000, 50000, 62000, 47000]
}

df = pd.DataFrame(data)

# a. Print the first five rows of the DataFrame
first_five_rows = df.head()
print("First Five rows of the DataFrame:")
print(first_five_rows)

# b. Get the summary statistics of the 'Age' and 'Salary' columns
summary_statistics = df[['Age', 'Salary']].describe()
print("\nSummary statistics of 'Age' and 'Salary':")
print(summary_statistics)

# c. Calculate the average salary of employees in the 'HR' department and add 'Bonus' column (10% of salary)
average_salary_hr = df[df['Department'] == 'HR']['Salary'].mean()
df['Bonus'] = df['Salary'] * 0.10

# 3. Filter the DataFrame to show employees aged between 25 and 30
filtered_by_age = df[(df['Age'] >= 25) & (df['Age'] <= 30)]
print("\nEmployees aged between 25 and 30:")
print(filtered_by_age)

# 4. Group the data by 'Department' and calculate the average salary for each department
avg_salary_by_dept = df.groupby('Department')['Salary'].mean()
print("\nAverage salary by department:")
print(avg_salary_by_dept)

# 5. Sort the DataFrame by 'Salary' in ascending order and save the result to a new CSV file
sorted_df = df.sort_values(by='Salary', ascending=True)
sorted_df.to_csv('sorted_employees.csv', index=False)
print("\nData sorted by salary and saved to 'sorted_employees.csv'")
