import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

def scrape_for_cv(url, url2, i):
    site_url = url + url2
    response = requests.get(url)
    html_content = response.content

    response = requests.get(site_url + str(i))
    print("\n", site_url + str(i))
    if response.status_code == 200:
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")
    else:
        print("Error accessing page ", i)
        pass

    links = soup.find_all('a')

    filtered_links = remove_duplicate_links(links)
    return filtered_links


def remove_duplicate_links(links):
    filtered_links = []
    for link in links:
        if link not in filtered_links:
            filtered_links.append(link)
    return filtered_links


def scrape_dynamic_page(link):
    options = Options()
    options.add_argument("headless")
    service = Service('/Users/${userName}/Drivers/chromedriver')
    browser = webdriver.Chrome(service=service, options=options)
    
    browser.get(link)
    title = (
        WebDriverWait(driver=browser, timeout=10)
        .until(visibility_of_element_located((By.CSS_SELECTOR, "h1")))
        .text
    )
    content = browser.page_source
    browser.close()
    return content


def find_all_offerings(links, url, word):
    work_offerings = []
    for link in links:
        href = link.get('href')
        if href and word in href.lower():
            link = url + href
            if link not in work_offerings:
                print("\nRastas darbo skelbimas: ", link)
                soup2 = BeautifulSoup(scrape_dynamic_page(link), "html.parser")
                title = getattr(soup2.find('h1'), 'text', 'Pavadinimas nerastas')
                work_offerings.append({title:(url + href)})
    return work_offerings


def find_all_offerings_cvbankas(links, word):
    work_offerings = []
    for link in links:
        href = link.get('href')
        if href and word in href.lower():
            print("\nRastas darbo skelbimas: ", href)
            if href not in work_offerings:
                soup2 = BeautifulSoup(scrape_dynamic_page(href), "html.parser")
                title = getattr(soup2.find('h1'), 'text', 'Pavadinimas nerastas')
                work_offerings.append({title: href})
    return work_offerings