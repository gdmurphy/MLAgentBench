## TODO Add more merge methods here
from methods.MyMethod import MyMethod

def all_method_handlers():
    """Enumerate and Load (import) all implemented methods."""
    loaded_methods = {
        "my_method" : MyMethod,
        ## TODO Add more merge methods here
    }
    
    return loaded_methods

