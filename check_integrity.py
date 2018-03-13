import sys
from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup
import urlparse
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from get_cookie import get_cookie
from print_excel import print_excel
from get_job import  get_jobkeys, get_job_details, parse_job_details

def check_integrity(query):
  job_details = []
  cookie = get_cookie()
  jobkeys = get_jobkeys(query, 70, cookie)
  job_json_dsc = get_job_details( jobkeys[0] )
  job_dsc = parse_job_details(job_json_dsc)
  job_details.append(job_dsc)

  print_excel(job_details)


query = 'https://www.indeed.com/jobs?q=marketing&l=New+York,+NY&radius=100&jt=contract&start=500'
check_integrity(query)
