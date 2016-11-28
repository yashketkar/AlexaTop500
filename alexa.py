import urllib
import re
print "Please enter the value of N:"
n = int(raw_input())
print "Getting top " + str(n) + " links from Alexa"
print "Please wait..."
alexatop500 = []
for i in range(20):
    alexatop500.extend(re.findall("<a href=\"/siteinfo/[^>]*>(.*?)</a>",urllib.urlopen("http://www.alexa.com/topsites/global;" + str(i)).read(),flags=0))
    if len(alexatop500)>=n:
        break
print "Download complete."
print "\nThe top " + str(n) + " links from Alexa are:"
for i in range(0,n):
    print i+1,alexatop500[i]
