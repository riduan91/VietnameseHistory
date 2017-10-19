# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 15:00:33 2016

@author: ndoannguyen
"""

import sys
sys.path.append('../Configuration/')
sys.path.append('../Basic/')
import configuration
import getWords

DATA_FOLDER = configuration.DATA_FOLDER

def test1():
    testwords = ["Đau", "đớn", "thay", "phận", "đàn", "Bà", 
                 "Ầm", "ầm", "Ũ", "rũ", "cũng", "Là", "lời", "chung."]
    results = [True, False, False, False, False, True, True, False, True,
               False, False, True, False, False]
    print "Test 1:"
    for index in xrange(len(testwords)):
        if getWords.isVNCapital(testwords[index])!=results[index]:
            print "Error at position ", index
            print testwords[index], ": expected", results[index], ", received", getWords.isVNCapital(testwords[index]), "." 
    print "Test 1 finished"
    print "------"

def test2():
    print "Test 2:"
    for properNoun in getWords.retrieveProperNounsFromSentence("Bà đỡ Trần là người huyện Đông Triều."):
        print properNoun
    print "Test 2 finished"
    print ["俆".decode('utf-8')]
    print "------"   

def test3():
    print "Test 3:"
    properNounsFile = open(DATA_FOLDER + 'Danhturieng.txt', 'w')
    properNouns = getWords.retrieveProperNounsFromFile(DATA_FOLDER + 'Khamdinhvietsuthonggiamcuongmuc.txt')
    for properNoun in properNouns:
        properNounsFile.write(properNoun)
        properNounsFile.write("\n")
    print "Test 3 finished"
    print "------"  
    properNounsFile.close()
    return properNouns
    
def test4():
    print "Test 4:"
    getWords.reformat(DATA_FOLDER + 'Khamdinhvietsuthonggiamcuongmuc.txt', DATA_FOLDER + 'Khamdinhvietsuthonggiamcuongmuc_updated.txt')
    getWords.getNotice(DATA_FOLDER + 'Khamdinhvietsuthonggiamcuongmuc_updated.txt', DATA_FOLDER + 'Khamdinhvietsuthonggiamcuongmuc_reupdated.txt', DATA_FOLDER + 'Khamdinhvietsuthonggiamcuongmuc_notice.txt')
    getWords.reformat(DATA_FOLDER + 'Khamdinhvietsuthonggiamcuongmuc_reupdated.txt', DATA_FOLDER + 'Khamdinhvietsuthonggiamcuongmuc_updated.txt')
    print "Test 4 finished."
    print "------" 

def test5():
    print "Test 5:"
    properNounsFile = open(DATA_FOLDER + 'DanhturiengTheoDong.txt', 'w')
    properNouns = getWords.retrieveProperNounsFromFileByLine(DATA_FOLDER + 'Khamdinhvietsuthonggiamcuongmuc_updated.txt')
    for properNoun in properNouns:
        properNounsFile.write(properNoun)
        properNounsFile.write("\n")
    print "Test 5 finished"
    print "------"  
    properNounsFile.close()
    return properNouns

#test1()
#test2()
#test3()
#test4()
#test3()
#test5()