# Animelist
Automatically generate a list of your favorite animation for [Flexget](http://flexget.com/) from [share.dmhy.org](http://share.dmhy.org)  
The default downloader is [xunlei-lixian](https://github.com/iambus/xunlei-lixian)
# Usage
1. First, run animelist.py to download the animation list from [share.dmhy.org](http://share.dmhy.org) and the animation list will be divided into two html files. The list in animeselect1.html is selected from some well-known groups (you can edit it if you don't like them). The list in animeselect2.html remains unchanged and needs to be selected manually.
2. Second, select your favourite animations and combine them into a new file named animeselect.html(the format should be as same as animeselect1.html). Then run animeselect2config.py
3. In addition, failure will be very frequent if you use the default downloader [xunlei-lixian](https://github.com/iambus/xunlei-lixian) due to the restrictions of Xunlei. Therefore, you can use failcheck.py to check if there are something wrong when flexget execution is over. This python script is only for [xunlei-lixian](https://github.com/iambus/xunlei-lixian). There is no point in taking it in consideration if your give up the default downloader.
