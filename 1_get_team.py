import requests

from utils import write_to_file

# 链接地址
url = 'https://cy.ncss.cn/adminprojects'

cookie = '_ga=GA1.2.1501093798.1621768016; XSRF-CCKTOKEN=f5e981f4a5181f51121bfc2f2ca5df33; CHSICC_CLIENTFLAGCY=66e8991c8efe9f211c49e08e621e46a6; CHSICC02=!fFQ9fz2Ualx3dR7zYxYLahOzddj6Y0RrOzQRsO9/ZBrXkaKoJ4Ly35yeBBLYkPzbTT3udzMRz+UgOw==; CHSICC01=!YUl9EEBkeJy1berzYxYLahOzddj6Y87nrxVekuk12xWrJeTN4IEYNiziGwls8D6SCroocHLhlIoh6w==; _gid=GA1.2.1317773140.1626369552; JSESSIONID=CED207835DFCB1C32267F0E92C3770D4; TS012ad6ee=01886fbf6ea433ea3f6c94aaf48df6218a3bf05dc8d7ab34c33d501b3c000abec2d3444a691e2bf5bce200cf54233acedae2633fb83b67b8b6ea43849fa8d3680ad53f54e722dac289417255e30a9fb4d559270f2e45acbf0f5a1f1abb4fb6264d67a14058266b5e2b3c281f19dfa4b2a1c5e4441e5ef3d0e39ee1edd58cf0fefb022ec102'

pages = 100

for i in range(pages):
    # 请求头
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': cookie,
        'Host': 'cy.ncss.cn',
        'Referer': 'https://cy.ncss.cn/adminprojects/home',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    # 参数
    params = {
        'keyWord': '',
        'provinceCode': '',
        'schoolCode': '',
        'isJoinRed': '',
        'jzw': '',
        'contestStauts': '1',
        'trackCode': '',
        'beginTime': '',
        'endTime': '',
        'pageIndex': i,
        'pageSize': '20',
        '_': '1626382259421'
    }

    # get  请求
    resp = requests.get(url, headers=headers, params=params)

    write_to_file(resp.text, f'./data/team/qnhszmzl/{i}.txt')
