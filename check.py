#-*-coding:utf-8 -*-
import yaml
import feedparser

config = yaml.load(open(os.path.join(workpath,'config.yml')).read())
for i in config['tasks']:
    if config['tasks'][i].values()[0]:
        print i,config['tasks'][i].keys()[0],config['tasks'][i].values()[0]
