#Author: Isaac Feldman (isaac.c.feldman.23@dartmouth.edu)

import os, argparse, feedparser
from os import path
parser = argparse.ArgumentParser()
parser.parse_args()

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



