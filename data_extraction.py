# data_extraction.py

import requests
from bs4 import BeautifulSoup
import os

def extract_article_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract article title
    title_element = soup.find("h1")
    article_title = title_element.get_text().strip() if title_element else "No title found"
    
    # Extract article text
    text_elements = soup.find_all("p")
    if text_elements:
        article_text = " ".join(paragraph.get_text().strip() for paragraph in text_elements)
    else:
        article_text = "No text found"
    
    return article_title, article_text

def save_article_to_file(url_id, article_title, article_text):
    # Create a folder to save articles if it doesn't exist
    if not os.path.exists("articles"):
        os.makedirs("articles")

    # Save the article to a text file with URL_ID as its name
    file_path = os.path.join("articles", f"{url_id}.txt")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(article_title + "\n\n")
        file.write(article_text)
