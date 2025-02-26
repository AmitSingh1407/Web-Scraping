from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Initialize the driver
driver = webdriver.Chrome()  # Replace with the path to your WebDriver

# Open Amazon search page
driver.get("https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sa")

# Initialize empty lists to store product data
product_names = []
prices = []
ratings = []
sellers = []

# Define a function to extract product information
def extract_product_details():
    products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
    for product in products:
        try:
            # Product Name
            name = product.find_element(By.TAG_NAME, "h2").text
            product_names.append(name)
            
            # Price
            try:
                price = product.find_element(By.CLASS_NAME, "a-price-whole").text
            except:
                price = "N/A"  # If price is not available
            prices.append(price)
            
            # Rating
            try:
                rating = product.find_element(By.CLASS_NAME, "a-icon-alt").text
            except:
                rating = "N/A"  # If rating is not available
            ratings.append(rating)
            
            # Seller
            try:
                seller = product.find_element(By.CLASS_NAME, "a-row.a-size-small").text
            except:
                seller = "N/A"  # If seller information is not available
            sellers.append(seller)
            
        except Exception as e:
            print(f"Error extracting product details: {e}")

# Extract product details from the first page
extract_product_details()

# Save data to a CSV
df = pd.DataFrame({
    "Product Name": product_names,
    "Price": prices,
    "Rating": ratings,
    "Seller": sellers
})
df.to_csv("amazon_products.csv", index=False)

# Close the driver
driver.quit()
