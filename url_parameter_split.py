#!/usr/bin/env python
# vim: set ts=4 sw=4 et smartindent ignorecase fileencoding=utf8:
import argparse
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse

def parse_option():
    parser = argparse.ArgumentParser(description='URLの引数を分解して必要なのだけを返す')
    parser.add_argument('url', type=str, nargs=1,help='URL`')
    parser.add_argument('param', type=str, nargs='*',help='必要な引数`')

    return parser.parse_args()

def main():
    args = parse_option()
    url = args.url[0]
    try:
        p = urlparse(url)
    except ValueError:
        print(f'{url}: url形式では無い')
        return 1
    if p.query:
        q = parse_qsl(p.query)
        rslt = []
        for v in q:
            key = v[0]
            value = v[1]
            if key in args.param:
                rslt.append((key, value))
        p = p._replace(query=urlencode(rslt))
    rslt = urlunparse(p)
    print(f'{rslt}')
    return 0

if __name__ == '__main__':
    main()