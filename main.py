# -*- coding: utf-8 -*-
# v0.0.1#2

from urllib.parse import unquote

import requests

url = input("请输入要下载的URL：")
headers = {
    "X-ND-AUTH": "MAC id=\"7F938B205F876FC398BCDC5BCE419D07BAC7D3514723EF4786BA8CDE8D9C6DBA85AEA50F8550B6F4D71391E168C655101B2CEADE63432EDC\",nonce=\"1758292663477:UJATFPSP\",mac=\"R9VZcOiRWzQFGiwxUiwKn83iOZImV6QZwRMalamYLv8=\""
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    filename = input("请输入保存的文件名：[{}]".format(unquote(url.split('/')[-1])))
    with open(filename if filename else '{}'.format(unquote(url.split('/')[-1])), "wb") as f:
        f.write(response.content)
    print("下载成功！")
else:
    print("下载失败，状态码：", response.status_code)