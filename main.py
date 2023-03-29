import os
from unidecode import unidecode
from create_html import create_html
import webbrowser
from scrape import scrape_for_cv, find_all_offerings, find_all_offerings_cvbankas


all_postings = []


def main(keyword1, keyword2, search_type, region):
    
    keyword1, keyword2 = format_keywords(keyword1, keyword2)
    keyword1, keyword2 = check_if_keywords_arent_empty(keyword1, keyword2)

    scrape_cv_lt(
        90, 
        keyword1, 
        keyword2, 
        search_type, 
        region
    )   
    
    scrape_cvmarket(
        172,  
        keyword1, 
        keyword2, 
        search_type, 
        region
        )
    
    scrape_cvbankas(
        112, 
        keyword1, 
        keyword2, 
        search_type, 
        region
        )

    create_html(remove_duplicates_from_all_postings())

    webbrowser.open((os.path.dirname(os.path.abspath(__file__))) + '/html/job_postings.html')


def format_keywords(keyword1, keyword2):
    keyword1, keyword2 = keyword1.lower(), keyword2.lower()
    keyword1, keyword2 = unidecode(keyword1), unidecode(keyword2)
    return keyword1, keyword2


def check_if_keywords_arent_empty(keyword1, keyword2):
    if keyword1 == "":
        keyword1 = keyword2
    if keyword2 == "":
        keyword2 = keyword1
    return keyword1, keyword2


def scrape_cv_lt(number_of_pages, keyword1, keyword2, search_type, region):
    i = 1
    for i in range(number_of_pages):
        CV_LT_URL = "https://www.cv.lt"
        CV_LT_URL_2 = "/nuolatinis-darbas?page="
        cv_lt_pasiulymai = find_all_offerings(
            scrape_for_cv(CV_LT_URL, CV_LT_URL_2, i), 
            CV_LT_URL, 
            keyword1, 
            keyword2, 
            search_type, 
            region
            )
        if cv_lt_pasiulymai:
            all_postings.extend(cv_lt_pasiulymai)
            return all_postings


def scrape_cvmarket(number_of_pages, keyword1, keyword2, search_type, region):
    i = 1
    for i in range(number_of_pages):    
        CVMARKET_URL = "https://www.cvmarket.lt"
        CVMARKET_URL_2 = "/darbo-skelbimai?start="
        cvmarket_pasiulymai = find_all_offerings(
            scrape_for_cv(CVMARKET_URL, CVMARKET_URL_2, i*25), 
            CVMARKET_URL, 
            keyword1, 
            keyword2, 
            search_type, 
            region
            )
        if cvmarket_pasiulymai:
            all_postings.extend(cvmarket_pasiulymai)
            return all_postings   


def scrape_cvbankas(number_of_pages, keyword1, keyword2, search_type, region):
    i = 1
    for i in range(number_of_pages):
        CVBANKAS_URL = "https://www.cvbankas.lt"
        CVBANKAS_URL_2 = "/?page="
        cvbankas_pasiulymai = find_all_offerings_cvbankas(
            scrape_for_cv(CVBANKAS_URL, CVBANKAS_URL_2, i), 
            keyword1, 
            keyword2, 
            search_type, 
            region
            )
        if cvbankas_pasiulymai:
            all_postings.extend(cvbankas_pasiulymai)
            return all_postings


def remove_duplicates_from_all_postings():
    all_postings_duplicates_removed_list = []
    for posting in all_postings:
        if posting not in all_postings_duplicates_removed_list:
            all_postings_duplicates_removed_list.append(posting)
    return all_postings_duplicates_removed_list