import sys, urllib

# track the page
pageNum = 0
PAGE_MAX = 312
SONG_MAX = 12
BASE = 'https://www.bandmusicpdf.org/all?p='
count = 0
expression = 'product-name notranslate'


for i in range(PAGE_MAX):
    
    # generate url for each page
    url = BASE + str(i + 1)
    
    # read in web content
    response = urllib.urlopen(url)
    webContent = response.read()
    
    # split each line into a row by '\n' character
    rows = webContent.split('\n')

    count = 0

    # look for expression
    for row in rows:
        if count < PAGE_MAX:
            if expression in str(row):
                row = row.strip()
                tokens = row.split('https://')
                tokens = tokens[1].split('\"')
                tokens[0].replace('\n', "")
                print('https://' + tokens[0])
                count += 1
        else: # stop when 12 have been found
            break
            