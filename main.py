import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_properties():
    """
    Scrapes property data (Title, Location, Price) and saves to CSV.
    """
    # URL to scrape (Using a scraper sandbox for demonstration safety)
    url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
    
    # Headers to mimic a real browser (prevents being blocked)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    print("Starting scraper...")
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("Failed to retrieve the website.")
        return

    soup = BeautifulSoup(response.content, "html.parser")
    
    properties = []
    
    # Find all product cards (logic applies to property cards on real estate sites)
    items = soup.find_all("div", class_="thumbnail")

    for item in items:
        try:
            title = item.find("a", class_="title").text.strip()
            price = item.find("h4", class_="price").text.strip()
            description = item.find("p", class_="description").text.strip()
            
            properties.append({
                "Property Title": title,
                "Price": price,
                "Description": description
            })
        except AttributeError:
            continue

    # Convert to DataFrame using Pandas
    df = pd.DataFrame(properties)
    
    # Save to CSV
    output_file = "real_estate_data.csv"
    df.to_csv(output_file, index=False)
    print(f"Scraping complete! {len(df)} items saved to {output_file}")
    
    # Display first few rows
    print(df.head())

if __name__ == "__main__":
    scrape_properties()
