# CV Scraper Finder

import os
from unidecode import unidecode
from create_html import create_html
import webbrowser
from scrape import scrape_for_cv, find_all_offerings, find_all_offerings_cvbankas


word = input("Parašykite paieškos žodį: ")
word = word.lower()
word = unidecode(word)


all_postings = []


def scrape_cv_lt(number_of_pages):
    i = 1
    for i in range(number_of_pages):
        cv_lt_url = "https://www.cv.lt"
        cv_lt_url_2 = "/nuolatinis-darbas?page="
        cv_lt_pasiulymai = find_all_offerings(scrape_for_cv(cv_lt_url, cv_lt_url_2, i), cv_lt_url, word)
        if cv_lt_pasiulymai:
            all_postings.extend(cv_lt_pasiulymai)
            return all_postings

def scrape_cvbankas(number_of_pages):
    i = 1
    for i in range(number_of_pages):
        cvbankas_url = "https://www.cvbankas.lt"
        cvbankas_url_2 = "/?page="
        cvbankas_pasiulymai = find_all_offerings_cvbankas(scrape_for_cv(cvbankas_url, cvbankas_url_2, i), word)
        if cvbankas_pasiulymai:
            all_postings.extend(cvbankas_pasiulymai)
            return all_postings

def scrape_cvmarket(number_of_pages):
    i = 1
    for i in range(number_of_pages):    
        cvmarket_url = "https://www.cvmarket.lt"
        cvmarket_url_2 = "/darbo-skelbimai?start="
        cvmarket_pasiulymai = find_all_offerings(scrape_for_cv(cvmarket_url, cvmarket_url_2, i*25), cvmarket_url, word)
        if cvmarket_pasiulymai:
            all_postings.extend(cvmarket_pasiulymai)
            return all_postings   


def remove_duplicates_from_all_postings():
    all_postings_duplicates_removed_list = []
    for posting in all_postings:
        if posting not in all_postings_duplicates_removed_list:
            all_postings_duplicates_removed_list.append(posting)
    return all_postings_duplicates_removed_list


scrape_cv_lt(90)
scrape_cvbankas(172)
scrape_cvmarket(112)


create_html(remove_duplicates_from_all_postings())


webbrowser.open((os.path.dirname(os.path.abspath(__file__))) + '/html/job_postings.html')