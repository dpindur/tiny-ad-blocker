import sys
import urllib2

adlists = [
    'https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts',
    'https://mirror1.malwaredomains.com/files/justdomains',
    'http://sysctl.org/cameleon/hosts',
    'https://zeustracker.abuse.ch/blocklist.php?download=domainblocklist',
    'https://s3.amazonaws.com/lists.disconnect.me/simple_tracking.txt',
    'https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt',
    'https://hosts-file.net/ad_servers.txt'
]

def download_list(list_name):
  response = urllib2.urlopen(list_name)
  html = response.read()
  return [x.strip() for x in html.splitlines()]

def strip_comments_and_blanks(items):
  return [x for x in items if not x.startswith('#') and x != '']

def strip_ip(item):
  if item.startswith('0.0.0.0'):
    return item.replace('0.0.0.0', '').strip()
  elif item.startswith('127.0.0.1'):
    return item.replace('127.0.0.1', '').strip()
  else:
    return item

def strip_ip_addresses(items):
  return [strip_ip(x) for x in items]

dest = sys.argv[1]

print 'Downloading ads into %s' % dest

domains = set()
for adlist in adlists:
  l = download_list(adlist)
  l = strip_comments_and_blanks(l)
  l = strip_ip_addresses(l)
  print 'Adding list from %s' % adlist
  for domain in l:
    domains.add(domain)

sorted_domains = sorted(domains)
with open(dest, 'w') as f:
  for domain in sorted_domains:
    if domain != '':
      f.write("127.0.0.1 %s\n" % domain)
