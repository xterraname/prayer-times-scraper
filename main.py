import requests
from bs4 import BeautifulSoup


URL = "https://islom.uz/"

def main():
    res = requests.get(URL)
    soup = BeautifulSoup(res.content, 'html.parser')

    box = soup.find("div", class_="in_header_p")

    if box:
        times_divs = box.find_all("div", class_="cricle")

        for time_div in times_divs:

            time_name = time_div.find("div", class_="p_v").get_text()
            time = time_div.find("div", class_="p_clock").get_text()
            
            print(f"{time_name.rjust(10)}: {time}")
    else:
        print("Times not found!")


if __name__ == "__main__":
    main()