# xScaper

A simple Twitter/X scraper built with Python. Collects tweets based on a keyword and saves the result to an Excel file.

## Requirements

- Python 3.10+
- twikit
- pandas
- openpyxl

Install dependencies:

```
pip install -r requirement.txt
```

## Setup

1. Get your Twitter cookies and save them as `auth/cookies.json`. You can export cookies from your browser using a browser extension like "Cookie-Editor".

2. Open `scraper.py` and adjust the configuration at the top of the file:

```python
KEYWORD = "saham indonesia"   # keyword to search
TARGET = 1000                  # how many tweets to collect
PRODUCT = "Top"                # "Top" or "Latest"
SLEEP_DURATION = 5             # delay between requests (seconds)
COOKIES_PATH = "auth/cookies.json"
```

3. Run the scraper:

```
python scraper.py
```

## Output

Results will be saved as an Excel file inside the `data/` folder. The filename follows this pattern:

```
data/scrape_<keyword>.xlsx
```

Each row contains:
- Username
- Isi Tweet (tweet content)
- Tanggal (date)
- Likes
- Retweets

## Notes

- This scraper uses cookies-based authentication, so no password is required.
- If you hit a rate limit (error 429), wait a few minutes before running again.
- The `data/` and `auth/` folders are excluded from git via `.gitignore`.
