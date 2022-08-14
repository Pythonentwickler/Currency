#pip install forex-python

#list of USD exchange rates
from forex_python.converter import CurrencyRates
c = CurrencyRates()
c.get_rates('USD')


#Convert USD to EURO
from forex_python.converter import CurrencyRates 
c = CurrencyRates()
Currency = c.get_rate('USD', 'EUR')  
print(Currency)
print(round(Currency, 3))


#bitcoin's price in USD
from forex_python.bitcoin import BtcConverter
b = BtcConverter()
b.get_latest_price('USD')
