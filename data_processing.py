import pandas as pd
import glob, re
from datetime import datetime as dt


def string_read():
    bot = {}
    not_in_file = []
    count = 0
    total_files = glob.iglob('D:/data/indeed_test/5b387050885711eda7780225a990f764.log', recursive=True)
    for files in total_files:
        count += 1
        log_file = open(files, 'r', encoding='utf8')
        content = log_file.readlines()
        search_str = ['BOT_NAME', 'LOG_FILE']
        pattern = '[{?,()%&$#@"!~]'
        for line in content:
            if any(word in line for word in search_str):
                new_line = re.sub(pattern, '', line)
                key, value = map(str.strip, new_line.split(':'))
                key = key.replace("'", '')
                value = value.replace("'", '')
                if key not in bot:
                    bot[key] = []
                bot[key].append(value)
    print(count)
    return bot


def date_parser(val):
    # pattern = r'[datetime.)' '("]'
    val = val.strip('datetime.').replace('(', '"').replace(')', '"').replace(' ', '').replace('"', '')
    new_val = re.split(',', val)
    date_components = [int(component) if component.isdigit() else 0 for component in new_val[:-1]]
    date_object = dt(*date_components)
    formatted_date = date_object.strftime("%Y-%m-%d %H:%M:%S.%f")
    return formatted_date


def data_read():
    json_data = {}
    not_in_file = []
    count = 0
    all_files = glob.iglob('D:/data/indeed_test/5b387050885711eda7780225a990f764.log', recursive=True)

    for files in all_files:
        count += 1
        log_file = open(files, 'r', encoding='utf8')
        file_lines = log_file.read()

        start_str = 'Dumping Scrapy stats:'
        end_str = 'Spider closed'
        pattern = '[{?%&$#@!~' ']'

        start_index = file_lines.find(start_str)
        end_index = file_lines.find(end_str)

        if start_index != -1 and end_index != -1:
            data_between_index = file_lines[start_index + len(start_str):end_index].strip()

            start_pos = '{'
            end_pos = '}'

            start_ind = data_between_index.find(start_pos)
            end_ind = data_between_index.find(end_pos)

            if start_ind != -1 and end_ind != -1:
                in_between_data = data_between_index[start_ind + len(start_pos):end_ind].strip()
                print(type(in_between_data))
                in_between_data = ''.join(list(in_between_data)).split('\n')

                for line in in_between_data:
                    new_line = re.sub(pattern, '', line)
                    key, val = map(str.strip, new_line.split(':'))
                    val = val.strip(',').replace("'", '')
                    key = key.replace("'", '')

                    if key.__contains__("finish_time") or key.__contains__("start_time"):
                        val = date_parser(val)

                    if key not in json_data:
                        json_data[key] = []
                    json_data[key].append(val)

        else:
            not_in_file.append(files)

    print(count)
    return json_data


if __name__ == '__main__':
    str_obj = string_read()
    data_obj = data_read()
    # print(data_obj)
    # str_obj.update(data_obj)
    # club_dict = str_obj | data_obj
    df = pd.DataFrame.from_dict(data_obj, orient='index')
    df = df.transpose()
    print(df)
    # df["'finish_time'"] = pd.to_datetime(df["'finish_time'"], format="mixed")
    # df.to_csv(r'C:\Users\girish.deshpande\Desktop\first5csv.csv', index=False)

