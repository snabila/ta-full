import sqlite3
import string
import requests
from bs4 import BeautifulSoup
from translate import Translator

# open connection to sqlite database
conn = sqlite3.connect('test.db')
c = conn.cursor()

# drop old table
c.execute('''DROP TABLE disease_info''')

# make a new table, comment after one run
c.execute('''CREATE TABLE disease_info(
    pk INTEGER NOT NULL PRIMARY KEY,
    disease_name TEXT,
    overview TEXT,
    symptoms TEXT,
    when_to_see_doctor TEXT,
    causes TEXT,
    risk_factors TEXT,
    complication TEXT,
    prevention TEXT
)''')

# start translator
translator = Translator(to_lang="id")

# mayo clinic index page : collecting disease page urls
index_url = "https://www.mayoclinic.org/diseases-conditions/index?letter="
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'}
alphabet = string.ascii_uppercase
alphabet += '0'
alphabet = list(alphabet)

disease_urls = []

for letter in alphabet:
    r = requests.get(index_url + letter, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")

    index_content = soup.find(id='index')
    ol = index_content.find('ol')
    a_tags = ol.find_all('a', href=True)

    for a in a_tags:
        link = 'https://www.mayoclinic.org' + a['href']

        if link not in disease_urls:
            disease_urls.append(link)

# there are 1171 diseases
# print('There are ' + str(len(disease_urls)) + ' diseases')


def extractText(data):
    result = ''
    for sibling in data.next_siblings:
        if sibling.name == 'p' or sibling.name == 'ul':
            # translated = translator.translate(sibling.text.strip())
            # result += translated
            result += sibling.text.strip()
        elif sibling.name and sibling.name.startswith('h'):
            break

    return result.strip()


def getDiseaseInfo(url, pk):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")

    # Disease name
    disease_name = soup.find('h1').text.strip().replace('\n', '')

    # Content wrapper
    content = soup.find(id="main-content").find('div', class_=None, id=None)

    for children in content.find_all(['h{}'.format(i) for i in range(1, 6)], recursive=False):
        header = children.text.lower().strip().replace('\n', '')

        if 'overview' in header:
            overview = extractText(children)
        elif 'symptoms' in header:
            symptoms = extractText(children)
        elif 'when to see' in header:
            when_to_see_doctor = extractText(children)
        elif 'causes' in header:
            causes = extractText(children)
        elif 'risk factors' in header:
            risk_factors = extractText(children)
        elif 'complication' in header:
            complication = extractText(children)
        elif 'prevention' in header:
            prevention = extractText(children)

    try:
        overview
    except NameError:
        overview = None
    try:
        symptoms
    except NameError:
        symptoms = None
    try:
        when_to_see_doctor
    except NameError:
        when_to_see_doctor = None
    try:
        causes
    except NameError:
        causes = None
    try:
        risk_factors
    except NameError:
        risk_factors = None
    try:
        complication
    except NameError:
        complication = None
    try:
        prevention
    except NameError:
        prevention = None

    c.execute('''INSERT INTO disease_info VALUES(?,?,?,?,?,?,?,?,?)''', (pk, disease_name,
              overview, symptoms, when_to_see_doctor, causes, risk_factors, complication, prevention))


pk = 1
for disease in disease_urls:
    getDiseaseInfo(disease, pk)
    pk += 1

# getDiseaseInfo(disease_urls[2], 1)

conn.commit()

# close database connection
conn.close()
