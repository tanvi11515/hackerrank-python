from html.parser import HTMLParser

class CustomHTMLParser(HTMLParser):
    
    def custom_print_attrs(self, attrs):
        if attrs:
            for attr in attrs:
                print('->', attr[0], '>', attr[1])
    
    def handle_starttag(self, tag, attrs):
        print(tag)
        self.custom_print_attrs(attrs)

    def handle_startendtag(self, tag, attrs):
        print(tag)
        self.custom_print_attrs(attrs)

html_parser = CustomHTMLParser()
pages = [input() for i in range(int(input()))]

for page in pages:
    html_parser.feed(page)