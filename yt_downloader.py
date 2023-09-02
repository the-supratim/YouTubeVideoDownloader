from pytube import YouTube

link = input("Enter link of YouTube Video: ")
yt = YouTube(link)

print("\nTitle: ",yt.title)

print("Views: ",yt.views)

yd = yt.streams.get_highest_resolution()

yd.download("D:\YouTube Downloader")

print("\nYour file has been downloaded successfully.")
print("Thank you for using this software.\n© Supratim Bhattacharjee")
