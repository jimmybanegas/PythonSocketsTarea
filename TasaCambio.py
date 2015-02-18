__author__ = 'Affisa-Jimmy'


from requests import get


r = get('https://www.interbanca.hn/INTERBANCA/INTERBANCA/BE_P_MOSTRARFACTOR?Pn_Empresa=1')

print (r.content)