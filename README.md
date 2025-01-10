# Data Science University Project 🎓
###### This is a documentation regarding the project I've created. This project was developed as part of a Data Science learning journey.
###### It reflects a combination of technical skills and practical applications to solve real-world data challenges.

## Table of contents

 - [Project Overview](#project-overview)
 - [Features](#features)
 - [Technologies](#technologies)
 - [Installation](#installation)
 - [Usage](#usage)
 - [Project Structure](#project-structure)


### Project Overview

This Python project automates the process of extracting product data from an e-commerce website, organizing it into a structured format, and visualizing the results. 
Using web scraping techniques powered by Selenium, it retrieves product names and prices from a given webpage. 
The project includes an intuitive GUI built with Tkinter, allowing users to interact with the data seamlessly.


![1](https://github.com/user-attachments/assets/848fb441-292a-4bf9-b4a1-cd12d9e3982f)


### Features

- User-Friendly GUI: Provides a Tkinter-based graphical user interface with buttons for data retrieval, visualization, and saving.
- Data Retrieval: Extracts product names and prices in real-time from an e-commerce website using Selenium.
- Data Organization: Structures the retrieved data into a pandas DataFrame for easy manipulation and analysis.
- Visualization: Generates a horizontal bar chart of product prices for quick insights into pricing.
- Matrix View: Displays the product and price data in a clear tabular format directly in the console.
- File Export: Allows users to save the organized data into an Excel file for offline use, formatted for readability.

### Technologies

1. Programming Language: Python *3.8 or later*
2. Libraries:
      - **Tkinter** *built-in* (for GUI design)
      - **Selenium** *4.27.1* (for automating web-based tasks such as web scraping)
      - **webdriver-manager** *4.0.* (for managing browser drivers required by Selenium)
      - **pandas** *2.2.3* (for data manipulation and analysis)
      - **matplotlib** *3.10.0* (for data visualization)
      - **openpyxl** *3.1.5* (for reading, writing, and modifying Excel files)
  

### Installation

OPTIONAL: Git installed on your machine (optional, for cloning the repository).

1. Clone the repository: **https://github.com/IuliaSapungiu/Data_Science.git**
2. Navigate to the project directory: **cd Data_Science**
3. Create a virtual environment: **python -m venv env_name**
4. Activate the virtual environment:

    - **On Windows:**
  
      ```
      source env_name\Scripts\activate
      ```

    - **On macOS and Linux:**

      ```
      source env_name/bin/activate
      ```


5. Install the required dependencies:

      ```
      pip install -r requirements.txt
      ```

6. Run the project:
    ```
    python PROJECT_IMS.py  
    ```

### Usage

1.  Click the "Retrieve Data" button in the GUI to scrape product details.

       ![2](https://github.com/user-attachments/assets/3d9f635b-d118-4b93-8bfb-31dc179fb2f8)

2. Click on "Open Chart" button to display product prices and names on a bar chart.
   
      ![3](https://github.com/user-attachments/assets/7d0340e9-e8a8-4db6-817c-1a7b8b4b3758)

3. Click on "Open Matrix" button to view organized products data in matrix form.

      ![4](https://github.com/user-attachments/assets/363e458d-d0ae-4d46-8948-bdabf437dd6e)

4. Click on "Open File" button to save the extracted data as an Excel file with the specified file name in the white text box.

      ![5](https://github.com/user-attachments/assets/90e1b3e7-c9fe-499f-9e28-4fa2f5d5115a)

After pressing each button, you can notice that the color changes if the operation succeeded.


### Project Structure

```
Data_Science/  
├── data.csv/
├── data.xlsx/                  
├── PROJECT_IMS.py/                
└── requirements.txt 
```
