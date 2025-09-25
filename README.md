
# 📰 News Headlines Scraper

A Python script that scrapes news headlines from a given website (default: **BBC News**) and saves them into a text file.

---

## 🚀 Features

* Scrapes headlines from HTML `<h2>` and `<h3>` tags.
* Works with most static news websites.
* Saves all scraped headlines into `headlines.txt`.
* Includes error handling for failed requests.

---

## 📦 Requirements

* Python 3.7+
* Install dependencies:

  ```bash
  pip install requests beautifulsoup4
  ```

---

## 🛠️ Usage

1. Clone this repository or copy the script.
2. Run the script:

   ```bash
   python scraper.py
   ```
3. Headlines will be saved in a file called **`headlines.txt`** in the same directory.

---

## ⚙️ Configuration

* Change the target URL inside the script:

  ```python
  url = "https://www.bbc.com/news"
  ```
* Change the HTML tags to scrape (default: `h2` and `h3`):

  ```python
  headlines = [el.get_text(strip=True) for el in soup.find_all(['h2', 'h3'])]
  ```

---

## 📂 Output

* Headlines are saved line by line in `headlines.txt`. Example:

  ```
  Global economy faces challenges
  Technology reshaping the future
  Climate change impacts increase
  ```

---

