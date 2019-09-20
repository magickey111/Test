import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') #打开url

counts = dict()
characters=0
for line in fhand:
    words = line.decode()       #字符转码
    characters = characters + len(words)  #累积字符长度
    if characters < 3000:       #完成条件3000以下
        print(line.decode().strip())

print(characters)