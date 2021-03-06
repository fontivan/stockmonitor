# MIT License
#
# Copyright (c) 2020 fontivan
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time

import logging
import random
import threading

'''
TODO: Add header
'''


class VendorThread(threading.Thread):
    sleep_time = None
    vendor = None
    logger = None
    loop_forever = True

    '''
    TODO: Add header
    '''

    def __init__(self, vendor, logger, loop_forever, sleep_time):
        self.logger = logger
        self.vendor = vendor
        self.loop_forever = loop_forever
        self.sleep_time = sleep_time
        super().__init__(daemon=loop_forever)

    '''
    TODO: Add header
    '''

    def run(self):
        self.vendor.log_msg('Daemon thread \'{}\' started for vendor'.format(self.getName()), logging.INFO)
        while True:
            self.vendor.check_stock_for_items()
            if not self.loop_forever:
                break
            generated_time = self.sleep_time + random.randrange(20)
            self.vendor.log_msg('Checked all items for vendor, sleeping for \'{}\' seconds'.format(generated_time),
                                logging.INFO)
            time.sleep(generated_time)
