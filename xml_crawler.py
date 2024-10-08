import requests
from bs4 import BeautifulSoup
from lxml import etree
import os

def get_sitemap_urls(sitemap_url, visited_urls):

    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'lxml')
        new_urls = []
        for loc in soup.find_all('loc'):
            url = loc.text
            if url not in visited_urls:
                new_urls.append(url)
                visited_urls.add(url)
        return new_urls
    except requests.exceptions.RequestException as e:
        print(f"Error fetching sitemap: {e}")
        return []

def fetch_and_save_html(urls):
    for i, url in enumerate(urls):
        if i >= 1000:
            break
        try:
            response = requests.get(url)
            response.raise_for_status()

            filename = f"{i+1}.html"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"Saved HTML from {url} to {filename}")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching or saving HTML from {url}: {e}")

def main():
    sitemap_url = "https://www.example.com/sitemap.xml" #replace with your sitemap url
    visited_urls = set()

    main_urls = get_sitemap_urls(sitemap_url, visited_urls)

    fetch_and_save_html(main_urls)

    for url in main_urls:
        if url.endswith('.xml'):
            nested_urls = get_sitemap_urls(url, visited_urls)
            fetch_and_save_html(nested_urls)

if __name__ == "__main__":
    main()