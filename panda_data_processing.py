import pandas as pd
import glob, ast
import json, re


def read_txt():
    log_file = open('D:/data/indeed_test/5b387050885711eda7780225a990f764.log', 'r', encoding='utf8')
    content = log_file.readlines()
    return content


def fetch_data(content):
    search_str = ['BOT_NAME', 'LOG_FILE']
    pattern = '[{?,(/)%&$#@!~]'
    bot = {}
    new_bot = {}
    for line in content:
        if any(word in line for word in search_str):
            new_line = re.sub(pattern, '', line)
            key, value = map(str.strip, new_line.split(':'))
            bot[key] = value
            for key, val in bot.items():
                new_key = key.replace("'", "")
                new_val = val.replace("'", "")
                new_bot[new_key] = new_val
    return new_bot


def to_dataframe(new_bot):
    df = pd.DataFrame.from_dict(new_bot, orient='index')
    return df


if __name__ == '__main__':
    file_content = read_txt()
    to_df = fetch_data(file_content)
    to_csv = to_dataframe(to_df)
    print(to_csv.index)
    print(to_csv.values)

# match = re.(search_str, line)
# if match:
#     # new_line = re.sub(pattern, '', line)
#     # nl = new_line.replace(':', '')
#     print(match)

# match = re.findall(r'\{ ([^{}]+) \} (?=\()', line)
# if match:
#     print(match)
#     break

# json_lines = [line.strip() for line in file_content if re.match(r'^\s*{.*}\s*$', line)]
# json_content = '\n'.join(json_lines)
# json_content_fixed = re.sub(r'\'', '"', json_content)
# file_content_fixed = file_content.replace(r'\'', '\"')
# file_content_fixed = re.sub(r'\s*}\s*', '}\n', re.sub(r'\'', '"', file_content))
# pattern = re.compile(r'\{.*?\}')
# matches = pattern.findall(json_content_fixed)
# data_list = []
# for match in matches:
#     data_dict = json.loads(match)
#     data_list.append(data_dict)
# df = pd.DataFrame(data_list)
# print(df)




