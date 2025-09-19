# -*- coding: utf-8 -*-
# v0.0.1#1

from urllib.parse import unquote

import requests

url = input("请输入要下载的URL：")
headers = {
    "X-ND-AUTH": 'MAC id="7F938B205F876FC398BCDC5BCE419D07BAC7D3514723EF4763F4F219D7B1CDE42BCE28F96538C251D9BA0946970D61AB89BFB24E4A59158A",nonce="1757259348628:8FRVAAP6",mac="n1v1y6QfUVGTpOvsSjchtrpX9zWKsrHN18fQV9alXgc="'
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    filename = input("请输入保存的文件名：[{}]".format(unquote(url.split('/')[-1])))
    with open(filename if filename else '{}'.format(unquote(url.split('/')[-1])), "wb") as f:
        f.write(response.content)
    print("下载成功！")
else:
    print("下载失败，状态码：", response.status_code)