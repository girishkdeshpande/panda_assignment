import sys

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

employee = pd.read_csv('D:/data/employee.csv')


def choice_response(value):
    plt.style.use('fivethirtyeight')
    match value:
        case 1:
            emp_by_edu = employee['EducationField'].value_counts()
            print(emp_by_edu)

        case 2:
            emp_travel_freq = employee[employee['BusinessTravel'] == 'Travel_Frequently'].head()
            print(emp_travel_freq.to_string(index=False, columns=['Department', 'EmployeeNumber', 'Gender']))

        case 3:
            emp_lives_far = employee[employee['DistanceFromHome'] > 21].head()
            print(emp_lives_far.to_string(index=False, columns=['Department', 'DistanceFromHome', 'EmployeeNumber', 'Gender']))

        case 4:
            emp_most_exp = employee['TotalWorkingYears' 'EmployeeNumber'].sort_values(by='TotalWorkingYears', ascending=False)
            print('Top 5 experienced employees are:\n', emp_most_exp.head())

        case 5:
            age_18_30 = employee[(employee['Age'] >= 18) & (employee['Age'] <= 30)].count()
            print('Employees age range (18-30): \n', age_18_30.values[0])
            age_31_49 = employee[(employee['Age'] >= 31) & (employee['Age'] <= 49)].count()
            print('Employees age range (31-49): \n', age_31_49.values[0])
            age_above_49 = employee[employee['Age'] > 49].count()
            print('Employees age range (above 49): \n', age_above_49.values[0])

        case 6:
            sys.exit()




def select_choice():
    print('''1. Employee count by education field
2. List the employees who travel frequently
3. List the employee who lives far from the office (more than 21 km)
4. Top 5 most experienced employees
5. List the employee age-wise. a) 18-30 b) 31-49 c) 49 above
6. Exit''')

    choice = int(input('Enter your choice: '))
    return choice


if __name__ == '__main__':
    selection = select_choice()
    choice_response(selection)
