# Copyright (c) 2019 RedLotus <ssfdust@gmail.com>
# Author: RedLotus <ssfdust@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from parser import WeatherParser
from picfinder import PicFinder
from reporter import WeatherRepoter
from paint import Painter
from datetime import datetime
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument('location')
    args = parser.parse_args()

    p = PicFinder()
    time = datetime.now()
    wr = WeatherRepoter(time.year, time.month, args.location)
    par = WeatherParser(wr.current, wr.forecast)
    par.parse()
    par.to_json("/home/ssfdust/.cache/weather.json")
    pa = Painter(par, p)
    pa.load()
    pa.paint()
    bg = pa.crop()
    bg.save("/home/ssfdust/.cache/weather.png")


if __name__ == '__main__':
    main()
