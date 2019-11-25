import sys, random, urllib, webbrowser

# create empty list
urls = list()

# add urls to list
for line in sys.stdin:
    urls.append(line)

# shuffle elements in list
random.shuffle(urls)

# copy first five elements from shuffled list
shortList = urls[0:5]

# open each link in a new tab
for link in shortList:
    link = link.replace("\n", "")
    webbrowser.open_new_tab(link)
