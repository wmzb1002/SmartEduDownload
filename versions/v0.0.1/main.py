# -*- coding: utf-8 -*-
# v0.0.1#3

from urllib.parse import unquote

import requests

url = input("请输入要下载的URL：")
headers = {
    "X-ND-AUTH": 'MAC id="7F938B205F876FC398BCDC5BCE419D07BAC7D3514723EF4751C57F43AE830A74CD960C5EE719D01E3B71D7E0943017E5EC70CCB4DF41A584",nonce="1758897798046:J2HW2VYE",mac="cen8i2p4vGuMJ3cnGalzHvvELyeKVjS6etTU0WKq7z0="'
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    filename = input("请输入保存的文件名：[{}]".format(unquote(url.split("/")[-1])))
    with open(
        filename if filename else "{}".format(unquote(url.split("/")[-1])), "wb"
    ) as f:
        f.write(response.content)
    print("下载成功！")
else:
    print("下载失败，状态码：", response.status_code)
