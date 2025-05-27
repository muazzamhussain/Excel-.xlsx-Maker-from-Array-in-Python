````markdown
 🧪 PrestaShop Product Display Page – Test Case Excel Generator

This Python script creates a structured Excel file containing formal test cases for the **Product Display Page (PDP)** of a PrestaShop-based e-commerce website.

 📄 Features

- Generates an Excel file (`.xlsx`) with detailed test cases.
- Follows a formal QA testing format with fields like:
  - Test Case ID
  - Test Scenario
  - Test Case Title
  - Pre-requisites
  - Test Steps
  - Test Data
  - Expected Result
  - Actual Result
  - Priority
  - Result
  - Comments

 📦 Requirements

- Python 3.x
- `openpyxl` package

To install dependencies:

pip install openpyxl
````

## 🚀 How to Use

1. Clone or download the repository containing `script.py`.
2. Add or update test cases inside the `test_cases` list in the script.
3. Run the script:

```bash
python script.py
```

4. A file named `PrestaShop_Product_Display_Test_Cases.xlsx` will be created in the same directory.

## 📝 Example Output

An Excel sheet will be created with rows like:

| Test Case ID | Test Scenario             | Test Case Title                                         | Pre-requisites       | Test Steps        | Test Data     | Expected Result                              | Actual Result  | Priority | Result | Comments |
| ------------ | ------------------------- | ------------------------------------------------------- | -------------------- | ----------------- | ------------- | -------------------------------------------- | -------------- | -------- | ------ | -------- |
| TC\_PDP\_001 | (TS\_007) Product Display | Validate product thumbnails on the Product Display Page | Open application URL | Steps to open PDP | Product: iMac | Thumbnails and lightbox function as expected | (to be filled) | High     |        |          |

## ✅ Notes

* You can expand the `test_cases` list with additional dictionaries to include more test cases.
* Supports multi-line test steps and expected results using triple quotes.

## 📁 Output File

* **Filename**: `PrestaShop_Product_Display_Test_Cases.xlsx`
* **Sheet Title**: `PrestaShop Test Cases`

---

### 📬 Contact

For improvements or issues, feel free to open a pull request or contact.
