import mechanize
import urllib
import shutil
import datetime
from bs4 import BeautifulSoup

def get_mls_data(**kwargs):
    '''
    Gets MLS data utilizing screen scraping of mechanize
    output will be saved to tab delemited file in outputs
    folder
    '''

    q_url = kwargs.get('q_url', None)           #Query URL
    l_url = kwargs.get('l_url', None)           #Login URL
    cs_url = kwargs.get('cs_url', None)         #Custom Search URL
    uid = kwargs.get('username', None)          #Username
    password = kwargs.get('password', None)     #Password

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
    date_list = get_date_list()
    query_url = map(lambda q: get_encoded_url(q, q_url), date_list)

    for query, date in query_url:
        br.open(query_url)
        br.select_form(name='downloadform')

        #Save results to file with name of day
        with open('/output/'+ date.replace('/', '') + '.txt', 'wb') as f:
            shutil.copyfileobj(br.submit(), f)

def get_date_list(numdays=1):
    date_list = []
    base = datetime.datetime.today()
    raw_date_list = [base - datetime.timedelta(days=x) for x in range(0, numdays)]
    for date in raw_date_list:
        date_list.append(date.strftime("%m/%d/%Y"))
    return date_list

def get_encoded_url(date, q_url, liststatus='closd'):
    encoded = urllib.quote_plus(
                     "((liststatus='" + liststatus +
                     "' and ClosedDate>=convert(datetime,'" + date +
                     "') AND ClosedDate<=convert(datetime,'" + date +
                     "')))"
                )
    encoded_query_url = q_url + encoded
    return encoded_query_url, date

def get_date_range(startdate, enddate):
    date_list = []
    date = datetime.date.today()
