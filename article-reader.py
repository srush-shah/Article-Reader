#Libraries: pyttsx3, requests
#Concepts: Web Scraping, Text-to-Speech

import pyttsx3, requests
from bs4 import BeautifulSoup

engine =  pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

text = str(input('Provide Article URL: '))
res = requests.get(text)
soup = BeautifulSoup(res.text, 'html.parser')

articles = []

for i in range(len(soup.select('.p'))):
    article = soup.select('.p')[i].getText().strip()
    articles.append(article)

text = ' '.join(articles)

speak(text)

engine.save_to_file(text, 'test.mp3')
engine.runAndWait()