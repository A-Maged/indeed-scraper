import sys
import requests
from BeautifulSoup import BeautifulStoneSoup
import urlparse

from get_cookie import get_cookie
from bs4 import BeautifulSoup


def get_jobkeys(query, start_number, cookie ):
  job_keys = []
  url = str(query)+'&start='+str(start_number)
  s = requests.Session()
  r = s.get(url, headers ={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Cookie': get_cookie() ,
    'Connection': 'close'
    },verify=False
  )

  b_soap = BeautifulSoup(r.text, 'html.parser')

  counter = len(b_soap.find_all('a'))

  for i in range(counter):
    try:
      all_a_tags = b_soap.find_all('a')[i]

      if 'jobTitle' in str(all_a_tags):
        job_keys_urls = all_a_tags['href']
        parsed = urlparse.urlparse(job_keys_urls)
        parsed_job_key = urlparse.parse_qs(parsed.query)['jk']
        if (parsed_job_key in job_keys):
          pass
        else:
          job_keys.append(parsed_job_key[0])
    except Exception as e:
      i =- 1
      pass

  return job_keys

def get_job_details(job_key):
  try:
    url = 'http://api.indeed.com/ads/apigetjobs?publisher=6265819488525287&jobkeys=' + str(job_key) + '&format=json&v=2'
    s = requests.Session()
    r = s.get(url, headers ={'Accept': 'text/html,application','Connection': 'close'}  ,verify=False )
    return r.json()
  except:
    pass

def parse_job_details(job_json_details ):
  try:
    job_title = job_json_details['results'][0]['jobtitle']
    snippet = job_json_details['results'][0]['snippet']
    date = job_json_details['results'][0]['date']
    url = job_json_details['results'][0]['url']
    company = job_json_details['results'][0]['company']
    city = job_json_details['results'][0]['city']
    state = job_json_details['results'][0]['state']
    expired = job_json_details['results'][0]['expired']
    # formattedLocation = job_json_details['results'][0]['formattedLocation']
    formattedLocationFull = job_json_details['results'][0]['formattedLocationFull']
    # formattedRelativeTime = job_json_details['results'][0]['formattedRelativeTime']
    if(job_json_details['results'][0]['sponsored']):
      sponsored = 'sponsored'
    else:
      sponsored = 'no'

    jobkey = job_json_details['results'][0]['jobkey']
    details = [ job_title, snippet, date, str(company), city, state, formattedLocationFull, sponsored, url,  jobkey ]
    return details
  except:
    return False
