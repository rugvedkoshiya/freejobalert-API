import json
import requests
from bs4 import BeautifulSoup


URL = "https://www.freejobalert.com/police-defence-jobs/"


def getData(url):
    response = requests.get(url)

    # with open("file.html", "w", encoding="utf-8") as file:
    #     file.write(response.text)

    soup = BeautifulSoup(response.content, "html.parser")
    tableTag = soup.find("table", class_=["lattbl"])

    # headings
    # postDate = tableTag.find("th", class_=["latcpb"])
    # recruitmentBoard = tableTag.find("th", class_=["latcr"])
    # postName = tableTag.find("th", class_=["latceb"])
    # qualification = tableTag.find("th", class_=["latcqb"])
    # advtNo = tableTag.find("th", class_=["latcab"])
    # lastDate = tableTag.find("th", class_=["latclb"])
    # moreInformation = tableTag.find("th", class_=["latcmb"])

    # data
    postDateData = tableTag.find_all("td", class_=["latcpb"])
    recruitmentBoardData = tableTag.find_all("td", class_=["latcr"])
    postNameData = tableTag.find_all("td", class_=["latceb"])
    qualificationData = tableTag.find_all("td", class_=["latcqb"])
    advtNoData = tableTag.find_all("td", class_=["latcab"])
    lastDateData = tableTag.find_all("td", class_=["latclb"])
    moreInformationData = tableTag.find_all("td", class_=["latcmb"])

    # check all data is same size
    if len(postDateData) == len(recruitmentBoardData) and len(postDateData) == len(postNameData) and len(postDateData) == len(postNameData) and len(postDateData) == len(qualificationData) and len(postDateData) == len(advtNoData) and len(postDateData) == len(lastDateData) and len(postDateData) == len(moreInformationData):
        dataDict = []
        for i in range(0, len(postDateData)):
            dataDict.append(
                {
                    "postDate": postDateData[i].text,
                    "recruitmentBoard": recruitmentBoardData[i].text,
                    "postName": postNameData[i].text,
                    "qualification": qualificationData[i].text,
                    "advtNo": advtNoData[i].text,
                    "lastDate": lastDateData[i].text,
                    "moreInformation": moreInformationData[i].find("strong").find("a").get("href"),
                }
            )
        # with open("data.json", "w", encoding="utf-8") as file:
        #     file.write(json.dumps(dataDict))
        return dataDict
    else:
        return []



# getData(URL)