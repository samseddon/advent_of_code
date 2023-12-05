import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from requests_toolbelt.utils import dump

def scrape(url):
#    session = HTMLSession()
#    session = requests.Session()
#    session.headers.update({'User-Agent': 'Custom user agent'})
#    r = session.get(url)
#    soup = BeautifulSoup(r.html.raw_html, features='lxml')
#    text = soup.get_text()
    session = requests.session()
    session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
    resp = session.get(url)

    print(dump.dump_all(resp).decode('utf-8'))
    return text.split("\n")
    
print("which day would you to create a template for? - Integers only, 2022 for now")
day = int(input())
problem_url = "https://adventofcode.com/2022/day/" + str(day)

Problem = scrape(problem_url)
for line in Problem:
    print(line)

input_url = problem_url + "/input"
input_Lines = scrape(input_url)
for line in input_Lines:
    print(line)
#
#test_class_string = "ds-text-tight-s ds-font-bold ds-flex ds-items-center ds-justify-center ds-text-center ds-w-6 ds-h-6 ds-text-typo"
#author = response.html.xpath(test_class_string, first=True)
#print(author)
