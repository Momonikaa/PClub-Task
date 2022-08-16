import requests
import json

url = "https://summerofcode.withgoogle.com/api/program/2022/organizations/"

soup = json.loads(requests.get(url).text)

for i in soup:
    for j in [
    "slug"
    ,"logo_url"
    ,"website_url"
    ,"license"
    ,"categories"
    ,"contact_links"
    ,"direct_comm_methods"
    ,"social_comm_methods"]:
        i.pop(j)

with open("./gsoc_org.json", 'w') as f:
    json.dump(soup, f)