from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        for i in attrs:
            print(f"-> {i[0]} > {i[1]}")

    def handle_endtag(self, tag):
        print ("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        for i in attrs:
            print(f"-> {i[0]} > {i[1]}")

    def handle_comment(self, data):
        if ("\n" in data):
            print(">>> Multi-line Comment")
        elif ("\n" not in data):
            print(">>> Single-line Comment")
        print(data)
                
    def handle_data(self, data):
        if (data != "\n"):
            print (">>> Data")
            print(data)


if __name__ == "__main__":
    lines = int(input())
    HTML_script = []

    for _ in range(lines):
        HTML_script.append(str(input()))

    # instantiate the parser and fed it some HTML
    parser = MyHTMLParser()
    parser.feed(''.join(x for x in HTML_script))


