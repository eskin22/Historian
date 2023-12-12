"""
Author:     Blake McBride (blakepm2@illinois.edu)
Created:    12/02/2023

Overview:   This file defines the `WebScraper` class which will be used to extract the text data some webpages at given URLS from the client
"""

# import standard modules
import requests
from bs4 import BeautifulSoup
import re
from alive_progress import alive_bar

# import src modules
from src.webScraping.document import Document

class WebScraper():
    """
    A class for extracting text data from webpages
    """
    
    def __init__(self) -> None:
        """
        Initializes a `WebScraper` object
        """
        self.corpus = []
        
    def getWebpageText(self, response : object) -> str:
        """
        Extracts and preprocesses the data from a webpage from a given `requests.Response` object

        Args:
            self (object): `WebScraper` object
            response (object): `requests.Response` object

        Returns:
            str: A clean string of the text data from the webpage
        """
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for script_or_style in soup(['script', 'style']):
            script_or_style.extract()
            
        text = soup.get_text()
        cleaned_text = re.sub(r'\s+', ' ', text)
        
        return cleaned_text
        
    def scrapeWebpages(self, urls : list) -> None:
        """
        Extracts text data from webpage(s) at a given url and saves their text data as a string into the `Webscraper.corpus` hashmap

        Args:
            self (object): `WebScraper` object
            urls (str | list): one or multiple urls for the webpages you want to scrape
        """
        
        urls = list(set(urls))

        with alive_bar(len(urls)) as bar:
            for url in urls:
        
                try: 
                    response = requests.get(url)
                    
                    soup = BeautifulSoup(response.content, 'html.parser')
                
                    title_tag = soup.find('title')
                    title = title_tag.text if title_tag else url
                    title = title.replace(':', '-').replace('|', '-').replace('?', '').replace('/', '-').replace('"', '').replace('*', '').replace('<', '').replace('>', '')
                    
                    text = self.getWebpageText(response)
                    
                    doc = Document(title, text, url)
                    
                    self.corpus.append(doc)
                    
                except Exception as e:
                    print(e); print(f"Error: Failed to scrape webpage at {url}\n\nPlease verify that this is a valid url.")
                
                bar()
        
        return self.corpus
                
    def saveCorpus(self, filepath='sample_data') -> None:
        """
        Saves the corpus of scraped webpages to .txt files
        
        Args:
            filepath (string): The destination to save the files (Default is `sample_data`)
        """
         
        for webpage_title, text in self.corpus.items():
            with open(f'{filepath}/{webpage_title}.txt', 'w', encoding='utf-8') as file:
                file.write(text)
    


