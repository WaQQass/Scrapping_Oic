import sys
import time
from bs4 import BeautifulSoup
import requests
import openpyxl


try:
    source = requests.get("https://www.oic-oci.org/home/?lan=en")
    # print(source)
    source.raise_for_status()
    soup = BeautifulSoup(source.text, 'html.parser')
    # print(soup)
    # for headings and headlines
    main_para = soup.find_all("div", class_="row")
    first_para = main_para[3]
    mainheading = (main_para[3].a.text)  # Hot news headline
    mainpara = ((main_para[3].p.text))  # hotnews Paragraph
    print("hot news headline>>>>\n", mainheading, "\n")
    print("hot news details>>>>\n", mainpara, "\n")
    for inner_news in range(4, 8):
        headings = (main_para[inner_news].a.text)

        paragraphs = (main_para[inner_news].p.text)

        paragraphs = paragraphs.replace("... more", "   ")

        print("Other news headlines are>>>>\n\n", headings, "\n\n",
              "other news paragraphs are>>>>\n\n", paragraphs, "\n\n")
    # For calender meetings
    all_meeings_box = soup.find_all("div", class_="media")
    for cal_meeting in range(1, 4):
        calender_meeting = all_meeings_box[cal_meeting].text
        print(
            f"There are three calender meetings which are >>>\n{calender_meeting}\n")
    # for getting departments heading
    departments_heading_fetch = soup.find_all("div", class_="panel-heading")
    department_heading = ((departments_heading_fetch[1]).text)
    print(department_heading)  # dparments heading get
    # for getting departments list and URL's
    dp_list_block = soup.find_all(
        "div", class_="panel-body")
    departmnts_list = dp_list_block[1].find_all("li")
    departmnts_list_link = dp_list_block[1].find_all("a")
    for i in range(len(departmnts_list)):
        show_list = departmnts_list[i].a.text
        print("*", show_list, "\n")  # dpt list
    for j in range(len(departmnts_list_link)):
        show_link = departmnts_list_link[j].get("href")
        print(show_link)  # dpt list url

except Exception as e:
    print(e)
