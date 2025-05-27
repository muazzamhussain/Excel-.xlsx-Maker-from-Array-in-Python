import openpyxl
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "PrestaShop Test Cases"

headers = [
    "Test Case ID", "Test Scenario", "Test Case Title", "Pre-requisites",
    "Test Steps", "Test Data", "Expected Result", "Actual Result",
    "Priority", "Result", "Comments"
]

ws.append(headers)

# Define the test cases data
test_cases = [
    {
        "Test Case ID": "TC_PDP_001",
        "Test Scenario": "TS_021",
        "Test Case Title": "Validate Product Name Display",
        "Pre-requisites": "1. Open the Application URL",
        "Test Steps": "1. Search for a product.<br>2. Click on the product from the search results.<br>3. Check the product name on the Product Detail Page.",
        "Test Data": "Product Name: iPhone 14 Pro",
        "Expected Result (ER)": "Product name should be displayed correctly with proper formatting and styling.",
        "Actual Result": "",
        "Priority": "High",
        "Result": "",
        "Comments": ""
    },
    {
        "Test Case ID": "TC_PDP_002",
        "Test Scenario": "TS_021",
        "Test Case Title": "Validate Product Code/SKU Display",
        "Pre-requisites": "1. Open the Application URL",
        "Test Steps": "1. Search for a product.<br>2. Click on the product from the search results.<br>3. Check the product SKU/code on the Product Detail Page.",
        "Test Data": "Product Name: iPhone 14 Pro, SKU: IP14P-128-BLK",
        "Expected Result (ER)": "Product SKU should be displayed correctly as unique identifier.",
        "Actual Result": "",
        "Priority": "High",
        "Result": "",
        "Comments": ""
    },
    {
        "Test Case ID": "TC_PDP_003",
        "Test Scenario": "TS_021",
        "Test Case Title": "Validate Product Price Display",
        "Pre-requisites": "1. Open the Application URL",
        "Test Steps": "1. Search for a product.<br>2. Click on the product from the search results.<br>3. Check the price display on the Product Detail Page.",
        "Test Data": "Product Name: iPhone 14 Pro, Price: $999.00",
        "Expected Result (ER)": "Price should be displayed correctly with regular price, sale price (if applicable), and tax inclusion/exclusion notation.",
        "Actual Result": "",
        "Priority": "High",
        "Result": "",
        "Comments": ""
    },
    {
        "Test Case ID": "TC_PDP_004",
        "Test Scenario": "TS_021",
        "Test Case Title": "Validate Availability Status Display",
        "Pre-requisites": "1. Open the Application URL",
        "Test Steps": "1. Search for a product.<br>2. Click on the product from the search results.<br>3. Check the availability status on the Product Detail Page.",
        "Test Data": "Product Name: iPhone 14 Pro",
        "Expected Result (ER)": "Real-time stock level indicators should be displayed correctly (In Stock/Out of Stock/Limited Stock).",
        "Actual Result": "",
        "Priority": "High",
        "Result": "",
        "Comments": ""
    },
    {
        "Test Case ID": "TC_PDP_005",
        "Test Scenario": "TS_021",
        "Test Case Title": "Validate Product Variants Display",
        "Pre-requisites": "1. Open the Application URL",
        "Test Steps": "1. Search for a product with variants.<br>2. Click on the product from the search results.<br>3. Check the product variants section on the Product Detail Page.",
        "Test Data": "Product Name: iPhone 14 Pro (128GB, 256GB, 512GB variants)",
        "Expected Result (ER)": "Size/color/material options should be displayed with visual swatches and combination-specific pricing.",
        "Actual Result": "",
        "Priority": "High",
        "Result": "",
        "Comments": ""
    },
    {
        "Test Case ID": "TC_PDP_006",
        "Test Scenario": "TS_022",
        "Test Case Title": "Validate Primary Product Image Display",
        "Pre-requisites": "1. Open the Application URL",
        "Test Steps": "1. Search for a product.<br>2. Click on the product from the search results.<br>3. Check the primary product image display.",
        "Test Data": "Product Name: Samsung Galaxy S23",
        "Expected Result (ER)": "Large, high-resolution main product photo should be displayed correctly.",
        "Actual Result": "",
        "Priority": "High",
        "Result": "",
        "Comments": ""
    },
    {
        "Test Case ID": "TC_PDP_007",
        "Test Scenario": "TS_022",
        "Test Case Title": "Validate Alternative Product Images",
        "Pre-requisites": "1. Open the Application URL",
        "Test Steps": "1. Search for a product with multiple images.<br>2. Click on the product from the search results.<br>3. Check the thumbnail gallery showing multiple product angles.",
        "Test Data": "Product Name: Samsung Galaxy S23",
        "Expected Result (ER)": "Thumbnail gallery should display multiple product angles with proper navigation.",
        "Actual Result": "",
        "Priority": "High",
        "Result": "",
        "Comments": ""
    },
    {
        "Test Case ID": "TC_PDP_008",
        "Test Scenario": "TS_022",
        "Test Case Title": "Validate Image Zoom Functionality",
        "Pre-requisites": "1. Open the Application URL",
        "Test Steps": "1. Search for a product.<br>2. Click on the product from the search results.<br>3. Click on the main product image to test zoom functionality.",
        "Test Data": "Product Name: Samsung Galaxy S23",
        "Expected Result (ER)": "Click-to-enlarge feature should work correctly for detailed examination.",
        "Actual Result": "",
        "Priority": "Medium",
        "Result": "",
        "Comments": ""
    },
    {
        "Test Case ID": "TC_PDP_009",
        "Test Scenario": "TS_022",
        "Test Case Title": "Validate 360-Degree View Functionality",
        "Pre-requisites": "1. Open the Application URL",
        "Test Steps": "1. Search for a product with 360-degree view.<br>2. Click on the product from the search results.<br>3. Test the 360-degree rotating product display.",
        "Test Data": "Product Name: Laptop with 360-degree view enabled",
        "Expected Result (ER)": "Rotating product display should function smoothly when available.",
        "Actual Result": "",
        "Priority": "Medium",
        "Result": "",
        "Comments": ""
    },
    {
        "Test Case ID": "TC_PDP_010",
        "Test Scenario": "TS_022",
        "Test Case Title": "Validate Video Integration",
        "Pre-requisites": "1. Open the Application URL",
        "Test Steps": "1. Search for a product with video demonstration.<br>2. Click on the product from the search results.<br>3. Test the product demonstration video playback.",
        "Test Data": "Product Name: Product with demonstration video",
        "Expected Result (ER)": "Product demonstration videos should play correctly and be properly integrated.",
        "Actual Result": "",
        "Priority": "Medium",
        "Result": "",
        "Comments": ""
    },
    {
        "Test Case ID": "TC_PDP_011",
        "Test Scenario": "TS_022",
        "Test Case Title": "Validate Image Navigation Controls",
        "Pre-requisites": "1. Open the Application URL",
        "Test Steps": "1. Search for a product with multiple images.<br>2. Click on the product from the search results.<br>3. Test previous/next controls for image Browse.",
        "Test Data": "Product Name: Product with multiple images",
        "Expected Result (ER)": "Previous/next controls should allow smooth navigation through all product images.",
        "Actual Result": "",
        "Priority": "Medium",
        "Result": "",
        "Comments": ""
    },
    {
        "Test Case ID": "TC_PDP_012",
        "Test Scenario": "TS_026",
        "Test Case Title": "Validate Quantity Selector Functionality",
        "Pre-requisites": "1. Open the Application URL",
        "Test Steps": "1. Search for a product.<br>2. Click on the product from the search results.<br>3. Test the quantity selector with increment/decrement controls.",
        "Test Data": "Product Name: Wireless Headphones",
        "Expected Result (ER)": "Input field with increment/decrement controls should work correctly and validate stock availability.",
        "Actual Result": "",
        "Priority": "High",
        "Result": "",
        "Comments": ""
    },
    {
        "Test Case ID": "TC_PDP_013",
        "Test Scenario": "TS_026",
        "Test Case Title": "Validate Add to Cart Button Functionality",
        "Pre-requisites": "1. Open the Application URL",
        "Test Steps": "1. Search for a product.<br>2. Click on the product from the search results.<br>3. Select quantity and click 'Add to Cart' button.",
        "Test Data": "Product Name: Wireless Headphones, Quantity: 2",
        "Expected Result (ER)": "Product should be added to cart successfully with loading states displayed during processing.",
        "Actual Result": "",
        "Priority": "High",
        "Result": "",
        "Comments": ""
    },
    {
        "Test Case ID": "TC_PDP_014",
        "Test Scenario": "TS_026",
        "Test Case Title": "Validate Add to Wishlist Functionality",
        "Pre-requisites": "1. Open the Application URL<br>2. User should be logged in",
        "Test Steps": "1. Search for a product.<br>2. Click on the product from the search results.<br>3. Click on 'Add to Wishlist' button.",
        "Test Data": "Product Name: Wireless Headphones",
        "Expected Result (ER)": "Product should be saved to wishlist with proper save for later functionality.",
        "Actual Result": "",
        "Priority": "Medium",
        "Result": "",
        "Comments": ""
    },
    {
        "Test Case ID": "TC_PDP_015",
        "Test Scenario": "TS_026",
        "Test Case Title": "Validate Product Comparison Functionality",
        "Pre-requisites": "1. Open the Application URL",
        "Test Steps": "1. Search for a product.<br>2. Click on the product from the search results.<br>3. Click on 'Add to Compare' option.",
        "Test Data": "Product Name: Wireless Headphones",
        "Expected Result (ER)": "Product should be added to comparison list for side-by-side evaluation with similar products.",
        "Actual Result": "",
        "Priority": "Medium",
        "Result": "",
        "Comments": ""
    },
    {
        "Test Case ID": "TC_PDP_016",
        "Test Scenario": "TS_026",
        "Test Case Title": "Validate Social Share Options",
        "Pre-requisites": "1. Open the Application URL",
        "Test Steps": "1. Search for a product.<br>2. Click on the product from the search results.<br>3. Test social media sharing buttons.",
        "Test Data": "Product Name: Wireless Headphones",
        "Expected Result (ER)": "Social media sharing buttons should function correctly and open appropriate sharing dialogs.",
        "Actual Result": "",
        "Priority": "Low",
        "Result": "",
        "Comments": ""
    },
    {
        "Test Case ID": "TC_PDP_017",
        "Test Scenario": "TS_026",
        "Test Case Title": "Validate Print Product Functionality",
        "Pre-requisites": "1. Open the Application URL",
        "Test Steps": "1. Search for a product.<br>2. Click on the product from the search results.<br>3. Click on 'Print Product' option.",
        "Test Data": "Product Name: Wireless Headphones",
        "Expected Result (ER)": "Printer-friendly product information should be generated correctly.",
        "Actual Result": "",
        "Priority": "Low",
        "Result": "",
        "Comments": ""
    },
    {
        "Test Case ID": "TC_PDP_018",
        "Test Scenario": "TS_027",
        "Test Case Title": "Validate Product Rating System Display",
        "Pre-requisites": "1. Open the Application URL",
        "Test Steps": "1. Search for a product.<br>2. Click on the product from the search results.<br>3. Check the product rating system display.",
        "Test Data": "Product Name: Gaming Laptop",
        "Expected Result (ER)": "5-star rating display with average scores should be shown correctly.",
        "Actual Result": "",
        "Priority": "Medium",
        "Result": "",
        "Comments": ""
    },
    {
        "Test Case ID": "TC_PDP_019",
        "Test Scenario": "TS_027",
        "Test Case Title": "Validate Customer Reviews Display",
        "Pre-requisites": "1. Open the Application URL",
        "Test Steps": "1. Search for a product.<br>2. Click on the product from the search results.<br>3. Check the customer reviews section.",
        "Test Data": "Product Name: Gaming Laptop",
        "Expected Result (ER)": "User-generated product feedback and comments should be displayed with proper formatting.",
        "Actual Result": "",
        "Priority": "Medium",
        "Result": "",
        "Comments": ""
    },
    {
        "Test Case ID": "TC_PDP_020",
        "Test Scenario": "TS_027",
        "Test Case Title": "Validate Q&A Section Functionality",
        "Pre-requisites": "1. Open the Application URL",
        "Test Steps": "1. Search for a product.<br>2. Click on the product from the search results.<br>3. Check the Q&A section for customer questions and merchant responses.",
        "Test Data": "Product Name: Gaming Laptop",
        "Expected Result (ER)": "Customer questions and merchant responses should be displayed in an organized format.",
        "Actual Result": "",
        "Priority": "Medium",
        "Result": "",
        "Comments": ""
    },
    {
        "Test Case ID": "TC_PDP_021",
        "Test Scenario": "TS_027",
        "Test Case Title": "Validate Recently Viewed Products",
        "Pre-requisites": "1. Open the Application URL<br>2. Browse multiple products",
        "Test Steps": "1. Search for and view multiple products.<br>2. Go to any product detail page.<br>3. Check the recently viewed products section.",
        "Test Data": "Previously viewed products: Laptop, Phone, Headphones",
        "Expected Result (ER)": "Products previously browsed by the customer should be displayed correctly.",
        "Actual Result": "",
        "Priority": "Low",
        "Result": "",
        "Comments": ""
    },
    {
        "Test Case ID": "TC_PDP_022",
        "Test Scenario": "TS_028",
        "Test Case Title": "Validate Description Tab Content",
        "Pre-requisites": "1. Open the Application URL",
        "Test Steps": "1. Search for a product.<br>2. Click on the product from the search results.<br>3. Click on the Description tab and verify content.",
        "Test Data": "Product Name: Smart TV",
        "Expected Result (ER)": "Comprehensive product descriptions and features should be displayed without formatting errors.",
        "Actual Result": "",
        "Priority": "High",
        "Result": "",
        "Comments": ""
    },
    {
        "Test Case ID": "TC_PDP_023",
        "Test Scenario": "TS_028",
        "Test Case Title": "Validate Specifications Tab Content",
        "Pre-requisites": "1. Open the Application URL",
        "Test Steps": "1. Search for a product.<br>2. Click on the product from the search results.<br>3. Click on the Specifications tab and verify technical details.",
        "Test Data": "Product Name: Smart TV",
        "Expected Result (ER)": "Technical details and product attributes should be displayed in a structured format.",
        "Actual Result": "",
        "Priority": "High",
        "Result": "",
        "Comments": ""
    },
    {
        "Test Case ID": "TC_PDP_024",
        "Test Scenario": "TS_028",
        "Test Case Title": "Validate Reviews Tab Functionality",
        "Pre-requisites": "1. Open the Application URL",
        "Test Steps": "1. Search for a product.<br>2. Click on the product from the search results.<br>3. Click on the Reviews tab and check customer feedback.",
        "Test Data": "Product Name: Smart TV",
        "Expected Result (ER)": "Customer feedback and rating submission interface should function correctly.",
        "Actual Result": "",
        "Priority": "Medium",
        "Result": "",
        "Comments": ""
    },
    {
        "Test Case ID": "TC_PDP_025",
        "Test Scenario": "TS_028",
        "Test Case Title": "Validate Shipping Tab Information",
        "Pre-requisites": "1. Open the Application URL",
        "Test Steps": "1. Search for a product.<br>2. Click on the product from the search results.<br>3. Click on the Shipping tab and verify delivery information.",
        "Test Data": "Product Name: Smart TV",
        "Expected Result (ER)": "Delivery information and estimated arrival times should be displayed accurately.",
        "Actual Result": "",
        "Priority": "Medium",
        "Result": "",
        "Comments": ""
    },
    {
        "Test Case ID": "TC_PDP_026",
        "Test Scenario": "TS_028",
        "Test Case Title": "Validate Return Policy Tab",
        "Pre-requisites": "1. Open the Application URL",
        "Test Steps": "1. Search for a product.<br>2. Click on the product from the search results.<br>3. Click on the Return Policy tab and verify exchange/refund information.",
        "Test Data": "Product Name: Smart TV",
        "Expected Result (ER)": "Exchange and refund information should be clearly displayed and easy to understand.",
        "Actual Result": "",
        "Priority": "Medium",
        "Result": "",
        "Comments": ""
    }
]

for case in test_cases:
    row = [
        case.get("Test Case ID", ""),
        case.get("Test Scenario", ""),
        case.get("Test Case Title", ""),
        case.get("Pre-requisites", ""),
        case.get("Test Steps", ""),
        case.get("Test Data", ""),
        case.get("Expected Result", ""),
        case.get("Actual Result", ""),
        case.get("Priority", ""),
        case.get("Result", ""),
        case.get("Comments", "")
    ]
    ws.append(row)

wb.save("PrestaShop_Product_Display_Test_Cases.xlsx")
print("Excel file created successfully!")
