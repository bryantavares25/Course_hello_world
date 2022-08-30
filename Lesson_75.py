import urllib

import urllib.request

# Acesso a internet

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Acesso indisponível...')
else:
    print('Acesso disponível...')
finally:
    print('Programa fucionando com sucesso. Teste a conexão novamente quando quiser.')