#-*-coding:utf-8 -*-
import re
import urllib
import urllib2
#urllink = "http://share.dmhy.org/cms/page/name/programme.html"
#user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0'
#headers = { 'User-Agent' : user_agent }
#req = urllib2.Request(urllink, None, headers)
#response = urllib2.urlopen(req)
#pagecontent = response.read()
#urllib.urlretrieve ("http://share.dmhy.org/cms/page/name/programme.html","anime.html")
page = open("anime.html")
pagecontent = page.read()
pagecontent = pagecontent[pagecontent.find('//其它'):pagecontent.find('IE新窗')]
urls = re.findall('.{3}array.*<a href=.*<\/a>',pagecontent)
target = open("animeselect1.html","w")
target2 = open("animeselect2.html","w")
for i in urls:
    i = re.sub('array.push\(\[\'[a-zA-z]+://[^\s,]*','',i)
    i = re.sub('\'','',i)
    unicodetemp = i.find(",")
    unicodeleft = i.find(",",unicodetemp + 1)
    unicoderight = i.find(",",unicodeleft + 1)
    i = i[:unicodeleft]+i[unicoderight:]
    i = i.replace('/topics/list','http://share.dmhy.org/topics/rss/rss.xml')
    if i[0:3] == "mon":
        i = i.replace('mon','星期一')
    if i[0:3] == "tue":
        i = i.replace('tue','星期二')
    if i[0:3] == "wed":
        i = i.replace('wed','星期三')
    if i[0:3] == "thu":
        i = i.replace('thu','星期四')
    if i[0:3] == "fri":
        i = i.replace('fri','星期五')
    if i[0:3] == "sat":
        i = i.replace('sat','星期六')
    if i[0:3] == "sun":
        i = i.replace('sun','星期日')
    rssaddress = re.findall('<a href=[^>]*\>[^<]*\</a\>',i)
    commaone = i.find(",")
    commatwo = i.find(",",commaone + 1)
    # 極影
    if i.find("team_id%3A185\"") != -1:
        for a in rssaddress:
            if a.find("team_id%3A185\"") != -1:
                pos = a.find( "\">" )
                content = a[:pos] + "+GB+720+MP4&sort_id=2" + a[pos:]
                target.write(i[:commatwo+1] + content + '<br>')
                rsstest = re.findall('http://[^"]*',content)
#                if urllib.urlopen(rsstest[0]).read().find("<item>") == -1:
#                    target.write("This rss address is wrong. Please check it manually.<br>")
                target.write('\n')
    # 華盟
    elif i.find("team_id%3A49\"") != -1:
        for a in rssaddress:
            if a.find("team_id%3A49\"") != -1:
                pos = a.find( "\">" )
                content = a[:pos] + "+%E7%AE%80%E4%BD%93+720+MP4&sort_id=2" + a[pos:]
                target.write(i[:commatwo+1] + content + '<br>')
                rsstest = re.findall('http://[^"]*',content)
#                if urllib.urlopen(rsstest[0]).read().find("<item>") == -1:
#                    target.write("This rss address is wrong. Please check it manually.<br>")
                target.write('\n')
    # 千夏
    elif i.find("team_id%3A283\"") != -1:
        for a in rssaddress:
            if a.find("team_id%3A283\"") != -1:
                pos = a.find( "\">" )
                content = a[:pos] + "+%E7%B9%81%E9%AB%94+720+MP4&sort_id=2" + a[pos:]
                target.write(i[:commatwo+1] + content + '<br>')
                rsstest = re.findall('http://[^"]*',content)
#                if urllib.urlopen(rsstest[0]).read().find("<item>") == -1:
#                    target.write("This rss address is wrong. Please check it manually.<br>")
                target.write('\n')
    #輕之國度
    elif i.find("team_id%3A321\"") != -1:
        for a in rssaddress:
            if a.find("team_id%3A321\"") != -1:
                pos = a.find( "\">" )
                content = a[:pos] + "+GB+720+MP4&sort_id=2" + a[pos:]
                target.write(i[:commatwo+1] + content + '<br>')
                rsstest = re.findall('http://[^"]*',content)
#                if urllib.urlopen(rsstest[0]).read().find("<item>") == -1:
#                    target.write("This rss address is wrong. Please check it manually.<br>")
                target.write('\n')
    #澄空
    elif i.find("team_id%3A58\"") != -1:
        for a in rssaddress:
            if a.find("team_id%3A58\"") != -1:
                pos = a.find( "\">" )
                content = a[:pos] + "+720+MP4&sort_id=2" + a[pos:]
                target.write(i[:commatwo+1] + content + '<br>')
                rsstest = re.findall('http://[^"]*',content)
#                if urllib.urlopen(rsstest[0]).read().find("<item>") == -1:
#                    target.write("This rss address is wrong. Please check it manually.<br>")
                target.write('\n')
    #異域
    elif i.find("team_id%3A271\"") != -1:
        for a in rssaddress:
            if a.find("team_id%3A271\"") != -1:
                pos = a.find( "\">" )
                content = a[:pos] + "+%E7%AE%80%E4%BD%93+720&sort_id=2" + a[pos:]
                target.write(i[:commatwo+1] + content + '<br>')
                rsstest = re.findall('http://[^"]*',content)
#                if urllib.urlopen(rsstest[0]).read().find("<item>") == -1:
#                    target.write("This rss address is wrong. Please check it manually.<br>")
                target.write('\n')
    else:
        target2.write(i + '<br>')
        target2.write('\n')
