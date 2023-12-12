import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from scipy.cluster.hierarchy import linkage
import string
import plotly.graph_objs as go


from src.dendrogram import Dendrogram

class HierarchicalClustering():
    """
    A class to implement hierarchical clustering for documents
    """
    
    def __init__(self) -> None:
        """
        Initializes a `HierarchicalClustering` object
        """
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.vectorizer = TfidfVectorizer()
    
    def preprocess(self, text : str) -> str:
        """
        Preprocesses text data from a document by performing normalization, tokenization, and lemmatization

        Args:
            text (str): the text data from a document

        Returns:
            str: processed text data
        """
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokens = nltk.word_tokenize(text)
        filtered_tokens = [self.lemmatizer.lemmatize(token) for token in tokens if token not in self.stop_words]
        
        return ' '.join(filtered_tokens)
    
    def preprocess_docs(self, docs : list) -> list:
        """
        Preprocesses text for a collection of documents by performing normalization, tokenization, and lemmatization

        Args:
            docs (list): A list of the documents you want to process

        Returns:
            list: A list of processed documents
        """
        processed_docs = [self.preprocess(doc.text) for doc in docs]
        
        return processed_docs
    
    def extract_features(self, docs : list) -> np.ndarray:
        """
        Implements Term Frequency (TF) - Inverse Document Frequency (IDF) weighting to a set of (processed) documents
        
        NOTE: This method assumes the text of your documents has already been preprocessed (normalized, tokenized, lemmatized)

        Args:
            docs (list): A list of the processed documents you want to analyze

        Returns:
            np.ndarray: A TF-IDF matrix
        """
        tfidf_matrix = self.vectorizer.fit_transform(docs)
        tfidf_matrix = tfidf_matrix.toarray()
        
        return tfidf_matrix
    
    def create_hierarchical_cluster(self, tfidf_matrix : np.ndarray):
        """
        Performs hierarchical/agglomerative clustering for a TF-IDF weighted matrix of text data from a collection of documents using Average-Link

        Args:
            tfidf_matrix (np.ndarray): A TF-IDF matrix

        Returns:
            Any: A hierarchical/agglomerative cluster of the data
        """
        cluster = linkage(tfidf_matrix, method='average')
        return cluster
    
    def create_dendrogram(self, cluster, docs : list) -> go.Figure:
        """
        Creates a dendrogram to visualize a hierarchical/agglomerative cluster

        Args:
            cluster (_type_): The hierarchical cluster of the data
            docs (list): The list of documents

        Returns:
            go.Figure: A dendrogram figure
        """
        # webpage_names = [doc.title for doc in docs]
        print(f"Cluster Shape: {cluster.shape}\nLabels Length: {len(docs)}")
        dendrogram = Dendrogram(cluster, docs).create()
        return dendrogram