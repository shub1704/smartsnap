from googlesearch import search
import img2text
import webbrowser

def searchresult(query):
    for i in search(query, tld="co.in", num=8, stop=8, pause=2):
        print(i)

def brow():
    query=input("enter what to search")
    webbrowser.open('https://www.google.com/search?q='+ query)


if __name__ == '__main__':
    query= "python"
    #img2text.imagetotext('snip1.png')
    print("for the query...", query)
    print("searching results .... ")
    #searchresult(query)
    brow()