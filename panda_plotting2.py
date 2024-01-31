import pandas as pd
import matplotlib.pyplot as plt
# import numpy as np

telcom = pd.read_csv('D:/data/telcom.csv')


def data_check_for_null():
    # Load the data and check if it consist of any missing data or not?
    # Stack chart
    if telcom.all:
        print('Dataframe consist null columns/rows')
    else:
        print('Dataframe does not consist null columns/rows')


def state_wise_distribution():
    # Show state wise distribution
    # Scatter chart
    state_wise_distr = telcom['state'].value_counts()
    print('State wise distribution :\n', state_wise_distr.head())


def call_distribution_churn_wise():
    # Show Churn wise distribution of the calls for morning, evening & night calls
    # Pie chart
    plt.style.use('ggplot')

    churn_f = telcom.loc[~telcom.churn]
    morning_call_series_f = churn_f['total day calls'].values
    evening_call_series_f = churn_f['total eve calls'].values
    night_call_series_f = churn_f['total night calls'].values
    total_morning_calls_f, total_evening_calls_f, total_night_calls_f = 0, 0, 0
    for morn in morning_call_series_f:
        total_morning_calls_f += morn

    for eve in evening_call_series_f:
        total_evening_calls_f += eve

    for nigt in night_call_series_f:
        total_night_calls_f += nigt

    churn_f_data = [total_morning_calls_f, total_evening_calls_f, total_night_calls_f]
    # print('Total Churn False call wise data', churn_f_data)

    churn_t = telcom.loc[telcom.churn]
    morning_call_series_t = churn_t['total day calls'].values
    evening_call_series_t = churn_t['total eve calls'].values
    night_call_series_t = churn_t['total night calls'].values
    total_morning_calls_t, total_evening_calls_t, total_night_calls_t = 0, 0, 0
    for morn in morning_call_series_t:
        total_morning_calls_t += morn

    for eve in evening_call_series_t:
        total_evening_calls_t += eve

    for nigt in night_call_series_t:
        total_night_calls_t += nigt

    churn_t_data = [total_morning_calls_t, total_evening_calls_t, total_night_calls_t]
    # print('Total Churn True call wise data', churn_t_data)

    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

    slices1 = [churn_f_data[0], churn_f_data[1], churn_f_data[2]]
    labels1 = ['Morning', 'Evening', 'Night']

    slices2 = [churn_t_data[0], churn_t_data[1], churn_t_data[2]]

    ax1.set_title('Churn wise distribution of the calls for morning, evening & night calls')
    ax1.pie(slices1, shadow=True, labels=labels1, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})
    ax1.legend(loc='upper left', title='Churn - False')

    ax2.pie(slices2, shadow=True, labels=labels1, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})
    ax2.legend(loc='lower right', title='Churn - True')

    plt.tight_layout()
    plt.show()


def voicemail_count_by_churn():
    # Count of voicemail plan by churn
    plt.style.use('ggplot')

    churn_f_voicemail = telcom.loc[~telcom.churn]
    voicemail_f_count = churn_f_voicemail['voice mail plan'].value_counts()

    churn_t_voicemail = telcom.loc[telcom.churn]
    voicemail_t_count = churn_t_voicemail['voice mail plan'].value_counts()

    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

    ax1.bar(voicemail_f_count.index, voicemail_f_count.values, color='b', label='Churn = False')
    ax1.set_title('Count of voicemail plan by churn')
    ax1.set_ylabel('Voice-mail Count')
    ax1.legend()

    ax2.bar(voicemail_t_count.index, voicemail_t_count.values, color='r', label='Churn = True')
    ax2.set_xlabel('Voice mail Plan')
    ax2.set_ylabel('Voice-mail Count')
    ax2.legend()

    plt.tight_layout()
    plt.show()


def top_5_states_account_length_wise():
    # Top 5 states account length wise
    # stem chart
    state_wise_top_5 = telcom[['state', 'account length']].sort_values(by='account length', ascending=False)
    print('Top 5 states account length wise :\n', state_wise_top_5.values[0:5, 0], state_wise_top_5.values[0:5, 1])

    # length_wise_top_5 = telcom[['state', 'account length']]
    # length_wise = length_wise_top_5['account length'].value_counts(ascending=False)
    # print('length wise:\n', length_wise.head())


def total_call_charges():
    # Total charge by morning, evening & night
    plt.style.use('seaborn-v0_8-dark')

    morning_charge_series = telcom['total day charge']
    evening_charge_series = telcom['total eve charge']
    night_charge_series = telcom['total night charge']
    morning_charge, evening_charge, night_charge = 0, 0, 0
    for morn in morning_charge_series:
        morning_charge += morn
        morning_charge = round(morning_charge, 2)

    for eve in evening_charge_series:
        evening_charge += eve
        evening_charge = round(evening_charge, 2)

    for nigt in night_charge_series:
        night_charge += nigt
        night_charge = round(night_charge, 2)

    # total_charge = [morning_charge, evening_charge, night_charge]
    # print('Total Charge: ', total_charge)

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
