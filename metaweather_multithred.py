#Last updated: 11/03/2021 5:12PM MST

import threading, requests, time

start = time.time()

SLC_woeid = str(2487610)
LA_woeid = str(2442047)
BOISE_woeid = str(2366355)

URL = 'https://www.metaweather.com/api/location/'
woeid_dict = {URL + SLC_woeid: 'Salt Lake City',
              URL + LA_woeid: 'Los Angeles',
              URL + BOISE_woeid: 'Boise' }
urls = []

for item in woeid_dict.items():
    urls.append(item[0])

def find_in_dict(value, dict):
    return dict.get(value)

def fetch_url(url):
    response = requests.get(url)
    jsonResponse = response.json()
    #print(jsonResponse)
    city_name = find_in_dict(url,woeid_dict)
    days_cnt = 0
    total_max_temp = 0
    for x in jsonResponse['consolidated_weather']:
        if len(str(x['max_temp'])) > 0:
            days_cnt += 1
            total_max_temp += float(x['max_temp'])
            #print ('days_cnt: ' + str(days_cnt) + ' -- ' + 'max_temp: ' + str(x['max_temp']))

        #print ('days_cnt: ' + str(days_cnt))
        #print ('total_max_temp: ' + str(total_max_temp))
    #print (city_name + ' ' + str(days_cnt) + ' day(s) average max temp: ' + str(round(total_max_temp/days_cnt,4)))
    print(city_name + ' average max temp: ' + str(round(total_max_temp / days_cnt, 4)))

threads = [threading.Thread(target=fetch_url, args=(url,)) for url in urls]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print ("\nTotal Run Time: %s" % (time.time() - start))