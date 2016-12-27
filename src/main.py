#coding: utf-8
'''
Created on 2016年12月22日

@author: Jane Wei
'''
#import Httpbase
from TestCase import TestCase
from Cases import Cases
from logger import logger,REPORT_FILE
import unittest
import HTMLTestRunner
import codecs

if __name__ == '__main__':
    '''
    tc = TestCase()
    caseFile='TestCase.xlsx'
    cases = tc.Cases(caseFile)

    for case in cases:
        logger.debug(case)
        tc.executeCase(case)
    
    
    caseFile='TestCase.xlsx'
    logger.debug('1')
    suite = unittest.Cases()
    logger.debug('2')
    suite.addTest(TestCase('test',caseFile,None))
    logger.debug('3')
    #logger.debug(suite)
    print type(suite)
    #print suite
    
    with codecs.open(REPORT_FILE,mode='wb',encoding='UTF-8') as fp:
        logger.debug('4')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='TEST REPORT',description='Test Cases running results as following:')
        logger.debug('5')
        runner.run(suite)'''
    
    
    caseFile='TestCase.xlsx'
    tc = Cases()
    cases = tc.testCases(caseFile)
    
    suite = unittest.TestSuite()
    
    for case in cases:
        suite.addTest(TestCase('test',case))
    
    with codecs.open(REPORT_FILE,mode='wb',encoding='UTF-8') as fp:
        logger.debug('4')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='TEST REPORT',description='Test Cases running results as following:')
        logger.debug('5')
        runner.run(suite)
    
    