import tweepy
from exchanges import CoinDesk
from time import sleep


count =1
mins = 30
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def get_price():
    price_usd = round(CoinDesk().get_current_price(currency='USD'), 2)
    price_inr = round(CoinDesk().get_current_price(currency='INR'), 2)

    bitcoin_rate = ''' 
    in USD : '''+ str(price_usd) +'''$
    in INR : '''+str(price_inr)+''' Rs
    
    #Bitcoin #Crypto #Cryptocurrency
    '''
    return bitcoin_rate


api.update_status("#"+str(count)+" Latest Bitcoin Price is " + get_price())
print("#"+str(count)+" Status posted so far :" + str(count))
count+=1
while True:
    sleep(30*mins)
    api.update_status("#"+str(count)+" Latest Bitcoin Price is "+get_price())
    print("#"+str(count)+" Status posted so far :" + str(count))
    count+=1



