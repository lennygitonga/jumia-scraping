# Jumia Flash Sales Scraper

A Python web scraper that collects product data from the Jumia Kenya flash sales page and saves it to a CSV file.

## Data Collected
- Product Name
- New Price (discounted)
- Old Price
- Discount (%)
- Brand
- Items Left
- Rating
- Time Left (if available)


## Libraries Used
- `selenium` - Controls the Chrome browser
- `beautifulsoup4` - Parses the HTML to extract data
- `pandas` - Saves the data to a CSV file
- `webdriver-manager` - Automatically installs the correct ChromeDriver

## Installation
Install all required libraries by running:
```bash
pip install requests beautifulsoup4 pandas selenium webdriver-manager
```

## How to Run
```bash
python jumia-scraper.py
```

## How It Works
1. Opens Chrome invisibly in the background (headless mode)
2. Goes through each page of the flash sales automatically
3. Extracts product data from every product card
4. Stops when it reaches the last page
5. Saves all collected data to `jumia_flash_sales.csv`

## Output
A CSV file named `jumia_flash_sales.csv` will be created in the same folder as the script.