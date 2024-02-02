import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def data_check_for_null():
    # Load the data and check if it consist of any missing data or not?
    # Horizontal Bar chart
    telcom = pd.read_csv('D:/data/telcom1.csv')

    plt.style.use('classic')

    # missing_values = pd.DataFrame(telcom.head(), columns=['state', 'account length', 'area code', 'phone number', 'international plan'])
    telcom.isnull().any()
    # nn_cols = [col for col in missing_values.columns if missing_values[col].notnull().any()]
    not_missing_count = telcom.notna().sum()
    # cols = [col for col in missing_values.columns if missing_values[col].isnull().any()]
    missing_count = telcom.isna().sum()
    y_indexes = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40])
    width = 0.5
    plt.barh(y_indexes, missing_count.values, color='r', label='Values missing')
    plt.barh(y_indexes+width, not_missing_count.values, color='b', label='Values not missing')
    plt.xlim([0, 10])
    plt.title('Missing data')
    plt.xlabel('Count of missing values')
    plt.ylabel('Columns')
    plt.yticks(ticks=y_indexes+width, labels=missing_count.index)
    plt.tight_layout()
    plt.legend()
    plt.show()


telcom = pd.read_csv('D:/data/telcom.csv')


def state_wise_distribution():
    # Show state wise distribution
    # Stem chart
    plt.style.use('classic')

    state_wise_distr = telcom['state'].value_counts()

    plt.stem(state_wise_distr.index, state_wise_distr.values)
    plt.title('State Wise Distribution')
    plt.xlabel('State')
    plt.ylabel('Distribution')
    plt.tight_layout()
    plt.show()


def call_distribution_churn_wise():
    # Show Churn wise distribution of the calls for morning, evening & night calls
    # Line chart
    plt.style.use('ggplot')

    churn_f = telcom.loc[~telcom.churn]
    morning_calls_f = churn_f['total day calls'].sum()
    evening_calls_f = churn_f['total eve calls'].sum()
    night_calls_f = churn_f['total night calls'].sum()

    churn_t = telcom.loc[telcom.churn]
    morning_calls_t = churn_t['total day calls'].sum()
    evening_calls_t = churn_t['total eve calls'].sum()
    night_calls_t = churn_t['total night calls'].sum()

    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
    slices1 = [morning_calls_f, evening_calls_f, night_calls_f]
    slices2 = [morning_calls_t, evening_calls_t, night_calls_t]
    labels1 = ['Morning', 'Evening', 'Night']

    ax1.plot(labels1, slices1, color='k', label='Churn = False')
    ax1.set_title('Churn wise distribution of the calls for morning, evening & night calls')
    ax1.set_ylabel('Total calls')
    ax1.legend(loc='upper right')

    ax2.plot(labels1, slices2, color='b', label='Churn = True')
    ax2.set_xlabel('Call Time Period')
    ax2.set_ylabel('Total calls')
    ax2.legend(loc='upper right')

    plt.tight_layout()
    plt.show()


def voicemail_count_by_churn():
    # Count of voicemail plan by churn
    # Bar chart
    plt.style.use('ggplot')

    churn_f_voicemail = telcom.loc[~telcom.churn]
    voicemail_f_count = churn_f_voicemail['voice mail plan'].value_counts()

    churn_t_voicemail = telcom.loc[telcom.churn]
    voicemail_t_count = churn_t_voicemail['voice mail plan'].value_counts()

    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

    ax1.bar(voicemail_f_count.index, voicemail_f_count.values, width=0.25, color='b', label='Churn = False')
    ax1.set_title('Count of voicemail plan by churn')
    ax1.set_ylabel('Voice-mail Count')
    ax1.legend()

    ax2.bar(voicemail_t_count.index, voicemail_t_count.values, width=0.25, color='r', label='Churn = True')
    ax2.set_xlabel('Voice mail Plan')
    ax2.set_ylabel('Voice-mail Count')
    ax2.legend()

    plt.tight_layout()
    plt.show()


def top_5_states_account_length_wise():
    # Top 5 states account length wise
    # stem chart
    plt.style.use('ggplot')

    # state_wise_top_5 = telcom[['state', 'account length']].sort_values(by='account length', ascending=False)
    # print('Top 5 states account length wise :\n', state_wise_top_5.values[0:5, 0], state_wise_top_5.values[0:5, 1])
    # x_axis = state_wise_top_5.values[0:5, 0]
    # y_axis = state_wise_top_5.values[0:5, 1]

    length_wise = telcom.groupby('state')['account length'].sum()
    top_5 = length_wise.sort_values(ascending=False).head()

    plt.stem(top_5.index, top_5.values)
    plt.title('Top 5 states account length wise')
    plt.xlabel('States')
    plt.ylabel('Account Length')
    plt.tight_layout()
    plt.show()


def total_call_charges():
    # Total charge by morning, evening & night
    # Horizontal Bar chart
    plt.style.use('seaborn-v0_8-dark')

    morning_charge = telcom['total day charge'].sum()
    morning_charge = round(morning_charge, 2)

    evening_charge = telcom['total eve charge'].sum()
    evening_charge = round(evening_charge, 2)

    night_charge = telcom['total night charge'].sum()
    night_charge = round(night_charge, 2)

    plt.barh(['Morning'], morning_charge, label='Morning', color='k')
    plt.barh(['Evening'], evening_charge, label='Evening', color='r')
    plt.barh(['Night'], night_charge, label='Night', color='y')
    plt.title('Total charge by morning, evening & night')
    plt.xlabel('Total Charges')
    plt.ylabel('Call Time')
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':

    print('''1. Load the data and check if it consist of any missing data or not?
2. Show state wise distribution
3. Show Churn wise distribution of the calls for morning, evening & night calls
4. Count of voicemail plan by churn
5. Top 5 states account length wise
6. Total charge by morning, evening & night''')

    choice = int(input('Enter your choice: '))

    match choice:
        case 1:
            data_check_for_null()
        case 2:
            state_wise_distribution()
        case 3:
            call_distribution_churn_wise()
        case 4:
            voicemail_count_by_churn()
        case 5:
            top_5_states_account_length_wise()
        case 6:
            total_call_charges()
