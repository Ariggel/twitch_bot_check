import pandas
from functions import evaluation
from functions.fnc_data import follow_data, user_data
from utils import storage


def extract(username : str, streamer : str) -> pandas.DataFrame:
    data_user = user_data.get(username)
    data_follow_to_streamer = follow_data.to_streamer(username, streamer)

    if not isinstance(data_follow_to_streamer, pandas.DataFrame):
        data_follow_to_streamer = pandas.DataFrame(
            [{"id": data_user.loc[0, "id"], "date_follow": data_follow_to_streamer}]
        )

    dataframe_result = data_user.merge(
        data_follow_to_streamer
        ,on = "id"
        ,how = "left"
    )
    return dataframe_result


def extract_all(username_list : list, streamer : str) -> pandas.DataFrame:
    extraction_list = []
    
    for username in username_list:
        extraction = extract(username, streamer)
        extraction_list.append(extraction)
    dataframe_result = pandas.concat(
        extraction_list
        ,axis=0
        ,ignore_index=True
    )
    return dataframe_result

def evaluate_bots(username_list : list, streamer :str) -> pandas.DataFrame:
    extraction = extract_all(username_list, streamer)
    categorization = evaluation.calculate(extraction)
    storage.save(categorization)
    print(storage.save(categorization))
    return categorization