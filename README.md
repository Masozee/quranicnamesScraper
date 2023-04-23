
# Quranic Names Scraper

This Python script scrapes the website https://quranicnames.com/girls/ to extract the URLs of each name and their details, and saves the data to two CSV files: "list_url.csv" and "detail_data.csv".

## Requirements

- Python 3.x
- Requests library (`pip install requests`)
- BeautifulSoup library (`pip install beautifulsoup4`)
- tqdm library (`pip install tqdm`)

## Usage

1. Clone or download the repository to your local machine.
2. Open a command prompt or terminal window and navigate to the directory containing the Python script.
3. Run the script using the following command: `python quranic_names_scraper.py`
4. Wait for the script to finish running. The extracted URLs and data will be saved to the "list_url.csv" and "detail_data.csv" files respectively.

## Output

### list_url.csv

This file contains a single column with the URLs of each name extracted from the website https://quranicnames.com/girls/.

### detail_data.csv

This file contains the following columns:

- `Name`: The name of the person.
- `Arabic Name`: The name in Arabic script.
- `Variant`: List of other variations for the name.
- `Content`: A short description of the meaning of the name.

## Disclaimer

This script is for educational purposes only. Use it at your own risk. The author is not responsible for any misuse or damage caused by this script.
