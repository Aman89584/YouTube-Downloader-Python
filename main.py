from pytube import YouTube

def Videotubedownloader(link):
    YoutubeObject = YouTube(link)
    YoutubeObject = YoutubeObject.streams.get_highest_resolution()
    try:
        YoutubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
print("Downloading...")
Videotubedownloader(link)