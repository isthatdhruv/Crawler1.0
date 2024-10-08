import requests
from proxy_requests import ProxyRequests ,ProxyRequestsBasicAuth

proxies = {
    "http": "http://brd.superproxy.io:22225",
    "https": "https://brd.superproxy.io:22225"
}
r = ProxyRequestsBasicAuth('https://kccitm.edu.in/', 'brd-customer-hl_3cb0b520-zone-residential_proxy1', '507exwqih8in')
print(r.json())
