from time import sleep

from threading import Thread

import getpass

from k_amino import(

Client,

SubClient

)

print(f"""\033[95mBy Kwel ate You Pizza and _[d]_[n]_[?]_

 ___  _____  ___  ____   __    __  __

 / __)(  _  )/ __)(  _ \ /__\  (  \/  )

( (__  )(_)( \__ \ )___//(__)\  )    (

 \___)(_____)(___/(__) (__)(__)(_/\/\_)

""")

client = Client()

email = input("email: ")

password = getpass.getpass("Password:  ")

client.login(email=email, password=password)

config_time = float(input("break between use:  "))

user_link = client.get_from_link(input("target link:  "))

user_id = user_link.objectId

com_id = user_link.comId

kam_client = SubClient(comId=com_id)

user_info = kam_client.get_user_info(userId=user_id).json

name_user = user_info["nickname"]

personal_chats = kam_client.get_chat_threads(size=100)

for num, title in enumerate(personal_chats.title, 1):

    print(f"{num} :  {title}")

chat_id = personal_chats.chatId[int(input(" Enter host chat number :  ")) -1]

def spam_asistent():

    while True:

        try:

            kam_client.set_cohost(chatId=chat_id, asistent_id=[user_id]),

            kam_client.del_cohost(chatId=chat_id, userId=user_id)

            print(f"set coHost:  {name_user}")

            sleep(config_time)

        except Exception as ExpectingValue:

            print(ExpectingValue)

            

for _ in range(int(input("range for coSpam: "))):

    Thread(target=spam_asistent).start()
