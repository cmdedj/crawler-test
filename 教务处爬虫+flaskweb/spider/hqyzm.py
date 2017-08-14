from requests import get, post, Session


def hqyzm():
	header = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; 2345Explorer/8.6.2.15784)'}
	s = Session()
	s.get('http://jwc.sut.edu.cn/index.jsp', headers=header)
	s.get('http://jwc.sut.edu.cn/ACTIONLOGON.APPPROCESS?mode=3', headers=header)
	sut = s.get('http://jwc.sut.edu.cn/ACTIONVALIDATERANDOMPICTURE.APPPROCESS', headers=header)
	with open("C:/Users/DLETC/Desktop/cmdedj/test/pytest/app/static/sut.jpeg", "wb") as file:
		file.write(sut.content)
	return s
