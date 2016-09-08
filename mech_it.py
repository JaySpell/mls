import mechanize
import urllib
import shutil
import datetime
from bs4 import BeautifulSoup

def get_mls_data():
    '''
    Gets MLS data utilizing screen scraping of mechanize
    output will be saved to tab delemited file in outputs
    folder
    '''
    q_url = config.get_q_url()          #Query URL
    l_url = config.get_l_url()          #Login URL
    cs_url = config.get_cs_url()        #Custom Search URL
    uid = config.get_user()             #Username
    password = config.get_password()    #Password

    #Login to site
    br = mechanize.Browser()
    br.addheaders = [
            ('User-agent',
                'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')
        ]

    br.open(l_url)
    br.select_form('LoginForm')
    br.form['LoginCtrl$txtLoginUsername'] = uid
    br.form['LoginCtrl$txtPassword'] = password
    br.submit()

    #Open custom search page -- this is so that referrer looks correct
    br.open(cs_url)

    #Get encoded url - open download page
    date_list = get_date_list
    query_url = q_url + get_encoded_url(date_list[0], date_list[1])
    br.open(query_url)
    br.select_form(name='downloadform')

    #Save results to file with name of day
    with open('results.txt', 'wb') as f:
        shutil.copyfileobj(br.submit(), f)

def get_date_list(start_date='today'):
    if start_date == 'today':
        date


def get_encoded_url(first_date, sec_date, liststatus='closd'):
    encoded = urllib.quote_plus(
                     "((liststatus='" + liststatus +
                     "' and ClosedDate>=convert(datetime,'" + first_date +
                     "') AND ClosedDate<=convert(datetime,'" + sec_date +
                     "')))"
                )
    return encoded
