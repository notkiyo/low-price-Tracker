
**Title:** Google Shopping Price Scraper (India)

**Description:**

This Python script scrapes Google Shopping results for a specified product in India using the SerpAPI library. It extracts product details like name, price, and source website.

**Features:**

- Retrieves shopping results from Google Search.
- Targets India (gl="in") and English language (hl="en").
- Cleans and converts product prices to numerical values.
- Sorts results by price (ascending).
- Displays details of the 6 lowest-priced products.

**Requirements:**

- Python 3.x
- SerpAPI library (install using `pip install serpapi`)

**Usage:**

1. Replace `'YOUR_SERPAPI_KEY'` in the script with your obtained SerpAPI key ([https://serpapi.com/](https://serpapi.com/)).
2. Run the script: `python scraper.py` (replace `scraper.py` with your actual file name).
3. Enter the product name when prompted.

**Example Output:**

```
Enter the product you want to search: Laptop

1. HP Pavilion 15-eg0013dx (11th Gen Intel Core i5-1135G7, 8GB RAM, 256GB SSD)
  - Price: ₹42,990
  - Source: https://www.flipkart.com/

2. Lenovo IdeaPad Slim 3 15IIL05 (10th Gen Intel Core i3-1005G1, 4GB RAM, 256GB SSD)
  - Price: ₹27,490
  - Source: https://www.reliancedigital.in/laptops/c/101035

... (Displays details of 4 more lowest-priced products)
```

**Disclaimer:**

- Using scraping techniques might violate terms of service of some websites. Ensure proper usage according to SerpAPI's guidelines and website robots.txt.
- The script relies on SerpAPI, which might have usage limits or costs associated with extensive use.

**Feel free to modify and adapt this script for your specific needs.**
