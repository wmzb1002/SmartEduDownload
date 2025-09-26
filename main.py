# -*- coding: utf-8 -*-
# v0.0.2#1

import re
import time
import urllib.parse
import urllib.request

url = input("请输入要下载的URL：")
try:
    headers = eval(urllib.parse.unquote(url.split("&headers=")[1]))

    requests = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(requests)

    if response.status == 200:
        filename = input(
            "请输入保存的文件名：[{}]".format(
                urllib.parse.unquote(
                    re.search(r"https(.*)pdf", url).group().split("/")[-1]
                )
            )
        )
        with open(
            (
                filename
                if filename
                else "{}".format(
                    urllib.parse.unquote(
                        re.search(r"https(.*)pdf", url).group().split("/")[-1]
                    )
                )
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
