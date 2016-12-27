#coding: utf-8
'''
Created on 2016��12��26��

@author: Jane Wei
'''
import xlrd
import os

class Cases(object):
    
    def __init__(self):
        '''
        Constructor
        '''
        #self.logger = logger
        pass
        #self.logger.debug(self.caseFile)
        
    def testCases(self,caseFile='TestCase.xlsx',suiteName=None):
        self.caseFile = os.getcwd()+'\\TestCase\\'+caseFile
        self.suiteName = suiteName
        with xlrd.open_workbook(self.caseFile) as f:
            if self.suiteName:
                table = f.sheet_by_name(self.suiteName) 
            else:
                table = f.sheet_by_index(0)
            nrows = table.nrows
            colnames = table.row_values(0)
            for rownum in range(1,nrows):
                row = table.row_values(rownum)
                if row:
                    case={}
                    for i in range(len(colnames)):
                        case[colnames[i]] = row[i]
                    yield case
