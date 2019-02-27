import bs4 as bs
import urllib.request
import csv

#URl to scrape data from
source = urllib.request.urlopen('http://www.thebest100lists.com/best100actors/').read()

soup = bs.BeautifulSoup(source, 'lxml')

#creating an empty list to store the data.
myList = []

#finding and filtering the source code which containts the 'ol' tag
for paragraph in soup.find_all('ol'):
    contents = paragraph.text.split('\n\n')
    for name in contents:
        if name:
            myList.append(name.strip())

#writing the data to a .csv file
with open('myList.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    for i in myList:
        writer.writerow([i])
