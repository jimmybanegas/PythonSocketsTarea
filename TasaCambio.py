from html.parser import HTMLParser
import re

__author__ = 'Affisa-Jimmy'


from requests import get


r = get('https://www.interbanca.hn/INTERBANCA/INTERBANCA/BE_P_MOSTRARFACTOR?Pn_Empresa=1')


class MyHTMLParser(HTMLParser):

    def getTasas(self):
        self.handle_data(self)

    def handle_data(self, data):
        if str(data).__contains__('Lps.'):
            print ("Encountered some data :", str(data).replace('Lps.',''))



# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(r.text)