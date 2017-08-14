from lxml import etree
from pymongo import MongoClient


def pa(text):
	html = etree.HTML(text)
	result = html.xpath('//tr/td[@class="color-row"]')
	for i in result:
		print(i.text)

	client = MongoClient("localhost", 27017)
	db = client.runoob
	test = db.student
	xinxi = {
		result[0].text: result[1].text,
		result[2].text: result[3].text,
		result[5].text: result[6].text,
		result[7].text: result[8].text,
		result[9].text: result[10].text,
		result[11].text: result[12].text,
		result[13].text: result[14].text,
		result[15].text: result[16].text,
		result[17].text: result[18].text,
		result[19].text: result[20].text,
		result[21].text: result[22].text,
		result[23].text: result[24].text,

	}
	test.insert(xinxi)
	return xinxi