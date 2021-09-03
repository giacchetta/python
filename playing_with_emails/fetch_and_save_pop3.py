#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os,poplib

admin_email = os.getenv('ADMIN_EMAIL')
admin_pass = os.getenv('ADMIN_PASS')

def getEmails():
    try:
        emails = {}
        M = poplib.POP3_SSL(host = 'pop.gmail.com', port = 995)
        M.user(admin_email)
        M.pass_(admin_pass)
        file = open('invite.eml','wb')   
        numMessages = len(M.list()[1])
        for i in range(numMessages):
            for j in M.retr(i+1)[1]:
                file.write(j)
        file.close()
        return emails
    except:
        return False
    finally:
        M.quit()

getEmails()