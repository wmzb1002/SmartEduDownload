# -*- coding: utf-8 -*-
# v0.0.1#4

from urllib.parse import unquote

import requests

url = input("请输入要下载的URL：")
headers = {
    "X-ND-AUTH": 'MAC id="7F938B205F876FC398BCDC5BCE419D07BAC7D3514723EF47CA7EA49216D036D12B2BC594178CDBE22072B13A8C3D9D80EE58724DACE63698",nonce="1759371427066:NAAGHZAY",mac="86vtDLIxx6fbIdYgxgiJGS2zY6SPnUYFUl2FeQ0H384="'
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
