import requests
from bs4 import BeautifulSoup


def monitor_gas_prices():
    # Perform web scraping
    url = 'https://www.peco-online.ro/index_en.php'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    # Extract gas station names and prices
    gas_stations = soup.find_all('div', class_='postare2')
    print(gas_stations)
    # Filter gas stations
    relevant_gas_stations = []
    for station in gas_stations:
        station_name = station.find('span', class_='titlu')
        if station_name.text.strip() in ['Petrom', 'OMV', 'Lukoil', 'MOL', 'RomPetrol']:
            relevant_gas_stations.append(station)
    print(relevant_gas_stations)


import requests
from bs4 import BeautifulSoup


def get_petrom_prices(url):
    # Fetch the HTML content of the webpage
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the tables containing gasoline and diesel prices
        tables = soup.find_all('table')

        # Initialize dictionaries to store gasoline and diesel prices
        gasoline_prices = {}
        diesel_prices = {}
        diesel_premium_prices = {}
        gasoline_premium_prices = {}
        LPG_prices = {}
        # Loop through each table
        for table in tables:
            # Find the table header containing the station name
            header = table.find('thead').find('tr').find('th')
            station_name = header.text.strip()


            #print(table)
            #print("+++++++++++++++++++")


            # Check if the station name contains "Petrom" to identify the desired station
            # Find all rows in the table body
            rows = table.find('tbody').find_all('tr')

            # Extract gasoline and diesel prices from each row
            for row in rows:
                columns = row.find_all('td')
                station_name = columns[0].text.strip()
                benzin_standard = columns[1].text.strip()
                diesel_standard  = columns[2].text.strip()
                lpg = columns[3].text.strip()
                benzin_premium = columns[4].text.strip()
                diesel_premium = columns[5].text.strip()
                gasoline_prices[station_name] = benzin_standard
                diesel_prices[station_name] = diesel_standard
                diesel_premium_prices[station_name] = diesel_premium
                gasoline_premium_prices[station_name] = gasoline_premium_prices
                LPG_prices[station_name] = LPG_prices
                # Check if the fuel type is gasoline or diesel
                #if "A95" in fuel_type.lower():
                #    gasoline_prices[station_name] = price
                #elif "Diesel" in fuel_type.lower():
                 #   diesel_prices[station_name] = price

        return gasoline_prices, diesel_prices, gasoline_premium_prices, diesel_premium_prices, LPG_prices
    else:
        # If the request was not successful, print an error message
        print("Failed to fetch webpage")


