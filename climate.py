import tweepy # for tweet mining
import pandas as pd
import numpy as np
import csv # to read and write csv files
import re # In-built regular expressions library
import string # Inbuilt sting library
import glob # to retrieve files/pathnames matching a specified pattern. 
import requests # to GET HTTP requests
from PIL import Image # for opening, manipulating, and saving many different image file f
import matplotlib.pyplot as plt # for plotting

from nltk.corpus import stopwords # get stopwords from NLTK library
from nltk.corpus import words # Get all words in english language

#Text Sentiments
#TextBlob - Python library for processing textual data
import textblob
from textblob import TextBlob 


# WordCloud - Python linrary for creating image wordclouds
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from ast import literal_eval


# Access keys and codes you need from your Twitter Developer Account
consumer_key = '3yWVRdPvvUwSlUiVT7nQPvpjJ'
consumer_secret = 'ot2jRWkMSmpTlC9a0oz6oIuw00IpEWAZTuCNtRYqviOcxOsOQC'
access_token = '430156574-lSwq3rIl70lyvGOcW1Onlif4jOmGYbujZ74fQx3g'
access_token_secret = 'jR5bFD5GyDr8Uof8TRdszAn4NPpZJ8fZxPSddbUx5VvAa'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) # Pass in Consumer key and secret for authentication by API
auth.set_access_token(access_token, access_token_secret) # Pass in Access key and secret for authentication by API
api = tweepy.API(auth,wait_on_rate_limit=True) # Sleeps when API limit is reached

def get_tweets(search_query, num_tweets):
    # Collect tweets using the Cursor object
    # Each item in the iterator has various attributes that you can access to get information about each tweet
    tweet_list = [tweets for tweets in tweepy.Cursor(api.search_tweets,
                                    q= search_query,
                                    lang="en",
                                    tweet_mode='extended').items(num_tweets)]
    # Begin scraping the tweets individually:
    for tweet in tweet_list:
        tweet_id = tweet.id # get Tweet ID result
        created_at = tweet.created_at # get time tweet was created
        text = tweet.full_text # retrieve full tweet text
        location = tweet.user.location # retrieve user location
        retweet = tweet.retweet_count # retrieve number of retweets
        favorite = tweet.favorite_count # retrieve number of likes
        with open('cop26a.csv','a', newline='', encoding='utf-8') as csvFile:
            csv_writer = csv.writer(csvFile, delimiter=',') # create an instance of csv object
            csv_writer.writerow([tweet_id, created_at, text, location, retweet, favorite]) # write each row
            
# Specifying exact phrase to search for. This is not case senstitive
search_words = "cop26 OR #cop26 OR #COP26 OR COP26 OR #ClimateCrisis OR climatecrisis"
# Exclude Links, retweets, replies
search_query = search_words + " -filter:retweets AND -filter:replies"
#with open('tweets_bridgerton.csv', encoding='utf-8') as data:
    #latest_tweet = int(list(csv.reader(data))[-1][0]) # Return the most recent tweet ID
#get_tweets(search_query,50000) # Call your function and pass in your search query and number of tweets you want to get

# THIS FUNCTION IS USED TO MINE TWEETS THAT ARE OLDER THAN THE TWEETS YOU HAVE.
def get_tweets2(search_query, num_tweets, max_id_num):
    # Collect tweets using the Cursor object
    # Each item in the iterator has various attributes that you can access to get information about each tweet
    tweet_list = [tweets for tweets in tweepy.Cursor(api.search_tweets,
                                                        q=search_query,
                                                        lang="en",
                                                        max_id=max_id_num, # max_id is the oldest tweet id you have
                                                        tweet_mode='extended').items(num_tweets)]
    # Begin scraping the tweets individually:
    for tweet in tweet_list:
        tweet_id = tweet.id  # get Tweet ID result
        created_at = tweet.created_at  # get time tweet was created
        text = tweet.full_text  # retrieve full tweet text
        location = tweet.user.location  # retrieve user location
        retweet = tweet.retweet_count  # retrieve number of retweets
        favorite = tweet.favorite_count  # retrieve number of likes
        with open('cop26b.csv', 'a', newline='', encoding='utf-8') as csvFile:
            csv_writer = csv.writer(csvFile, delimiter=',')  # create an instance of csv object
            csv_writer.writerow([tweet_id, created_at, text, location, retweet, favorite])  # write each row
            
# Specifying exact phrase to search
search_words = "cop26 OR #cop26 OR #COP26 OR COP26 OR #ClimateCrisis OR climatecrisis" 
# Exclude Links, retweets, replies
search_query = search_words + " -filter:retweets AND -filter:replies"
with open('cop26a.csv', encoding='utf-8') as data:
    oldest_tweet = int(list(csv.reader(data))[-1][0]) # Return the oldest tweet ID
#get_tweets2(search_query,50000,oldest_tweet) 

# THIS FUNCTION IS USED TO MINE TWEETS THAT ARE NEWER THAN THE TWEETS YOU HAVE.
#def get_tweets3(search_query, num_tweets, since_id_num):
#    # Collect tweets using the Cursor object
#    # Each item in the iterator has various attributes that you can access to get information about each tweet
#    tweet_list = [tweets for tweets in tweepy.Cursor(api.search_tweets,
#                                    q=search_query,
#                                    lang="en",
#                                    since_id=since_id_num, # since_id is the most recent tweet id you have
#                                    tweet_mode='extended').items(num_tweets)]
#    # Begin scraping the tweets individually:
#    for tweet in tweet_list:
#        tweet_id = tweet.id # get Tweet ID result
#        created_at = tweet.created_at # get time tweet was created
#        text = tweet.full_text # retrieve full tweet text
#        location = tweet.user.location # retrieve user location
#        retweet = tweet.retweet_count # retrieve number of retweets
#        favorite = tweet.favorite_count # retrieve number of likes
#        with open('tweets3.csv','a', newline='', encoding='utf-8') as csvFile:
#            csv_writer = csv.writer(csvFile, delimiter=',') # create an instance of csv object
#            csv_writer.writerow([tweet_id, created_at, text, location, retweet, favorite]) # write each row
## Specifying exact phrase to search
#search_words = "Squidgame OR Squidgames OR #squidgame OR #squidgames OR #squidgamesnetflix OR #squidgamenetflix OR #squidgamelive" 
## Exclude Links, retweets, replies
#search_query = search_words + " -filter:retweets AND -filter:replies"
#with open('tweets2.csv', encoding='utf-8') as data:
#    latest_tweet = int(list(csv.reader(data))[0][0]) # Return the most recent tweet ID
#get_tweets3(search_query,100,latest_tweet)



path = r"/Users/gold/Desktop/learning_python/Squid_Game/climate_change/cop2021"  # use your path
all_files = glob.glob(path + "/*.csv")

tweets = []

for filename in all_files:
    df = pd.read_csv(filename, index_col = None, header = None) # Convert each csv to a dataframe
    tweets.append(df)

tweets_df = pd.concat(tweets, axis=0, ignore_index = True) # Merge all dataframes
tweets_df.columns = ('new_id','id','created_at','text','location','fave','likes','location_data')
#tweets_df.index+=1

tweets_df.drop('new_id',axis=1, inplace=True)
tweets_df = tweets_df.drop([0])
tweets_df.drop_duplicates(subset=['id'],keep='last',inplace=True)


tweets_df['location'] = tweets_df['location'].fillna('No location')        
        
#tweets_df.drop([95038,24531], inplace=True)


#Convert all Nan values in location_data to string
def try_literal_eval(s):
    try:
        return literal_eval(s)
    except ValueError:
        result = "{'items': []}"
        return result


tweets_df['location_to_string'] = tweets_df['location_data'].apply(try_literal_eval)

#convert all string values in location_data to dict
def try_literal(s):
    try:
        return literal_eval(s)
    except ValueError:
        return s

tweets_df['location_to_dict'] = tweets_df['location_to_string'].apply(try_literal)



URL = "https://geocode.search.hereapi.com/v1/geocode"  # Deevloper Here API link
api_key = 'o9Ga7EuC_pj9eViLzurCh5wel1PkhPhGm2gmfTl2imA'  # Acquire api key from developer.here.com


#Run this code once to get get the geographic location of all values in location_data

#def getCoordinates(location):
#    PARAMS = {'apikey': api_key, 'q': location} # required parameters
#    r = requests.get(url=URL, params=PARAMS)  # pass in required parameters
#    # get raw json file. I did  this because when I combined this step with my "getLocation" function, 
#    # it gave me error for countries with no country_code or country_name. Hence, I needed to use try - except block
#    data = r.json() # Raw json file 
#    return data
##
#tweets_df['Location_data']=tweets_df['location'].apply(getCoordinates) # Apply getCoordinates Function




#This function seperates teh country_code from the country_name
def getLocation(location):
                
    for data in location:
        if len(location['items']) > 0:
            try:   
                country_code = location['items'][0]['address']['countryCode']
                country_name = location['items'][0]['address']['countryName']
            except TypeError:
                country_code = float('Nan')
                country_name = float('Nan')
        else: 
            country_code = float('Nan') 
            country_name = float('Nan')
        result = (country_code, country_name)
        return result

tweets_df['Country_name_code'] = tweets_df['location_to_dict'].apply(getLocation) #apply getLocation function


# Extraction of Country names to different columns
tweets_df[['Country_Code','Country_Name']] = pd.DataFrame(tweets_df['Country_name_code'].tolist(),index=tweets_df.index)


# Drop unnecessary columns
tweets_df.drop(['location','location_data','Country_name_code','location_to_string','location_to_dict'], axis = 1, inplace = True)


def getHashtags(tweet):
    tweet = tweet.lower()  #has to be in place
    tweet = re.findall(r'\#\w+',tweet) # Seperate hastags with REGEX
    return " ".join(tweet)

tweets_df['Hashtags'] = tweets_df['text'].apply(getHashtags)

hashtags_list = tweets_df['Hashtags'].tolist()

#iterate over all hashtags so they can be split where there is more than one hashtag per row
hashtags = []
for item in hashtags_list:
    item = item.split()
    for i in item:
        hashtags.append(i)

        #Use the Built-in Python Collections module to determine Unique count of all hashtags used
from collections import Counter
counts = Counter(hashtags)
hashtags_df = pd.DataFrame.from_dict(counts, orient='index').reset_index()
hashtags_df.columns = ['Hashtags', 'Count']
hashtags_df.sort_values(by='Count', ascending=False, inplace=True)
print (f'Total Number of Unique Hashtags is: {hashtags_df.shape[0]}.')

hashtags_df["Percentage"] = 100*(hashtags_df["Count"]/hashtags_df['Count'].sum())
hashtags_df = hashtags_df.head(10)


# Create function to obtain Polarity Score
def getPolarity(tweet):
    return TextBlob(tweet).sentiment.polarity

# Create function to obtain Sentiment category
def getSentimentTextBlob(polarity):
    if polarity < 0:
        return "Negative"
    else:
        return "Positive"
    

#Code to create wordcloud

# Start with one review to see how it shows up:
tweets_df['text'][3]

#concantonate all tweets for easy parsing of words for word cloud
text = " ".join(review for review in tweets_df.text)


#Create stopwords to eliminate unecessary characters or words
stopwords = set(STOPWORDS)
morewords = ['’', '...', '..', '.', '.....', '....','t', 'https','co','need','amp','look','using','far','says','going','car','made','yet','girl','c','s','girls','ve','emailed','AlokSharma_RDG','unknown Alt','unknown','re','wituawaboot','email','see','us']
alphabets = list(string.ascii_lowercase)

new_words = alphabets + morewords

stopwords.update(new_words)

#insert image to use for word cloud
climate_change_mask = np.array(Image.open("warming2.png"))


# Instantiate the Twitter word cloud object
climate_wordcloud = WordCloud(stopwords=stopwords,background_color='salmon', max_words=200, mask=climate_change_mask, contour_width=3, contour_color='green')

# generate the word cloud
climate_wordcloud.generate(text)

# display the word cloud
fig = plt.figure()
fig.set_figwidth(14)  # set width
fig.set_figheight(18)  # set height

plt.imshow(climate_wordcloud, interpolation="bilinear")
plt.axis('off')
plt.show()

climate_wordcloud.to_file("climate_mask.png")

