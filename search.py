import requests
from requests.exceptions import ConnectionError

# This script was created to crawl a list of websites to look for keywords.
# Author: Brad D Fears (2/16/2022)

keywords = ["DOD","USDA","DOE","DHS","HHS","NIH","NSF"]

# Output file
myfile = open("results.txt", 'w')

# List of URLs
urlsFile = open("urls.txt", 'r')

while(True):
	line = urlsFile.readline()
	print(line.strip())
	if not line:
		break
	try:
		page = requests.get("https://" + line.strip(), allow_redirects=False, timeout=5)
	except requests.exceptions.RequestException:
		continue
	content = str(page.content)
	
	for x in keywords:
		if x in content:
			myfile.write(x + " | " + line.strip())
			myfile.write("\n")

urlsFile.close()
myfile.close()
