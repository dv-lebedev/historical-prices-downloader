"""
The MIT License (MIT)

Copyright (c) 2015 Denis Lebedev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import urllib.request
from datetime import datetime
import os.path


def main():

    destination_path = os.getcwd()

    start_date = datetime(2012, 5, 1)
    end_date = datetime(2012, 6, 1)

    symbols = [
        'GOOG',
        'IBM',
        'JPM'
    ]

    download_all(symbols, start_date, end_date, destination_path)


def download_all(symbols, start_dt, end_dt, folder_path):
    for symbol in symbols:
        data = download(symbol, start_dt, end_dt)
        write(folder_path, symbol, data)


def download(symbol, start_date, end_date):
    request_str = create_request_string(symbol, start_date, end_date)
    with urllib.request.urlopen(request_str) as f:
        return f.read()


def create_request_string(symbol, start_date, end_date):
    request_str = "http://www.google.com/finance/historical?q="
    request_str += symbol
    request_str += "&startdate={}".format(datetime_to_str(start_date))
    request_str += "&enddate={}".format(datetime_to_str(end_date))
    return request_str + "&output=csv"


def datetime_to_str(dt):
    res = "{:%B %d %Y}".format(dt).split(' ')
    return "{}+{}%2C+{}".format(res[0][:3], res[1], res[2])


def write(folder_path, symbol, data):
    with open(os.path.join(folder_path, symbol + ".csv"), 'wb') as file:
        file.write(data)


if __name__ == '__main__':
    main()
