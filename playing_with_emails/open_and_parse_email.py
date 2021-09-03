#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email import policy
import email


def getEmails():
    try:
        emails = {}
        file = open('invite.eml','r')
        msg = file.read()
        file.close()

        msg = email.message_from_string(msg, policy = policy.default)
        body = msg.get_body(preferencelist=('plain')).get_content()
        arr = body.splitlines()
        test = '/login/invite'
        for line in arr:
            if test in line:
                emails.update({0: line.strip('<>')})
        return emails
    except:
        return False

print(getEmails())