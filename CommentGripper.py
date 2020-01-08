import sys
import requests
import re
import optparse
import colorama
from colorama import Fore, Style

def sendRequest(url):
        try:
            URL = url
            r = requests.get(url = URL)
            respond = r.text    
            comments = re.findall(r'<!--(.+?)-->',respond)
            if not comments:
                print(Fore.RED+"No comments in the page!!!")
                sys.exit(0)
            x=1
            for i in comments: 
                print("---------- comment %s ----------" % (x))
                print (Fore.GREEN+i)
                print(Style.RESET_ALL)
                x +=1
        except requests.exceptions.RequestException as e:
            print(Fore.RED+"Target has no response !!!")

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-u", "--url", dest="url", help="Enter target url to grip its HTML comments")
    (options, arguments) = parser.parse_args()
    if not options.url:
        parser.error("[-] Please specify target url, use --help for more info.")
    else:
        return options

def main():
    print("# coded by Scizo -> @dbis_7 < twitter #\n\n\n\n\n\n")
    options = get_arguments()
    sendRequest(options.url)

main()

