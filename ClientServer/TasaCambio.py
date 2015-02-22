from html.parser import HTMLParser
import re

__author__ = 'Affisa-Jimmy'

from requests import get

def getTasas():
    r = get('https://www.interbanca.hn/INTERBANCA/INTERBANCA/BE_P_MOSTRARFACTOR?Pn_Empresa=1')

    class MyHTMLParser(HTMLParser):
        lista =''
        def handle_data(self, data):
            if str(data).__contains__('Lps.'):
                self.lista+= str(data).replace('Lps.','').strip()+','

    parser = MyHTMLParser()
    parser.feed(r.text)

    return parser.lista