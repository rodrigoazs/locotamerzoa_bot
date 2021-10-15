from TwitterAPI import TwitterAPI
import time
import re

from textgenrnn import textgenrnn

api = TwitterAPI(
    "CAByBGau3qyUrCzUuv68VGkVC",
    "yOxh3ltcQ8j6P4hmU09PIZ8XwLMfhVZT1IaEhshEfxmZYNJ81B",
    "1448618690585534464-KnTrl7HPOCDLpJxAqIbyJYZSUhgTVY",
    "BDjX12qVkOqCuWKsHFe6xrLh5Cd6ExwnDCUNzHYsKi2Zu",
    # auth_type="oAuth2"
)

USER = "locotamerbot"

textgen = textgenrnn()
textgen.load('textgenrnn_weights.hdf5')

while True:
    # post a tweet
    # tweet = textgen.generate(temperature=0.9, return_as_list=True)
    # r = api.request('statuses/update', {'status': tweet[0]})
    # print('SUCCESS' if r.status_code == 200 else r.text)
    # time.sleep(60)

    # answer tweets
    r = api.request('search/tweets', {'q': USER})
    mentions = []
    my_replies = []

    # iterate over tweets
    for item in r.get_iterator():

        if "user_mentions" in item["entities"]:
            for mention in item["entities"]["user_mentions"]:
                if mention["screen_name"] == USER:
                    mentions.append(item)
                    break
        if "in_reply_to_status_id" in item and item["user"]["screen_name"] == USER:
            if item["in_reply_to_status_id"]:
                my_replies.append(item["in_reply_to_status_id"])

    # check not replied mentions
    for item in mentions:
        if item["id"] not in my_replies:
            if item["user"]["screen_name"] != USER:
                text = re.sub(r'@[a-zA-Z0-9_]+', '', item["text"])
                text = " ".join(text.split())
                tweet = textgen.generate(prefix=text, temperature=0.9, return_as_list=True)
                tweet = tweet[0][len(text):]
                print("answering", item["text"])
                mentions = "@{}".format(item["user"]["screen_name"])
                tweet = "{} {}".format(mentions, tweet)
                r = api.request('statuses/update', {'status': tweet, 'in_reply_to_status_id': item["id_str"]})
                print('SUCCESS' if r.status_code == 200 else r.text)

    print("sleeping")
    # check mentions 
    time.sleep(240)