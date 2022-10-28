from re import S
from bs4 import BeautifulSoup
import requests as re

base_link = 'https://genius.com/'
artist = 'the-beatles-'
song_title = 'hey-jude-'
page = base_link + artist + song_title + 'lyrics'
print(page)
source = re.get(page).text

#soup object 
soup = BeautifulSoup(source, 'lxml')

#get the Genre class 
tag_div = soup.find('div', class_='SongTags__Container-xixwg3-1 bZsZHM')

#get the first genre from genre class
tag_name = tag_div.a.text

print("Genre: ", tag_name)

#prints 
# https://genius.com/song_name
# Genre: Rock

