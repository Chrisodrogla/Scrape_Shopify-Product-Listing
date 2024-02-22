from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options
import time
import re

Overall_Links = "https://www.danner.com/women/all-footwear?sortId=product-family&stock_status%5B%5D=1&stock_status%5B%5D=0"
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get(Overall_Links)
chrome_options = Options()
chrome_options.add_argument('--headless')

limit = 3  ################# Change this to None to collect all Eg. None ######################

links = driver.find_elements("xpath", "//li[@class='item product product-item']/a")
if limit is not None:
    links = links[:limit]

websites = [link.get_attribute("href") for link in links]

driver.quit()

all_data = []

for website in websites:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(website)

    handle1 = website.replace("https://www.danner.com/women/all-footwear/", "")
    handle2 = handle1.split(".html")[0]

    # Check if "danner" is already present in handle2
    if "danner" not in handle2:
        handle3 = "danner-" + handle2
    else:
        handle3 = handle2

    Style = driver.find_element("xpath", """//*[@id="product-specs--table"]/tbody/tr[1]/td""").text

    Handle = handle3 + "-" + Style

    UPC_LIST = []
    Upc_SRCS = driver.find_elements("xpath", "//select[@name='super_attribute[592]']/option[@value!='']")
    for Upc in Upc_SRCS:
        Upc.click()
        try:
            UPC_element = driver.find_element("xpath", '//script[contains(@src, "upc")]')
            UPC_value = UPC_element.get_attribute("src")
            split_values = UPC_value.split('upc=')
            if len(split_values) > 1:
                UPC_code = split_values[1].split('&')[0]
                UPC_LIST.append(UPC_code)
            else:
                UPC_LIST.append("N/A")
        except:
            UPC_LIST.append("N/A")

    Sizes = [re.sub(r'\([^)]*\)', '', option.get_attribute('innerText').strip()) for option in
             driver.find_elements("xpath", "//select[@name='super_attribute[592]']/option[@value!='']")]

    title1 = driver.find_element("xpath", """//*[@id="maincontent"]/div[2]/div/div[1]/div[1]/div[3]/h1""").text
    try:
        title2 = driver.find_element("xpath", """//*[@id="maincontent"]/div[2]/div/div[1]/div[1]/div[3]/h5[2]""").text

    except:
        title2 = " "

    # Check if "Danner" is already present in title1
    if "Danner" in title1:
        Title = title1 + " " + title2
    else:
        Title = "Danner " + title1 + " " + title2

    Title_SEO = title1 + " " + title2

    try:
        Type = driver.find_element("xpath", """//*[@id="maincontent"]/div[2]/div/div[1]/div[1]/div[1]/ul/li[3]""").text
        desc2_html = driver.find_element("xpath", """//*[@id="product-specs--table"]""").get_attribute(
            "outerHTML")

        desc1_html = driver.find_element("xpath", """//div[@class="product-detail description"]""").get_attribute(
            "outerHTML")
    except:
        desc1_html = " "
        desc2_html = " "
        Type = "All Footwear"

    #     desc2_html = driver.find_element("xpath", """//*[@id="product-specs--table"]""").get_attribute(
    #         "outerHTML")
    Body_HTML_ = desc1_html + desc2_html
    Color_Value = driver.find_element("xpath", """//*[@id="product-specs--table"]/tbody/tr[6]/td""").text

    Vendor = "Danner"

    Product_Category = " "

    #     Type = driver.find_element("xpath", """//*[@id="maincontent"]/div[2]/div/div[1]/div[1]/div[1]/ul/li[3]""").text

    Tags = "N/A"

    Published = "TRUE"

    Option1_Name = "Color"

    Option1_Value = Color_Value

    Option2_Name = "Size"

    Option2_Value = Sizes

    try:
        width1 = driver.find_element("xpath", """//*[@id="attribute593"]/option[2]""").text
        width2 = width1.replace("Women's ", "")
        Width_Value = width2.split(" -")[0]
    except:
        Width_Value = "N/A"

    Option3_Name = "Width"

    Option3_Value = Width_Value

    Variant_Grams = 0

    Variant_Inventory = "shopify"

    Variant_Inventory_Policy = 'deny'

    Variant_Fulfillment_Service = 'manual'

    Variant_Price = driver.find_element("xpath", """//meta[@itemprop='price']""").get_attribute("content")

    Variant_Comp_Price = Variant_Price

    Variant_Requires_Shipping = "TRUE"

    Variant_Taxable = "TRUE"

    Variant_Barcode = " "

    Image_Src = []
    Images = driver.find_elements("xpath", """//div[@class="more-views"]/ul/li/button/img""")
    for image in Images:
        src = image.get_attribute("src")
        Image_Src.append(src)

    Image_Position = [str(i + 1) for i in range(len(Image_Src))]

    Gift_Card = "FALSE"

    SEO_Title = Title_SEO

    SEO_Description = desc1_html

    Google_Shopping_Google_Product_Category = " "

    GoogleShoppingGender = " "

    GoogleShoppingAgeGroup = " "

    GoogleShoppingMPN = " "

    GoogleShoppingCondition = " "

    GoogleShoppingCustomProduct = " "

    GoogleShoppingCustomLabel_0 = " "

    GoogleShoppingCustomLabel_1 = " "

    GoogleShoppingCustomLabel_2 = " "

    GoogleShoppingCustomLabel_3 = " "

    GoogleShoppingCustomLabel_4 = " "

    Variant_Image = Image_Src[0]

    Variant_Weight_Unit = "lb"

    Variant_Tax_Code = " "

    Cost_per_item = " "

    Included_United_States = " "

    Price_United_States = " "

    Compare_At_Price_United_States = " "

    Included_International = "TRUE"

    Price_International = " "

    Compare_At_Price_International = " "

    Status = "active"

    Image_Alt_Text = [SEO_Title for _ in Image_Src]

    # Determine the maximum number of rows needed for this website
    max_rows = max(len(Sizes), len(Image_Src), len(Image_Position), len(Image_Alt_Text), len(UPC_LIST))

    # Add rows to the all_data list
    for idx in range(max_rows):
        if idx < len(Sizes):
            size = Sizes[idx]
        else:
            size = ''

        if idx < len(Image_Src):
            image = Image_Src[idx]
        else:
            image = ''

        if idx < len(Image_Position):
            image_c = Image_Position[idx]
        else:
            image_c = ''

        #         if idx < len(Image_Alt_Text):
        #             image_Alt = Image_Alt_Text[idx]
        #         else:
        #             image_Alt = ''

        if idx < len(Image_Alt_Text):
            image_alt = Image_Alt_Text[idx]
        else:
            image_alt = ''

        if idx < len(UPC_LIST):
            upc_v = UPC_LIST[idx]
        else:
            upc_v = ''

        if idx == 0:  # Only add Handle and Title for the first row of each website's data
            all_data.append({
                'Handle': Handle,
                'Title': Title,
                'Body (HTML)': Body_HTML_,
                'Vendor': Vendor,
                'Product Category': Product_Category,
                'Type': Type,
                'Tags': Tags,
                'Published': Published,
                'Option1 Name': Option1_Name,
                'Option1 Value': Color_Value,
                'Option2 Name': Option2_Name,
                'Option2 Value': size,
                'Option3 Name': Option3_Name,
                'Option3 Value': Option3_Value,
                'UPC': upc_v,
                'Variant SKU': " ",
                'Incomplete Variant SKU': Style + "-" + Color_Value + "-" + size + Option3_Value,
                'Variant Grams': Variant_Grams,
                'Variant Inventory Tracker': Variant_Inventory,
                'Variant Inventory Policy': Variant_Inventory_Policy,
                'Variant Fulfillment Service': Variant_Fulfillment_Service,
                'Variant Price': Variant_Price,
                'Variant Compare At Price': Variant_Comp_Price,
                'Variant Requires Shipping': Variant_Requires_Shipping,
                'Variant Taxable': Variant_Taxable,
                'Variant Barcode': Variant_Barcode,
                'Image Src': image,
                'Image Position': image_c,
                'Image Alt Text': image_alt,
                'Gift Card': Gift_Card,
                'SEO Title': SEO_Title,
                'SEO Description': SEO_Description,
                'Google Shopping / Google Product Category': Google_Shopping_Google_Product_Category,
                'Google Shopping / Gender': GoogleShoppingGender,
                'Google Shopping / Age Group': GoogleShoppingAgeGroup,
                'Google Shopping / MPN': GoogleShoppingMPN,
                'Google Shopping / Condition': GoogleShoppingCondition,
                'Google Shopping / Custom Product': GoogleShoppingCustomProduct,
                'Google Shopping / Custom Label 0': GoogleShoppingCustomLabel_0,
                'Google Shopping / Custom Label 1': GoogleShoppingCustomLabel_1,
                'Google Shopping / Custom Label 2': GoogleShoppingCustomLabel_2,
                'Google Shopping / Custom Label 3': GoogleShoppingCustomLabel_3,
                'Google Shopping / Custom Label 4': GoogleShoppingCustomLabel_4,
                'Variant Image': Variant_Image,
                'Variant Weight Unit': Variant_Weight_Unit,
                'Variant Tax Code': Variant_Tax_Code,
                'Cost per item': Cost_per_item,
                'Included / United States': Included_United_States,
                'Price / United States': Price_United_States,
                'Compare At Price / United States': Compare_At_Price_United_States,
                'Included / International': Included_International,
                'Price / International': Price_International,
                'Compare At Price / International': Compare_At_Price_International,
                'Status': Status

            })
        else:
            all_data.append({
                'Handle': Handle,  # Empty handle for subsequent rows of each website's data
                'Title': '',
                'Body (HTML)': '',
                'Vendor': '',
                'Product Category': '',
                'Type': '',
                'Tags': '',
                'Published': '',
                'Option1 Name': '',
                'Option1 Value': Color_Value,
                'Option2 Name': '',
                'Option2 Value': size,
                'Option3 Name': '',
                'Option3 Value': Option3_Value,
                'UPC': upc_v,
                'Variant SKU': " ",
                'Incomplete Variant SKU': Style + "-" + Color_Value + "-" + size + Option3_Value,
                'Variant Grams': Variant_Grams,
                'Variant Inventory Tracker': Variant_Inventory,
                'Variant Inventory Policy': Variant_Inventory_Policy,
                'Variant Fulfillment Service': Variant_Fulfillment_Service,
                'Variant Price': Variant_Price,
                'Variant Compare At Price': Variant_Comp_Price,
                'Variant Requires Shipping': Variant_Requires_Shipping,
                'Variant Taxable': Variant_Taxable,
                'Variant Barcode': Variant_Barcode,
                'Image Src': image,
                'Image Position': image_c,
                'Image Alt Text': image_alt,
                'Gift Card': '',
                'SEO Title': '',
                'SEO Description': '',
                'Google Shopping / Google Product Category': '',
                'Google Shopping / Gender': '',
                'Google Shopping / Age Group': '',
                'Google Shopping / MPN': '',
                'Google Shopping / Condition': '',
                'Google Shopping / Custom Product': '',
                'Google Shopping / Custom Label 0': '',
                'Google Shopping / Custom Label 1': '',
                'Google Shopping / Custom Label 2': '',
                'Google Shopping / Custom Label 3': '',
                'Google Shopping / Custom Label 4': '',
                'Variant Image': Variant_Image,
                'Variant Weight Unit': Variant_Weight_Unit,
                'Variant Tax Code': '',
                'Cost per item': Cost_per_item,
                'Included / United States': '',
                'Price / United States': Price_United_States,
                'Compare At Price / United States': Compare_At_Price_United_States,
                'Included / International': '',
                'Price / International': '',
                'Compare At Price / International': '',
                'Status': ''

            })

    driver.quit()  # Close the WebDriver after processing each website

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(all_data)

df.to_csv('Womens_Danner_Products.csv', index=False)
