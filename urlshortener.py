import pyshorteners

url = input("Enter the url to shorten: ")

def shorturl(url):

        shortt=pyshorteners.Shortener()
        print("The shortened url is: ")
        print(shortt.tinyurl.short(url))

shorturl(url)
