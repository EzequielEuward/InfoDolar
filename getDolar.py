import requests
import time
from bs4 import BeautifulSoup

def getDolarVenta():
    url = 'https://www.infodolar.com/cotizacion-dolar-provincia-cordoba.aspx'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    dolar_blue_venta = soup.select_one('table#BluePromedio.cotizaciones td.colCompraVenta + td').text.split()[1].strip()
    
    dolar_blue_venta = dolar_blue_venta.replace(".", "")
    dolar_blue_venta = dolar_blue_venta.replace(",",".")
    dolar_blue_venta = float(dolar_blue_venta)
    return dolar_blue_venta


def getDolarCompra():
    url = 'https://www.infodolar.com/cotizacion-dolar-provincia-cordoba.aspx'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    dolar_blue_compra = soup.select_one('table#BluePromedio.cotizaciones td.colCompraVenta').text.split()[1].strip()
    dolar_blue_compra = dolar_blue_compra.replace(".", "")
    dolar_blue_compra = dolar_blue_compra.replace(",", ".")
    dolar_blue_compra = float(dolar_blue_compra)
    return dolar_blue_compra














