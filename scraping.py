import requests
from bs4 import BeautifulSoup
import json

def getLanguageCode(language):
  req = requests.get("https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes")
  content = req.text
  bs = BeautifulSoup(content, "lxml")
  table = bs.findAll("table", class_="wikitable")[1]
  activeData = table.findAll('td', class_="active")
  object = [{ "language": item['title'], "code":item.get_text(strip=True)} for item in activeData if len(item.get_text(strip=True)) == 2 and item.get('title').lower() == language.lower()]
  return object[0]['code']
  
def getLanguageCodes():
  req = requests.get("https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes")
  content = req.text
  bs = BeautifulSoup(content, "lxml")
  table = bs.findAll("table", class_="wikitable")[1]
  activeData = table.findAll('td', class_="active")
  objects = [{ "language": item['title'], "code":item.get_text(strip=True)} for item in activeData if len(item.get_text(strip=True)) == 2 and item.get('title')]
  return json.dumps(objects)

def getLanguageFromCode(code):
  req = requests.get("https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes")
  content = req.text
  bs = BeautifulSoup(content, "lxml")
  table = bs.findAll("table", class_="wikitable")[1]
  activeData = table.findAll('td', class_="active")
  object = [{ "language": item['title'], "code":item.get_text(strip=True)} for item in activeData if len(item.get_text(strip=True)) == 2 and item.get_text(strip=True).lower() == code.lower()]
  return object[0]['language']