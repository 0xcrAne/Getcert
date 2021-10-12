# python3
# -*- coding: utf-8 -*-
# Date: 09/09/2021
# Author: Crane

import ssl
import OpenSSL
import argparse
import sys
import os
from socket import setdefaulttimeout


def usage():
    print("Eg: \n    python3 getcert.py -u 127.0.0.1")
    print("    python3 getcert.py -f ip.txt")


def getcert(server, port=443):
    setdefaulttimeout(3)
    try:
        cert = ssl.get_server_certificate((server, port))
    except Exception:
        return None
    if not cert:
        return None
    result = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    subject = result.get_subject()
    issued_to = subject.CN  # 只取域名，其他都不要了
    return {"issued_to": issued_to}


if __name__ == '__main__':
    port = '443'
    parser = argparse.ArgumentParser(description="获取网站证书，可以单个获取和批量获取，不要带http头和端口号，如127.0.0.1或www.xxx.com")
    parser.add_argument('-u', '--url', type=str, help="单个地址获取")
    parser.add_argument('-f', '--file', type=str, help="批量获取证书，结果输入到当前目录result.txt")
    args = parser.parse_args()
    if len(sys.argv) == 3:
        if sys.argv[1] in ['-u', '--url']:
            issuedDic = getcert(args.url, port)
            if issuedDic == None:
                print("未找到ssl信息")
            else:
                print(issuedDic['issued_to'])
        elif sys.argv[1] in ['-f', '--file']:
            if os.path.isfile(args.file) == True:
                with open(args.file) as target:
                    hosts = target.read().splitlines()
                    for host in hosts:
                        issuedDic = getcert(host, port)
                        if issuedDic == None:
                            print(host + ":" + "未找到ssl信息")
                        else:
                            with open("result.txt", "a+") as f:
                                f.write(host + ":" + str(issuedDic['issued_to']) + "\n")
    else:
        parser.print_help()
        usage()
