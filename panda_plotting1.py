import pandas as pd
import matplotlib.pyplot as plt

employee = pd.read_csv('D:/data/employee.csv')


def visual_response(value):
    plt.style.use('fivethirtyeight')
    match value:
        case 1:
            emp_most_exp = employee['TotalWorkingYears'].value_counts()
            x_axis = emp_most_exp.index
            y_axis = emp_most_exp.values
            plt.bar(x_axis, y_axis, color='orange')
            plt.title('Experience Level Distribution')
            plt.xlabel('Experience in Years')
            plt.ylabel('Total employees')
            plt.tight_layout()
            plt.show()

        case 2:
            age_18_30 = employee[(employee['Age'] >= 18) & (employee['Age'] <= 30)].count()
            age_31_49 = employee[(employee['Age'] >= 31) & (employee['Age'] <= 49)].count()
            age_above_49 = employee[employee['Age'] > 49].count()
            labels = ['18-30', '31-49', '49 Above']
            slices = [age_18_30.values[0], age_31_49.values[0], age_above_49.values[0]]
            plt.pie(slices, labels=labels, shadow=True,
                    autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})
            plt.title(' Employee age wise distribution')
            plt.tight_layout()
            plt.legend()
            plt.show()

        case 3:
            emp_attrition = employee['Attrition'].value_counts()
            slices = emp_attrition.values
            labels = emp_attrition.index
            explode = [0, 0.1]
            plt.pie(slices, labels=labels, explode=explode, shadow=True,
                    autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})
            plt.title(' Employee Attrition')
            plt.legend()
            plt.tight_layout()
            plt.show()

        case 4:
            emp_job_satisfaction = employee['JobSatisfaction'].value_counts()
            slices = emp_job_satisfaction.values
            labels = emp_job_satisfaction.index
            plt.pie(slices, labels=labels, shadow=True,
                        autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})
            plt.title('Job Satisfaction Distribution')
            plt.tight_layout()
            plt.legend()
            plt.show()

        case 5:
            width = 0.15
            # gender_wise = employee.groupby('Gender')['Department'].value_counts()
            # print(gender_wise)
            male_wise = employee[employee['Gender'] == 'Male']
            print(male_wise.head())
            male_department_wise = male_wise['Department'].value_counts()
            female_wise = employee[employee['Gender'] == 'Female']
            print(female_wise.head())
            female_department_wise = female_wise['Department'].value_counts()

            x_indexes = np.arange(len(male_department_wise.index))

            plt.bar(x_indexes, male_department_wise.values, width=width, label='Male', color='b')
            plt.bar(x_indexes+width, female_department_wise.values, width=width, label='Female', color='r')

            plt.xlabel('Department')
            plt.ylabel('Gender wise Employees')
            plt.xticks(ticks=x_indexes, labels=male_department_wise.index)
            plt.legend()
            plt.tight_layout()
            plt.show()


def select_choice():
    print('''1. Show the experience level distribution in an organization
2. Employee age wise distribution. a) 18-30 b) 30-49 c) 49 above
3. Show employee attrition
4. Job satisfaction distribution.
5. Department wise distribution over gender''')

    choice = int(input('Enter your choice: '))
    return choice


if __name__ == '__main__':
    selection = select_choice()
    visual_response(selection)
