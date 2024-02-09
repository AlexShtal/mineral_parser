from bs4 import BeautifulSoup
import requests


def parse(site_url):
    url = site_url
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36'}

    page = requests.get(url, headers=headers)
    print(page.status_code)

    soup = BeautifulSoup(page.text, "html.parser")

    all_minerals = soup.find("div", class_="reference").\
        find("table", class_='watch_table').find("tbody").find_all("tr")

    mineral_names = []

    for mineral in all_minerals:
        # Parse name
        name = mineral.find('td')
        mineral_names.append(name.text)

    for i in mineral_names:
        print(i)
    """ Check
    for i in range(len(vac_companies)):
        print("{0}\t{1}\t{2}\t{3}".format(vac_names[i], vac_refs[i], vac_salaries[i], vac_companies[i]))
    """


parse("https://www.silver-lines.ru/silver/info/reference/v/?id=61889")
