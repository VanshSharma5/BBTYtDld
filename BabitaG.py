from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from yt_dlp import YoutubeDL
from os.path import join
from time import sleep
from sys import exit
import re


# Requirements
#    "selenium>=4.39.0",
#    "yt-dlp>=2025.12.8",


class BabitaG:
    pool = list(range(100))
    def __init__(self, *, driver="chrome", headless=True, waitTime=5, restTime=10):
        self.driver = self.get_driver(driver, headless)
        self.waitTime = waitTime
        self.restTime = restTime

    def get_driver(self, driver, headless):
        options = Options()
        options.add_argument("--headless=new") if headless else None
        match(driver):
            case "edge":
                return webdriver.Edge(options)
            case "firefox":
                return webdriver.Firefox(options)
            case _:
                return webdriver.Chrome(options)

    def get_song_by_name(self, query, download=True):
        url = "None"
        
        # hardcode
        self.driver.get(f"https://www.youtube.com/results?search_query={query}")
        
        # don't stress her let give some time
        sleep(self.waitTime)
        
        try:
            elements = self.driver.find_elements(By.ID, "video-title") 
            for element in elements:
                print(f"\rThis One => {element.text}", end=" ")
                temp = input("(Y/N)?").lower()
                if temp == "n":
                    return None
                if temp == "y":
                    url = element.get_property("href")
                    break
            
            temp_name = self.get_song(url) if download else None
            return url, temp_name
        except Exception as e:
            print("Error", e)
            return url
    
    def get_song(self, url, media="./media"):
        if len(BabitaG.pool) == 0:
            exit(1)
            return None
        if BabitaG.pool.pop()%2 == 0:
            print("I an exhausted")
            sleep(self.restTime)
            return None
        try:
            # g! snippet 
            if url != "None":
                ydl_opts = {
                    'format': 'bestaudio/best', # selects the best audio format
                    'outtmpl': join("downloads", "%(title)s.%(ext)s"), # Output filename template
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio', # Extracts the audio
                        'preferredcodec': 'mp3',      # Converts to MP3 format
                        # 'preferredquality': '192',    # Sets the audio quality to 192k
                    }],
                    'noplaylist': True, # Prevents downloading a whole playlist if a playlist URL is provided
                }
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

        except Exception as e:
            print(f"ERROR : {e}")        
            return None

# work on linux 
# problems : win32 API cause some errors
def main():
    print("Hello from babitag!")

    # wait time to give some time to load we content to scrap
    babitaG = BabitaG(waitTime=3)

    # print(babitaG.get_song_by_name("mukesh ambani"))
    # print(babitaG.get_song_by_name("mukesh ambani", download=True))
    babitaG.get_song("https://www.facebook.com/sadhguru/videos/what-a-truly-beautiful-face-looks-like/1335155401639937/")
    babitaG.get_song("https://www.facebook.com/sadhguru/videos/what-a-truly-beautiful-face-looks-like/1335155401639937/")

if __name__ == "__main__":
    main()