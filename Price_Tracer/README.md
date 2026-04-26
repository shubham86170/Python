Description

This program extracts the price of a product from an Amazon webpage and compares it with a given target price.

Features/Methods

- Fetches webpage using requests
- Analyse HTML using BeautifulSoup
- Extracts the product price
- Converts price into numeric value
- Compares product price with target price
- Handles network errors

How to Run

1. Install dependencies:
   pip install requests beautifulsoup4 lxml

2. Run the script:
   python PriceTracer.py

Output

- Displays the product name and current price
- Gives suggests to buy or wait for sometime.