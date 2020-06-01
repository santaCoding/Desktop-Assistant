import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen('https://habr.com/ru/post/210288/')
contents = html.read()


soup = BeautifulSoup(contents, 'lxml')
imgs = []
for img in soup.findAll('img'):
    imgs.append(str(img['src']))

for img in range(len(imgs)):
    if 'https:' not in imgs[img]:
        imgs[img] = 'https:' + imgs[img]
print(imgs)

for img in range(len(imgs)):
    image = urllib.request.urlopen(imgs[img]).read()
    out = open(f"img{img}.jpg", "wb")
    out.write(image)
    out.close()