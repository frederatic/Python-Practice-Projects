# Checks for curse words in a text file

import urllib

def read_text():
    text = open("file_location")
    content = text.read()
    print(content)
    text.close()
    checker(content)

def checker(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!!!")
    elif "false" in output:
        print("This document has no curse words! :)")
    else:
        print("Could not scan the doccument properly")


read_text()
