# blinkit-assesment
# 🛒 BlinkIt Nachos Scraper

This project is a web scraper using Playwright library of python to extract product data from BlinkIt's public API. It targets specific categories and subcategories based on provided latitude and longitude coordinates, outputting the data into a structured CSV file.

---

### Prerequisites

- Python 3
- [Playwright](https://playwright.dev/python/docs/intro)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/blinkit-category-scraper.git
   cd blinkit-category-scraper

2. **Create a virtual env:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # If using Windows: venv\Scripts\activate

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    playwright install #Not Mandatory


# Run The Script using Below command -
    
```bash
python blinkit_with_playwright.py
```

**PUBLIC API ENDPOINT** : **https://api.blinkit.com/v1/categories/{category_id}/subcategories/{subcategory_id}/products?lat={latitude}&lon={longitude}**