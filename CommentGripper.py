import requests
import optparse
import sys
from colorama import Fore, Style
from bs4 import BeautifulSoup, Comment

def FindComments(url):
        try:
            # send a request to the target page
            r = requests.get(url)
            # recieve the respond
            respond = BeautifulSoup(r.text, "html.parser")
            # store all comments to the variable comments
            comments = respond.findAll(text = lambda text: isinstance(text, Comment))
            
            # if there is no comment print exeception and exit
            if not comments:
                print(Fore.RED+"No comments in the page!!!")
                sys.exit()
            # else  
            else:
                # intialize a counter for the comments
                counter = 0
                # loop and print the comments
                for i in comments: 
                    print("---------- comment %s ----------" % (counter))
                    print(Fore.GREEN+i)
                    print(Style.RESET_ALL)
                    counter +=1
        except requests.exceptions.RequestException as e:
            print(Fore.RED+"Target has no response !!!")

def get_arguments():
    # the purpose of this function to get the target url and deal with its execption
    parser = optparse.OptionParser()
    parser.add_option("-u", "--url", dest="url", help="Enter target url to grip its HTML comments")
    (options, arguments) = parser.parse_args()
    if not options.url:
        parser.error("[-] Please specify target using: --url [target], or use --help for more info.")
    else:
        return options

if __name__ == "__main__":
    #show a banner of the coder
    print("# coded by schizo -> @5ch1zo < twitter #\n\n")
    # get target url argument
    options = get_arguments()
    # pass the url and get its comments  
    FindComments(options.url)
