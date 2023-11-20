import plotly.graph_objects as go
import networkx as nx

# Create a graph
G = nx.Graph()
G.add_edges_from([("Programming for Beginners", "Hello World"), ("Programming for Beginners", "How to install Python"), ("Programming for Beginners", "Free Code Camp"),
                  ("Programming for Beginners", "Software Engineer Salary"), ("Programming for Beginners", "How to become a software engineer"), ("Programming for Beginners", "Is coding hard?")])

# Position the nodes using a layout algorithm
pos = nx.spring_layout(G)

# Calculate the degree of each node (number of connections)
degrees = dict(G.degree())

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

# Edge trace
edge_trace = go.Scatter(x=edge_x, y=edge_y, line=dict(width=0.5, color='#888'), hoverinfo='none', mode='lines')

# Node trace
node_trace = go.Scatter(x=node_x, y=node_y, mode='markers', hoverinfo='text',
                        marker=dict(showscale=True, colorscale='YlGnBu', size=[5 * degrees[node] for node in G.nodes()],
                                    line_width=2))

# Update hover text with node names and degree
node_trace.text = [f'{node} (# of connections: {degrees[node]})' for node in G.nodes()]

# Create figure
fig = go.Figure(data=[edge_trace, node_trace], layout=go.Layout(
                title='<br>Network graph with node sizes based on connections',
                showlegend=False, hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

# Show the figure
fig.show()