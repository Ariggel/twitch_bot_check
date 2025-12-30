from functions import pipelines, credentials
from functions.fnc_data import follow_data

#credentials.get_access_token(scope = "private")


#print(pipelines.extract("ariggeldiggel"))
list = [
"arasil__"
,"bsar4"
,"budyja"
,"dj3vil"
,"doctor_kingeis"
,"headhunterspyro"
,"j0hnb0y_w4lt0n"
,"lady_of_flame"
,"seniorsebi"
,"therealplobi"
,"von_kreutz"
,"xhaos_morgaine"
,"xpummelhummelx"
]

streamer = "dschulsii"

print(pipelines.evaluate_bots(list, streamer))