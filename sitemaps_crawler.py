import requests
from bs4 import BeautifulSoup
import os
def get_sitemap_urls(sitemap_url,visited_urls):

    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'lxml')
        urls = [loc.text for loc in soup.find_all('loc')]

        return urls
    except requests.exceptions.RequestException as e:
        print(f"Error fetching sitemap: {e}")
        return []

def main():
    sitemap_url = "https://www.example.com/sitemap.xml" #replace with your sitemap url
    visited_urls = set()
    urls = get_sitemap_urls(sitemap_url, visited_urls)
    print(urls)


if __name__ == "__main__":
    main()