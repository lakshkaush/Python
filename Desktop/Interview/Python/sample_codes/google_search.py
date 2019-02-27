""" Sample google search code using json """
"""https://www.pythonforbeginners.com/code-snippets-source-code/google-command-line-script/ """

# To make use of urlencode
import urllib
# To load URL response
import urllib2
# Google returns json
import json

url = "https://www.googleapis.com/customsearch/v1?key=AIzaSyCc1Fu90hV7PTuURkOUIMlx7JAnwEcJSxs&cx=016130308476981765959:yytmcj1fulo&"
query = raw_input("What do you want to search for?>>")
query = urllib.urlencode({'q' : query })
response = urllib2.urlopen (url + query).read()
data = json.loads(response)
print (data)
print "Headers"
print (data.queries)

results = data['queries']['link']

print "Results is :",results

for result in results:
    title = result['title']
    url = result['siteSearch']
    print (title + ';' + url)


