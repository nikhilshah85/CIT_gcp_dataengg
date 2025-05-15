# Import the pandas library to create a DataFrame
import pandas as pd

# Create a dictionary with employee data
employee_data = {
    "empno": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "firstname": ["John", "Emma", "Michael", "Sophia", "William", "Olivia", "James", "Ava", "George", "Isabella", "Charles", "Mia", "Frank", "Charlotte", "Robert", "Amelia", "Richard", "Harper", "Thomas", "Evelyn"],
    "lastname": ["Doe", "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez"],
    "designation": ["Software Engineer", "Data Scientist", "Product Manager", "Marketing Manager", "Sales Manager", "HR Manager", "Finance Manager", "Operations Manager", "IT Manager", "Customer Support", "Business Analyst", "Data Analyst", "Software Developer", "Quality Assurance", "DevOps Engineer", "UX Designer", "Technical Writer", "Graphic Designer", "Network Administrator", "Database Administrator"],
    "salary": [80000, 90000, 100000, 110000, 120000, 130000, 140000, 150000, 160000, 170000, 180000, 190000, 200000, 210000, 220000, 230000, 240000, 250000, 260000, 270000]
}

# Create a DataFrame from the dictionary
employee_df = pd.DataFrame(employee_data)

# Print the DataFrame
print(employee_df)

def increase_salary(df):
    """
    Increase the salary values in the DataFrame by 10%.
    
    Parameters:
    df (pandas DataFrame): The DataFrame containing the employee data.
    
    Returns:
    pandas DataFrame: The updated DataFrame with increased salary values.
    """
    df['salary'] = df['salary'].apply(lambda x: x * 1.10)
    return df

# Call the function to update the salary values
employee_df = increase_salary(employee_df)

# Print the updated DataFrame
print(employee_df)