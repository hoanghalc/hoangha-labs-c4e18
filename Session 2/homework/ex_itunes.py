from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

# song_dl = {
#     'default_search': 'ytsearch',
#     'max_downloads': 1
# }
# dl = YoutubeDL(song_dl)


url = 'https://www.apple.com/itunes/charts/songs/'
#1. Download webpage
song_content = urlopen(url).read().decode("utf-8")
#2. Extract ROI
soup = BeautifulSoup(song_content,'html.parser')
sec = soup.find('section','section chart-grid')

#3. Extract song list
song_list = []
li_list = sec.find_all('li')
for li in li_list:
    h3 = li.h3
    h4 = li.h4
    songs = {}
    songs['Name of Song'] = h3.string
    songs['Artist'] = h4.string
    song_list.append(songs)

    # download = []
    # download = h3.string + ' ' + h4.string
    # dl.download([download])
    

pyexcel.save_as(records = song_list, dest_file_name = 'itunes_top100_song.xlsx')
