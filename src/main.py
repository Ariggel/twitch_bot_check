from functions import pipelines, credentials
from functions.fnc_data import follow_data

#credentials.get_access_token(scope = "private")


#print(pipelines.extract("ariggeldiggel"))
list = [
"64dragonlord64"
,"arasil__"
,"blutzoll"
,"bsar4"
,"budyja"
,"catotech"
,"deathpunch_gaming"
,"dj3vil"
,"domimnemonic"
,"dreadlp"
,"duudt"
,"flaydynea"
,"j0hnb0y_w4lt0n"
,"kenziecontact"
,"lady_of_flame"
,"martos1"
,"modus_lti"
,"morpheelius"
,"nightwolf_ger"
,"pfandwert"
,"playdiary"
,"sephoran69"
,"splitterniko"
,"steaky187"
,"thecrow1971"
,"tsuki_cat"
,"unbeteiligter01"
,"vesmupwi"
,"zensetzu"
]

streamer = "dschulsii"

print(pipelines.evaluate_bots(list, streamer))