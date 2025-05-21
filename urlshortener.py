import pyshorteners

def shorturl(url):
        short=pyshorteners.Shortener() 
        print("The shortened url is: ")
        print(short.tinyurl.short(url))
        
url = input("Enter the url to shorten: ")
shorturl(url)
