from urllib.request import urlopen
from urllib.parse import urlencode
def qr_code(data):
    para={'cht':'qr','chs':'400x400','chl':data}
    qr_link='https://chart.googleapis.com/chart?'+urlencode(para)
    qr_make=urlopen(qr_link)
    qr_cod=qr_make.read()
    qr=open('qr.png','wb')
    qr.write(qr_cod)
    qr.close()