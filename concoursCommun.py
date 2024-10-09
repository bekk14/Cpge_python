#!/bin/env/python3
##############################################
#    bekk@14 : bakkalihamza2014@gmail.com    #
#                                            #
#    $> python3 concoursCommun.py            #
##############################################
import os
bienV = r"""
 /\_/\  
( o.o ) 
 > ^ <
------
.:. Bekk@14
.:. e-mail: bakkalihamza2014@gmail.com
$-> enonce     | $-> annee |$- enonces files  
$-> correction | $-> annee |$- correction files 

... La route du succès est pavée de détermination et de persévérance.
------
"""


def check_requests_installed():
    try:
        import requests
        print("The 'requests' module is installed.")
    except ModuleNotFoundError:
        print("The 'requests' module is NOT installed. Please install it using 'pip install requests'.")
        exit()
print(bienV)

check_requests_installed()
import requests
base_url = "https://cpgemaroc.com/cnc/"
categories_physique = ["ph1psi", "ph2psi", "ph1mp", "ph2mp", "ph1tsi", "ph2tsi"]
categories_chimie = ["chpsi", "chmp", "chtsi"]
years_physique = range(2000, 2025)
years_chimie = range(2000, 2025)

def download_file(url, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    try:
        response = requests.get(url)
        response.raise_for_status()
        file_name = url.split("/")[-1]
        file_path = os.path.join(dest_folder, file_name)
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"Downloaded: {file_name}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download: {url}")
        return False
    return True

#PHYSIQUE 
for category in categories_physique:
    for year in years_physique:
        file_name = f"e_{category}{year}.pdf"
        url = f"{base_url}{category}/{file_name}"
        dest_folder = f"enonce/{year}"
        ###
        if not download_file(url, dest_folder):
            alt_file_name = f"e_{category.replace('ph1', 'ph').replace('ph2', 'ph')}{year}.pdf"
            alt_url = f"{base_url}{category}/{alt_file_name}"
            download_file(alt_url, dest_folder)

# CHIMIE
for category in categories_chimie:
    for year in years_chimie:
        file_name = f"e_{category}{year}.pdf"
        url = f"{base_url}{category}/{file_name}"
        dest_folder = f"enonce/{year}"
        if not download_file(url, dest_folder):
            alt_file_name = f"e_{category.replace('ch', 'ch')}{year}.pdf"
            alt_url = f"{base_url}{category}/{alt_file_name}"
            download_file(alt_url, dest_folder)

#CORRECTIONS
for category in categories_physique + categories_chimie:
    for year in range(2000, 2025):
        file_name = f"c_{category}{year}.pdf"
        url = f"{base_url}{category}/{file_name}"
        dest_folder = f"correction/{year}"
        if not download_file(url, dest_folder):
            alt_file_name = f"c2_{category}{year}.pdf"
            alt_url = f"{base_url}{category}/{alt_file_name}"
            download_file(alt_url, dest_folder)

