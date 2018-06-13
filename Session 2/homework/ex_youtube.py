from youtube_dl import YoutubeDL

#1. Download single video
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=aJOTlE1K90k'])

#2. Download multiple video, using list of url
dl.download(['https://www.youtube.com/watch?v=aJOTlE1K90k','https://www.youtube.com/watch?v=32sYGCOYJUM'])

#3. Download audio
audio_download = {'format': 'bestaudio/audio'}
dl = YoutubeDL(audio_download)
dl.download(['https://www.youtube.com/watch?v=aJOTlE1K90k'])

#4. Search & Download
option = {
    'default_search': 'ytsearch',
    'max_download' : 1,
    'format' : 'bestaudio/audio'
}
dl = YoutubeDL(option)
dl.download(['Chạy ngay đi'])

