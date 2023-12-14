"""
Author(s):  Blake McBride (blakepm2@illinois.edu)
Created:    12/06/2023

Overview:   This file defines the backend server functionality for Historian
"""

# import standard modules
import dash
from dash import dcc 
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from flask import request
from flask_cors import CORS
from flask import jsonify
from flask_caching import Cache

# import src modules
from src.webScraping.webScraper import WebScraper
from src.graphing.hierarchicalClustering import HierarchicalClustering

# initialize the Historian app
app = dash.Dash("Historian")
server = app.server

# initialize cache to save dendrogram if fetch fails 
cache = Cache(app.server, config={
    'CACHE_TYPE' : 'filesystem',
    'CACHE_DIR' : 'cache-directory'
})

cache.init_app(server)

# configure CORS to allow requests from frontend
extension_id = "efgnmahmglilhimdpjgjedjieapjkjeh"
CORS(app.server, resources={r"/*": {"origins": f"chrome-extension://{extension_id}"}})

# setup initial app layout
app.layout = html.Div([
    dcc.Graph(id='graph'),
    html.Div(id="hidden-div", style={'display': 'none'})
])

# @app.callback(
#     Output('graph', 'figure'),
#     [Input('graph', 'clickData')]
# )
# def display_click_data(clickData):
#     if clickData:
#         point_url = clickData['points'][0]['customdata']
#         webbrowser.open_new_tab(point_url)
#     return dendro

# create server route for clients to send data to the backend 
@app.server.route('/receive_data', methods=['POST'])
def receive_data():
    
    # get the list of urls sent from the client and print them
    data = request.json    
    urls = data.get('urls', [])
    print("——————————————————————————————————————————————————————————————————————————————————————————————————————————————")
    print("RECEIVED URLS FROM CLIENT")
    print("——————————————————————————————————————————————————————————————————————————————————————————————————————————————")
    for url in urls:
        print("     ", url)
    print("——————————————————————————————————————————————————————————————————————————————————————————————————————————————\n")
    
    # scrape the text data at the webpages
    print("——————————————————————————————————————————————————————————————————————————————————————————————————————————————")
    print("EXTRACTING WEBPAGE TEXT")
    print("——————————————————————————————————————————————————————————————————————————————————————————————————————————————")
    
    webscraper = WebScraper()    
    docs = webscraper.scrapeWebpages(urls)
    
    print("\nDONE")
    print("——————————————————————————————————————————————————————————————————————————————————————————————————————————————\n")
    
    # preprocess the webpage documents and perform agglomerative hierarchical clustering
    # then visualize the results in a Dendrogram figure and display it for the user to see
    print("——————————————————————————————————————————————————————————————————————————————————————————————————————————————")
    print("PROCESSING WEBPAGE DATA")
    print("——————————————————————————————————————————————————————————————————————————————————————————————————————————————")
    
    hc = HierarchicalClustering()
    dendro = hc.main(docs)

    print("\nDONE")
    print("——————————————————————————————————————————————————————————————————————————————————————————————————————————————\n")
    
    # store the figure in cache in case fetch fails
    cache.set('dendrogram', dendro)
    
    # update the figure on the frontend
    app.layout = html.Div([
        dcc.Graph(
            id="graph",
            figure=dendro
        )
    ])
    
    return jsonify(message='Dendrogram generated'), 200

@app.callback(
    Output('graph', 'figure'),
    [Input('hidden-div', 'children')]
)

# create server route to check figure availability on the server side
@app.server.route('/check_dendrogram', methods=['GET'])
def check_dendrogram():
    dendro = cache.get('dendrogram')
    if dendro is not None:
        return jsonify(available=True)
    return jsonify(available=False)

if __name__ == '__main__':
    
    # start the server
    app.run_server(debug=False)
