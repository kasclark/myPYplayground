#!/usr/bin/python3
# this script will look up the repulation of a given site using apivoid.com

import requests
import sys
import json
import socket

def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True

API_KEY = "INSERT YOUR API KEY HERE"

if len(sys.argv)== 1:
    print("Please supply target host. './apivoid.py www.badsite.com'")
    exit()

host = sys.argv[1]

if(is_valid_ipv4_address(host)):
    URL = "https://endpoint.apivoid.com/iprep/v1/pay-as-you-go/?key=" + API_KEY + "&ip=" + host
else:
    URL = "https://endpoint.apivoid.com/domainbl/v1/pay-as-you-go/?key=" + API_KEY + "&host=" + host

try:
    r = requests.get(url=URL)
    response = r.json()
    detections = response["data"]["report"]["blacklists"]["detections"]
    detection_rate = response["data"]["report"]["blacklists"]["detection_rate"]
    engines_count = response["data"]["report"]["blacklists"]["engines_count"]
    print("Host: " + host + ", Detection rate: " + detection_rate + ", Detections: " + str(detections) + ", Engines: " + str(engines_count))
except:
    print("Host: " + host + ", ERROR")





