class Document():
    """
    A class to represent documents (webpages) of text data in a collection
    """
    def __init__(self, file, test=False) -> None:
        """
        Initializes a `Document` object

        Args:
            file (_type_): The file path to the document .txt file
            test (bool, optional): Use `True` for sample data and `False` for real data. Defaults to False.
        """
        self.title = file
        
        self.load_doc_text(test)
    
    def load_doc_text(self, test=False) -> None:
        """
        Loads a given .txt file in as a `Document` object

        Args:
            test (bool, optional): Use `True` for sample data and `False` for real data. Defaults to False.
        """
        filepath = self.title if not test else f'sample_data/{self.title}'
        with open(filepath, 'r', encoding='utf-8') as file:
            self.text = file.read()
            file.close()

if __name__ == '__main__':
    
    # sample usage
        
    import os

    # load in sample documents as Document objects
    for i, file in enumerate(os.listdir('sample_data')):
        try:
            Document(file, test=True)
            print(f"Successfully loaded file #{i+1}")
        except Exception as e:
            print(e); print(f"Error occured for {file}")