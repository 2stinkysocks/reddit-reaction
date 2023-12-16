import requests
import json

stories = requests.get("https://reddit.com/r/nosleep/hot.json", headers={"User-Agent":"Mozilla/5.0 (X11; Linux i686; rv:110.0) Gecko/20100101 Firefox/110.0."})

file = open("stories.json", 'w')
file.write(stories.content.decode('utf-8'))