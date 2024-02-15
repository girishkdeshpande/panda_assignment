from bs4 import BeautifulSoup
import pandas as pd
import requests


def get_url(next_url):
    print(next_url)
    payload = {}
    headers = {
      'authority': 'quotes.toscrape.com',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'accept-language': 'en-US,en;q=0.9',
      'referer': 'https://quotes.toscrape.com/',
      'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'document',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-user': '?1',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", next_url, headers=headers, data=payload)

    response_data = BeautifulSoup(response.text, 'lxml')

    get_data(response_data)


def get_data(content_data):

    tag_data = []
    quotes = content_data.find_all('div', class_='quote')
    for quote in quotes:
        actual_quote = quote.find('span', class_='text').text
        clean_quote = actual_quote.replace('"', '')
        url_data['Quote'].append(clean_quote)

        author = quote.find('small', class_='author')
        url_data['Author'].append(author.string)

        auth_link = quote.find_all('a')
        for link in auth_link:
            if '(about)' in link:
                url_data['Author_link'].append(link.get('href'))

        tags = quote.find_all('a', class_='tag')
        for tag in tags:
            tag_data.append(tag.string)

        url_data['Tags'].append(tag_data)
        tag_data = []

    next_page = content_data.find('li', class_='next')
    if next_page:
        url_path = next_page.find('a')['href']
        new_url = 'https://quotes.toscrape.com' + str(url_path)
        get_url(new_url)
    else:
        df = pd.DataFrame.from_dict(url_data, orient='index')
        df = df.transpose()
        print(df)
        # df.to_csv('D:/panda_assignment/beautiful.csv')


if __name__ == '__main__':
    url_data = {'Quote': [], 'Author': [], 'Author_link': [], 'Tags': []}
    url = 'https://quotes.toscrape.com'
    get_url(url)

