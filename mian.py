import requests

url = "https://r2-ndr-private.ykt.cbern.com.cn/edu_product/esp/assets/453025ca-58bd-442e-8543-5ef5222d50c6.pkg/%E4%B9%89%E5%8A%A1%E6%95%99%E8%82%B2%E6%95%99%E7%A7%91%E4%B9%A6%20%E8%8B%B1%E8%AF%AD%20%E5%85%AB%E5%B9%B4%E7%BA%A7%20%E4%B8%8A%E5%86%8C_1756191699270.pdf"
headers = {
    "X-ND-AUTH": 'MAC id="7F938B205F876FC398BCDC5BCE419D07BAC7D3514723EF4763F4F219D7B1CDE42BCE28F96538C251D9BA0946970D61AB89BFB24E4A59158A",nonce="1757259348628:8FRVAAP6",mac="n1v1y6QfUVGTpOvsSjchtrpX9zWKsrHN18fQV9alXgc="'
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    with open("英语八年级上册.pdf", "wb") as f:
        f.write(response.content)
    print("下载成功！")
else:
    print("下载失败，状态码：", response.status_code)