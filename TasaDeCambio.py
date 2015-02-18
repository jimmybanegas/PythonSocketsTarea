__author__ = 'Affisa-Jimmy'

import urllib2

f = urllib.request.urlopen('https://www.interbanca.hn/INTERBANCA/INTERBANCA/BE_P_MOSTRARFACTOR?Pn_Empresa=1')

html = f.read()

doc = pyquery.PyQuery(html)

for td in doc("table.fk-specs-type2").find("td.specs-key"):
    print (td.text, td.getnext().text)