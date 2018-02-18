import tweepy
from exchanges import CoinDesk
from time import sleep

last_price =  8873.72

count =1
mins = 60

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def get_graph_data(current_price):
    global prices,hour
    prices.append(current_price)
    hour.append(datetime.datetime.now().strftime("%H:%M"))


def get_price():
    price_usd = round(CoinDesk().get_current_price(currency='USD'), 2)
    price_inr = round(CoinDesk().get_current_price(currency='INR'), 2)
    get_graph_data(price_usd)
    global last_price
    per_change = ((float(price_usd) - last_price) / float(price_usd)) * 100
    per_change = round(per_change, 2)
    last_price = float(price_usd)

    bitcoin_rate = '''
       in USD : ''' + str(price_usd) + '''$
       in INR : ''' + str(price_inr) + ''' Rs

       %age change since last update= ''' + str(per_change) + '''%

       #bitcoin #crypto #cryptocurrency
       '''
    return bitcoin_rate


def plot_graph():
    global prices, hour
    day = 'Bitcoin Price behaviour for ' + datetime.datetime.now().strftime("%d-%m-%Y")
    plt.title(str(day))
    plt.plot(hour, prices)
    plt.grid(True)
    plt.xlabel('Time')
    plt.ylabel('Price in USD')
    name = 'graphs/' + str(datetime.datetime.now().strftime("%d-%m-%Y")) + '.png'
    plt.savefig(str(name))
    prices=[]
    hour=[]
    return str(name)



while True:
    if(count%48==0):
        graph_stat = '''Today's Bitcoin Price Activity in graph 
        #bitcoin #crypto #cryptocurrency'''
        api.update_with_media(plot_graph(),graph_stat)
        api.update_status("Latest Bitcoin Price is " + get_price())
    else:
        api.update_status("Latest Bitcoin Price is "+get_price())

    print("Status posted so far :" + str(count))
    count+=1
    sleep(30 * mins)