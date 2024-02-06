import pandas as pd
import glob, re


def string_read():
    bot = {}
    not_in_file = []
    count = 0
    total_files = glob.iglob('D:/data/zippia/*.log', recursive=True)
    for files in total_files:
        count += 1
        log_file = open(files, 'r', encoding='utf8')
        content = log_file.readlines()
        search_str = ['BOT_NAME', 'LOG_FILE']
        pattern = '[{?,()%&$#@''!~]'
        for line in content:
            if any(word in line for word in search_str):
                new_line = re.sub(pattern, '', line)
                key, value = map(str.strip, new_line.split(':'))
                if key not in bot:
                    bot[key] = []
                bot[key].append(value)

    print(count)
    return bot


def data_read():
    json_data = {}
    not_in_file = []
    count = 0
    all_files = glob.iglob('D:/data/**/*.log', recursive=True)
    for files in all_files:
        count += 1
        pattern = '[{?,%&$#@!~' ']'
        log_file = open(files, 'r', encoding='utf8')
        file_lines = log_file.read()
        start_str = 'Dumping Scrapy stats:'
        end_str = 'Spider closed'
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
                in_between_data = ''.join(list(in_between_data)).split('\n')
                for line in in_between_data:
                    new_line = re.sub(pattern, '', line)
                    key, val = map(str.strip, new_line.split(':'))
                    if key not in json_data:
                        json_data[key] = []
                    json_data[key].append(val)
        else:
            not_in_file.append(files)

    print(count)
    return json_data, not_in_file


if __name__ == '__main__':
    str_obj = string_read()
    # data_obj, file_obj = data_read()
    # print(data_obj)
    # str_obj.update(data_obj)
    # club_dict = str_obj | data_obj
    df = pd.DataFrame.from_dict(str_obj)
    print(df)
    # df = df.transpose()
    # df.to_csv(r'C:\Users\girish.deshpande\Desktop\secondcsv.csv', index=False)

