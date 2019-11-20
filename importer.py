# this code is largely based on this very interesting tutorial by Marco Bonzanini: 
# https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/

from datetime import datetime, date, time, timedelta
import pymysql
import tweepy
from tweepy import OAuthHandler
from collections import Counter

consumer_key = 'INSERT YOUR KEY HERE'
consumer_secret = 'INSERT YOUR SECRET HERE'
access_token = 'INSERT YOUR ACCESS TOKEN HERE'
access_secret = 'INSERT YOUR ACCESS SECRET HERE'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

account_list = ["GiuseppeConteIT","luigidimaio","nzingaretti","matteorenzi","GiorgiaMeloni","matteosalvinimi","CarloCalenda","berlusconi","civati"]

if len(account_list) > 0:
  for target in account_list:
    item = api.get_user(target)
    user_name =  str(item.name)
    screen_name = str(item.screen_name)
    profile_image_url = str(item.profile_image_url)
    description = str(item.description)
    statuses_count = str(item.statuses_count)
    friends_count = str(item.friends_count)
    followers_count = str(item.followers_count)
    tweets = str(item.statuses_count)
    account_created_date = item.created_at
    delta = datetime.utcnow() - account_created_date
    account_age_days = delta.days
    average_tweets = 0
    if account_age_days > 0:
      average_tweets = str(round(int(tweets)/int(account_age_days),2))
    account_age_days = str(account_age_days)
    hashtags = []
    mentions = []
    tweet_count = 0
    end_date = datetime.utcnow() - timedelta(days=365)
    for status in tweepy.Cursor(api.user_timeline, id=target).items():
      tweet_count += 1
      if hasattr(status, "entities"):
        entities = status.entities
        if "hashtags" in entities:
          for ent in entities["hashtags"]:
              if ent is not None:
                if "text" in ent:
                  hashtag = ent["text"]
                  if hashtag is not None:
                    hashtags.append(hashtag)
        if "user_mentions" in entities:
          for ent in entities["user_mentions"]:
              if ent is not None:
                if "screen_name" in ent:
                  name = ent["screen_name"]
                  if name is not None:
                    mentions.append(name)
      if status.created_at < end_date:
          break
      most_mentioned_users = ""
    for item, count in Counter(mentions).most_common(10):
      most_mentioned_users += item + "\t" + str(count) + "\n"
    most_used_hashtags = ""
    for item, count in Counter(hashtags).most_common(10):
      most_used_hashtags += item + "\t" + str(count) + "\n"
    processed_tweets = str(tweet_count)
    creation_day = str(datetime.today().strftime('%Y-%m-%d'))
    creation_date = str(datetime.now())
    
    # write to db
    db = pymysql.connect("localhost","YOUR USERNAME","YOUR PASSWORD","YOUR DB NAME")
    cursor = db.cursor()
    sql = "INSERT INTO scrapes (name, screen_name, profile_image_url, description, statuses_count, friends_count, followers_count, account_age_days, average_tweets, most_mentioned_users, most_used_hashtags,processed_tweets, creation_date, creation_day) VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    try:
      cursor.execute(sql,(user_name, screen_name, profile_image_url, description, statuses_count, friends_count, followers_count, account_age_days, average_tweets, most_mentioned_users, most_used_hashtags, processed_tweets, creation_date, creation_day))
      db.commit()
    except:
      print(cursor._last_executed)
      raise
      db.rollback()
    print(screen_name + " processed successfully.")
    db.close()
