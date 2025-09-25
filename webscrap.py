import requests
from bs4 import BeautifulSoup

def fetch_headlines(url, tag='h2'):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; NewsScraper/1.0)'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = [el.get_text(strip=True) for el in soup.find_all(tag)]
        return headlines
    except Exception as e:
        print(f"Error fetching headlines: {e}")
        return []

if __name__ == "__main__":
    url = "https://www.bbc.com/news"
    headlines = fetch_headlines(url)
    with open('headlines.txt', 'w', encoding='utf-8') as f:
        for line in headlines:
            f.write(line + '
')
    print(f"Scraped {len(headlines)} headlines to headlines.txt")
