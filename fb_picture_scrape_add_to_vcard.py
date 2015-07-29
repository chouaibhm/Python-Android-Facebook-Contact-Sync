#!/usr/bin/env python2
__author__ = 'f41c0r'
__license__ = "GPL"
__version__ = "1.0"

from bs4 import BeautifulSoup
from PIL import Image
import codecs,sys,urllib,vobject,os,base64,io,PIL

versionNumber = 1.0

def usage():
    print >> sys.stderr, "Usage:  %s [OPTIONS]" % (sys.argv[0])
    print >> sys.stderr, """
OPTIONS may be some of:
    -v    --version            Output version of the password generator program

    -h    --help               Output this message

This script expects a file called in.vcf with your contacts, and a file index.html with the html from your facebook friend's page.
""" % {'command': sys.argv[0]}

def version():
    print "Python Password Generator Version: " + str(versionNumber)

def getImageResize9090Base64(link):
    rawPicFromInternet100100 = urllib.urlopen(link).read()
    rawPicFromInternet100100Bytes = io.BytesIO(rawPicFromInternet100100)
    imageObject = Image.open(rawPicFromInternet100100Bytes)

    imageBuffer = io.BytesIO()
    pic9090 = imageObject.resize((90, 90), PIL.Image.ANTIALIAS)
    pic9090.save(imageBuffer,format="JPEG")

    enc = base64.b64encode(imageBuffer.getvalue())
    return enc

def main(argv):
    UTF8Writer = codecs.getwriter('utf8')
    sys.stdout = UTF8Writer(sys.stdout)

    soup = BeautifulSoup(open('index.html','r'))
    imgList = soup.find_all(class_="_s0 _rv img")
    namesList = soup.find_all(class_="fsl fwb fcb")

    if len(imgList) != len(namesList):
        print "You have friends who deleted their facebook profile. Go unfriend them, and re-generate your index.html for this script to work."
        return

    name2PicLinkDict = {}
    for i in xrange(0,len(imgList)):
        name2PicLinkDict[namesList[i].find_all('a')[0].contents[0].lower()] = imgList[i].get('src')

    f = open("in.vcf","rb")
    contents = f.read()
    contents = contents.decode('utf-8')
    f.close()

    outvcf = []

    components = vobject.readComponents(contents, validate=True)
    for component in components:
        for child in component.getChildren():
            if child.name == "FN":
                if child.value.lower() in name2PicLinkDict:
                    component.add('photo')
                    component.photo.encoding_param = 'BASE64'
                    print child.value.lower()
                    component.photo.value = getImageResize9090Base64(name2PicLinkDict.pop(child.value.lower()))
        outvcf.append(component)

    f = open("out.vcf", 'wb')
    for vcard in outvcf:
        f.write(vcard.serialize())
    f.close()
 

if __name__ == "__main__":
       sys.exit(main(sys.argv)) 
