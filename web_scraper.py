import requests
from bs4 import BeautifulSoup
import argparse
from urllib.parse import urljoin

def web_scraper(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all links on the page
            links = soup.find_all('a')

            # Print the absolute links
            for link in links:
                href = link.get('href')
                if href:
                    full_url = urljoin(url, href)  # Resolve relative URLs
                    print(full_url)

        else:
            print('Failed to retrieve the webpage, status code:', response.status_code)

    except Exception as e:
        print('An error occurred: %s' % e)

def main():
    parser = argparse.ArgumentParser(description='Web Scraper')
    parser.add_argument('url', help='URL to scrape')
    args = parser.parse_args()

    web_scraper(args.url)

if __name__ == '__main__':
    main()
