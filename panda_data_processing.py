import pandas as pd
import glob, ast, re


def file_list():
    bot = {}
    count = 0
    total_files = glob.iglob('D:/data/**/*.log', recursive=True)
    for files in total_files:
        count += 1
        log_file = open(files, 'r', encoding='utf8')
        content = log_file.readlines()
        search_str = ['BOT_NAME', 'LOG_FILE']
        pattern = '[{?,()%&$#@!~]'
        for line in content:
            if any(word in line for word in search_str):
                new_line = re.sub(pattern, '', line)
                key, value = map(str.strip, new_line.split(':'))
                if key not in bot:
                    bot[key] = []
                bot[key].append(value)

    print(count)
    return bot


def to_dataframe(new_bot):
    df = pd.DataFrame.from_dict(new_bot)
    return df


if __name__ == '__main__':
    to_df = file_list()
    df_to_csv = to_dataframe(to_df)
    print(df_to_csv)
    # df_to_csv.to_csv(r'C:\Users\girish.deshpande\Desktop\firstcsv.csv')


# def read_txt():
#     log_file = open('D:/data/indeed_test/5b387050885711eda7780225a990f764.log', 'r', encoding='utf8')
#     content = log_file.readlines()
#     return content
#
#
# def fetch_data(content):
#     search_str = ['BOT_NAME', 'LOG_FILE']
#     pattern = '[{?,(/)%&$#@!~]'
#     bot = {}
#     new_bot = {}
#     for line in content:
#         if any(word in line for word in search_str):
#             new_line = re.sub(pattern, '', line)
#             key, value = map(str.strip, new_line.split(':'))
#             bot[key] = value
#             for key, val in bot.items():
#                 new_key = key.replace("'", "")
#                 new_val = val.replace("'", "")
#                 new_bot[new_key] = new_val
#     return new_bot

    # df_to_csv.to_csv(r'C:\Users\girish.deshpande\Desktop\datatemp.csv')
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

'''
'downloader/request_bytes',
                      'downloader/request_count',
                      'downloader/request_method_count/GET',
                      'downloader/response_bytes',
                      'downloader/response_count',
                      'downloader/response_status_count/200',
                      'downloader/response_status_count/301',
                      'downloader/response_status_count/302',
                      'dupefilter/filtered',
                      'elapsed_time_seconds',
                      'finish_reason',
                      'finish_time',
                      'httpcompression/response_bytes',
                      'httpcompression/response_count',
                      'log_count/DEBUG',
                      'log_count/ERROR',
                      'log_count/INFO',
                      'log_count/WARNING',
                      'memusage/max',
                      'memusage/startup',
                      'request_depth_max',
                      'response_received_count',
                      'scheduler/dequeued',
                      'scheduler/dequeued/memory',
                      'scheduler/enqueued',
                      'scheduler/enqueued/memory',
                      'start_time', 'zyte_smartproxy/delay/reset_backoff',
                      'zyte_smartproxy/request',
                      'zyte_smartproxy/request/method/GET',
                      'zyte_smartproxy/response',
                      'zyte_smartproxy/response/status/200',
                      'zyte_smartproxy/response/status/301',
                      'zyte_smartproxy/response/status/302']'''

