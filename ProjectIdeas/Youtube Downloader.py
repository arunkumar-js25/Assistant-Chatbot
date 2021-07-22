from pytube import YouTube, Playlist
#other modules to download youtube videos : pafy

source = input("Do you want to download Youtube Video (v) / audio (a) / Playlist (p) : ")
if(source in ['v','V']):
    youtube_video_url = input("Enter Youtube Video URL to download : ") #'https://www.youtube.com/watch?v=DkU9WFj8sYo'
    try:
        yt_obj = YouTube(youtube_video_url)

        DetailView = input("Do you want see the video details (y/n): ")
        print('')
        if(DetailView in ['y','Y','Yes','yes']):
            print(f'Video Title is {yt_obj.title}')
            print(f'Video Length is {yt_obj.length} seconds')
            print(f'Video Description is {yt_obj.description}')
            print(f'Video Rating is {yt_obj.rating}')
            print(f'Video Views Count is {yt_obj.views}')
            print(f'Video Author is {yt_obj.author}')
            print('')

            for stream in yt_obj.streams:
                print(stream)

        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
        '''
        The “progressive” stream contains the file having both audio and video.
        The “adaptive” stream contains either audio or video.
        The “mime_type”, “res”, and “fps” attributes can be used to filter the stream that we want to download.
        '''

        need = input("Do you want to save video with new name and new location(y/n): ")
        if(need in ['y','Y','Yes','yes']):
            path = input("     local destination path: ")
            name = input("     Video File Name: ")

            if(path in [None,''] and name in [None,'']):
                filters.get_lowest_resolution().download()
                print('Video Downloaded Successfully')
            elif(path not in [None,''] and name not in [None,'']):
                filters.get_lowest_resolution().download(output_path=path, filename=name+'.mp4')
                print('Video Downloaded Successfully')
        else:
            filters.get_lowest_resolution().download()
            print('Video Downloaded Successfully')

        #Download Video Command :  filters.get_highest_resolution().download()  /  filters.get_lowest_resolution(),download()
        #Download in specific Path & Name download(output_path='/Users/pankaj/temp', filename='yt_video.mp4')
        #In case Downloading Audio only,  yt_obj.streams.get_audio_only().download(output_path='/Users/pankaj/temp', filename='audio')

    except Exception as e:
        print(e)

elif(source in ['p','P']):
    try:
        playlist = Playlist(input('Enter Youtube Playlist URL to download : '))

        print("Do you want to save the playlist in new location : ")
        path = input("Enter the local destination path: ")
        if(path in ['',None]):
            playlist.download_all()
            print('Playlist Downloaded Successfully')
        else:
            playlist.download_all(download_path=path)
            print('Playlist Downloaded Successfully')

    except Exception as e:
        print(e)

elif(source in ['a','A']):
    try:
        yt_obj = YouTube(input("Enter Youtube Video URL to download audio only : "))

        print("Do you want to save Audio with name and location : ")
        path = input("    Local destination path: ")
        name = input("    Audio FileName: ")

        if(path in [None,''] and name in [None,'']):
            yt_obj.streams.get_audio_only().download()
            print('Audio Downloaded Successfully')
        elif(path not in [None,''] and name not in [None,'']):
            yt_obj.streams.get_audio_only().download(output_path=path, filename=name)
            print('Audio Downloaded Successfully')

    except Exception as e:
        print(e)


'''
## importing the module
import pafy
## url of the video
url = "https://www.youtube.com/watch?v=cr3-J5wDLsM"
## calling the new method of pafy
result = pafy.new(url)
## getting the best quality of video from the 'result' using the getbest()
best_quality_video = result.getbest()
best_quality_audio = result.getbestaudio()  ##To download audio file
## you can print it to see the quality of the video
print(best_quality_video)
## download it using the download()
best_quality_video.download()
'''