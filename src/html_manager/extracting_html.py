import requests
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from decorators.exception_decorator import logging_exception

@logging_exception
def extracting_html(url):
    """
    Extracts and parses HTML content from a given URL.
    
    Args:
        url (str): The URL from which the HTML content is to be fetched.

    Returns:
        BeautifulSoup object: Parsed HTML of the page.
    """
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    return None

def encoding_joining_url(baseurl, query, choice):
    """
    Encodes the search query and constructs a URL based on the base URL and search choice.

    Args:
        baseurl (str): The base URL of the news website.
        query (str): The search query to be encoded.
        choice (int): The choice of URL structure (1 or 2) based on the site.

    Returns:
        str: The full URL with the encoded query.
    """
    encoded_query = quote_plus(query)
    
    if choice == 1:
        return f"{baseurl}search?searchtext={encoded_query}" #returns article url
    elif choice == 2:
        return f"{baseurl}search?q={encoded_query}" #returns article url
    return ""
