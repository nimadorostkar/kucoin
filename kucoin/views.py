from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django import template
from django.urls import reverse
from kucoin.client import Client





#------------------------------------------------------------------------------
def index(request):
    return render(request, 'index.html', context)




#------------------------------------------------------------------------------
def client(request):

    api_key = '<api_key>'
    api_secret = '<api_secret>'
    api_passphrase = '<api_passphrase>'

    client = Client(api_key, api_secret, api_passphrase)

    # or connect to Sandbox
    # client = Client(api_key, api_secret, api_passphrase, sandbox=True)

    # get currencies
    currencies = client.get_currencies()

    # get market depth
    depth = client.get_order_book('KCS-BTC')

    # get symbol klines
    klines = client.get_kline_data('KCS-BTC')

    # get list of markets
    markets = client.get_markets()

    # place a market buy order
    order = client.create_market_order('NEO', Client.SIDE_BUY, size=20)

    # get list of active orders
    orders = client.get_active_orders('KCS-BTC')


    context = {'client':client,
        'currencies':currencies,
        'depth':depth,
        'klines':klines,
        'markets':markets,
        'order':order,
        'orders':orders
    }
    
    return render(request, 'client.html', context)












# End
