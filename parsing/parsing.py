import feedparser
newsfeed = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")
for i in range(5):
    print(newsfeed['entries'][i]['title'])
    print(newsfeed['entries'][i]['link'])