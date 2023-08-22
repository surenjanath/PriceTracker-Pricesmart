import asyncio
from time import perf_counter
from bs4 import BeautifulSoup as bs
import aiohttp
import pandas as pd
import os
from datetime import datetime as dt
import json
import datetime
import os
from uuid import uuid4

# SQL DATABASE Libraries
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, JSON, DateTime
from sqlalchemy.orm import declarative_base

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

cwd = os.getcwd()

Location = r'ScrapedData'
WorkingDir = os.path.join(cwd, Location)

if os.path.isdir(WorkingDir) :
    pass
else:
    os.mkdir(WorkingDir)

Database = os.path.join(WorkingDir,  'PriceSmart_DATABASE.db')



# # Initialize Method
Base = declarative_base()


# Export Database
db_path        = Database


class PriceTracking(Base):
    __tablename__           = 'PriceTracker'
    id                      = Column(Integer, primary_key=True)
    name                    = Column(String)
    pid                      = Column(String)
    price                   = Column(Float)
    weight                  = Column(Float)
    brand                   = Column(String)
    list                    = Column(String)
    images                  = Column(JSON)
    unitOfMeasureWeight     = Column(String)
    category                = Column(String)

    # Utility Variable
    uniqueId = Column(String)
    date_created = Column(Date)
    last_updated = Column(Date)

    def __init__(self, name, pid, price, weight, brand, list, images, unitOfMeasureWeight, category):

        self.name                  = name
        self.pid                    = pid
        self.price                 = price
        self.weight                = weight
        self.brand                 = brand
        self.list                  = list
        self.images                = images
        self.unitOfMeasureWeight   = unitOfMeasureWeight
        self.category              = category

        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
        if self.date_created is None:
            self.date_created = datetime.datetime.now()


        self.last_updated = datetime.datetime.now()

    def __repr__(self):
        return f"<PriceTracking(pid='{self.pid}')>"


class ErrorLog(Base):
    __tablename__  = 'errorLog'
    id             = Column(Integer, primary_key=True)
    Status         = Column(String)
    Error          = Column(String)
    RunDate        = Column(DateTime)
    NumItems       = Column(Integer)
    TimeTaken      = Column(Float)

    # Utility Variable
    uniqueId = Column(String)
    date_created = Column(Date)
    last_updated = Column(Date)

    def __init__(self, Status, Error,NumItems, TimeTaken):
        self.Status     = Status
        self.Error      = Error
        self.NumItems   = NumItems
        self.TimeTaken  = TimeTaken

        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
        if self.date_created is None:
            self.date_created = datetime.datetime.now()

        self.last_updated = datetime.datetime.now()
        self.RunDate = datetime.datetime.now()

    def __repr__(self):
        return f"<ErrorLog(RunDate='{self.RunDate}')>"



############################################
#               FUNCTIONS
############################################

def add_to_db(session, price_tracking_records):
    price_tracking_objects = [PriceTracking(**record) for record in price_tracking_records]
    session.add_all(price_tracking_objects)
    session.commit()
    print('[*] Added to Database ')
    print(f'[*] Number of Items added : {len(price_tracking_objects)}')
    session.commit()
    return


def add_to_ErrorLog(session, ERROR):
    ErrorLogging = [ErrorLog(**record) for record in ERROR]
    session.add_all(ErrorLogging)
    session.commit()
    print('[*] Added Status ')
    session.commit()
    return

def parseData(soup, url):
    impressions = []
    try:

        try:
            data = json.loads(str(soup.find_all('div', {'id':'container-category-result'})[0].find('script'))[48:-55].strip().replace('\\\\','\\').replace('\\"','"').replace('\\x3C','<').replace('\\\'',"'"))
        except Exception as e:
            # print(soup.find('div', {'id':'container-category-result'}).find_all('script'))
            print(soup)

            print(f'[*] Soomething Wrong With Page itself : {e} on {url}')


        items = data['response']['docs']
        if len(items)>0:
            for i in range(len(items)):
                product = items[i]



                try:
                    cat = product['attr_crumbs'][-1]
                except : cat = None

                try:
                    prod = product['attr_crumbs'][0]
                except : prod = None

                try:
                    imgs = [image['path'] for image in product['images']['imageGroup'][0]['image']]
                except : imgs = []

                product_impression = {
                    'name': product['title'],
                    'pid': product['pid'],
                    'price': product['productPricing']['listPrice'],
                    'weight': product['productPricing']['weight'],
                    'brand': product['brand'],
                    'category': cat,
                    'list': prod,
                    'images' : imgs,
                    'unitOfMeasureWeight': product['unitOfMeasureWeight'],
                }
                impressions.append(product_impression)
    except Exception as e:
        print(f'[*] Error Occurred  : {e}')
    return impressions

class WebScraper(object):
    def __init__(self, urls):
        self.urls = urls
        # Global Place To Store The Data:
        self.all_data  = []
        self.ParsedData = []
        self.master_dict = {}
        # Run The Scraper:
        asyncio.run(self.main())

    async def fetch(self, session, url):

        try:
            async with session.get(url) as response:
                # 1. Extracting the Text:
                text = await response.text()
                # 2. Extracting the  Tag:
                title_tag = await self.extract_Data(text, url)
                return text, url, title_tag
        except IndentationError as e:
            print(str(e))

    async def extract_Data(self, text, url):
        try:
            soup = bs(text, 'html.parser')
            dictionary_data = parseData(soup,url)

            return dictionary_data
        except IndentationError as e:
            print(str(e))

    async def main(self):
        tasks = []
        headers = {

            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Cookie': 'userPreferences=country=tt&lang=en&selectedClub=8001;',
            'Host': 'www.pricesmart.com',
            'Referer': 'https://www.pricesmart.com',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            }
        async with aiohttp.ClientSession() as session:
            for url in self.urls:

                tasks.append(self.fetch(session, url))

            htmls = await asyncio.gather(*tasks)
            self.all_data.extend(htmls)

            # Storing the raw HTML data.
            for html in htmls:

                if html is not None:
                    url = html[1]
                    self.master_dict['data'] = {'Raw Html': html[0], 'Results': html[2]}
                    self.ParsedData.extend(html[2])
                else:
                    continue

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

pages = range(1,100)
cat = 'G10D03'
amt = 12
start = perf_counter()

engine = create_engine(f'sqlite:///{Database}',  echo=False) # Echo = True means that it shows the logs
Base.metadata.create_all(engine)

# # Create a session
Session = sessionmaker(bind=engine)
session = Session()

try:

    datenow = dt.now().ctime().replace(" ",'').replace(':','')
    urls = [f'https://pricesmart.com/site/tt/en/category/groceries?cat={cat}&r127_r1_r3_r1:page={page}&r127_r1_r3_r1:_sps={amt}' for page in pages]
    scraper = WebScraper(urls = urls)
    stop = perf_counter()
    print("[*] Time taken : ", stop - start)

    print('[*] Length of Data Gathered : ', len(scraper.ParsedData))
    ExportPath = os.path.join(os.getcwd(),'Results')
    EXPORTPATH = os.path.join(ExportPath, f'{datenow}_{cat}_Data.xlsx')
    pd.DataFrame(scraper.ParsedData).to_excel(EXPORTPATH)

    price_tracking_records = scraper.ParsedData
    add_to_ErrorLog(session, [{
    'Status' : 'Scraped Successfully',
    'Error' : '',
    'NumItems' : len(scraper.ParsedData),
    'TimeTaken' : stop - start,
    }])

except Exception as e:
    try:stop = perf_counter()
    except:stop = 0
    session.rollback()
    add_to_ErrorLog(session, [{
    'Status' : 'Scraped Failed',
    'Error' : f'Error : {e}',
    'NumItems' : 0,
    'TimeTaken' : stop - start,
    }])
    price_tracking_records = []

try:
    if len(price_tracking_records) > 0:

        add_to_db(session, price_tracking_records)
        session.close()
        print('[*] PROGRAM ENDED')
        print('*'*50)
    else:
        pass

except Exception as e:
    print('*'*100)
    print(f'Error Occured : {e}')
    print('*'*100)