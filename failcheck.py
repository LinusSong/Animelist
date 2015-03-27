#-*-coding:utf-8 -*-
import linecache
resource = "/home/l/.flexget/flexget.log"
resource1 = "/home/l/.flexget/flexget.log.1"
target = open('faillist.txt','w')
resourcelen = len(open(resource).readlines())
resourcelen1 = len(open(resource1).readlines())
a = []
a1 = []
for i in range(0, resourcelen):
    linecontent = linecache.getline(resource,i+1)
    if linecontent.find('NotImplementedError') != -1:
        if i == 0:
            a.insert(0, linecache.getline(resource1,resourcelen1))
        else:
            a.insert(0, linecache.getline(resource,i))
for i in range(0, resourcelen1):
    linecontent1 = linecache.getline(resource1,i+1)
    if linecontent1.find('NotImplementedError') != -1:
        if i == 0:
            a1.insert(0, '请到上一个文件查找')
        else:
            a1.insert(0, linecache.getline(resource1,i))

for i in a:
    target.write(i)
for i in a1:
    target.write(i)
