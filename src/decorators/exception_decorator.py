import logging

# Configure the logging
logging.basicConfig(
    filename='app.log',  # Log file name
    level=logging.DEBUG,  # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
)

def logging_exception(func):
    """
    A decorator to log exceptions that occur in the wrapped function.
    
    Args:
        func (function): The function to be wrapped by the decorator.
        
    Returns:
        wrapper function: The wrapped function that includes exception logging.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error in function {func.__name__}: {str(e)}")  # Log the error with function name and exception
            return None 
           
    return wrapper
