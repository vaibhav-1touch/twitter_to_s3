import tweepy
import json
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

consumer_key = 'qtykcLhI0wFG229kvnX9TAUFX'
consumer_secret = '8UWGqW3JjzDAzJdZ2PVdatmdGgQ9GVqC4F5WK22k7XSzSLyAGQ'
access_key = '1257214984943104000-Cq2sWlBzVJhuHLANQwOn1CLfUnzcGU'
access_secret = 'Qm2Nbz1sD8e8zV3rZ8ileKWjG8SEVbqaNUCAo6gf5tyEc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

class myStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        future = producer.send('my_topic', (json.dumps({'user':status.user.screen_name, 'tweet':status.text})).encode('utf-8'))
        response = future.get(timeout=10)
        print(response.topic)
        print(response.partition)
        print(response.offset)
        print(status)
    def on_error(self, status_code):
        if status_code == 420:
            return False

listener = myStreamListener()

myStream = tweepy.Stream(auth=api.auth, listener=listener)

myStream.filter(track=['Modi'])