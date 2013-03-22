from bs4 import BeautifulSoup
import urllib2,urllib,sys
import os.path

def AddUrlList(mainList):
    num = 0
    urlList = []
    for main in mainList :
        html = urllib2.urlopen(main)
        soup = BeautifulSoup(html)
        print 'Load URL'
        while True:
            try:
                urlList.append(soup.find('a' , {'class','mdEndView01Pagination01Next'})['href'])
                html = urllib2.urlopen(urlList[num])
                soup = BeautifulSoup(html)
                num = num + 1
            except :
                break
    return urlList

def AddImgList(urlList):
    imageList = []
    print 'Load Image'
    for url in urlList:
        html = urllib2.urlopen(url)
        soup = BeautifulSoup(html)
        elements = soup.findAll('img')
        for e in elements:
            if ('jpg' in e['src']):
                imageList.append(e['src'])
    return imageList

def SaveImgList(imageList):
    
    for image in imageList:
        print 'get:%s' % (image)
        home = os.environ['HOME']
        output_dir = os.path.join(home, 'Pictures')
        output_dir = os.path.join(output_dir, 'Photos')
        try:
            savefile = os.path.join(output_dir,os.path.basename(image))
            urllib.urlretrieve( image, savefile )
        except:
            os.mkdir(output_dir)
            savefile = os.path.join(output_dir,os.path.basename(image))
            urllib.urlretrieve( image, savefile )
    print 'output %s' % output_dir

mainList = []
mainList.append('http://matome.naver.jp/odai/2136232246408838201/2136232643009992503')
#mainList.append('http://matome.naver.jp/odai/2136231874807871301/2136232181708614003')
#mainList.append('http://matome.naver.jp/odai/2136231160605704601/2136231534806954603')
#mainList.append('http://matome.naver.jp/odai/2134115119051056901/2134977195636793803')
#mainList.append('http://matome.naver.jp/odai/2134134096564928801/2134976595736003003')
#mainList.append('http://matome.naver.jp/odai/2134155293378664301/2134980511641314303')

SaveImgList(AddImgList(AddUrlList(mainList)))