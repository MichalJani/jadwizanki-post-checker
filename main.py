from bs4 import BeautifulSoup
from requests import get, post
from datetime import date, datetime
from babel.dates import format_date
from dotenv import load_dotenv
import os


load_dotenv()

HOOK_URL = os.getenv('DISCORD_HOOK')
URL = 'http://www.przedszkole-jadwizanek.wroc.pl'

def check_for_new_posts():
    page = get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    elements = soup.find_all('div', class_='art-postheadericons art-metadata-icons')
    text = elements[0].get_text()
    arr = text.split()
    date_only = arr[1:-1]
    parsed_date = ' '.join(date_only)
    
    now = datetime.now()
    todays_date = format_date(now, 'd MMMM yyyy', locale='pl_PL')
  
    if parsed_date == todays_date:
        data= { "content":"Dzisiaj pojawił się nowy post na stronie przedszkola jadwizanek \n" + URL }
        print('There is a post with today\'s date!')
        post(HOOK_URL, data=data)
        return 0

    print('No post with today\'s date...')
    return 1
    
  
