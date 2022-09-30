currency_dict={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
currency_input= input('please enter a currency, eg: Dollar, Euro or Yen:')
print(currency_dict.get(currency_input, 'currency not found'))