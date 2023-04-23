import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm

url_base = 'https://quranicnames.com/girls/page/'
page_num = 1
url = url_base + str(page_num) + '/'
response = requests.get(url)

list_url_csv = open('list_url.csv', 'w', newline='', encoding='utf-8')
list_url_writer = csv.writer(list_url_csv)
list_url_writer.writerow(['URL'])

detail_data_csv = open('detail_data.csv', 'w', newline='', encoding='utf-8')
detail_data_writer = csv.writer(detail_data_csv)
detail_data_writer.writerow(['Name', 'Arabic Name', 'Variant', 'Content'])

urls_list = []

while response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    name_divs = soup.find_all('div', {'class': 'post'})
    
    for div in name_divs:
        name_link = div.find('a', {'class': 'girls'})
        if name_link:
            url = name_link['href']
            urls_list.append(url)
            list_url_writer.writerow([url])
        else:
            url = 'N/A'
        
    page_num += 1
    url = url_base + str(page_num) + '/'
    response = requests.get(url)

pbar = tqdm(total=len(urls_list))
for url in urls_list:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        name_elem = soup.find('h1', {'class': 'entry-title name'})
        name = name_elem.text.strip() if name_elem else 'N/A'
        arabic_name_elem = soup.find('td', {'class': 'arspelling'})
        arabic_name = arabic_name_elem.text.strip() if arabic_name_elem else 'N/A'
        variant_list = soup.find_all('div', {'class': 'variant'})
        variant = ', '.join([v.text.strip() for v in variant_list]) if variant_list else 'N/A'
        content_elem = soup.find('div', {'id': 'name_details'}).find('p')
        content = content_elem.text.strip() if content_elem else 'N/A'
        
        detail_data_writer.writerow([name, arabic_name, variant, content])
    
    pbar.update(1)

list_url_csv.close()
detail_data_csv.close()
pbar.close()
