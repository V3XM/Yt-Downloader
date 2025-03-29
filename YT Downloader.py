import yt_dlp
try:
    type= input('PlayList Or Video? p/v|: ').strip().lower()
    if type == 'v':
        vid_url = input('Please Enter The URL: ').strip()
        vid_attr={
            'format':'bestvideo+bestaudio/best'
        }
        yt_dlp.YoutubeDL(vid_attr).download(vid_url)
    elif type == 'p':
        Play_url = input('Please Enter The URL: ').strip()
        Play_attr={
            'format':'bestvideo+bestaudio/best',
            'noplaylist':'false',
            'outtmpl': '%(playlist_index)s - %(title)s.%(ext)s'
        }
        yt_dlp.YoutubeDL(Play_attr).download(Play_url)
    else:
        print('Please Choose (video)-->"v" or (PlayList)-->"p')
except Exception as e:
    print(f'Error: {e}')
