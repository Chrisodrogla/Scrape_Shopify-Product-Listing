import time
import requests  # Add this line
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup


# extract links from a given page from OJP
def get_links_from_page(driver, page_url):
    driver.get(page_url)
    time.sleep(4)

    link_visit = []

    # Find and store the links on the current page
    post_links = driver.find_elements("xpath", '//figure/a')
    for post in post_links:
        href = post.get_attribute("href")
        link_visit.append(href)

    return link_visit


# extract data from a given link using BeautifulSoup
def extract_data(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')

    handles = "mens-hunting-hoodies-pullovers"
    titles = soup.find('h1', {'class': 'main-product__title h5'}).text
    html_bodies = soup.find_all('div', {'class': 'accordion__content p2 p2--fixed rte'})
    vendors = soup.find('p', {
        'class': 'main-product__text-field p2 p2--fixed underlined-link underlined-link--no-offset bold'}).a.text
    product_categories = "  "
    type = "  "
    tags = "  "
    published = "TRUE"
    colors_elements = soup.find_all('div', {'class': 'main-product__form-option--style-label'})
    colors = ', '.join([element.text.strip().strip('') for element in colors_elements])

    sizes_elements = soup.find_all('div', {'class': 'main-product__form-option'})
    sizes = []

    for element in sizes_elements:
        label = element.find('label', {'class': 'p2 p2--fixed motion-reduce'})
        if label:
            size_value = label.text.strip()
            sizes.append(size_value)

    variant_sku = soup.find('span', {'class': 'main-product__sku-span'}).text
    variant_grams = "0"
    variant_inventory_tracker = "shopify"
    variant_inventory_policy = "deny"
    variant_fulfillment_service = "manual"
    variant_price_element = soup.find('ins', {'class': 'price__sale'})
    variant_price = variant_price_element.text if variant_price_element else "  "
    variant_compare_at_price_element = soup.find('del', {'class': 'price__compare'})
    variant_compare_at_price = variant_compare_at_price_element.text if variant_compare_at_price_element else "  "
    variant_requires_shipping = "TRUE"
    variant_taxable = "TRUE"
    variant_barcode = "  "
    variant_image = "  "
    variant_weight_unit = "lb"
    variant_tax_code = "  "
    cost_per_item = "  "
    status = "draft"

    # Create a dictionary for the data
    data = {
        "Handle": handles,
        "Title": titles,
        "Body(HTML)": html_bodies,
        "Vendor": vendors,
        "Product Category": product_categories,
        "Type": type,
        "Tags": tags,
        "Published": published,
        "Colors": colors,
        "Sizes": sizes,
        "Variant SKU": variant_sku,
        "Variant Grams": variant_grams,
        "Variant Inventory Tracker": variant_inventory_tracker,
        "Variant Inventory Policy": variant_inventory_policy,
        "Variant Fulfillment Service": variant_fulfillment_service,
        "Variant Price": variant_price,
        "Variant Compare At Price": variant_compare_at_price,
        "Variant Requires Shipping": variant_requires_shipping,
        "Variant Taxable": variant_taxable,
        "Variant Barcode": variant_barcode,
        "Variant Image": variant_image,
        "Variant Weight Unit": variant_weight_unit,
        "Variant Tax Code": variant_tax_code,
        "Cost per item": cost_per_item,
        "Status": status
    }

    return data


# Specifying the base URL
base_url = 'https://banded.com/collections/mens-hunting-hoodies-pullovers?collections=0%3Dmens-hunting-hoodies-pullovers&filterchange=true&page={}'

# the driver get
driver = webdriver.Chrome()

# Specify the range of pages you want to scrape
start_page = 1
end_page = 2  # Adjust as needed

overall_links = []

for page_number in range(start_page, end_page + 1):
    page_url = base_url.format(page_number)
    links_on_page = get_links_from_page(driver, page_url)

    # Add the links to overall_links
    overall_links.extend(links_on_page)

data_list = []

for link in overall_links:
    data = extract_data(link)
    data_list.append(data)

df = pd.DataFrame(data_list)

driver.quit()

print(df)
# Save DataFrame to Excel file
excel_file_path = '42_Items_scraped.xlsx'  # Change the filename as needed
df.to_excel(excel_file_path, index=False)
