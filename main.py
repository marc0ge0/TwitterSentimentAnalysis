import config
import tweepy
from textblob import TextBlob as tb

# use api keys and access tokens to access twitter api using tweepy library
auth = tweepy.OAuthHandler(config.apiKey, config.apiSecretKey)
auth.set_access_token(config.accessToken, config.secretAccessToken)

api = tweepy.API(auth)

# set word you want a sentiment analysis of. In this case I used the word 'dog'
myWord = "dog"


# This function finds the average sentiment values for the most recent tweets that contain a
# particular word. This helps us gain insight into public opinion surrounding the word based on
# the subjectivity and polarity of the tweets
def findAvgSentiment(word):
    # find all public tweets containing the word
    publicTweets = api.search(word)

    # the sum of all the subjectivity values and polarity values of every tweet
    total_subjectivity = 0
    total_polarity = 0

    # the total number of tweets queried
    tweet_count = float(0)

    # for every tweet in the query
    for tweet in publicTweets:
        # get sentiment values from textblob
        sentiment = tb(tweet.text).sentiment
        subjectivity = sentiment.subjectivity
        polarity = sentiment.polarity

        # add them to the total values
        total_subjectivity += subjectivity
        total_polarity += polarity

        # increment tweet count
        tweet_count += 1

    avg_subjectivity = total_subjectivity / tweet_count
    avg_polarity = total_polarity / tweet_count

    print("Out of the most recent tweets with the word " + word + ", the average subjectivity of "
                                                                 "the tweets on a scale from -1 "
                                                                 "to 1 was:")
    print(avg_subjectivity)
    print("And the average polarity was: ")
    print(avg_polarity)


findAvgSentiment("dog")
findAvgSentiment("coronavirus")
findAvgSentiment("teenager")
findAvgSentiment("hate")
findAvgSentiment("happy")
