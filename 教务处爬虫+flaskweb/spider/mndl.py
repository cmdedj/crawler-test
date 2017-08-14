from requests import get, post, Session


def mndl(s, username, password, yzm):
	header = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; 2345Explorer/8.6.2.15784)'}
	form = {'WebUserNO': username, 'Password': password, 'Agnomen': yzm}
	getcookie = s.post("http://jwc.sut.edu.cn/ACTIONLOGON.APPPROCESS?mode=4", headers=header, data=form)
	getxinxi = s.get("http://jwc.sut.edu.cn/ACTIONQUERYSTUDENT.APPPROCESS", headers=header)
	return getxinxi.text
