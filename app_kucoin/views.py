from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django import template
from django.urls import reverse
from kucoin.client import Client
from app_authentication.models import Profile
from app_kucoin.models import Exchange

import ccxt



#------------------------------------------------------------------------------
def index(request):
    return render(request, 'index.html')





#------------------------------------------------------------------------------
def dashboard(request):
    profile = get_object_or_404(Profile, user=request.user)
    exchanges = Exchange.objects.filter(user=request.user)
    context = {'profile':profile,'exchanges':exchanges}
    return render(request, 'dashboard/dashboard.html', context)












#------------------------------------------------------------------------------
def exchangeItem(request, id):
    # https://readthedocs.org/projects/python-kucoin/downloads/pdf/stable/   <- Good Documentation
    # https://github.com/sammchardy/python-kucoin/blob/develop/kucoin/client.py
    # https://hive.blog/hive-169321/@dkmathstats/crypto-data-from-kucoin-in-python
    profile = get_object_or_404(Profile, user=request.user)
    exchange = get_object_or_404(Exchange, id=id)

    client = Client(exchange.api_key, exchange.api_secret, exchange.api_passphrase)
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
    #order = client.create_market_order('NEO', Client.SIDE_BUY, size=20)

    # get list of active orders
    #orders = client.get_active_orders('KCS-BTC')


    btc = client.get_currency('BTC')

    #account = client.create_account('trade', 'BTC')
    #get_account = client.get_account('6257f0570b9df500013d54c5')



    context = {'exchange':exchange,
        'profile':profile,
        'client':client,
        'currencies':currencies,
        'depth':depth,
        'klines':klines,
        'markets':markets,
        #'order':order,
        #'orders':orders,
        'btc':btc
        }
    return render(request, 'dashboard/exItem.html', context)


















#------------------------------------------------------------------------------
def addExchange(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method=="POST":
        exchange=Exchange()
        exchange.user = request.user
        exchange.api_key = request.POST['api_key']
        exchange.api_secret = request.POST['api_secret']
        exchange.api_passphrase = request.POST['api_passphrase']
        exchange.status = request.POST['status']
        exchange.name = request.POST['name']
        exchange.save()
        return render(request, 'dashboard/addExchange.html', {'profile':profile, 'exchange':exchange})

    context = {'profile':profile}
    return render(request, 'dashboard/addExchange.html', context)










#------------------------------------------------------------------------------
def client(request):

    #https://python-kucoin.readthedocs.io/en/latest/
    api_key = '62402a681634ba000102877f'
    api_secret = 'bb2ce4a8-ff4a-4859-965d-547e0fa43068'
    api_passphrase = '12345678test'

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
    #order = client.create_market_order('NEO', Client.SIDE_BUY, size=20)

    # get list of active orders
    #orders = client.get_active_orders('KCS-BTC')


    context = {'client':client,
        'currencies':currencies,
        'depth':depth,
        'klines':klines,
        'markets':markets,
        #'order':order,
        #'orders':orders
    }

    return render(request, 'client.html', context)





#------------------------------------------------------------------------------
def currencies(request):
    # DEFINE YOUR EXCHANGE AND TICKERS:
    my_exchange = 'Kucoin' # example of crypto exchange
    ticker1 = 'BTC' # first ticker of the crypto pair
    ticker2 = 'USDT' # second ticker of the crypto pair
    method_to_call = getattr(ccxt,my_exchange.lower()) # retrieving the # method from ccxt whose name matches the given exchange name
    exchange_obj = method_to_call() # defining an exchange object
    pair_price_data = exchange_obj.fetch_ticker(ticker1+'/'+ticker2)
    closing_price = pair_price_data['close']

    context = { 'pair_price_data':pair_price_data, 'closing_price':closing_price}
    return render(request, 'currencies.html', context)










# End
