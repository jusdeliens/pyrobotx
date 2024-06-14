from dotenv import dotenv_values
from getpass import getpass

env = dotenv_values(".env") 

ROBOTID = env['ROBOTID'] if 'ROBOTID' in env else input("🤖 robotId: ")
PLAYERID = env['PLAYERID'] if 'PLAYERID' in env else None
USEPROXY = bool(int(env['USEPROXY'])) if 'USEPROXY' in env else False
print(USEPROXY)
ARENA = env['ARENA'] if 'ARENA' in env else input("🎲 arena: ")
BROKERADDRESS = env['BROKERADDRESS'] if 'BROKERADDRESS' in env else input("🌐 server: ")
BROKERPORT = int(env['BROKERPORT']) if 'BROKERPORT' in env else int(input("📭 port: "))
USERNAME = env['USERNAME'] if 'USERNAME' in env else input("👤 username: ")
PASSWORD = ""
if 'PASSWORD' in env:
    PASSWORD = env['PASSWORD'] 
else: 
    print("🔑 password") 
    PASSWORD = getpass("> ")
VERBOSITY = int(env['VERBOSITY']) if 'VERBOSITY' in env else int(input("🪲 verbosity: "))