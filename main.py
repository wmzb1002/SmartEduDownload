# -*- coding: utf-8 -*-
# v0.0.2#1
# https://basic.smartedu.cn/pdfjs/2.15/web/viewer.html?hasCatalog=true&file=https://r1-ndr-private.ykt.cbern.com.cn/edu_product/esp/assets/8c419b19-b3a9-4dbf-a8b4-546b7d337528.pkg/%E4%B9%89%E5%8A%A1%E6%95%99%E8%82%B2%E6%95%99%E7%A7%91%E4%B9%A6%20%E5%8C%96%E5%AD%A6%20%E4%B9%9D%E5%B9%B4%E7%BA%A7%20%E4%B8%8A%E5%86%8C_1756191710781.pdf&headers=%7B%22X-ND-AUTH%22:%22MAC%20id=%5C%227F938B205F876FC398BCDC5BCE419D07BAC7D3514723EF47CA7EA49216D036D12B2BC594178CDBE22072B13A8C3D9D80EE58724DACE63698%5C%22,nonce=%5C%221759371427066:NAAGHZAY%5C%22,mac=%5C%2286vtDLIxx6fbIdYgxgiJGS2zY6SPnUYFUl2FeQ0H384=%5C%22%22%7D

import re
import time
import urllib.parse
import urllib.request

url = input("请输入要下载的URL：")
try:
    headers = eval(urllib.parse.unquote(url.split("&headers=")[1]))

    url = re.search(r"file=(.*)pdf", url).group().split("=")[-1]
    requests = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(requests)

    if response.status == 200:
        filename = input(
            "请输入保存的文件名：[{}]".format(urllib.parse.unquote(url.split("/")[-1]))
        )
        with open(
            (
                filename
                if filename
                else "{}".format(urllib.parse.unquote(url.split("/")[-1]))
            ),
            "wb",
        ) as f:
            data = response.read(1024)  # 每次读取1024字节
            while data:
                f.write(data)
                data = response.read(1024)
        print("下载成功！3秒后退出程序。。。")
    else:
        print("下载失败，状态码：", response.status_code)
except Exception as e:
    print("错误！请检查链接、保存路径是否正确或此版本是否有效。错误码：", e)

time.sleep(3)
