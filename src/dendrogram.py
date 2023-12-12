from scipy.cluster.hierarchy import dendrogram
import plotly.graph_objs as go

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