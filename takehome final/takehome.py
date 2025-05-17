import requests
import xmltodict
import json
import random
import threading
import datetime
from datetime import datetime, timedelta
import os

rates = ["EUR", "GBP", "USD", "DZD", "AUD", "BWP", "BND", "CAD", "CLP", "CNY", "COP", "CZK", "DKK", "HUF", "ISK", "INR", "IDR", "ILS", "KZT", "KRW", "KWD", "LYD", "MYR", "MUR", "NPR", "NZD", "NOK", "OMR", "PKR", "PLN", "QAR", "RUB", "SAR", "SGD", "ZAR", "LKR", "SEK", "CHF", "THB", "TTD"]
ratesForBase = [r for r in rates if r != "USD" and r != "EUR" and r != "GBP"]

def pulldata(base, date):
    
    directories = f"currency_data//{base}"
    os.makedirs(directories, exist_ok=True)

    # URL of the XML data
    url = f"https://www.floatrates.com/historical-exchange-rates.html?operation=rates&pb_id=1775&page=historical&currency_date={date}&base_currency_code={base}&format_type=xml"
    # print(url)
    # Fetch the XML data
    response = requests.get(url)
    response.raise_for_status()  # Ensure we notice bad responses

    try:
        # Parse the XML data to a Python dictionary
        data_dict = xmltodict.parse(response.text)

        # Convert the dictionary to a JSON string
        json_data = json.dumps(data_dict, indent=4)

        # Print the JSON data
        # print(json_data)

        # Optionally, write the JSON data to a file
        with open(f"{directories}//{date}_exchange_rates_{base}.json", 'w') as json_file:
            json_file.write(json_data)
    except Exception:
        print(url)
        return 

def sewingmachine(base, date): #get it, threads hehe
    threadsPool.acquire()
    # print(f"Thread {base} is starting")
    pulldata(base,date)
    # print(f"Thread {base}: finishing")
    threadsPool.release()

def increment_date(startdate, enddate):
    startobject = datetime.strptime(startdate, "%Y-%m-%d")
    endobject = datetime.strptime(enddate, "%Y-%m-%d")
    dates = []
    currentdate = startobject
    while currentdate <= endobject:
        dates.append(currentdate.strftime("%Y-%m-%d"))
        currentdate += timedelta(days=1)
    
    return dates

if __name__ == "__main__":
    
    max_threads = 1000
    threadsPool = threading.Semaphore(max_threads)

    date = "2011-05-04"
    bases = random.sample(ratesForBase, 5)

    for base in bases:
        # pulldata(base, date)
        #daylist = increment_date(date, today)

        threads = []
        for x in increment_date(date, "2025-05-16"):
            thread = threading.Thread(target=sewingmachine, args=(base,x,))
            threads.append(thread)
            thread.start()

    #for day in daylist:
    #    pulldata(base, day)