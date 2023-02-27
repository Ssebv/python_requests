from bs4 import BeautifulSoup  # Import BeautifulSoup for parsing HTML
import requests  # Import requests for making an HTTP request
import csv  # Import csv for writing extracted data to a CSV file

# Get the HTML content of the website
source = requests.get('http://coreyms.com').text

# Create a 'soup' object from the HTML content
soup = BeautifulSoup(source, 'lxml')

# Create a CSV file in write mode and a 'csv_writer' object to write to it
csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)

# Write a header row to the CSV file
csv_writer.writerow(['headline', 'summary', 'video_link'])

# Iterate through each article on the webpage
for article in soup.find_all('article'):
    
    # Get the headline and summary of the article
    headline = article.h2.a.text
    summary = article.find('div', class_='entry-content').p.text

    # Try to get the YouTube video URL and create a link to it
    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4].split('?')[0]
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    # Write a row to the CSV file with the headline, summary, and video link (if it exists)
    csv_writer.writerow([headline, summary, yt_link])

# Close the CSV file
csv_file.close()