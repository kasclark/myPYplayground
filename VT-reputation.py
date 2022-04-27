#!/usr/bin/python3

# given a url, compute the reputation

import vt
import sys

if len(sys.argv)== 1:
    print("Please supply target domain. './reputation.py www.badsite.com'")
    exit()

domain = sys.argv[1]

client = vt.Client("INSERT YOUR API KEY HERE")

try:
    url_id = vt.url_id(domain)
    url = client.get_object("/urls/{}",url_id)
except vt.error.APIError as e:
    print("Domain: " + domain + ", ERROR:" + str(e))
    client.close()
    exit()
    
harmless_votes = url.total_votes['harmless']
malicious_votes = url.total_votes['malicious']
total_votes = harmless_votes + malicious_votes

if total_votes < 1:
    score = 0
else:
    score = round(harmless_votes/total_votes * 100)

print("Domain: " + domain + ", Community Score: " + str(url.reputation) + ", Scanner votes: " + str(score) + "%")

# clean up
client.close()
