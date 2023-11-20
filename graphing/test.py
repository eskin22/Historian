import plotly.graph_objects as go
import networkx as nx

# Create a graph with named nodes
G = nx.Graph()
G.add_edges_from([("Programming for Beginners", "Hello World"), ("Programming for Beginners", "How to install Python"), ("Programming for Beginners", "Free Code Camp"),
                  ("Programming for Beginners", "Software Engineer Salary"), ("Programming for Beginners", "How to become a software engineer"), ("Programming for Beginners", "Is coding hard?")])

# Position the nodes using NetworkX's layout
pos = nx.spring_layout(G)

# Extracting node and edge information for plotting
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

node_x = [pos[node][0] for node in G.nodes()]
node_y = [pos[node][1] for node in G.nodes()]

# Create edges
edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

# Create nodes
node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        colorscale='YlGnBu',
        size=10,
        color=[],
        line_width=2))

# Update node marker color and hover text
node_adjacencies = []
node_text = []
for node in G.nodes():
    node_adjacencies.append(len(G[node]))  # Count of adjacent nodes (degree)
    node_text.append('Name: ' + str(node))  # Node name for hover text

node_trace.marker.color = node_adjacencies
node_trace.text = node_text

# Create figure
fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='Knowledge Graph',
                titlefont_size=16,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )

# Show the figure
fig.show()
