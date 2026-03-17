# 📰 BBC News Web Scraper mini project 1

This project is a simple and efficient **web scraping tool** built using Python.  
It extracts the latest news headlines from the BBC News website and stores them in a structured CSV file for further analysis.

## 🚀 Project Objective

The goal of this project is to:

- Extract live news headlines from BBC News
- Clean and structure the scraped data
- Store results in CSV format
- Demonstrate practical web scraping skills using Python

## 🛠 Technologies Used

- Python
- Requests
- BeautifulSoup (bs4)
- Pandas

## 📌 How It Works

1. Sends an HTTP request to the BBC News homepage
2. Parses the HTML content using BeautifulSoup
3. Extracts article titles and links
4. Removes duplicate entries
5. Saves the data to a CSV file


## 📂 Repository Structure
├── bbc_scraper.py

├── bbc_headlines.csv

└── README.md

## 🧩 Code Overview

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

requests → Fetches webpage content

BeautifulSoup → Parses HTML

pandas → Structures and exports data

The script filters anchor tags containing /news in their URL to collect relevant BBC News articles.

📊 Output

The scraped data is saved as:

bbc_headlines.csv

Columns include:

Title

Date (currently set as "N/A")

Link

▶ How to Run

Install required libraries:

pip install requests beautifulsoup4 pandas

Run the script:

python bbc_scraper.py

Output CSV file will be generated automatically.

📈 Skills Demonstrated

Web scraping fundamentals

HTML parsing

Data cleaning (duplicate removal)

Data export using Pandas

Automation scripting

⚠ Note

This scraper is for educational purposes only.
Always respect website terms of service and robots.txt policies when scraping websites.

🏁 Conclusion

This project demonstrates practical skills in data extraction and automation.
The extracted data can be further used for:

News trend analysis

Sentiment analysis

NLP projects

AI-based news classification
