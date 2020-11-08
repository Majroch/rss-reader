#!/usr/bin/env python3
import Feeder, MenuRenderer

feedurls = []

try:
    with open('rss.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip()
            if line:
                feedurls.append(line)
except FileNotFoundError:
    print("Cannot find `rss.txt` file in this directory! Creating one...")
    with open("rss.txt", 'w') as file:
        file.write("")
    exit()

feeder = Feeder.Feeder(feedurls)

options = feeder.getTitles()

menu = MenuRenderer.MenuRenderer("Select RSS to Show", options)

selected = menu.run()

print("\nAll Feeds in this topic:\n\n")
for feed in feeder.getFeedsByIndex(selected):
    print(feed.title, ":")
    print('\t', feed.link)
    print('\n\t', feed.summary, '\n')
