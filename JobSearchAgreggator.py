import pandas as pd
import requests
from bs4 import BeautifulSoup

url_base = 'https://www.net-empregos.com/pesquisa-empregos.asp?page='
url_local = '&cidade=Sines'
url_estrangeiro = '&categoria=0&zona=29&tipo='
url_all = '&categoria=0&zona=0&tipo=0'
netemprego = 'https://www.net-empregos.com'


def get_jobs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    job_items = soup.select('div.job-item.media')

    job_listings = []

    for job_item in job_items:
        job_string = job_item.select_one('h2')
        job_title = job_string.select_one('a').text.strip()
        job_href = job_string.select_one('a').get('href')
        location = job_item.select_one('li i.flaticon-pin').find_next_sibling(text=True).strip()
        work_type = job_item.select_one('li i.fa.fa-tags').find_next_sibling(text=True).strip()
        company = job_item.select_one('li i.flaticon-work').find_next_sibling(text=True).strip()
        date = job_item.select_one('li i.flaticon-calendar').find_next_sibling(text=True).strip()


        job_listings.append({
            'Date': date,
            'Job Title': job_title,
            'Company': company,
            'Work Type': work_type,
            'Location': location,
            'Link': f'{netemprego}{job_href}'
        })

    return job_listings


def rodar():
    pages = int(input('Paginas?: '))
    job_data = []
    for page in range(1, pages + 1):
        url = f'{url_base}{page}{url_local}'
        for job in get_jobs(url):
            job_data.append(job)

    df = pd.DataFrame(job_data, columns=['Date', 'Job Title', 'Company', 'Work Type', 'Location', 'Link'])
    print(df)  # print todo o DataFrame
    #Salva os resultados em XLS
    #df.to_excel('trabalhos.xlsx', index=False)
    return df

rodar()

