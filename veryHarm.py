i = 0
token = "your token here"
headers = {'Authorization': token}
j = requests.get("https://discordapp.com/api/v9/users/@me/channels", headers=headers).json()
for dm in j:
   i += 1
   dm_id = dm["id"]
   requests.delete(f"https://discordapp.com/api/v9/channels/{dm_id}", headers=headers)
   print(f"deleted dm / groupchat, id {dm_id}, things deleted : {i}")

start = input("press enter to start :D...")
deleter()
close = input(f"closed {i} dm's / gc's.  ty for using me :)   (click enter to close)...")

# credits to JustSkillNoBan#6646, i coded this lol