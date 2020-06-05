import re
import numpy as np
SPAM = 1
NOT_SPAM = 0

class Filter():
    def __init__(self):
        self.pA = 0
        self.pnotA = 0
        self.dict_spam = {}
        self.dict_no_spam = {}
        self.SPAM = 1
        self.NOT_SPAM = 0
        self.word_spam = 0
        self.word_no_spam = 0
        self.mail_spam = 0
        self.no_spam = 0
        self.spam = 0
        
        
    def train(self, data):
        for  mail, label in data:
            self.calculate_word_frequencies(mail, label)
            if label == SPAM:
                self.mail_spam += 1
        total_mail = len(data)
        self.pA = self.mail_spam / total_mail
        self.pnotA = 1 - self.pA
        
    def calculate_word_frequencies(self, body, lab):
        for i in re.findall(r"\w+",body):
            
            if lab == SPAM:
                self.dict_spam[i.lower()] = self.dict_spam.get(i.lower(),0) + 1
                self.word_spam+=1
            else:
                self.dict_no_spam[i.lower()] = self.dict_no_spam.get(i.lower(),0) + 1
                self.word_no_spam+=1

    def calculate_P_Bi_A(self, word, label):

        if label == SPAM:
            return (self.dict_spam.get(word,0) + 1)/self.word_spam

        else:
            return (self.dict_no_spam.get(word,0) + 1)/self.word_no_spam

    
    def calculate_P_B_A(self, text, label):
        result = 1
        for i in re.findall(r"\w+",text):
            result += np.log(self.calculate_P_Bi_A(i.lower(), label))
        return result

    
    def classify(self, email):
        self.spam = np.log(self.pA)+self.calculate_P_B_A(email, SPAM)
        self.no_spam = np.log(self.pnotA)+self.calculate_P_B_A(email, NOT_SPAM)
        if self.spam > self.no_spam:
            return 'Spam'
        else:
            return 'Not Spam'