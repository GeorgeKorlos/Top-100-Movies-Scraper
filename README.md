# Top 100 Movies Scraper

This Python script scrapes a list of the top 100 movies from a web page and stores the titles in a text file. The list is scraped from an archived version of Empire Online's "Top 100 Movies" feature.

## Features

- **Web Scraping**: Uses `requests` to fetch the webpage and `BeautifulSoup` to parse the HTML.
- **Movie Title Extraction**: Extracts movie titles from the page and reverses the list to match the intended order.
- **File Output**: Saves the movie titles into a text file named `movies.txt`.

## Prerequisites

- Python 3.x
- Required Python packages: `requests`, `beautifulsoup4`

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/top-100-movies-scraper.git
   cd top-100-movies-scraper
