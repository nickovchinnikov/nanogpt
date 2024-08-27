# %%
import requests

# We always start with a dataset to train on. Let's download the tiny shakespeare dataset
url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"

# Download the data by url with python requests
data = requests.get(url).text
len(data)

# %%