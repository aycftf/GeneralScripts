

#refresher and testing public web scraping w/ scapy and asyinco

import asyncio, aiohttp, requests
import json
from urllib.parse import urlparse
import scrapy, timeit
import sys, xmltojson, os



#Goal: Use classes, and oop for general strucure for web scraper
#Goal#2: Use different http/https req methods to get data and read/format
#Goal-3: Execute different requests and processes at same time w asynio


#class oopscrape(self):
#    def scrapeme():
#        pass
    
    

LINK = "https://en.wikipedia.org/wiki/Dog"
async def testfunc():
    current_dir = os.getcwd()
    filetocheck = "sample.txt"
    headerss = {
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 5.1.1; pt-br; SM-J105B Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3'
    }
    async with aiohttp.ClientSession() as sesh:
        try:
            
            async with sesh.get(url=LINK, headers=headerss) as res:
                data = await res.text()
                checkpath = os.path.join(current_dir, filetocheck)
                
                if data != None:
                    if not os.path.exists(checkpath):  
                        with open ("sample.txt", "w", encoding='utf-8') as samp:
                            samp.write(data)
                
                    else:
                        sys.exit("file already exists!")
                
        except aiohttp.ClientConnectionError as ef:
            sys.exit(f"RE TRY YOUR LINK {ef}")
            
            
asyncio.run(testfunc())


TESTME = [77, 8, 6, 24, 28, 12, "Testtwo324", "Apple", None, 22, 1, 17]

async def task1():
    ints = 0
    strs = 0
    others = 0
    for x in TESTME:
        if isinstance(x, int):
            ints += 1
        elif isinstance(x, str):
            strs += 1
        else:
            others += 1

    return ints, strs, others


#aa = input("Enter two nums: ")
async def task2():
    onlynum = []
    for x in TESTME:
        if isinstance(x, int):
            onlynum.append(x)
    yme = [y for y in onlynum if y % 2 == 0]
    print(f"Even nums out of list: %s"% yme)


async def bothfuncs():
    await asyncio.gather(task1(), task2())

asyncio.run(bothfuncs())
    
    
    



