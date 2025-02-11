from html_manager.extracting_html import extracting_html, encoding_joining_url
from output_writer.markdown_writer import writing_markdown_file
from decorators.exception_decorator import logging_exception

@logging_exception
def extracting_BBC(baseurl, query):
    """
    Extracts and prints the body of the first article returned 
    by a search query from the BBC website.

    Args:
        baseurl (str): The base URL of the BBC website.
        query (str): The search query string to find relevant articles on the BBC site.

    Returns:
        None
    """

    #Exception handling for query if it is empty
    if query=="":
        raise ValueError("Query in empty or invalid!")
    
    #Creating the url with the query 
    final_url = encoding_joining_url(baseurl, query, 2)
    html = extracting_html(final_url)

    #Fetch the first article for that query
    first_news = html.find("div", class_="sc-c6f6255e-0")
    a_tag = first_news.find('a', class_="sc-2e6baa30-0")

    # Get the href for the first article
    link = a_tag.get("href")
    article_link = baseurl + link

    #Get the html of the whole artcile (first artcile)
    article_html = extracting_html(article_link)

    #Extracting article title
    article_title = article_html.find("h1", class_="sc-518485e5-0")

    #Extracting article body 
    article_body_section = article_html.find_all("div", class_="dlWCEZ")

    body = "".join([para.text for para in article_body_section])

    writing_markdown_file(article_title, body)
