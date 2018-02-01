import tweepy


auth = tweepy.OAuthHandler('pp4D8qUHx5dItxs4WUzXBcqpZ','ALINzkGlnYtjUqL9LZkl3DScuzegmoAv5L9NOMB1LkNhMt3PcP')
auth.set_access_token('3151015956-PR2cBInu83IcORPcPZQp1xkTfO3qBRmtrew1902','n2GJyHu4Ov5oPuSY1EchuLFG8xl8WIHC61F0LmRapxp5G')

api = tweepy.API(auth)

text=input("Enter the Text you want to tweet")

api.update_status(text)


