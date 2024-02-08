import pandas as pd
import glob, re
import os
from datetime import datetime as dt


def read_fetch_data():
    search_str1 = ['BOT_NAME', 'LOG_FILE']
    # search_str2 = 'LOG_FILE'
    search_str3 = 'Dumping Scrapy stats:'
    search_str4 = 'Spider closed'
    pattern = '[{?,()%&$#@"!~]'
    new_line = ''
    string_presence, string_absence = [], []
    stat_presence,  stat_absence = [], []
    counter = 0

    # Reading files from folder
    all_files = glob.iglob('D:/data/indeed/*.log', recursive=True)
    for file in all_files:
        log_file = open(file, 'r', encoding='utf8')
        content = log_file.readlines()

        # Searching string 'BOT_NAME' & 'LOG_FILE' in file
        for line in content:
            if any(word in line for word in search_str1):
                new_line = re.sub(pattern, '', line)
                string_presence.append(new_line)

        if new_line == '':
            string_absence.append(file)

        print(f'Data not present in file - {string_absence}')

        # Searching stat data in file
        start_line = next((i for i, line in enumerate(content, start=1) if search_str3 in line), None)
        end_line = next((i for i, line in enumerate(content, start=1) if search_str4 in line), None)

        if start_line is not None and end_line is not None:
            data_between_strings = content[start_line:end_line-1]
            result = ''.join(data_between_strings).strip()
            stat_presence.append(result)
        else:
            stat_absence.append(file)

        counter += 1

    print(counter)
    # print(f'Data not present in file - {stat_absence}')
    return string_presence, string_absence, stat_presence, stat_absence


def date_parser(val):
    val = val.strip('datetime.').replace('(', '"').replace(')', '"').replace('"', '')
    new_val = re.split(',', val)
    date_components = [int(component) if component.isdigit() else 0 for component in new_val[:-1]]
    date_object = dt(*date_components)
    formatted_date = date_object.strftime("%Y-%m-%d %H:%M:%S.%f")
    return formatted_date


def file_data_processing(string_presence_data, string_absence_data, stat_presence_data, stat_absence_data):

    str_ab_data = string_absence_data
    stat_ab_data = stat_absence_data

    pattern = '[}{?%&$#@!~' ']'
    bot = {}
    json_data = {}

    if string_presence_data:
        for string in string_presence_data:
            key, value = map(str.strip, string.split(':'))
            key = key.replace("'", '')
            value = value.replace("'", '')
            if key not in bot:
                bot[key] = []
            bot[key].append(value)

    # if string_absence_data:
    #     for item in string_absence_data:
    #         print(item)

    if stat_presence_data:
        for stat in stat_presence_data:
            new_line = re.sub(pattern, '', stat).replace("'", '').replace(' ', '')
            fixed_line = ''.join(list(new_line)).split('\n')
            for line in fixed_line:
                key, val = map(str.strip, line.split(':'))
                val = val.strip(',').replace("'", '')
                key = key.replace("'", '')

                if key.__contains__("finish_time") or key.__contains__("start_time"):
                    val = date_parser(val)

                if key not in json_data:
                    json_data[key] = []
                json_data[key].append(val)

    # if stat_absence_data:
    #     for item in stat_absence_data:
    #         print(item)

    return bot, str_ab_data, json_data, stat_ab_data


if __name__ == '__main__':
    str_p, str_a, stat_p, stat_a = read_fetch_data()
    str_data_p, str_data_a, stat_data_p, stat_data_a = file_data_processing(str_p, str_a, stat_p, stat_a)
    str_data_p.update(stat_data_p)
    df = pd.DataFrame.from_dict(str_data_p, orient='index')
    df = df.transpose()
    print(df)
    # df.to_csv(r'C:\Users\girish.deshpande\Desktop\fixedcsv.csv', index=False)

    for str_item in str_data_a:
        print('String BOT_NAME & LOG_FILE not found in below files:\n')
        print(str_item)

    for stat_item in stat_data_a:
        print('Stats not found in below files:\n')
        print(stat_item)


