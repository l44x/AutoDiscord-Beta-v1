import requests
import random
import time as cm
from colorama import Fore, init

init(autoreset=True)

def banner():
    bnn = r"""
                                                  ______
                                               .-"      "-.       ▓█████ ▄████▄   ██░ ██  ██ ▄█▀    
                                              /            /      ▓█   ▀▒██▀ ▀█  ▓██░ ██▒ ██▄█▒            
                                             |              |     ▒███  ▒▓█    ▄ ▒██▀▀██░▓███▄░        
                                             |,  .-.  .-.  ,|     ▒▓█  ▄▒▓▓▄ ▄██▒░▓█ ░██ ▓██ █▄ 
                                             | )(_o/  \o_)( |     ░▒████▒ ▓███▀ ░░▓█▒░██▓▒██▒ █▄
                                             |/     /\     \|     ░░ ▒░ ░ ░▒ ▒  ░ ▒ ░░▒░▒▒ ▒▒ ▓▒  
                                   (@_       (_     ^^     _)      ░ ░  ░ ░  ▒    ▒ ░▒░ ░░ ░▒ ▒░
                              _     ) \_______\__|IIIIII|__/_____  ░  ░         ░  ░░ ░░ ░░ ░ 
                             (_)@8@8{}<________|-\IIIIII/-|___________________________>
                                    )_/        \          /
                                   (@           `--------`
    """
    print(Fore.RED + f"{bnn}")

def discordChangeNameGroup(id_channel):
    main_url=f"https://discord.com/api/v9/channels/{id_channel}"

    s = requests.Session()
    token = str(input(Fore.LIGHTCYAN_EX+"\t\t\t\t[+] Enter Your Token > "+Fore.BLACK))

    messages_data = []

    print("-------------------------------------------")
    print(Fore.BLUE+f"\t||||||||\t\t\tIngresa los mensajes que deseas enviar. Escribe 'q' para finalizar.")
    while True:
        msg_input = input(Fore.BLUE+f"\t||||||||\t\t\t> Ingresa un mensaje o 'q' para salir: "+Fore.LIGHTMAGENTA_EX)
        if msg_input == 'q':
            break
        messages_data.append(msg_input)
    print(Fore.WHITE+"-------------------------------------------\n")
    initial_messages = messages_data.copy()


    header={
        'Authorization': f'{token}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
    }

    print(Fore.WHITE+"-------------------------------------------")
    while True:
        if not messages_data:
            messages_data = initial_messages.copy()

        msg = random.choice(messages_data)
        messages_data.remove(msg) 

        data_status = {
            "name":f"{msg}",
            "type":2,
            "user_limit": 1,
        }

        r = requests.patch(main_url, headers=header, json=data_status)

        if r.status_code == 200:
            print(Fore.GREEN + f"> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ [200 STATUS - NAME GROUP SUCCESSLY]")
            cm.sleep(0.5)
        else:
            print(Fore.RED + f"> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ [INVALID STATUS ERROR - NAME GROUP FAILED]")
            cm.sleep(0.5)

def discordChangeStatusGroup(id_channel):
    main_url=f"https://discord.com/api/v9/channels/{id_channel}/voice-status"

    s = requests.Session()
    token = str(input(Fore.LIGHTCYAN_EX+"\t\t\t\t[+] Enter Your Token > "+Fore.BLACK))
    messages_data = []

    print("-------------------------------------------")
    print(Fore.BLUE+f"\t||||||||\t\t\tIngresa los mensajes que deseas enviar. Escribe 'q' para finalizar.")
    while True:
        msg_input = input(Fore.BLUE+f"\t||||||||\t\t\t> Ingresa un mensaje o 'q' para salir: "+Fore.LIGHTMAGENTA_EX)
        if msg_input == 'q':
            break
        messages_data.append(msg_input)
    print(Fore.WHITE+"-------------------------------------------\n")
    initial_messages = messages_data.copy()

    header={
        'Authorization': f'{token}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
    }

    while True:
        if not messages_data:
            messages_data = initial_messages.copy()

        msg = random.choice(messages_data)
        messages_data.remove(msg)  

        data_status = {
            "status": f"{msg}"
        }

        r = requests.put(main_url, headers=header, json=data_status)
        print(Fore.GREEN + f"> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ [200 STATUS - Name Group Created Successfully]")
        cm.sleep(0.2)

def discordChangeNickName(server_id):
    main_url=f"https://discord.com/api/v9/guilds/{server_id}/members/@me"

    s = requests.Session()
    token = str(input(Fore.LIGHTCYAN_EX+"\t\t\t\t[+] Enter Your Token > "+Fore.BLACK))
    messages_data = []

    print("-------------------------------------------")
    print(Fore.BLUE+f"\t||||||||\t\t\tIngresa los mensajes que deseas enviar. Escribe 'q' para finalizar.")
    while True:
        msg_input = input(Fore.BLUE+f"\t||||||||\t\t\t> Ingresa un mensaje o 'q' para salir: "+Fore.LIGHTMAGENTA_EX)
        if msg_input == 'q':
            break
        messages_data.append(msg_input)
    print(Fore.WHITE+"-------------------------------------------\n")
    initial_messages = messages_data.copy()

    header={
        'Authorization': f'{token}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
    }

    while True:
        if not messages_data:
            messages_data = initial_messages.copy()

        msg = random.choice(messages_data)
        messages_data.remove(msg)  

        data_status = {
            "nick": f"{msg}"
        }

        r = requests.patch(main_url, headers=header, json=data_status)

        if r.status_code == 200:
            print(Fore.GREEN + f"> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ [200 STATUS - Nickname Change Successfully]")
            cm.sleep(10)
        else:
            print(Fore.RED + f"> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ [INVALID STATUS ERROR - Nickname Change Failed]")
            cm.sleep(10)

def raidChannelTemp(server_id, channel_id, user_id, categoria_id, nickname_channel, amount):

    main_url=f"https://discord.com/api/v9/guilds/{server_id}/channels"

    s = requests.Session()

    token = str(input(Fore.LIGHTCYAN_EX+"\t\t\t\t[+] Enter Your Token > "+Fore.BLACK))

    header={
        'Authorization': f'{token}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        'Content-Type': 'application/json',
        'Referer': f'https://discord.com/channels/{server_id}/{channel_id}',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
    }

    for i in range(0, amount):
        data_status ={  
                "type":2,
                "name": f"{nickname_channel}",  # name_channel_duplicated
                "permission_overwrites":[
                    {
                        "id": f"{server_id}", # server_id
                        "type":0,
                        "allow":"268436496",
                        "deny":"0"
                    },
                    {
                        "id":"472911936951156740",
                        "type":1,
                        "allow":"286542865",
                        "deny":"0"
                    },
                    {
                        "id": f"{user_id}",  #usuario
                        "type":1,
                        "allow":"1048576",
                        "deny":"0"
                    }
                ],
                "parent_id": f"{categoria_id}" # categoria_id
                }

        r = requests.post(main_url, headers=header, json=data_status)
        print(Fore.GREEN + f"> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ [200 STATUS - Temporary Channel Successfully Created]")

def discordOnCall():
    
    banner()
    print("-------------------------------------------")
    print(Fore.GREEN + f"\t|\t\t\tAutoDiscord Beta v1")
    print(Fore.GREEN + f"\t|\t\t\tCredits > Ech0k")
    print(Fore.GREEN + f"\t|\t\t\thttps://github.com/l44x")
    print("-------------------------------------------\n")

    options=["Autochange Your Group Name", "Autochange Your Status Group", "Autochange Your Nickname", "Raid Temps Channels"]

    print("-------------------------------------------")
    for index,optione in enumerate(options):
            print(Fore.RED + f"\t||\t\t\t[AutoDiscord - Menu Options] > " + Fore.CYAN + f"[{index+1}]" +  " > " +  Fore.GREEN + f"{optione}")
    print("-------------------------------------------\n")

    print("-------------------------------------------")
    option = int(input(Fore.YELLOW+"\t||||\t\t\t~ [M3NU OPTIONS CONTROL by: Ech0k] Selecciona una opcion > " + Fore.WHITE))
    print("-------------------------------------------\n")
    if option == 1:
        print("-------------------------------------------")
        id_channel_send = str(input(f"\t||||||\t\t\t> Enter your Channel ID > "))
        print("-------------------------------------------\n")
        discordChangeNameGroup(id_channel_send)
    elif option == 2:
        print("-------------------------------------------")
        id_channel_send = str(input(f"\t|\t\t\t> Enter your Channel ID > "))
        print("-------------------------------------------\n")
        discordChangeStatusGroup(id_channel_send)
    elif option == 3:
        print("-------------------------------------------")
        server_id_send = str(input(f"\t|\t\t\t> Enter your Server ID > "))
        print("-------------------------------------------\n")
        discordChangeNickName(server_id_send)
    elif option == 4:
        print("-------------------------------------------")
        server_id = str(input(Fore.LIGHTMAGENTA_EX+f"\t||||||||||\t\t> Enter Server ID: "+Fore.YELLOW))
        categoria_id = str(input(Fore.LIGHTMAGENTA_EX+f"\t||||||||||\t\t> Enter Category ID: "+Fore.YELLOW))
        nick_name_channel = str(input(Fore.LIGHTMAGENTA_EX+f"\t||||||||||\t\t> Enter Nickname Channel: "+Fore.YELLOW))
        id_channel = str(input(Fore.LIGHTMAGENTA_EX+f"\t||||||||||\t\t> Enter Channel ID: "+Fore.YELLOW))
        user_id = str(input(Fore.LIGHTMAGENTA_EX+f"\t||||||||||\t\t> Enter User ID: "+Fore.YELLOW))
        amount_v = int(input(Fore.LIGHTMAGENTA_EX+f"\t||||||||||\t\t> Enter Amount Channels: "+Fore.YELLOW))
        raidChannelTemp(server_id, id_channel, user_id, categoria_id, nick_name_channel, amount_v)

if __name__ == '__main__':
    discordOnCall()
