#imports
import time
import os 
import requests
import art
from time import *
from time import time
from requests import Session
import threading
import logging
import timeit
from time import time, strftime, gmtime, sleep






#installs
print("""

██████╗░██████╗░░█████╗░██╗░░██╗██╗░░░██╗░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝╚██╗░██╔╝██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██████╔╝██████╔╝██║░░██║░╚███╔╝░░╚████╔╝░██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
██╔═══╝░██╔══██╗██║░░██║░██╔██╗░░░╚██╔╝░░██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██║░░░░░██║░░██║╚█████╔╝██╔╝╚██╗░░░██║░░░╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝   Version 1.2 By DumbDannyLol


""")


#elapsed time





os.system(f"title ProxyChecker v1.2 Loading..")
print("Loading Proxies...")


start = time()
time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
#counts amount of proxies in proxies.txt
proxycount1 = open("proxies.txt", "r")
proxycount2 = 0
for line in proxycount1:
    if line != "\n":
        proxycount2 +=1
proxycount1
proxycount3 = 0
gproxy_count = 0
print(proxycount2, "proxies loaded!")
os.system(f"title ProxyChecker v1.2 ^| {proxycount2} proxies loaded ^| Elapsed Time: {time_elapsed}")
#update titles
def title1():
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        os.system(f"title ProxyChecker v1.2 ^| Normal Mode ^| {proxycount2} proxies loaded ^| Time Elapsed: {time_elapsed}")

def title2():
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        os.system(f"title ProxyChecker v1.2 ^| QuickMode ^| {proxycount2} proxies loaded  ^| Time Elapsed: {time_elapsed}")

def title3():
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        os.system(f"title ProxyChecker v1.2 ^| DoubleCheck Mode ^| {proxycount2} proxies loaded  ^| Time Elapsed: {time_elapsed}")

def title3():
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        os.system(f"title ProxyChecker v1.2 ^| SpeedMode ^| {proxycount2} proxies loaded  ^| Time Elapsed: {time_elapsed}")

def titlemenu():
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        os.system(f"title ProxyChecker v1.2 ^| Main Menu ^| {proxycount2} proxies loaded  ^| Time Elapsed: {time_elapsed}")
#elapsed time

#logging
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S" )



#select option for how fast it will go.
print("Select an option:")
print("   ")
print("Normal Mode [1]  Quick Mode [2]   Double-Check Mode [3]")

mode = int(input(""))

#if stuff
if mode == 1:
    a = threading.Thread(target= title1)
    a.start()
    session1 = Session()
    session1.headers.update({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36'
    '(KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36'
    })

    def mil_seconds():
        return int(round(time() * 1000))
    
    with open ('proxies.txt') as proxies_text, open ('sites.txt') as sitelist_text:
        proxies = proxies_text.read().splitlines()
        sites = sitelist_text.read().splitlines()

    

    if not proxies:
        print("Error! Either you didn't put proxies in the proxies.txt file or you are missing the proxies.txt file!")
        exit()
    
    else:
        print("You currently have", proxycount2, "proxies loaded!")
        print('Testing on sites {}\n\n'.format(sites))
        good_proxies, bad_proxies = [], []
        def normalmode(proxy):
            try:
                proxy_parts = proxy.split(':')
                ip, port, user, passw, = proxy_parts[0], proxy_parts[
                    1], proxy_parts[2], proxy_parts[3]
                proxies = {
                    'http': 'http://{}:{}@{}:{}'.format(user, passw, ip, port),
                    'https': 'https://{}:{}@{}:{}'.format(user, passw, ip, port)
                }
            except IndexError:
                proxies = {'http': 'http://' + proxy, 'https': 'https://' + proxy}
            
            for url in sites:
                start_time = mil_seconds()
                try:
                    response = session1.get(url, proxies = proxies)
                    if response.status_code != 200:
                        print('invalid proxy: {}'.format(proxy))
                        bad_proxies.append(proxy)
                    else:
                        print('{} responded in {} ms on {}'.format(proxy, mil_seconds() - start_time, url))
                        good_proxies.append(proxy)
                except:
                    print('{} is a bad proxy on {}'.format(proxy, url))

    if __name__ == '__main__':
        for z in proxies:
            normalmode(z)
        good_proxies_set, bad_proxies_set, = set(good_proxies), set(bad_proxies)

        with open('results.txt', 'a') as proxy_results:
            proxy_results.write('\nWebsites tested on: {}\n'.format(sites))
            if good_proxies_set:
                proxy_results.write('\n Working proxies:')
                for proxy in good_proxies_set:
                    proxy_results.write('{}\n'.format(proxy))
            if bad_proxies_set:
                proxy_results.write('\n Bad proxies: \n')
                for proxy in bad_proxies_set:
                    proxy_results.write('{}\n'.format(proxy))
        if good_proxies_set:
            print('\n\n Good proxies: {}'.format(good_proxies_set))
        else:
            print('\nNo Good proxies!')





elif mode == 2:
    b = threading.Thread(target=title2)
    b.start()
    print("  ")
    print("Please note Quick Mode is not always accurate, so Normal Mode is reccomended!")
    sleep(3)
    session1 = Session()
    session1.headers.update({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36'
    '(KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36'
    })

    def mil_seconds():
        return int(round(time() * 1000))
    
    with open ('proxies.txt') as proxies_text, open ('sites.txt') as sitelist_text:
        proxies = proxies_text.read().splitlines()
        sites = sitelist_text.read().splitlines()

    

    if not proxies:
        print("Error! Either you didn't put proxies in the proxies.txt file or you are missing the proxies.txt file!")
        exit()
    
    else:
        print("You currently have", proxycount2, "proxies loaded!")
        print('Testing on sites {}\n\n'.format(sites))
        good_proxies, bad_proxies = [], []
        def quickmode(proxy):
            try:
                proxy_parts = proxy.split(':')
                ip, port, user, passw, = proxy_parts[0], proxy_parts[
                    1], proxy_parts[2], proxy_parts[3]
                proxies = {
                    'http': 'http://{}:{}@{}:{}'.format(user, passw, ip, port),
                    'https': 'https://{}:{}@{}:{}'.format(user, passw, ip, port)
                }
            except IndexError:
                proxies = {'http': 'http://' + proxy, 'https': 'https://' + proxy}
            
            for url in sites:
                start_time = mil_seconds()
                try:
                    response = session1.get(url, proxies = proxies, timeout=1)
                    if response.status_code != 200:
                        print('invalid proxy: {}'.format(proxy))
                        bad_proxies.append(proxy)
                    else:
                        print('{} responded in {} ms on {}'.format(proxy, mil_seconds() - start_time, url))
                        good_proxies.append(proxy)
                        gproxy_count = gproxy_count + [1]
                except:
                    print('{} is a bad proxy on {}'.format(proxy, url))

    if __name__ == '__main__':
        for z in proxies:
            quickmode(z)
        good_proxies_set, bad_proxies_set, = set(good_proxies), set(bad_proxies)

        with open('results.txt', 'a') as proxy_results:
            proxy_results.write('\nWebsites tested on: {}\n'.format(sites))
            if good_proxies_set:
                proxy_results.write('\n Working proxies:')
                for proxy in good_proxies_set:
                    proxy_results.write('{}\n'.format(proxy))
            if bad_proxies_set:
                proxy_results.write('\n Bad proxies: \n')
                for proxy in bad_proxies_set:
                    proxy_results.write('{}\n'.format(proxy))
        if good_proxies_set:
            print('\n\n Good proxies: {}'.format(good_proxies_set))
        else:
            print('\nNo Good proxies!')


elif mode == 3:
    c = threading.Thread(target = title3)
    c.start()
    print("Double Check mode takes the longest of the three.")
    session1 = Session()
    session1.headers.update({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36'
    '(KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36'
    })

    def mil_seconds():
        return int(round(time() * 1000))
    
    with open ('proxies.txt') as proxies_text, open ('sites.txt') as sitelist_text:
        proxies = proxies_text.read().splitlines()
        sites = sitelist_text.read().splitlines()

    

    if not proxies:
        print("Error! Either you didn't put proxies in the proxies.txt file or you are missing the proxies.txt file!")
        exit()
    
    else:
        print("You currently have", proxycount2, "proxies loaded!")
        print('Testing on sites {}\n\n'.format(sites))
        good_proxies, bad_proxies = [], []
        def normalmode(proxy):
            try:
                proxy_parts = proxy.split(':')
                ip, port, user, passw, = proxy_parts[0], proxy_parts[
                    1], proxy_parts[2], proxy_parts[3]
                proxies = {
                    'http': 'http://{}:{}@{}:{}'.format(user, passw, ip, port),
                    'https': 'https://{}:{}@{}:{}'.format(user, passw, ip, port)
                }
            except IndexError:
                proxies = {'http': 'http://' + proxy, 'https': 'https://' + proxy}
            
            for url in sites:
                start_time = mil_seconds()
                try:
                    response = session1.get(url, proxies = proxies)
                    response = session1.get(url, proxies = proxies)
                    if response.status_code != 200:
                        print('invalid proxy: {}'.format(proxy))
                        bad_proxies.append(proxy)
                    else:
                        print('{} responded in {} ms on {}'.format(proxy, mil_seconds() - start_time, url))
                        good_proxies.append(proxy)
                except:
                    print('{} is a bad proxy on {}'.format(proxy, url))

    if __name__ == '__main__':
        for z in proxies:
            normalmode(z)
        good_proxies_set, bad_proxies_set, = set(good_proxies), set(bad_proxies)

        with open('results.txt', 'a') as proxy_results:
            proxy_results.write('\nWebsites tested on: {}\n'.format(sites))
            if good_proxies_set:
                proxy_results.write('\n Working proxies:')
                for proxy in good_proxies_set:
                    proxy_results.write('{}\n'.format(proxy))
            if bad_proxies_set:
                proxy_results.write('\n Bad proxies: \n')
                for proxy in bad_proxies_set:
                    proxy_results.write('{}\n'.format(proxy))
        if good_proxies_set:
            print('\n\n Good proxies: {}'.format(good_proxies_set))
        else:
            print('\nNo Good proxies!')
