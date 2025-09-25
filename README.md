# Web Scraper for News Headlines

## Objective
This project is a Python script to scrape top news headlines from a public news website (default: BBC News) and save them in a text file.

## Tools Used
- Python 3.x
- requests
- BeautifulSoup (bs4)

## How It Works
1. Fetches the HTML content of the target news site using the requests library.
2. Parses the page for headline elements (using the `h2` tag by default) with BeautifulSoup.
3. Writes the extracted headlines to `headlines.txt`, one per line.

## Usage

1. **Install dependencies** (if required):
    ```
    pip install requests beautifulsoup4
    ```
2. **Run the script**:
    ```
    python news_headlines_scraper.py
    ```

3. **Output**: Check `headlines.txt` for the list of scraped headlines.

## Notes
- You can change the `url` variable in the script to target a different news site as needed.
- The script uses a User-Agent header to emulate a browser request for better compatibility.

## Deliverables
- `news_headlines_scraper.py`: Python script
- `headlines.txt`: Output file containing scraped headlines
- `README.md`: This instruction file

---

**Task by Elevate Labs for Python Developer Internship**  
Covers: HTTP requests, Web scraping, HTML parsing with BeautifulSoup.
