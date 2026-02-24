import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import urllib.parse


class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.listen_on_mic()

    def listen_on_mic(self):
        with sr.Microphone() as source:
            print("Adjusting for background noise...")
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening...")

            while True:
                try:
                    audio = self.recognizer.listen(source)
                    command = self.recognizer.recognize_google(audio).lower()
                    print("You said:", command)

                    if "search" in command:
                        query = command.replace("search", "").strip()
                        self.search_google(query)
                    if "stop" in command:
                        print("Stopping the script")
                        break

                except sr.UnknownValueError:
                    print("Could not understand audio")

                except sr.RequestError as e:
                    print(f"Recognition error: {e}")

                except Exception as e:
                    print(f"Error: {e}")

    def search_google(self, query):
        if not query:
            print("No search query detected.")
            return

        encoded_query = urllib.parse.quote(query)

        options = Options()
        options.add_argument("--start-maximized")

        driver = webdriver.Chrome(options=options)
        driver.get(f"https://www.google.com/search?q={encoded_query}")

        input("Press Enter to close browser...")
        driver.quit()


if __name__ == "__main__":
    VoiceAssistant()