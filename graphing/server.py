import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import webbrowser
import os
from flask import request
from flask_cors import CORS
from flask import jsonify
from flask_caching import Cache

from document import Document
from webscraper import WebScraper
from clustering import HierarchicalClustering

# Initialize the Dash app
app = dash.Dash(__name__)
server = app.server

cache = Cache(app.server, config={
    'CACHE_TYPE' : 'filesystem',
    'CACHE_DIR' : 'cache-directory'
})

cache.init_app(server)

extension_id = "inkjogmocgpoclmjkngkdblcpceagmnc"
CORS(app.server, resources={r"/*": {"origins": f"chrome-extension://{extension_id}"}})

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

@app.server.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.json
    urls = data.get('urls', [])
    print(urls)
    
    webscraper = WebScraper()
    
    docs = webscraper.scrapeWebpage(urls)
    
    hc = HierarchicalClustering()
    
    processed_docs = hc.preprocess_docs(docs)
    tfidf_matrix = hc.extract_features(processed_docs)
    
    cluster = hc.create_hierarchical_cluster(tfidf_matrix)
    
    dendro = hc.create_dendrogram(cluster, docs)
    
    cache.set('dendrogram', dendro)
    
    return jsonify(message='Dendrogram generated'), 200

@app.callback(
    Output('graph', 'figure'),
    [Input('hidden-div', 'children')]
)

def update_output(div):
    dendro = cache.get('dendrogram')
    # if dendro is None:
    #     return go.Figure()
    return dendro

@app.server.route('/check_dendrogram', methods=['GET'])
def check_dendrogram():
    dendro = cache.get('dendrogram')
    if dendro is not None:
        return jsonify(available=True)
    return jsonify(available=False)

if __name__ == '__main__':
    app.run_server(debug=False)
