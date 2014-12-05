from lxml.builder import E
from lxml import html 

def CLASS(*args):
    return {"class":' '.join(args)}

s = "WuWeichang"

page = E.html(       # create an Element called "html"
        E.head(
            E.title("This is a sample document")   ),
            E.body(
                   E.h1("Hello!", CLASS("title"), Name=s),
                   E.p("This is a paragraph with ", E.b("bold"), " text in it!"),
                   E.p("This is another paragraph, with a", "\n      ",
                       E.a("link", Href="http://www.python.org"), "."),
                       E.p("Here are some reservered characters: <spam&egg>."),
                       )
            )
        

print html.tostring(page, pretty_print = True) 