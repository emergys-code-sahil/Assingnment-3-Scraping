def writing_markdown_file(article_title, body):
    """
    Creates and writes the article content to a markdown file.

    Args:
        article_title (str): The title of the article to be written.
        body (str): The body text of the article to be written.

    Returns:
        None: Writes the content to a markdown file named "new.md".
    """
    # Creating the markdown
    markdown_content = f'''# {article_title.text}
    
    {body}'''

    # Writing the markdown to the file
    with open("new.md", "w", encoding='utf-8') as file:
        file.write(markdown_content)
