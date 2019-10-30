import requests 
from requests.auth import HTTPBasicAuth
import sys
import os
import unicodedata
  
for i in range('YOUR COMPUTER ID START RANGE', 'YOUR COMPUTER END ID'): #These need to be int's
	# api-endpoint 
	URL = "YOUR_JAMF_URL/JSSResource/computers/id/" + str(i) + "/subset/ExtensionAttributes"
	
   
# sending get request and saving the response as response object 
	r = requests.get(url = URL, auth=HTTPBasicAuth('YOUR_USERNAME', 'YOUR_PASSWORD'), headers = {'Accept': 'application/json' }) 

	if r.status_code == 404:
		print('Does Not Exist')
	else:
 
		data = r.json() 
  
		extensionList = data['computer']['extension_attributes'][0]['value']

		utf8string = extensionList.encode("utf-8") 

		boolFind = False
		filepath = 'YOUR_FILENAME' #Create a file prior to running and put the name/filepath here    


		for Jline in utf8string.splitlines():
			with open(filepath, "a") as myfile:
				with open(filepath) as fp:
   					Tline = fp.readline()
   					boolFind = False
   					while Tline:
   						#print(Jline.rstrip() + '     : Tline')
   						#print(Tline.rstrip() + '     : Jline')
						if Jline.rstrip() == Tline.rstrip():
							boolFind = True
							Tline = fp.readline()
						else:
							print("No Match")
							Tline = fp.readline()
					
					if boolFind:
						print("Found Match")
					else:
						print('Writing:  ' + Jline)
						myfile.write(Jline + '\n')	
	
		fp.close()
		myfile.close()

# sort this list alphabetically with this bash/zsh command:
# sort YOUR_FILE_NAME.txt -o YOUR_NEW_FILE_NAME.txt
# I would recommend changing the sorted output files name to something else - just in case.