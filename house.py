import requests
from bs4 import BeautifulSoup
import csv
import time

page_list=list(range(1,24))

file = open('house_price.csv','w')
write_csv = csv.writer(file)
write_csv.writerow(['num_bedroom','location','bedroom_width','bedroom_height',
                    'bathroom_width','bathroom_height','garage_width','garage_height','erf_size',
                    'room_floor_size','bath_amenities','car_parks','price'])

for i, page_number in enumerate (page_list):

    if page_number == 1:
        url = 'https://www.property24.com/houses-for-sale/alias/cape-town-city/19/western-cape/9#'
    else:
        url = f'https://www.property24.com/houses-for-sale/alias/cape-town-city/19/western-cape/9/p{page_number}'

    time.sleep(5)

    data = requests.get(url).text
    page = BeautifulSoup(data,'lxml')

    all_features = page.find_all('span', class_='p24_content')

    for feature in all_features:

        try:
            price = feature.find('span', class_='p24_price').text
        except:
            price = None

        try:
            num_bedroom = feature.find('span', {'class':'p24_featureDetails', 'title':'Bedrooms'}).find('span').text
        except:
            num_bedroom = None

        try:
            location = feature.find('span', class_='p24_location').text
        except:
            location = None

        try:
            bedroom_width = feature.find('span', class_='p24_icons').find('span', {'class':'p24_featureDetails', 'title':'Bedrooms'}).find('svg').get('width')
        except:
            bedroom_width = None

        try:
            bedroom_height = feature.find('span', class_='p24_icons').find('span', {'class':'p24_featureDetails', 'title':'Bedrooms'}).find('svg').get('height')
        except:
            bedroom_height = None

        try:
            bathroom_width = feature.find('span', class_='p24_icons').find('span', {'class':'p24_featureDetails', 'title':'Bathrooms'}).find('svg').get('width')
        except:
            bathroom_width = None

        try:
            bathroom_height = feature.find('span', class_='p24_icons').find('span', {'class':'p24_featureDetails', 'title':'Bathrooms'}).find('svg').get('height')
        except:
            bathroom_height = None

        try:
            garage_width = feature.find('span', class_='p24_icons').find('span', {'class':'p24_featureDetails', 'title':'Parking Spaces'}).find('svg').get('width')
        except:
            garage_width = None

        try:
            garage_height = feature.find('span', class_='p24_icons').find('span', {'class':'p24_featureDetails', 'title':'Parking Spaces'}).find('svg').get('height')
        except:
            garage_height = None

        try:
            erf_size = feature.find('span', class_='p24_icons').find('span', {'class':'p24_size', 'title':'Erf Size'}).find('span').text
        except:
            erf_size = None

        write_csv.writerow([num_bedroom,location,bedroom_width,
                            bedroom_height,bathroom_width,bathroom_height,
                            garage_width,garage_height,erf_size,None,None,None,price])

        print("retrieving next 1 xxxxxx")

#file.close()

site2_pages = list(range(1,105))

file2 = open('house_price2.csv', 'w')
writer_csv = csv.writer(file2)
writer_csv.writerow(['num_bedroom','location','bedroom_width','bedroom_height',
                    'bathroom_width','bathroom_height','garage_width','garage_height','erf_size',
                    'room_floor_size','bath_amenities','car_parks','price'])

for k, val in enumerate(site2_pages):
    if val == 1:
        url2 = 'http://www.remax.co.za/property/for-sale/south-africa/western-cape/cape-town/'
    else:
        url2 = f'http://www.remax.co.za/property/for-sale/south-africa/western-cape/cape-town/?page={val}'

    time.sleep(5)

    site2 = requests.get(url2).text
    web_page = BeautifulSoup(site2,'lxml')
    props = web_page.find_all('div', class_='property-card-info')

    for item in props:

        try:
            price = item.find('div', class_='property-card-info__price').find('span').text
        except:
            price = None

        try:
            num_bedroom = item.find('div',class_='property-card-info__icons').find('span', itemprop='numberOfRooms').text
        except:
            num_bedroom = None

        try:
            bath_amenities = item.find('div', class_='property-card-info__icons').find('span',itemprop='amenityFeature').text
        except:
            bath_amenities = None

        try:
            car_parks = item.find('div', class_='property-card-info__icons').find('span', itemprop='amenityFeature').text
        except:
            car_parks = None

        try:
            room_floor_size = item.find('div', class_='property-car-info__icons').find('span', itemprop='floorSize').text
        except:
            room_floor_size = None

        try:
            house_area = item.find('div', class_='property-card-info__icons').find('span').text
        except:
            house_area = None

        try:
            location = item.find('div', {'class':'property-card-info__address', 'itemprop':'address'}).text
        except:
            location = None

        writer_csv.writerow([num_bedroom,location,None,None,None,None,None,None,
                            house_area,room_floor_size,bath_amenities,car_parks,price])

        print("retrieving next 2 xxxxxx")
#file2.close()
