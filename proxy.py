from urllib import request
url = 'http://httpbin.org/ip'
# resp = request.urlopen(url)
# print(resp.read())
handler = request.ProxyHandler({'HTTP': '110.243.2.201:9999'})
opener = request.build_opener(handler)
resp = opener.open(url)
print(resp.read())
