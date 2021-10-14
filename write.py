from TwitterAPI import TwitterAPI
import time

from textgenrnn import textgenrnn

# api = TwitterAPI("vYuCfQfvXww8eixiO1Fdoa0u6", "5R5ZtEiXk6DrF1Imnw2ggzzGwiFZCshK3z45RaEzLqOTIRc5ei", auth_type="oAuth2")

# r = api.request('statuses/update', {'status': 'Test'})
# print(str(r))
# print('SUCCESS' if r.status_code == 200 else r.text)

textgen = textgenrnn()
textgen.load('textgenrnn_weights.hdf5')

while True:
    time.sleep(10)
    print(textgen.generate(temperature=0.9, return_as_list=True))