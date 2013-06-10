from bs4 import BeautifulSoup
import urllib2,urllib,sys
import os.path

def FlushText(text):
    sys.stdout.write(text)
    sys.stdout.flush()

def AddUrlList(mainList):
    num = 0
    urlList = []
    for main in mainList :
        html = urllib2.urlopen(main)
        soup = BeautifulSoup(html)
        print 'Load URL'
        urlList.append(main)
        while True:
            try:
                FlushText('\r\t'+urlList[num])
                html = urllib2.urlopen(urlList[num])
                soup = BeautifulSoup(html)
                urlList.append(soup.find('a' , {'class','mdMTMEnd01Pagination01Next'})['href'])
                num = num + 1
            except :
                print '\nend'
                break
    return urlList

def AddImgList(urlList):
    imageList = []
    print 'Load Image'
    for url in urlList:
        FlushText('\r\t'+url)
        html = urllib2.urlopen(url)
        soup = BeautifulSoup(html)
        elements = soup.findAll('img')
        for e in elements:
            if ('jpg' in e['src']):
                imageList.append(e['src'])
    print '\nend'
    return imageList

def SaveImgList(imageList):
    print 'Get Image'
    home = os.environ['HOME']

    output_dir = os.path.join(home, 'Pictures', 'Photo')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for image in imageList:
        FlushText('\r\t'+image)
            
        savefile = os.path.join(output_dir,os.path.basename(image))
        try:
            urllib.urlretrieve( image, savefile )
        except:
            print 'no image...'
            continue
    print '\noutput %s' % output_dir

def main():
    mainList = []
    mainList.append('http://matome.naver.jp/odai/2136232246408838201/2136232643009992503')
    #mainList.append('http://matome.naver.jp/odai/2136231874807871301/2136232181708614003')
    #mainList.append('http://matome.naver.jp/odai/2136231160605704601/2136231534806954603')
    #mainList.append('http://matome.naver.jp/odai/2134115119051056901/2134977195636793803')
    #mainList.append('http://matome.naver.jp/odai/2134134096564928801/2134976595736003003')
    #mainList.append('http://matome.naver.jp/odai/2134155293378664301/2134980511641314303')
    
    urlList = AddUrlList(mainList)
    imageList = AddImgList(urlList)
    SaveImgList(imageList)


if __name__ == '__main__':
    main()

