### FEEDER CLASS ###
import feedparser

class Feeder:
    def __init__(self, urls:list=[]):
        self.urls = urls

    def getTitles(self) -> list:
        output = []
        for url in self.urls:
            output.append(feedparser.parse(url)['feed']['title'])

        return output
            
    def getLatestFeeds(self) -> list:
        output = []
        for url in self.urls:
            for feed in feedparser.parse(url).entries[:10]:
                output.append(feed)
        
        return output

    def getFeedsByIndex(self, index:int=0) -> list:
        try:
            feedurl = self.urls[index]
        except KeyError:
            print("Cannot find that feed you're lookin' for :/")
            return []

        return feedparser.parse(feedurl).entries[:10]
