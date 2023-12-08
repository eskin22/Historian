from webscraper import WebScraper
from clustering import HierarchicalClustering

scraper = WebScraper()

PARAM = 0
# PARAM = 1

if PARAM == 0:
    
    print("TEST CASE")

    urls = [
        
        "https://www.cntraveler.com/gallery/best-cities-us",
        "https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population",
        "https://en.wikipedia.org/wiki/Basketball",
        "https://www.complex.com/sports/a/adam-caparell/best-nba-players-of-all-time-ranked",
        "https://www.stxnext.com/python-vs-other-programming-languages/",
        "https://www.cntraveler.com/gallery/best-cities-us",
        "https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population",
        "https://en.wikipedia.org/wiki/Basketball",
        "https://www.complex.com/sports/a/adam-caparell/best-nba-players-of-all-time-ranked",
        "https://www.google.com/search?q=best+basketball+players+of+all+time&rlz=1C1VDKB_enUS1062US1062&oq=best+basketball+players+of+all+time&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCDczNTJqMGo0qAIAsAIA&sourceid=chrome&ie=UTF-8",
        "https://www.stxnext.com/python-vs-other-programming-languages/",
        # "https://www.google.com/search?q=how+is+python+different+from+other+languages"
        
    ]

elif PARAM == 1:
    
    print("WORKING CASE")

    urls = [
        
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

    ]

print(f"# of URLS: {len(urls)}")

# urls = list(set(urls))

print(f"# of URLS after prune: {len(urls)}")

docs = scraper.scrapeWebpage(urls)

# docs = list(set(docs))

hc = HierarchicalClustering()

processed_docs = hc.preprocess_docs(docs)
tfidf_matrix = hc.extract_features(processed_docs)

cluster = hc.create_hierarchical_cluster(tfidf_matrix)

dendro = hc.create_dendrogram(cluster, docs)