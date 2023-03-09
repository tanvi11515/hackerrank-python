from html.parser import HTMLParser
num=int(input())
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        for attr in attrs:
            print("->", attr[0],'>',attr[1])
    def handle_endtag(self, tag):
        print ("END   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
for i in range(num):
    parser.feed(input())