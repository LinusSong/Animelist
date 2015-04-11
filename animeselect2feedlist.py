#-*-coding:utf-8 -*-
import re
resource = open("animeselect.html")
target = open("feedlist.txt","w")
a = 0
linecontent = resource.read().split("\n")
linecontent.pop(-1)
for i in linecontent:
    commaone = i.find(",")
    commatwo = i.find(",",commaone + 1)
    teamone = i.find("\">")
    teamtwo = i.find("</a>",teamone + 1)
    title = i[:commatwo] + ',' + i[teamone + 2:teamtwo] + ':'
    rssone = i.find("href=") + 6
    rsstwo = teamone
    rss = i[rssone:rsstwo]
    target.write(title + rss + '\n')
