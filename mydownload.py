import flickr
import urllib, urlparse
import os
import sys
    
tag_list = []
page_index = ['1', '2', '3', '4', '5', '6']

for tag in tag_list:
    for pi in page_index:
        # downloading image data
        f = flickr.photos_search(tags=tag, per_page='1', page=pi)
        print len(f)
        urllist = [] #store a list of what was downloaded
        # downloading images
        for k in f:
            try:
                url = k.getURL(size='Large', urlType='source')
            except:
                print 'error'
                continue
            urllist.append(url)
            image = urllib.URLopener()
            image.retrieve(url, os.path.basename(urlparse.urlparse(url).path))
            print 'downloading:', url