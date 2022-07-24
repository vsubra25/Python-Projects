import tweepy

auth = tweepy.OAuthHandler("OkrZIqfb5cd4Rz6BRWNhJ70j4",
                           "AQVYzRipy0mngdgEyC6o4St9NBbH1aleYJm7UCNHM6nn8HKCJ2")
auth.set_access_token(
    "1490542150987120642-w8EN0HLlxUaCbFS9M1HjLytkW10SCD", "R7eFFrGh1GqYGzEvKOZHSllc4A7MgxgFuzKQyGOpcAfje")

#bearer Token
client = tweepy.Client(
    "AAAAAAAAAAAAAAAAAAAAAMnUYwEAAAAAwnPVvnroUB0dAyU3Q5mITISqWnE%3DPSVDmKijQgklxxeWG1iaahm9X4uIkAS4gZmFXeDQkZHkT3ucs2")
api = tweepy.API(auth)

user=api.me()

def limit_handle(cursor):
    try:
        while true:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


search_str='python'

numberOfTweets=2


for response in tweepy.Paginator(client.get_users_followers, 2244994945,max_results=1000, limit=5):
    print(response.meta)

for tweet in tweepy.Paginator(client.search_recent_tweets, "Tweepy", max_results=100).flatten(limit=250):
    print(tweet.id)



# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     print(follower)

