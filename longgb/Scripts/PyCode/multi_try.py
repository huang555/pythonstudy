#-*- coding:utf-8 -*-
import numpy as np
import sys
import time

from multi.multi import Process
from MyTools import myTools


import logging


def aa(x):
    return x + 3


def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s (%(filename)s) [line:%(lineno)d] [ %(levelname)s ] %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        # filename='ModelSolve.log',
                        # filemode='w'
                        )
    logger = logging.getLogger("SubProcess")

    print 'get Data'
    data = range(10000000)
    # data = map(lambda x: [x], data)

    print 'Method 1 ...'
    t1 = time.time()
    sub = Process(split_data=data, target=aa, dis_n=10, keep_dis=True, logger=logger, dis_files=['MyTools.py', 'multi'])
    results2 = sub.start()
    myTools.runTime(t1)
    print len(results2)


    print 'Method 2 ...'
    t1 = time.time()
    results = map(lambda x: aa(x), data)
    myTools.runTime(t1)
    print len(results)


if __name__ == '__main__':
    main()


# import multiprocessing
# multiprocessing.Process