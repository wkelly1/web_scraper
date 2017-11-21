from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url1 = 'https://assess.joincyberdiscovery.com/challenge-files/clock-pt1?verify=2jiuUX8oAaTAL3AW3qVxVA%3D%3D'
url2 = 'https://assess.joincyberdiscovery.com/challenge-files/clock-pt2?verify=2jiuUX8oAaTAL3AW3qVxVA%3D%3D'
url3 = 'https://assess.joincyberdiscovery.com/challenge-files/clock-pt3?verify=2jiuUX8oAaTAL3AW3qVxVA%3D%3D'
url4 = 'https://assess.joincyberdiscovery.com/challenge-files/clock-pt4?verify=2jiuUX8oAaTAL3AW3qVxVA%3D%3D'
url5 = 'https://assess.joincyberdiscovery.com/challenge-files/clock-pt5?verify=2jiuUX8oAaTAL3AW3qVxVA%3D%3D'

page1 = uReq(url1)
page2 = uReq(url2)
page3 = uReq(url3)
page4 = uReq(url4)
page5 = uReq(url5)

html1 = page1.read()
html2 = page2.read()
html3 = page3.read()
html4 = page4.read()
html5 = page5.read()

soup1 = soup(html1, "html.parser")
soup2 = soup(html2, "html.parser")
soup3 = soup(html3, "html.parser")
soup4 = soup(html4, "html.parser")
soup5 = soup(html5, "html.parser")

page1.close()
page2.close()
page3.close()
page4.close()
page5.close()

print(str(soup1),soup2,soup3,soup4,soup5)
print(str(soup1)+str(soup2)+str(soup3)+str(soup4)+str(soup5))


