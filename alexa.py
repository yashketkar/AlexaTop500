import urllib
import re
import sys
intError = "Please enter an integer between 1 to 500 only."
ioError = "An IOError occured, please make sure you are connected to the internet and python has access to it."
def errorAndExit(error):
    print error
    sys.exit()
try:
    if len(sys.argv) >= 2:
        n = int(sys.argv[1])
    else:
        print "Please enter the value of N (1-500):"
        n = int(raw_input())
    if n>500 or n<1:
        errorAndExit(intError)
except ValueError:
    errorAndExit(intError)
print "Getting top " + str(n) + " link(s) from Alexa"
print "Please wait..."
alexatop500 = []
for i in range(20):
    try:
        alexatop500.extend(re.findall("<a href=\"/siteinfo/[^>]*>(.*?)</a>",\
        urllib.urlopen("http://www.alexa.com/topsites/global;" + str(i)).read(),flags=0))
    except IOError:
        errorAndExit(ioError)
    if len(alexatop500)>=n:
        break
print "Download complete."
print "\nThe top " + str(n) + " link(s) from Alexa are:"
for i in range(0,n):
    print i+1,alexatop500[i]
