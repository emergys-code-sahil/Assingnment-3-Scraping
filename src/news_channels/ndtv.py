from html_manager.extracting_html import extracting_html, encoding_joining_url
from output_writer.markdown_writer import writing_markdown_file
from decorators.exception_decorator import logging_exception


@logging_exception
def extracting_TheNDTV(baseurl, query):
    """
    Extracts and prints the title and body of the first article returned 
    by a search query from the NDTV website.

    Args:
        baseurl (str): The base URL of the NDTV website.
        query (str): The search query string to find relevant articles on the NDTV site.

    Returns:
        None
    """

    #Exception handling for query if it is empty
    if query=="":
        raise ValueError("Query in empty or invalid!")
    
    #Creating the url with the query 
    final_url = encoding_joining_url(baseurl, query, 1)
    html = extracting_html(final_url)

    #Fetch the first article for that query
    first_news = html.find('div', class_='SrchLstPg-a')
    a_tag = first_news.find('a', class_="SrchLstPg_img")

    # Get the href for the first article
    link = a_tag.get("href")
    
    #Get the html of the whole artcile (first artcile)
    article_html = extracting_html(link)

    # Extracting article title
    article_title = article_html.find('h1', class_="sp-ttl")
    if not article_title:
        title_div = article_html.find('div', class_='lead_heading')
        if title_div:
            article_title = title_div.find('h1')

    # Extracting article body
    article_body = article_html.find('div', 'sp_txt')
    if not article_body:
        article_body = article_html.find('div', class_='content_text')

    article_p = article_body.find_all('p')
    body = "".join([para.text for para in article_p])

    writing_markdown_file(article_title, body)


