import school

import requests
from bs4 import BeautifulSoup

def get_school_names():
    page = requests.get("https://www.lstreports.com/schools/")
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find("table", id="listAllSchools")
    links = table.find_all('a')
    names = []
    full_names = []
    for link in links:
        if link['href'].find("state/") == -1:
            names.append(link['href'][35:-1])
            full_names.append(link.get_text())
    return names


def get_school_data(name):
    page = requests.get("https://www.lstreports.com/compare/" + name + "/")
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.find_all('div', class_='big_num')

def get_school(name):
    # Should lawschooltransparency ever change their formatting, this has to change too.
    data = get_school_data(name)

    a = float(pop_last(str(data[2].get_text())))
    b = float(pop_last(str(data[4].get_text())))
    c = float(pop_last(str(data[5].get_text())))
    d = float(pop_last(str(data[7].get_text())))
    e = float(pop_last(str(data[6].get_text())))
    f = float(pop_last(str(data[3].get_text())))
    g = float(pop_first(str(data[9].get_text())))
    h = float(pop_last(str(data[8].get_text())))
    i = get_prestige(name)
    j = 4.00 #FIXME: scrape GPA from somewhere
    g = 156 #FIXME: scrape LSAT from somewhere
    
    #FIXME: Get full name from somewhere
    return school.School(name, name, a, b, c, d, e, f, g, h, i, j, g)

def get_all_schools(names):
    result = []
    for n in names:
        result.append(get_school(n))
    return result

def get_prestige(name):
    return 2

def pop_first(string):
    if string == "Unknown" or string.find('%') != -1:
        return "0"
    else:
        st = string[1:]
        st = st.replace(',', '')
        return st

def pop_last(string):
    st = string[:-1]
    return st