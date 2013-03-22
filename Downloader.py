from bs4 import BeautifulSoup
import urllib2,urllib,sys
import os.path

mainList = []
urlList = []
imageList = []
num = 0

mainList.append('http://matome.naver.jp/odai/2136232246408838201/2136232643009992503')
mainList.append('http://matome.naver.jp/odai/2136231874807871301/2136232181708614003')
mainList.append('http://matome.naver.jp/odai/2136231160605704601/2136231534806954603')
mainList.append('http://matome.naver.jp/odai/2134115119051056901/2134977195636793803')
mainList.append('http://matome.naver.jp/odai/2134134096564928801/2134976595736003003')
mainList.append('http://matome.naver.jp/odai/2134155293378664301/2134980511641314303')

for main in mainList :
    html = urllib2.urlopen(main)
    soup = BeautifulSoup(html)
    while True:
        try:
#            print soup.find ('a' , {'class','mdEndView01Pagination01Next'})['href']
            urlList.append(soup.find('a' , {'class','mdEndView01Pagination01Next'})['href'])
            html = urllib2.urlopen(urlList[num])
            soup = BeautifulSoup(html)
            num = num + 1
        except :
            break

for url in urlList:
    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html)
    elements = soup.findAll('img')
    for e in elements:
        if ('jpg' in e['src']):
            imageList.append(e['src'])
     
for image in imageList:
    print 'get:%s' % (image)
    output_dir = os.path.join(os.path.dirname(__file__), 'Photos')
    savefile = os.path.join(output_dir,os.path.basename(image))
    urllib.urlretrieve( image, savefile )


