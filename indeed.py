import urllib
import urllib2
from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup
import urlparse
import json
import Cookie
import threading
import signal
import time
import sys
import xlwt
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from get_cookie import get_cookie
from print_excel import print_excel
from get_job import  get_jobkeys, get_job_details, parse_job_details
from tuning_queries import tuning_queries

cookie = get_cookie()
exit_while = 'False'
class BreakAllTheLoops(BaseException): pass

def write_output(output ,filename):
  f = open( str(filename)+".txt" ,"a" )
  f.write(unicode(output))
  f.close()

def jobs_total_num(jobkeys):
  jobs_total_num =0
  for ndx, jk in enumerate(jobkeys):
    for jkndx, m in enumerate (jk) :
      jobs_total_num += 1
  return jobs_total_num

def check_status(jobkeys):
  while 1:
    time.sleep(10)
    print '\npages total-number for 1 query out of 50 : ',len(jobkeys)
    print 'jobs total number: ',jobs_total_num(jobkeys)

def limit_jobs(jobkeys, jobs_limit):
  total_num = jobs_total_num(jobkeys)

  if (total_num >= ( jobs_limit + 60 ) ) :
    # print 'limit reached ', (total_num)
    print 'limit reached '
    return 'True'
  else:
    return False


def main():
  try:
    jobkeys = []
    job_details = []
    query_list = tuning_queries()
    global exit_while

    # for debugging
    # query_list = ['https://www.indeed.com/jobs?q=marketing&l=New+York%2CNY&radius=100&jt=part-time&limit=10','https://www.indeed.com/jobs?q=php&l=New+York%2CNY&radius=100&jt=part-time&limit=10']

    print '\nthe results can get up to 51000 jobs ,that will take time'

    jobs_limit_choise = str(raw_input('do you want to limit the total numer of jobs to crawl ? yes or no (prefered): ') )

    if 'yes' in jobs_limit_choise:
      jobs_limit = int(raw_input('\nenter the total number of jobs to crawl (60-51000): '))

    print '\n\n\n        =======================================  CRAWLING INDEED.COM======================================='
    print '\n\n\n[*]queries total number:', len(query_list)

    # status output thread
    t = threading.Thread(target=check_status, args=(jobkeys,))
    t.daemon = True
    t.start()

    # loop over all pages
    pages_counter = 0
    while (pages_counter < 1000) & (exit_while == 'False') :
      # debug
      print '\n\n[*]crawling page number ['+ str(pages_counter)+ '] for all queries/locations\n\n\n'

      # try:
      # get the job keys
      if exit_while == 'False':
        for query in query_list:
          keys = get_jobkeys(query, pages_counter, cookie)

          # for jobs status
          jobkeys.append(keys)

          # get the job details
          for ndx, job in enumerate(keys) :
            if 'jobs_limit' in locals():
              # check if its exceded
              is_exceded = limit_jobs(jobkeys, jobs_limit)
              if (is_exceded == 'True'):
                raise BreakAllTheLoops()
            try:
              job_json_dsc = get_job_details( job)
              job_dsc = parse_job_details(job_json_dsc)
              # print job_dsc[0]
              if job_dsc != False:
                job_details.append(job_dsc)


          # except KeyboardInterrupt:
          #   print("W: interrupt received")
          #   print_excel(job_details)
          #   sys.exit(0)
            except TypeError:
              pass



      # increament  "&start=" / pages  by 10
      pages_counter = pages_counter + 10

      # except Exception as e:
      #   print 'error line 152'
      #   print str(e)
      #   if 'HTTPSConnectionPool' in str(e):
      #     print '[-]there\'s problems getting the cookie'
      #   pass

    #save all job keys as backup
    # write_output(jobkeys,'jobkeys' )



    print_excel(job_details)
  except (BreakAllTheLoops,KeyboardInterrupt):
    print_excel(job_details)
    pass


main()
