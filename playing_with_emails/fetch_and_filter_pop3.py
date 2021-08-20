#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import poplib

def getEmails(search,strip):
    try:
        emails = {}
        M = poplib.POP3_SSL(host = 'pop.gmail.com', port = 995)
        M.user(admin_email)
        M.pass_(admin_pass)
        numMessages = len(M.list()[1])
        for i in range(numMessages):
            for j in M.retr(i+1)[1]:
                line = j.decode("utf-8").strip(strip)
                if search in line:
                    emails[i] = line
        return emails
    except:
        return False
    finally:
        M.quit()
