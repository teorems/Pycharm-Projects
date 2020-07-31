import sys
import os
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore

args = sys.argv

directory_name = args[1]
try:

    # Create target Directory
    os.mkdir(directory_name)
except FileExistsError:
    pass




pages = []


def writetocache(page):
    pages.append(request.rstrip(".com").lstrip("https://"))
    file_name = request.rstrip(".com").lstrip("https://") + ".txt"
    path = os.path.join(os.getcwd(),directory_name, file_name)
    with open(path, "w") as cache:
        cache.write(page)


def back():
    try:
        read_history(pages[-2])
    except IOError:
        pass


def read_history(site):
    page_file = site + ".txt"
    path = os.path.join(os.getcwd(), directory_name, page_file)
    with open(path, "r") as cached_page:
        print(cached_page.read())


def retrieve_page():
    r = requests.get(request)
    soup = BeautifulSoup(r.content, 'html.parser')
    anchor_tags = soup.find_all('a')
    init()
    for anchor_tag in anchor_tags:
        anchor_tag.string = f"{Fore.BLUE}{anchor_tag.string}"
    tags = soup.select('h, p, ul, ol')
    page_content = "\n".join([tag.get_text() for tag in tags])
    writetocache(page_content)
    print(page_content)


while True:
    request = input()
    try:
        retrieve_page()
    except:
        if request == "exit":
            exit()

        elif request == "back":
            back()

        elif request in pages:

            read_history(request)

        else:
            request = "https://" + request
            try:
                retrieve_page()
            except:
                print("Error : Incorrect URL")
