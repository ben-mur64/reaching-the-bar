import school

import requests
from bs4 import BeautifulSoup

def get_school_names():
    page = requests.get("https://www.lstreports.com/schools/")
    soup = BeautifulSoup(page.content, 'html.parser')


def get_school_data(name):
    page = requests.get("https://www.lstreports.com/compare/" + name + "/")
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.find_all('div', class_='big_num')

def get_school(name):
    # Should lawschooltransparency ever change their formatting, this has to change too.
    data = get_school_data(name)
    return school.School(name, float(pop_last(str(data[2].get_text()))), float(pop_last(str(data[4].get_text()))), float(pop_last(str(data[5].get_text()))), float(pop_last(str(data[7].get_text()))), float(pop_last(str(data[6].get_text()))), float(pop_last(str(data[3].get_text()))), float(pop_first(str(data[9].get_text()))), float(pop_last(str(data[8].get_text()))), get_prestige(name))

def get_all_schools(names):
    result = []
    for n in names:
        result.append(get_school(n))
    return result

def get_prestige(name):
    return 2

def pop_first(string):
    st = string[1:]
    st = st.replace(',', '')
    return st

def pop_last(string):
    st = string[:-1]
    return st