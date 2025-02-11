from news_channels.ndtv import extracting_TheNDTV
from news_channels.bbc import extracting_BBC
from decorators.exception_decorator import logging_exception


@logging_exception
def main():
    """
    Main function to interact with the user and fetch the desired news article.
    It asks the user for the news channel and search query, then invokes
    the corresponding extraction function.
    """
    print("Welcome to the News Extractor!")
    print("Please choose a news channel:")
    print("1. NDTV")
    print("2. BBC")

    choice = input("Enter the number of your choice: ")

    query = input("Enter the search query: ")

    if choice == '1':
        extracting_TheNDTV("https://www.ndtv.com/", query)
    elif choice == '2':
        extracting_BBC("https://www.bbc.com/", query)
    else:
        print("Invalid choice. Please select a valid news channel.")

if __name__ == "__main__":
    main()
