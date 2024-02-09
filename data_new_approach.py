import pandas as pd
import glob, re
from datetime import datetime as dt
import logging
logging.basicConfig(filename="D:/panda_assignment/data_processing.log", format='%(asctime)s-%(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


# Function to parse date
def date_parser(val):
    val = val.strip('datetime.').replace('(', '').replace(')', '').replace(' ', '').replace('"', '')
    new_val = re.split(',', val)
    date_components = [int(component) if component.isdigit() else 0 for component in new_val[:-1]]
    date_object = dt(*date_components)
    formatted_date = date_object.strftime("%Y-%m-%d %H:%M:%S.%f")
    return formatted_date


# Function to read txt log files & fetching required data
def read_fetch_data():
    search_str1 = ['BOT_NAME', 'LOG_FILE']
    search_str3 = 'Dumping Scrapy stats:'
    search_str4 = 'Spider closed'
    pattern = '[}{?%&$#@!~' ']'
    new_line = ''
    json_data, bot = {}, {}

    string_presence, string_absence = [], []
    stat_presence,  stat_absence = [], []
    counter = 0

    # Reading files from folder
    all_files = glob.iglob('D:/data/**/*.log', recursive=True)
    for file in all_files:
        string_present = False
        logger.info(f'Reading file - {file}')
        log_file = open(file, 'r', encoding='utf8')
        content = log_file.readlines()

        # Searching stat data in file
        logger.info(f'Searching stats {search_str3} & {search_str4} ')
        start_line = next((i for i, line in enumerate(content, start=1) if search_str3 in line), None)
        end_line = next((i for i, line in enumerate(content, start=1) if search_str4 in line), None)

        # Checking if stats present or not
        logger.info(f'Checking for stats {search_str3} & {search_str4} if present in file')
        if start_line is not None and end_line is not None:
            data_between_strings = content[start_line:end_line-1]
            result = ''.join(data_between_strings).strip()
            new_line = re.sub(pattern, '', result).replace("'", '').replace(' ', '')
            fixed_line = ''.join(new_line).split('\n')
            for line in fixed_line:
                key, val = map(str.strip, line.split(':'))
                val = val.strip(',').replace("'", '')
                key = key.replace("'", '')

                if key.__contains__("finish_time") or key.__contains__("start_time"):
                    val = date_parser(val)

                if key not in json_data:
                    json_data[key] = []
                json_data[key].append(val)

            # stat_presence.append(result)
        else:
            stat_absence.append(file)

        # Searching string 'BOT_NAME' & 'LOG_FILE' in file
        logger.info(f'Searching for string - {search_str1}')
        for line in content:
            if any(word in line for word in search_str1):
                new_line = re.sub(pattern, '', line)
                logger.info(f'line value is - {new_line}')
                string_present = True
                # string_presence.append(new_line)
                key, value = map(str.strip, new_line.split(':'))
                key = key.replace("'", '')
                value = value.replace("'", '')
                logger.info(f'key - {key}')

                if key not in bot:
                    bot[key] = []
                bot[key].append(value)

        # Checking if string not present
        logger.info(f'Checking for strings if not present- {search_str1}')
        if not string_present:
            logger.info('Appending file which has no strings')
            string_absence.append(file)

        json_data.update(bot)
        counter += 1

    print(counter)
    return json_data, string_absence, stat_absence

'''
# Function to convert fetched data into json format
def file_data_processing(string_presence_data, string_absence_data, stat_presence_data, stat_absence_data):

    str_ab_data = string_absence_data
    stat_ab_data = stat_absence_data

    pattern = '[}{?%&$#@!~"]'
    bot = {}
    json_data = {}

    # Converting string data into json
    logger.info('Converting fetched string data into json')
    if string_presence_data:
        for string in string_presence_data:
            key, value = map(str.strip, string.split(':'))
            key = key.replace("'", '')
            value = value.replace("'", '')
            logger.info(f'key - {key}')

            if key not in bot:
                bot[key] = []
            bot[key].append(value)

    # Converting stat data into json
    logger.info('Converting stat data into json')
    if stat_presence_data:
        for stat in stat_presence_data:
            new_line = re.sub(pattern, '', stat).replace("'", '').replace(' ', '')
            fixed_line = ''.join(new_line).split('\n')

            for line in fixed_line:
                key, val = map(str.strip, line.split(':'))
                val = val.strip(',').replace("'", '')
                key = key.replace("'", '')

                if key.__contains__("finish_time") or key.__contains__("start_time"):
                    val = date_parser(val)

                if key not in json_data:
                    json_data[key] = []
                json_data[key].append(val)

    logger.info('Returning json data for df')
    return bot, str_ab_data, json_data, stat_ab_data
'''

if __name__ == '__main__':
    str_p, str_a, stat_a = read_fetch_data()
    # str_data_p, str_data_a, stat_data_p, stat_data_a = file_data_processing(str_p, str_a, stat_p, stat_a)
    # str_p.update(stat_p)
    df = pd.DataFrame.from_dict(str_p, orient='index')
    df = df.transpose()
    print(df)
    print(df['BOT_NAME'])
    # df.to_csv(r'C:\Users\girish.deshpande\Desktop\fixedcsv.csv', index=False)

    print('String BOT_NAME & LOG_FILE not found in below files:')
    for str_item in str_a:
        logger.info(f'Strings absent in file - {str_item}')
        print(str_item)

    print('\nStats not found in below files:')
    for stat_item in stat_a:
        logger.info(f'Stats absent in file - {stat_item}')
        print(stat_item)




