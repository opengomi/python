import httplib

conn = httplib.HTTPConnection('codeshell.kr')
conn.request('POST', '/probs/readonly/', 'input=dlqfur_ahtgkwl?zz', {'Cookie':'PHPSESSID=k7prt27f0748sj8j289go9t206', 'Content-type':'application/x-www-form-urlencoded'})
body = conn.getresponse().read()
print body

