# need to have requests & time pre-installed
import requests
import time

def deleter(token):
    i = 0
    headers = {'Authorization': token}
    j = requests.get("https://discordapp.com/api/v9/users/@me/channels", headers=headers).json()
    for dm in j:
        i += 1
        dm_id = dm["id"]
        requests.delete(f"https://discordapp.com/api/v9/channels/{dm_id}", headers=headers)
        print(f"deleted dm / groupchat, id {dm_id}, things deleted : {i}")

tok = input("input token : ")
input("press enter to start :D...")
start_time = time.time()
deleter(tok)
end_time = time.time()
time_lapsed = end_time - start_time
input(f"closed {i} dm's / gc's in {time_lapsed}.  ty for using me :)   (click enter to close)...")

# credits to JustSkillNoBan#6646, i coded this lol

# made things better, added a stopwatch (just fixed it p much)
