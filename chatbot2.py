# -*- coding: utf-8 -*-
"""
Created on Sat May 23 10:18:56 2020

@author: Gunashekar Chenna
"""

#this is a chat bot prgrame using reflections

from nltk.chat.util import Chat, reflections
pairs = [
        ['my name is (.*)', ['hi %1'] ],
        ['(hi|hello|hey|hola)', ['hey there','hi there', 'hey miss']],
        ['(.*) created you ?' , ['Mr.Guna created me']],
        ['(.*) your name ?' , ['My name is firstbot! ']],
        ['how are you ?',['Im good!, thank you.']]
        ]
chat = Chat(pairs,reflections)
chat.converse()
