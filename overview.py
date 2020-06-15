#Author: Isaac Feldman (isaac.c.feldman.23@dartmouth.edu)

import os, feedparser, requests, json

def get_top_news(n):
    """
    Pulls the top n news headlines from Google News
    :param n: number of headlines
    :return: a dict with format "headline":"link"
    """
    newsfeed = feedparser.parse("https://news.google.com/news/rss")
    headlines = {}
    for i in range(n):
        title = newsfeed.entries[i]['title']
        link = newsfeed.entries[i]['link']
        headlines[title] = link
    return headlines

def get_weather(loc):
    access_key = "426c2cdfb8d60e4504479e3814e21802"
    response = requests.get("http://api.weatherstack.com/current?"+"access_key="+access_key+"&query="+loc)
    content = json.loads(response.content)

    location = content['location']['name']
    region = content['location']['region'] # Todo: Why is this in quotes?
    temp = content['current']['temperature']
    desc = content['current']['weather_descriptions']
    precip = content['current']['precip']

    if content['request']['unit'] == 'm':
        unit = "C"
    else:
        unit = "F"

    print("The weather in %s, %r is:" % (location, region))
    print("Temp: %r%s" %(temp, unit))
    print("Chance of Precipitation: %s percent" % precip)
    print(", ".join(desc))



def glance():
    print("Here are the top stories of the day:")
    stories = get_top_news(5)
    for line in stories.keys():
        print(line)

    get_weather("New York")

if __name__ == "__main__":
    glance()

