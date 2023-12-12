import requests
from bs4 import BeautifulSoup
import re

from src.document import Document

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
        
    def scrapeWebpage(self, urls : list) -> None:
        """
        Extracts text data from webpage(s) at a given url and saves their text data as a string into the `Webscraper.corpus` hashmap

        Args:
            self (object): `WebScraper` object
            urls (str | list): one or multiple urls for the webpages you want to scrape
        """
        
        urls = list(set(urls))
     
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
                
if __name__ == '__main__':

    # sample usage

    # create WebScraper object
    scraper = WebScraper()

    # scrape webpages at the desired urls 
    docs = scraper.scrapeWebpage([
        
        # software engineering
        "https://www.forbes.com/advisor/education/become-software-engineer/",
        "https://www.mtu.edu/cs/undergraduate/software/what/",
        "https://www.cnbc.com/2019/06/14/how-much-google-facebook-other-tech-giants-pay-software-engineers.html",
        
        # basketball
        "https://www.britannica.com/list/the-10-greatest-basketball-players-of-all-time",
        "https://www.breakthroughbasketball.com/basics/basics.html",
        
        # computer science
        "https://joinhandshake.com/blog/students/top-10-jobs-for-computer-science-majors/",
        "https://www.zdnet.com/education/computers-tech/best-careers-with-computer-science-degree/",
        "https://undergrad.cs.umd.edu/what-computer-science"

    ])
    
    docs = scraper.scrapeWebpage([
        "https://www.forbes.com/advisor/education/become-software-engineer/",
        "https://www.cnbc.com/2019/06/14/how-much-google-facebook-other-tech-giants-pay-software-engineers.html"
    ])
    
    for doc in docs:
        print(doc)

    # save the results
    # scraper.saveCorpus()
    


