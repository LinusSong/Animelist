#-*-coding:utf-8 -*-
import re
import yaml
import requests

def parsepage(url):
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36'
    headers = { 'User-Agent' : user_agent }
    page = requests.get(url, headers=headers).text.encode('utf8')
    return page

def conv_Weekday2Chinese(attr):
    if attr == "mon":
        weekday = '星期一'
    elif attr == "tue":
        weekday = '星期二'
    elif attr == "wed":
        weekday = '星期三'
    elif attr == "thu":
        weekday = '星期四'
    elif attr == "fri":
        weekday = '星期五'
    elif attr == "sat":
        weekday = '星期六'
    elif attr == "sun":
        weekday = '星期日'
    return weekday

def rssaddr_chosenteams(addr):
    if addr.find("team_id%3A321") != -1:
        addr = addr + "+GB+720+MP4&sort_id=2"
    elif addr.find("team_id%3A58") != -1:
        addr = addr + "+720+MP4&sort_id=2"
    elif addr.find("team_id%3A185") != -1:
        addr = addr + "+GB+720+MP4&sort_id=2"
    elif addr.find("team_id%3A49") != -1:
        addr = addr + "+%E7%AE%80+720+MP4&sort_id=2"
    elif addr.find("team_id%3A283") != -1:
        addr = addr + "+%E7%B9%81%E9%AB%94+720+MP4&sort_id=2"
    elif addr.find("team_id%3A271") != -1:
        addr = addr + "+%E7%AE%80%E4%BD%93+720&sort_id=2"
    return addr

page = parsepage("http://share.dmhy.org/cms/page/name/programme.html")
page = page[page.find('//其它'):page.find('IE新窗')]
items = re.findall(".{3}array\.push.*?(?=;)",page)

blacklists = ['櫻桃小丸子','海賊王(航海王)','寶石寵物','七龍珠改魔人普烏篇',
              '美妙旋律Pripara','火影忍者','妖怪手錶','蠟筆小新','寵物小精靈',
              '名偵探柯南','美少女戰士Crystal','遊戲王ARC-V','偶像傳說']
chosenteams = ['321','58','185','49','283','271']
#ID对应'輕之國度','澄空','極影','華盟','千夏','異域'

dict_all = {}
dict_firstselect = {}
dict_remain ={}
dict_select ={}
for i in items:
    flag_blacklist = 1
    for blackitem in blacklists:
        if i.find(blackitem) != -1:
            flag_blacklist = 0
    if flag_blacklist == 0:
        continue
    weekday = conv_Weekday2Chinese(i[0:3])
    title = re.findall("(?<=,').*?(?=',)",i)[0]
    urls = re.findall("(?<=a href=\").*?(?=</a>)",i)

    dict_item = {}
    for url in urls:
        team = url[url.find(">")+1:]
        rssaddr = "http://share.dmhy.org/topics/rss/rss.xml" + url[:url.find(">")-1]
        rssaddr = rssaddr_chosenteams(rssaddr)
        dict_item[team] = rssaddr
    dict_all[weekday + ',' + title] = dict_item

    flag_remain = 1
    flag_first = 0
    dict_item = {}
    for chosenteam in chosenteams:
        if i.find("team_id%3A"+chosenteam+"\"") != -1:
            for url in urls:
                if url.find("team_id%3A"+chosenteam+"\"") != -1:
                    team = url[url.find(">")+1:]
                    rssaddr = "http://share.dmhy.org/topics/rss/rss.xml" + url[:url.find(">")-1]
                    rssaddr = rssaddr_chosenteams(rssaddr)
                    dict_item[team] = rssaddr
            flag_first = flag_first + 1
            flag_remain = 0
            if flag_first == 1:
                dict_firstselect[weekday + ',' + title] = {team:rssaddr}
    if flag_remain == 0:
        dict_select[weekday + ',' + title] = dict_item
    if flag_remain == 1:
        dict_item = {}
        for url in urls:
            team = url[url.find(">")+1:]
            rssaddr = "http://share.dmhy.org/topics/rss/rss.xml" + url[:url.find(">")-1]
            dict_item[team] = rssaddr
        dict_remain[weekday + ',' + title] = dict_item

yaml.safe_dump({'tasks':dict_all},file("all.yml","w"),default_flow_style=False,allow_unicode=True)
yaml.safe_dump({'tasks':dict_select},file("select.yml","w"),default_flow_style=False,allow_unicode=True)
yaml.safe_dump({'tasks':dict_firstselect},file("firstselect.yml","w"),default_flow_style=False,allow_unicode=True)
yaml.safe_dump({'tasks':dict_remain},file("remain.yml","w"),default_flow_style=False,allow_unicode=True)
