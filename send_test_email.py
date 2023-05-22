#! /usr/bin/python

# Imports
import requests
import os
def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/sandboxa23eea2d073241058ce1703da7ba11a2.mailgun.org/messages",
		auth=("api", "becd0fee112532e388a257f368b3c942-50f43e91-9541815d"),
		data={"from": "Me <mailgun@sandboxa23eea2d073241058ce1703da7ba11a2.mailgun.org>",
			"to": ["artaimer00@gmail.com"],
			"subject": "test",
			"text": "xin day met lam r"})
request = send_simple_message()
print ('Status: '+format(request.status_code))
print ('Body:'+ format(request.text))
os.system("aplay /home/pi/mo.wav")

