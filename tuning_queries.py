import urllib

def tuning_queries():
	query = []
	location= ['New York,NY', 'Los Angeles, CA', 'Chicago, IL', 'Houston, TX', 'Philadelphia, Pa', 'Phoenix, AZ', 'San Antonio, TX', 'San Diego, CA', 'Dallas, TX', 'San Jose, CA', 'Austin, TX', 'Jacksonville, FL', 'San Francisco\xa0, CA', 'Indianapolis, IN', 'Columbus, OH', 'Fort Worth\xa0, TX', 'Charlotte, NC', 'Detroit, MI', 'El Paso, TX', 'Seattle\xa0, WA', 'Denver\xa0, CO', 'Washington, DC', 'Memphis, TN', 'Boston, MA', 'Nashville, TN', 'Baltimore, MD', 'Oklahoma City, OK', 'Portland\xa0, OR', 'Las Vegas\xa0, NV', 'Louisville-Jefferson County, KY', 'Milwaukee, WI', 'Albuquerque, NM', 'Tucson, AZ', 'Fresno, CA', 'Sacramento, CA', 'Long Beach, CA', 'Kansas City, MO', 'Mesa, AZ', 'Atlanta\xa0, GA', 'Virginia Beach, VA', 'Omaha\xa0, NE', 'Colorado Springs, CO', 'Raleigh, NC', 'Miami, FL', 'Oakland, CA', 'Minneapolis, MN', 'Tulsa, OK', 'Cleveland, OH', 'Wichita, KS', 'New Orleans, LA', 'Arlington, TX']
	jop_types = ['commision','contract','internship','full-time','temporary','part-time']
	radius_list = [5,15, 15, 25, 50, 100]

	search_term = raw_input('\n[*]enter job name: ')
	print '\n'

	# choose job type
	for ndx, job in enumerate(jop_types):
		print '[',ndx,']-',job 
	j_type = int( raw_input('\n[*]enter the number next to job-type you want: ') )
	jop_type = jop_types[j_type]	
	print '\n'
		
	# choose radius
	for ndx, rad in enumerate(radius_list):
		print '[',ndx,']- within',rad,'miles' 
	r = int( raw_input('\n[*]enter the number next to the radius you want: ') )
	radius = radius_list[r]	
	
	for loc in location:
		query_structure = 'https://www.indeed.com/jobs?q='+str(search_term)+'&l='+urllib.quote_plus(loc)+'&radius='+str(radius)+'&jt='+str(jop_type)+'&limit=50'
		query.append(query_structure)

	return query

# print tuning_queries()
