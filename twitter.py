import tweepy
from exchanges import CoinDesk
from time import sleep

last_price =  8873.72

count =1
mins = 30

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def get_price():
    price_usd = round(CoinDesk().get_current_price(currency='USD'), 2)
    price_inr = round(CoinDesk().get_current_price(currency='INR'), 2)

    global last_price
    per_change = ((float(price_usd) - last_price) / float(price_usd)) * 100
    per_change = round(per_change, 2)
    last_price = float(price_usd)

    bitcoin_rate = ''' 
       in USD : ''' + str(price_usd) + '''$
       in INR : ''' + str(price_inr) + ''' Rs

       %age change since last update = ''' + str(per_change) + '''%

       #Bitcoin #Crypto #Cryptocurrency
       '''
    return bitcoin_rate

api.update_status("#"+str(count)+" Latest Bitcoin Price is " + get_price())
print("Status posted so far :" + str(count))
count+=1
while True:
    sleep(30*mins)
    api.update_status("#"+str(count)+" Latest Bitcoin Price is "+get_price())
    print("Status posted so far :" + str(count))
    count+=1


