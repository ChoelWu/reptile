import requests

from utils import write_to_file, read_from_file

# 读取文件，并且将编号转化为数组
code_text = read_from_file('./data/team/team_links2.txt')
code_text = code_text.replace(" ", "").replace("[", "").replace("]", "").replace("\"", "").replace("\"", "")
code_str_list = code_text.splitlines()

code_list = []

for code_str in code_str_list:
    code_list = code_list + code_str.split(',')

#
# 访问链接
url = 'https://cy.ncss.cn/adminprojects/'

# cookie
cookie = '_ga=GA1.2.1501093798.1621768016; XSRF-CCKTOKEN=f5e981f4a5181f51121bfc2f2ca5df33; CHSICC_CLIENTFLAGCY=66e8991c8efe9f211c49e08e621e46a6; CHSICC02=!fFQ9fz2Ualx3dR7zYxYLahOzddj6Y0RrOzQRsO9/ZBrXkaKoJ4Ly35yeBBLYkPzbTT3udzMRz+UgOw==; CHSICC01=!YUl9EEBkeJy1berzYxYLahOzddj6Y87nrxVekuk12xWrJeTN4IEYNiziGwls8D6SCroocHLhlIoh6w==; _gid=GA1.2.1317773140.1626369552; JSESSIONID=CED207835DFCB1C32267F0E92C3770D4; TS012ad6ee=01886fbf6ea433ea3f6c94aaf48df6218a3bf05dc8d7ab34c33d501b3c000abec2d3444a691e2bf5bce200cf54233acedae2633fb83b67b8b6ea43849fa8d3680ad53f54e722dac289417255e30a9fb4d559270f2e45acbf0f5a1f1abb4fb6264d67a14058266b5e2b3c281f19dfa4b2a1c5e4441e5ef3d0e39ee1edd58cf0fefb022ec102'

for i in code_list:
    # 请求头
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': cookie,
        'Host': 'cy.ncss.cn',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }

    print(url + i)
    # get  请求
    resp = requests.get(url + i, headers=headers)
    p = "./data/individual/qnhszmzl/" + i + ".txt"
    print(p)

    write_to_file(resp.text, './data/individual/qnhszmzl/' + i + '.txt')
