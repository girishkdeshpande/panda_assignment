import pandas as pd
import glob, re, ast, json, numpy as np


def read_txt():
    json_data = {}
    count = 0
    all_files = glob.iglob('D:/data/**/*.log', recursive=True)
    for files in all_files:
        count += 1
        file_read = open(files, 'r', encoding='utf8')
        file_lines = file_read.read()
        # pattern = re.compile('([^{]*?)(?=\})')
        # matches = pattern.search(file_lines)
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
                    key, val = line.split(':')
                    if key not in json_data:
                        json_data[key] = []
                    json_data[key].append(val)

    print(count)
    return json_data


def json_to_df(into_json):
    df = pd.DataFrame.from_dict(into_json, orient='index')
    df = df.transpose()
    return df


if __name__ == '__main__':
    data = read_txt()
    # str_to_json = data_to_str(data)
    to_df = json_to_df(data)
    print(to_df)
