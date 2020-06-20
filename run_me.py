from pages.accountDetails import AccountDetail
from pages.chabot import Chabot

print('''

  ______   .__   __.  _______  __    __       ___       ______  __  ___     __    __       _______.
 /  __  \  |  \ |  | |   ____||  |  |  |     /   \     /      ||  |/  /    |  |  |  |     /       |
|  |  |  | |   \|  | |  |__   |  |__|  |    /  ^  \   |  ,----'|  '  /     |  |  |  |    |   (----`
|  |  |  | |  . `  | |   __|  |   __   |   /  /_\  \  |  |     |    <      |  |  |  |     \   \
|  `--'  | |  |\   | |  |____ |  |  |  |  /  _____  \ |  `----.|  .  \   __|  `--'  | .----)   |
 \______/  |__| \__| |_______||__|  |__| /__/     \__\ \______||__|\__\ (__)\______/  |_______/


''')

print("|=================================|")
print("|                                 |")
print("|    PLEASE USE 'USA' VPN         |")
print("|                                 |")
print("|                                 |")
print("|            Modified by Beast    |")
print("|                Original: dydx   |")
print("|=================================|")

email = input("Enter your email (do not enter Fake) : ")
accountdetails = AccountDetail()
info = accountdetails.getInfo()
print(info)
chabot = Chabot(info, email)
chabot.start_process()