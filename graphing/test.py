from webscraper import WebScraper
from clustering import HierarchicalClustering

urls = [
        
    "https://www.google.com/search?q=top+10+cities+in+the+us&rlz=1C1VDKB_enUS1062US1062&oq=top+10+cities+in+the+us&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCTE3NjIyajBqNKgCALACAA&sourceid=chrome&ie=UTF-8#ip=1",
    "https://www.google.com/search?q=top+10+cities+in+the+us&rlz=1C1VDKB_enUS1062US1062&oq=top+10+cities+in+the+us&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCTE3NjIyajBqNKgCALACAA&sourceid=chrome&ie=UTF-8",
    "https://www.cntraveler.com/gallery/best-cities-us",
    "https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population",
    "https://en.wikipedia.org/wiki/Basketball",
    "https://www.google.com/search?q=what+is+basketball%3F&rlz=1C1VDKB_enUS1062US1062&oq=what+is+basketball%3F&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCDg2NjFqMGo0qAIAsAIA&sourceid=chrome&ie=UTF-8",
    "https://www.complex.com/sports/a/adam-caparell/best-nba-players-of-all-time-ranked",
    "https://www.google.com/search?q=best+basketball+players+of+all+time&rlz=1C1VDKB_enUS1062US1062&oq=best+basketball+players+of+all+time&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCDczNTJqMGo0qAIAsAIA&sourceid=chrome&ie=UTF-8",
    "https://www.stxnext.com/python-vs-other-programming-languages/",
    "https://www.google.com/search?q=how+is+python+different+from+other+languages%3F&rlz=1C1VDKB_enUS1062US1062&oq=how+is+python+different+from+other+languages%3F&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQABiABDIICAIQABgWGB4yCAgDEAAYFhgeMg0IBBAAGIYDGIAEGIoF0gEINTgzOWowajSoAgCwAgA&sourceid=chrome&ie=UTF-8",
    "https://www.google.com/search?q=top+10+cities+in+the+us&rlz=1C1VDKB_enUS1062US1062&oq=top+10+cities+in+the+us&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCTE3NjIyajBqNKgCALACAA&sourceid=chrome&ie=UTF-8#ip=1",
    "https://www.google.com/search?q=top+10+cities+in+the+us&rlz=1C1VDKB_enUS1062US1062&oq=top+10+cities+in+the+us&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCTE3NjIyajBqNKgCALACAA&sourceid=chrome&ie=UTF-8",
    "https://www.cntraveler.com/gallery/best-cities-us",
    "https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population",
    "https://en.wikipedia.org/wiki/Basketball",
    "https://www.google.com/search?q=what+is+basketball%3F&rlz=1C1VDKB_enUS1062US1062&oq=what+is+basketball%3F&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCDg2NjFqMGo0qAIAsAIA&sourceid=chrome&ie=UTF-8",
    "https://www.complex.com/sports/a/adam-caparell/best-nba-players-of-all-time-ranked",
    "https://www.google.com/search?q=best+basketball+players+of+all+time&rlz=1C1VDKB_enUS1062US1062&oq=best+basketball+players+of+all+time&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCDczNTJqMGo0qAIAsAIA&sourceid=chrome&ie=UTF-8",
    "https://www.stxnext.com/python-vs-other-programming-languages/",
    "https://www.google.com/search?q=how+is+python+different+from+other+languages"
]

urls = list(set(urls))

webscraper = WebScraper()

docs = webscraper.scrapeWebpage(urls)

hc = HierarchicalClustering()

processed_docs = hc.preprocess_docs(docs)
tfidf_matrix = hc.extract_features(processed_docs)

cluster = hc.create_hierarchical_cluster(tfidf_matrix)

dendro = hc.create_dendrogram(cluster, docs)