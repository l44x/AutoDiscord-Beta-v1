import requests
import json, random,time 
def get_discord():
    data_url="https://discord.com/api/v9/users/@me/clan"
    s = requests.Session()

    id_clan = ["ID_CLAN_GUILD", "ID_CLAN_GUILD", "ID_CLAN_GUILD"]

    header={
        'Host': 'discord.com',
        'Authorization': f'<YOUR_TOKEN>',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0',
        'Referer': 'https://discord.com/channels/@me',
        'Origin': 'https://discord.com'
    }

    while True:
        if not id_clan:
            id_clan = ["ID_CLAN_GUILD", "ID_CLAN_GUILD", "ID_CLAN_GUILD"]
        clan = random.choice(id_clan)
        data = {
            "identity_guild_id":f"{clan}",
            "identity_enabled": True
        }

        id_clan.remove(clan) 
        r = requests.put(data_url, headers=header, json=data)

        print(f"Mensaje enviado: {data}")
        print(f"Status Code: {r.content}")
        time.sleep(.4)

if __name__ == '__main__':
    get_discord()
