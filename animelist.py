#-*-coding:utf-8 -*-
import re
import yaml
import requests

blacklists = ['櫻桃小丸子','海賊王(航海王)','寶石寵物','光之美少女','龍珠',
              '美妙旋律Pripara','火影忍者','妖怪手錶','蠟筆小新','寵物小精靈',
              '名偵探柯南','美少女戰士Crystal','遊戲王','偶像傳說','Doraemon',
              'FAIRY TAIL']
#blacklists主要是一些长篇作品，不包含它们以减少筛选工作量
chosenteams = ['321','58','185','49','283','430','90','498','241','303','271','532']
#ID对应'輕之國度','澄空','極影','華盟','千夏','幻之','恶魔岛','KNA','幻樱','动漫国','異域','傲娇零'
#此列表的顺序代表优先选择的字幕组顺序
teamsettings = {'321':"+GB+720+MP4&sort_id=2",#輕之國度
                '58':"+720+MP4&sort_id=2",#澄空
                '185':"+GB+720+MP4&sort_id=2",#極影
                '49':"+%E7%AE%80+720+MP4&sort_id=2",#華盟
                '283':"+%E7%B9%81+720+MP4&sort_id=2",#千夏
                '271':"+%E7%AE%80+720&sort_id=2",#異域
                '532':"+GB+720+MP4&sort_id=2",#傲娇零
                '498':"+%E7%B9%81+720+MP4&sort_id=2",#KNA
                '430':"+GB+720+MP4&sort_id=2",#幻之
                '90':"+GB+720+MP4&sort_id=2",#恶魔岛
                '303':"+%E7%AE%80+720&sort_id=2",#动漫国
                '241':"+GB+720+MP4&sort_id=2"#幻樱
                }

def parsepage(url):
    user_agent = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
                  ' (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36')
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

def add_teamsettings(addr):
        for i in teamsettings:
            if addr.find("team_id%3A" + i) != -1:
                addr += teamsettings[i]
                break
        return addr

page = parsepage("https://share.dmhy.org/cms/page/name/programme.html")
page = page[page.find('//其它'):page.find('IE新窗')]
items = re.findall(".{3}array\.push.*?(?=;)",page)

dict_all = {}
dict_remain ={}
dict_select ={}

#第一个循环用于得到dict_all
for i in items:
    #此部分用于黑名单
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
        rssaddr = "https://share.dmhy.org/topics/rss/rss.xml" + url[12:url.find(">")-1]
        rssaddr = add_teamsettings(rssaddr)
        dict_item[team] = rssaddr
    dict_all.update({weekday + ',' + title:{'team':None,'rss':dict_item}})

#第二个循环用于从dict_all得到dict_select和dict_remain
for weekday_title in dict_all:
    dict_item = {}
    for team in dict_all[weekday_title]['rss']:
        if re.search("(?<=team_id%3A)\d+",dict_all[weekday_title]['rss'][team]).group() in chosenteams:
            dict_item.update({team:dict_all[weekday_title]['rss'][team]})
    if dict_item != {}:
        flag = 0
        for chosenteam in chosenteams:
            for team in dict_item:
                if re.search("(?<=team_id%3A)\d+",dict_item[team]).group() == chosenteam:
                    flag = 1
                    favoriteTeam = team
                    break
            if flag == 1:
                break
        dict_select.update({weekday_title:{'team':favoriteTeam,'rss':dict_item}})
    else:
        dict_remain[weekday_title] = dict_all[weekday_title]

yaml.safe_dump(dict_all,file("all.yml","w"),default_flow_style=False,allow_unicode=True)
yaml.safe_dump(dict_select,file("select.yml","w"),default_flow_style=False,allow_unicode=True)
yaml.safe_dump(dict_remain,file("remain.yml","w"),default_flow_style=False,allow_unicode=True)
