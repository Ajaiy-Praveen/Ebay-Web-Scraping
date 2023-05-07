
# Web Scraping eBay for Amazon Gift Card Data

Overview
This project involves web scraping eBay's website to gather data on sold Amazon gift cards. The project involves several steps including navigating the website, identifying URL variables, parsing HTML data, and using RegEx to extract relevant data. The data gathered includes the title, price, and shipping price of each item, as well as an analysis of whether the gift card sold above face value.

Requirements
Python (3.6 or later)
BeautifulSoup4

Instructions

Clone the repository to your local machine.
Install the required dependencies.
Run the ebay_gift_card_scraper.py file in your Python IDE.
The script will automatically navigate to eBay's website and begin scraping data.
The data will be saved to individual HTML files named "amazon_gift_card_XX.htm", where XX represents the page number.
After scraping is complete, the script will parse the HTML data and print relevant information to the console.

Conclusion
This project demonstrates the power of web scraping for data collection and analysis. By utilizing Python and several libraries, we were able to automate the process of gathering and analyzing data from eBay's website. This information can be used to make informed purchasing decisions and gain insights into consumer behavior.
