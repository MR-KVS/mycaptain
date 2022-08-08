import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect

parser = argparse.ArgumentParser()
parser.add_argument("--page_num_max",help= "enter the number of pages to oarse",type = int)
parser.add_argument("--dbname",help = "enter the name of db",type=str)
args = parser.parse_args()

oyo_url = "https://www.oyorooms.com/search?location=Bangalore%2C%20Karnataka%2C%20India&city=Bangalore&searchType=city&checkin=08%2F08%2F2022&checkout=09%2F08%2F2022&roomConfig%5B%5D=2&guests=2&rooms=1&filters%5Bcity_id%5D=4"
page_num_MAX = args.page_num_max 
scraped_info_list = []
connect.connect(args.dbname)

for page_num in range(1,page_num_MAX):
    url= oyo_url + str(page_num)
    print("GET request for:" +url)
    req = requests.get(url)
    content = req.content
    
    soup = BeautifulSoup(content,"html.parser")
    all_hotels = soup.find_all("div" , {"class":"hotelcardllisting"})
    
    for hotel in all_hotels:
        hotel_dict = {}
        hotel_dict["name"] = hotel.find("h3",{"class":"listinghotelDescription_hotelName"}).text
        hotel_dict["address"] = hotel.find("span",{"itemprop":"streetAddress"}).text
        hotel_dict["price"] = hotel.find("span",{"class":"listingPrice__ratingsummary"}).text
        try:
            hotel_dict["rating"]= hotel.find("span",{"class":"hotelrating_ratingsummary"}).text
        except AttributeError:
            pass
        
        parent_amenities_element = hotel.find("div",{"class":"amenitiyWrapper"})
            
        amenities_list=[]
        for amenity in parent_amenities_element.find_all("div",{"class":"ammenityWrapper__amenity"}):
            amenities_list.append(amenity.find("span",{"class": "d-body-sm"}).text.strip())
            
        hotel_dict["amenities"] = ','.join(amenities_list[:-1])
       
        scraped_info_list.append(hotel_dict)
        connect.insert_into_table(args.dbname)
        connect.get_hotel_info(args.dbname)
       
            
            
        
        