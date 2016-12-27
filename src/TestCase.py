#coding: utf-8
'''
Created on 2016年12月22日

@author: Jane Wei
'''
import xlrd
import os
import re
import Httpbase
from proboscis.asserts import assert_equal
import unittest
from logger import logger

class TestCase(unittest.TestCase):
    '''
    classdocs
    '''
    def __init__(self,testName,case):
        '''
        Constructor
        '''
        super(TestCase, self).__init__(testName) 
        self.logger = logger
        self.case = case
    
    def test(self):
        self.logger.debug(self.case)
        self.executeCase(self.case)
                    
    def executeCase(self,case):
        self.verificationsErrors = []
        methods = {'http':self.__httpTest,
               'https':self.__httpsTest,
               'SOAP': self.__SOAP,
               #'default': self.__NoExecute,
               }
        
        #self.logger.debug(type(case))
        protocol = case['Protocol'].lower()
        self.logger.debug(protocol)
        #self.logger.debug( callable(methods.get(protocol) ))
        methods.get(protocol,self.__NoExecute)(case)
        '''
        if []==self.verificationsErrors:
            return True
        else:
            return False'''
        self.assertEqual([], self.verificationsErrors, 'Case %d FAILED'%case['ID'])

    def __httpTest(self,case):
        #self.logger.debug(type(case))
        conn = Httpbase.Http(host=case['Host'], port=case['Port'], path=case['Path'], method=case['Method'], params=case['Params'])
        response = conn.request()
        self.logger.debug(response[0])
        
        if response[0]>=500:
            self.logger.error('Case %d: CODE %s, REASON %s , please check your server'%(case['ID'],response[0],response[1]))
            self.verificationsErrors.append('Case %d: CODE %s, REASON %s , please check your server'%(case['ID'],response[0],response[1]))
            
        elif response[0]>=400:
            self.logger.error('Case %d: CODE %s, REASON %s , please check your client'%(case['ID'],response[0],response[1]))
            self.verificationsErrors.append('Case %d: CODE %s, REASON %s , please check your client'%(case['ID'],response[0],response[1]))
            
        elif response[0]>=300:
            self.logger.info('Case %d: CODE %s, REASON %s , Redirection'%(case['ID'],response[0],response[1]))
        elif response[0]>=200:
            self.logger.info('Case %d: CODE %s, REASON %s , Success'%(case['ID'],response[0],response[1]))
        elif response[0]>=100:
            self.logger.info('Case %d: CODE %s, REASON %s , Accept'%(case['ID'],response[0],response[1]))
        else:
            self.logger.error('Case %d: CODE %s, REASON %s , Errors'%(case['ID'],response[0],response[1]))
        
        self.logger.debug(case['Check point'])  
        #self.logger.debug(response[2]) 
        if case['Check point'] and response[2]:
            try:
                #cps=eval(case['Check point'])
                cps = case['Check point'].split(';;')
                for cp in cps:
                    if not re.search(re.escape(cp),response[2]):
                        print 'Not match'
                        self.logger.error('Case %d: Not match "%s"'%(case['ID'],cp))
                        self.verificationsErrors.append('Case %d: Not match "%s"'%(case['ID'],cp))
            except Exception,e:
                self.logger.error('Case %d, Exception: %s'%(case['ID'],e))
                self.verificationsErrors.append('Case %d, Exception: %s'%(case['ID'],e))
    
    def __httpsTest(self,case):
        conn = Httpbase.Http(host=case['Host'], port=case['Port'], path=case['Path'], method=case['Method'], params=case['Params'])
        response = conn.request(0)
        if response[0]>=500:
            self.logger.error('Case %d: CODE %s, REASON %s , please check your server'%(case['ID'],response[0],response[1]))
            self.verificationsErrors.append('Case %d: CODE %s, REASON %s , please check your server'%(case['ID'],response[0],response[1]))
            
        elif response[0]>=400:
            self.logger.error('Case %d: CODE %s, REASON %s , please check your client'%(case['ID'],response[0],response[1]))
            self.verificationsErrors.append('Case %d: CODE %s, REASON %s , please check your client'%(case['ID'],response[0],response[1]))
            
        elif response[0]>=300:
            self.logger.info('Case %d: CODE %s, REASON %s , Redirection'%(case['ID'],response[0],response[1]))
        elif response[0]>=200:
            self.logger.info('Case %d: CODE %s, REASON %s , Success'%(case['ID'],response[0],response[1]))
        elif response[0]>=100:
            self.logger.info('Case %d: CODE %s, REASON %s , Accept'%(case['ID'],response[0],response[1]))
        else:
            self.logger.error('Case %d: CODE %s, REASON %s , Errors'%(case['ID'],response[0],response[1]))
            
        if case['Check point'] and response[2]:
            try:
                cps=eval(case['Check point'])
                for cp in cps:
                    if not re.search(cp,response[2]):
                        self.logger.error('Case %d: Not match "%s"'%(case['ID'],cp))
                        self.verificationsErrors.append('Case %d: Not match "%s"'%(case['ID'],cp))
            except Exception,e:
                self.logger.error('Case %d, Exception: %s'%(case['ID'],e))
                self.verificationsErrors.append('Case %d, Exception: %s'%(case['ID'],e))
    
    def __SOAP(self,case):
        pass          
    def __NoExecute(self,case):
        self.logger.error('Please check case %d'%case['ID']) 
        self.verificationsErrors.append('Please check case %d'%case['ID'])               