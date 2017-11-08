import re
from urllib.request import Request, urlopen


request = Request("http://psl-t20.com", headers={'User-Agent': 'Mozilla/5.0'})
htmlText = urlopen(request).read()
html = str(htmlText)

pslDetails = re.finditer("<span id=\"count-\d\" class=\"word-count\">(\d+)</span>", html)

print("****************************************************\n"
      "****************************************************\n"
      "**********                                *********\n"
      "**********   Online PSL-T20-2017 Detail   **********\n"
      "**********                                **********\n"
      "****************************************************\n"
      "****************************************************\n")

pslTitle = ["Run Machine","Total Howzat","Total Sixes","Total Fours"]
index = 0
for x in pslDetails:
    print(pslTitle[index]+": "+x.group(1))
    index += 1

teamDetailTable = re.search("<table class=\"kode-table kode-table-v2\">(.+?)</table>",html)
teamDetailBody = re.search("<tbody>(.*)</tbody>", teamDetailTable.group(1))
teamDetailRows = re.finditer("<tr>(.*?)</tr>",teamDetailBody.group(1))
teamDetailRows = [x.group(1) for x in teamDetailRows]

teams = ["Islamabad United","Peshawar Zalmi","Quetta Gladiators","Karachi Kings","Lahore Qalandars"]
titles = ["Match","Won","Lost","Tied","No Result","Aban","Bonus Point","Points","Net RR"];

for x in range(len(teamDetailRows)):
    print("\n|||||||||||  "+teams[x]+"  |||||||||||")
    teamDetailCols = re.finditer("<td(.*?)>(.+?)</td>",teamDetailRows[x])
    detailList = [y.group(2) for y in teamDetailCols]
    detailList = detailList[1:len(detailList)]
    for y in range(len(detailList)):
        print(titles[y]+": "+str(detailList[y]+", "), end="")
    print()

print("\nDeveloped by: Rehan Javed(RJ APPS)")