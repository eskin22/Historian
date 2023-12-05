import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import webbrowser
import os

from document import Document
from clustering import HierarchicalClustering

def associate_urls(docs):
    mapping = {
        'Basketball Basics - The Rules, Concepts, Definitions, and Player Positions.txt' : 
            "https://www.breakthroughbasketball.com/basics/basics.html",
        'Everything You Should Know About How To Become A Software Engineer – Forbes Advisor.txt' :
            "https://www.forbes.com/advisor/education/become-software-engineer/",
        'How much Google, Facebook, other tech giants pay software engineers.txt' :
            "https://www.cnbc.com/2019/06/14/how-much-google-facebook-other-tech-giants-pay-software-engineers.html",
        'The 10 Greatest Basketball Players of All Time - Britannica.txt' : 
            "https://www.britannica.com/list/the-10-greatest-basketball-players-of-all-time",
        'The best computer science careers in 2022 - ZDNET.txt' : 
            "https://www.zdnet.com/education/computers-tech/best-careers-with-computer-science-degree/",
        'Top 10 jobs for Computer Science majors - Handshake.txt' : 
            "https://joinhandshake.com/blog/students/top-10-jobs-for-computer-science-majors/",
        'What is Computer Science - Undergraduate Computer Science at UMD.txt' : 
            "https://undergrad.cs.umd.edu/what-computer-science",
        'What is Software Engineering - Michigan Technological University.txt' : 
            "https://www.mtu.edu/cs/undergraduate/software/what/"
    }
    
    for doc in docs:
        doc.url = mapping.get(doc.title)
    
    return docs

# load in sample documents as Document objects
docs = [Document(file, test=True) for file in os.listdir('sample_data')]
docs = associate_urls(docs)

# create a HierarchicalClusting object to cluster documents
hc = HierarchicalClustering()

# preprocess the documents and create TF-IDF matrix
processed_docs = hc.preprocess_docs(docs)
tfidf_matrix = hc.extract_features(processed_docs)

# create hierarchical cluster of documents
cluster = hc.create_hierarchical_cluster(tfidf_matrix)

# create and visualize hierarchical cluster with dendrogram
dendro = hc.create_dendrogram(cluster, docs)
# dendro.show()

# Initialize the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(
        id='plotly-graph',
        figure=dendro
    )
])

@app.callback(
    Output('plotly-graph', 'figure'),
    [Input('plotly-graph', 'clickData')]
)
def display_click_data(clickData):
    if clickData:
        point_url = clickData['points'][0]['customdata']
        webbrowser.open_new_tab(point_url)
    return dendro

if __name__ == '__main__':
    app.run_server(debug=False)
