import requests
from atlassian import Confluence
from pprint import pprint
import json

contentApiUrl = '/rest/api/content'
# Change these based on your instance
confluenceBaseUrl = 'https://securonix.atlassian.net/wiki'
pageId = '123456789' # add the page id of the confluence page
username = 'user@securonix.com' # add conflluence username user@securonix.com
password = '' # add your api token key

requestUrl = '{confluenceBaseUrl}{contentApiUrl}/{pageId}?expand=body.view'.format(confluenceBaseUrl = confluenceBaseUrl, contentApiUrl = contentApiUrl, pageId = pageId)
print(requestUrl)

requestResponse = requests.get(requestUrl, auth=(username, password))

print(requestResponse)

jsonval = requestResponse.json()

# Adjust path here to point to doc\content\
# Name your file according to the name of the you want it to be displayed on the site
with open('doc2\content\docs\example\sampletestmarkdown_view_html3.md', 'w') as f:
    f.write("\n")
    f.write("# " + jsonval['title'])
    f.write("\n")
    f.write("{{< rawhtml >}} \n")
    f.write(jsonval['body']['view']['value'])
    f.write("{{< /rawhtml >}} \n")
    