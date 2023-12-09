import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram
import string
import plotly.graph_objs as go
import os

from document import Document

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
    
class Dendrogram():
    """
    A class to create dendrogram visualizations of hierarchical/agglomerative clusters
    """
    def __init__(self, cluster, docs : list):
        """
        Initializes a `Dendrogram` object

        Args:
            cluster (_type_): The hierarchical cluster of the data
            docs (list): The list of documents
        """
        
        doc_titles = [doc.title for doc in docs]
        
        print(f"Labels: \n{doc_titles}")
        
        self.documents = {}
        for doc in docs:
            self.documents[doc.title] = doc
            
        print(f"Labels after conversion to hashmap: {self.documents.keys()}")
        
        for doc in doc_titles:
            if doc not in self.documents.keys():
                print(f"This is one bad apple: {doc}")
        
        print(f"# of Labels Right Before Dendrogram Creation: {len(self.documents.keys())}")
        
        # for key, val in self.documents.items():
        #     print(f'key: {key} val: {val}')
        
        dendro = dendrogram(cluster, labels=list(self.documents.keys()), no_plot=True)
        self.icoords, self.dcoords = dendro['icoord'], dendro['dcoord']
        self.color_list = dendro['color_list']
        self.names = dendro['ivl']
        
        self.lines = []
        self.midpoints = []
        self.name_pointer = 0
    
    def create(self) -> go.Figure:
        """
        Creates a dendrogram figure for a hierarchical/agglomerative cluster

        Returns:
            go.Figure: A dendrogram figure
        """
        
        self.create_lines()
        self.create_nodes()
        self.create_layout()
        
        fig = go.Figure(data=self.lines, layout=self.layout)
        return fig
        
    def create_lines(self):
        """
        Creates the lines representing the relationships between nodes in a dendrogram
        """
        for i, (x, y) in enumerate(zip(self.icoords, self.dcoords)):
            self.lines.append(go.Scatter(
                x = x,
                y = y,
                mode = 'lines',
                line = dict(
                    color = '#fecb52',
                    width = 4
                ),
                hoverinfo = 'none'
            ))
            
    def create_nodes(self):
        """
        Creates the nodes representing the documents in a dendrogram
        """
        for i, icoord in enumerate(self.icoords):
            x_coord_l = icoord[0]
            x_coord_r = icoord[2]
            x_coord_c = 0.5 * (icoord[0] + icoord[2])
            self.midpoints.append(x_coord_c)
            
            y_coord = 0
            
            if x_coord_l not in self.midpoints:
                self.lines.append(go.Scatter(
                    x = [x_coord_l], y = [y_coord],
                    mode = 'markers',
                    hoverinfo = 'text',
                    hovertext = self.names[self.name_pointer],
                    marker = dict(
                        size = 35,
                        color = '#636efa',
                    ),
                    hoverlabel = dict(
                        font = dict (
                            color = 'white',
                            size = 18
                        ),
                        bordercolor = 'white'
                    ),
                    customdata=[
                        self.documents.get(self.names[self.name_pointer]).url
                    ]
                ))
                self.name_pointer += 1

            if x_coord_r not in self.midpoints:
                self.lines.append(go.Scatter(
                    x = [x_coord_r], y = [y_coord],
                    mode = 'markers',
                    hoverinfo = 'text',
                    hovertext = self.names[self.name_pointer],
                    marker = dict(
                        size = 35,
                        color = '#636efa',
                    ),
                    hoverlabel = dict(
                        font = dict (
                            color = 'white',
                            size = 18
                        ),
                        bordercolor = 'white'
                    ),
                    customdata=[
                        self.documents.get(self.names[self.name_pointer]).url
                    ]
                ))
                self.name_pointer += 1
    
    def create_layout(self):
        """
        Creates the layout of the dendrogram
        """
        self.layout = go.Layout(
            title = dict(
                text = None
                # x = 0.5,
                # xanchor = 'center',
                # font = dict(
                #     family = 'Raleway',
                #     size = 40,
                #     color = 'white'
                # )
            ),
            # annotations = [
            #     dict(
            #         x = 0.5,
            #         y = 1.07,
            #         xref = 'paper',
            #         yref = 'paper',
            #         text = 'Hierarchical Clustering Dendrogram',
            #         showarrow = False,
            #         font = dict(
            #             family = 'Open Sans, sans-serif',
            #             size = 18,
            #             color = 'white'
            #         ),
            #         xanchor = 'center'
            #     )
            # ],
            xaxis = dict(
                showgrid = False,
                showticklabels = False
            ),
            yaxis = dict(
                showgrid = False,
                showticklabels = False,
                zeroline = False
            ),
            width = 1200, height = 600,
            font = dict(
                size = 16
            ),
            showlegend= False,
            paper_bgcolor='rgba(0, 0, 0, 0)',
            plot_bgcolor='rgba(0, 0, 0, 0)'
        )

if __name__ == '__main__':
    
    # sample usage
    
    # load in sample documents as Document objects
    docs = [Document(file, test=True) for file in os.listdir('sample_data')]
    print(docs)
    # create a HierarchicalClusting object to cluster documents
    hc = HierarchicalClustering()
    
    # preprocess the documents and create TF-IDF matrix
    processed_docs = hc.preprocess_docs(docs)
    tfidf_matrix = hc.extract_features(processed_docs)
    
    # create hierarchical cluster of documents
    cluster = hc.create_hierarchical_cluster(tfidf_matrix)
    
    # create and visualize hierarchical cluster with dendrogram
    dendro = hc.create_dendrogram(cluster, docs)
    dendro.show()
                