from pytube import YouTube

link = input("Enter a youtube video's URL: ") # i.e. https://youtu.be/dQw4w9WgXcQ

yt = YouTube(link)
yt.streams.first().download(output_path="/Users/dhruv/Downloads", filename="myvideo.mp4")

print("Downloaded", yt.title)


# from pytube import YouTube

# def Download(link):
#     youtubeObject = YouTube(link)
#     youtubeObject = youtubeObject.streams.get_highest_resolution()
#     try:
#         youtubeObject.download()
#     except:
#         print("An error has occurred")
#     print("Download is completed successfully")


# link = input("Enter the YouTube video URL: ")
# Download(link)


