import yt_dlp

try:
    type_choice = input('Vid Or PlayList? Answer by: v/p |: ').strip().lower()

    if type_choice == 'v':
        url = input("Please Enter The Video Url: ").strip()
        yt_dlp.YoutubeDL({'format': 'bestvideo+bestaudio/best'}).download([url])
    
    elif type_choice == 'p':
        purl = input("Please Enter The PlayList Url: ").strip()
        options = {
            'format': 'bestvideo+bestaudio/best',
            'noplaylist': False,
            'outtmpl': '%(playlist_index)s - %(title)s.%(ext)s'
        }
        
        yt_dlp.YoutubeDL(options).download([purl])
        print("✅ Playlist downloaded successfully!")
    
    else:
        print("❌ Invalid choice! Please enter 'v' for video or 'p' for playlist.")

except Exception as e:
    print(f"❌ Error: {e}")
