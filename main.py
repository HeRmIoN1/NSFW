#by Hermione
import time 
import fade
from colorama import Fore
import requests
import sys
import os
from discord_webhook import DiscordWebhook, DiscordEmbed
def webh():
 banner = """

            ─────────────────────────────────────────────────────────────────────────────────────────────────────
                ─██████████████─██████████─████████████████───██████████████─██████████████─██████████████─
                ─██░░░░░░░░░░██─██░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
                ─██░░██████░░██─████░░████─██░░████████░░██───██░░██████░░██─██████░░██████─██░░██████████─
                ─██░░██──██░░██───██░░██───██░░██────██░░██───██░░██──██░░██─────██░░██─────██░░██─────────
                ─██░░██████░░██───██░░██───██░░████████░░██───██░░██████░░██─────██░░██─────██░░██████████─
                ─██░░░░░░░░░░██───██░░██───██░░░░░░░░░░░░██───██░░░░░░░░░░██─────██░░██─────██░░░░░░░░░░██─
                ─██░░██████████───██░░██───██░░██████░░████───██░░██████░░██─────██░░██─────██░░██████████─
                ─██░░██───────────██░░██───██░░██──██░░██─────██░░██──██░░██─────██░░██─────██░░██─────────
                ─██░░██─────────████░░████─██░░██──██░░██████─██░░██──██░░██─────██░░██─────██░░██████████─
                ─██░░██─────────██░░░░░░██─██░░██──██░░░░░░██─██░░██──██░░██─────██░░██─────██░░░░░░░░░░██─
                ─██████─────────██████████─██████──██████████─██████──██████─────██████─────██████████████─
            ──────────────────────────────────────────────────────────────────────────────────────────────────────
"""   
 faded_banner = fade.pinkred(banner)
 for o in faded_banner:
     time.sleep(0.0001)
     sys.stdout.write(o)
     sys.stdout.flush()
 time.sleep(1.3)
 url = input(f'{Fore.CYAN}Enter discord webhook:\n{Fore.BLUE}>>> {Fore.GREEN}')
 def loop():
  category = input(f'{Fore.CYAN}Select an Category:\t{Fore.YELLOW}({Fore.LIGHTRED_EX}anal{Fore.YELLOW},{Fore.LIGHTRED_EX}blowjob{Fore.YELLOW},{Fore.LIGHTRED_EX}cum{Fore.YELLOW},{Fore.LIGHTRED_EX}neko{Fore.YELLOW},{Fore.LIGHTRED_EX}pussylick{Fore.YELLOW},{Fore.LIGHTRED_EX}solo{Fore.YELLOW},{Fore.LIGHTRED_EX}yuri{Fore.YELLOW},{Fore.LIGHTRED_EX}yaoi{Fore.YELLOW},{Fore.LIGHTRED_EX}threesome_ffm{Fore.YELLOW},{Fore.LIGHTRED_EX}threesome_fff{Fore.YELLOW}){Fore.GREEN}\n{Fore.BLUE}>>>{Fore.GREEN} ')
  os.system('cls')
  webhook2 = DiscordWebhook(url=url)
  embed = DiscordEmbed(title='title', description='des', color='03b2f8')
  image = requests.get(f'https://purrbot.site/api/img/nsfw/{category}/gif')
  if image.status_code == 200:
    webhook = DiscordWebhook(url=url, content='@everyone')
    embed = DiscordEmbed(title="Nude Sender", description=f"category : {category}", color='03b2f8')
    embed.set_image(url=f'{image.json()["link"]}')
    embed.set_author(name='Pirate Tool', url='https://discord.gg/kos')
    embed.set_timestamp()
    webhook2.add_embed(embed)
    response = webhook.execute()
    response = webhook2.execute(embed)
  else:
     print('error')
 while True:
   loop()
webh()
