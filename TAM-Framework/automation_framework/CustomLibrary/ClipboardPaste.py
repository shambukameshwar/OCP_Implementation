# from datetime import datetime

# # start=self.get_slot('startDate')
# # end=self.get_slot('EndDate')
# # lost=self.get_slot('lossdate')
# start="07/20/2015"
# end="10/20/2021"
# lost="12/21/2021"
# valid= False
# startdate= datetime.strptime(start,'%m/%d/%Y')
# enddate= datetime.strptime(end,'%m/%d/%Y')
# lostdate= datetime.strptime(lost,'%m/%d/%Y')
# if ((lostdate >= startdate) and (lostdate <= enddate)):
#     print("valid date")
#     valid=True
# else:
#     print("invalid date")
# print(valid)


# import win32com.client

# outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

# inbox = outlook.GetDefaultFolder(6) # "6" refers to the index of a folder - in this case,
#                                     # the inbox. You can change that number to reference
#                                     # any other folder
# messages = inbox.Items
# message = messages.GetLast()
# body_content = message.body
# print(body_content)

# import win32com.client
# import os
# outlook=win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI")
# inbox=outlook.GetDefaultFolder(6) #Inbox default index value is 6
# message=inbox.Items
# message2=message.GetLast()
# subject=message2.Subject
# body=message2.body
# date=message2.senton.date()
# sender=message2.Sender
# attachments=message2.Attachments
# for m in message:
#     if m.Subject=="Test mail":# here in my requirement i will change the dates
#         print(m.body)

import pyperclip as pc
a = pc.paste()
print(a)