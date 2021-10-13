from TwitterAPI import TwitterAPI
import time

api = TwitterAPI("vYuCfQfvXww8eixiO1Fdoa0u6", "5R5ZtEiXk6DrF1Imnw2ggzzGwiFZCshK3z45RaEzLqOTIRc5ei", auth_type="oAuth2")
r = api.request('search/tweets', {'q':'locotamerzoa'})


def produce_message(topic: str, key: int, value: str) -> None:
    print(
        f"{value}"
    )


counter=0
while True:
    for item in r.get_iterator():
        counter += 1
        print("{} {} {}".format(item["created_at"], item['user']['screen_name'], item['text']))
        # produce_message(
        #         topic="tweets_pizza",
        #         key=counter,
        #         value=" ".join([item['user']['screen_name'], item['text']]),
        # )
    time.sleep(1)
    print(counter)