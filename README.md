# Getcert
批量获取网站SSL证书里的域名  
用于批量扫描漏洞，然后定位资产时，提高定位效率


```

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     单个地址获取
  -f FILE, --file FILE  批量获取证书，结果输入到当前目录result.txt
Eg: 
    python3 getcert.py -u 127.0.0.1
    python3 getcert.py -f ip.txt

```

