import urllib.request
url = 'https://raw.githubusercontent.com/evgeniikozlov/pythonista_app/master/test.py'
contents = urllib.request.urlopen(url).read().decode('utf-8')
pass
