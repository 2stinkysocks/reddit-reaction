import json
import sys

from tiktokvoice import tts

if(len(sys.argv) <= 1):
    print("No args!")
    exit()

index = sys.argv[1]

file = open("stories.json", 'r')
stories = json.loads(file.read())
#print(stories)
file.close()

title = stories["data"]['children'][int(index)]["data"]["title"].replace("\n", "").replace("\r", "")
body = stories["data"]['children'][int(index)]["data"]["selftext"].replace("\n", "").replace("\r", "")

fulltts_text = title + "...  " + body
print(fulltts_text)

tts(fulltts_text, "en_us_006", "tts.mp3")

'''
get the title and get the body
convert the title and body to tts with tiktok tts
convert tiktok tts to subtitles with timestamps
cut random point in mc parkour
overlay the tiktok tts and create subtitles 
'''