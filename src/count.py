from bs4 import BeautifulSoup
import urllib2
import re
from collections import Counter

page = urllib2.urlopen("http://localhost")
soup = BeautifulSoup(page, features="html.parser")
text = soup.get_text()
lst = re.findall(r'\w+',text)
count = Counter(str(x) for x in lst)
result = count.most_common(1)[0]
word = result[0]
times = result[1]

print "The most frequent word is " + word +", it has appeared " + str(times) +" times."
