from pytube import YouTube

video_list = ["https://www.youtube.com/watch?v=73C7s1_DwU0&list=RD73C7s1_DwU0&start_radio=1,"]

for i in video_list:
  try:
    yt = YouTube(i)
    print(' Link: ' + i)
    print(' video/sound: ' + yt.streams[0].title)
  except:
    print("Error")

  
  stream = yt.streams.filter(only_video=True).get_highest_resolution() #.get_by_resolution #.get_audio_only #.get_lowest_resolution
  stream.download("py/Downloads/")
print('Downloaded')