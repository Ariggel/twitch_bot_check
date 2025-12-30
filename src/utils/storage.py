import pandas, os
from datetime import datetime
from utils import paths

def save(dataset : pandas.DataFrame):
    """
    Save a pandas DataFrame to a CSV file with a timestamped filename.

    The filename is generated using the current date and time in the format:
        DD.MM.YYYY_HH-MM_bot_evaluation.csv
    where HH-MM represents the hour and minute in 24-hour format. This ensures
    that each file saved has a unique name.

    The file is saved in the same directory as the path specified by
    `paths.GetPath.data`.

    Parameters:
        dataset (pandas.DataFrame): The DataFrame to be saved as CSV.
    """
    timestamp = datetime.now().strftime("%d.%m.%Y_%H-%M")
    filename = f"{timestamp}_bot_evaluation.csv"
    full_path = os.path.join(paths.GetPath.data,filename)
    dataset.to_csv(full_path, index=False)
    return full_path