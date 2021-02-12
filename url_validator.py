import csv
import os
import urllib
import requests
from urllib.error import HTTPError

#! [Variables]
s_count = 0
file_ext = '.csv'
file_name = 'results'
path = os.getcwd()  # Get the current working directory (cwd)
current_dir = os.path.dirname(os.path.realpath(__file__))
files = os.listdir(current_dir) # Get all the files in that directory



#! [Define Functions]
def save_values_as_csv(a,b,c):
    with open(current_dir + "/" + file_name + file_ext, 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([a, b, c])

def save_data(a,b,c):
    if not os.path.isfile(current_dir + "/" + file_name + file_ext):
        save_values_as_csv('index', 'url', 'exists')
    save_values_as_csv(a, b, c)

def does_url_exist(url):
    headers = {'USER-AGENT': 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}
    r = requests.get(url, headers=headers)
    #if code == 200:  #Edited per @Brad's comment
    if r.status_code == 200:
        return True
    else:
        return False


#! [Main]
inputfile = csv.reader(open(current_dir +'/data.csv','r'))

for row in inputfile:
    url = ', '.join(row).replace('"', "").strip()
    status = does_url_exist(url)
    print(status)
    s_count = s_count + 1  
    save_data(s_count, url, status)
