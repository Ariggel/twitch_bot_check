import pandas, numpy

def calculate(dataset : pandas.DataFrame) -> pandas.DataFrame:
    """
    Classify Twitch users based on heuristic bot-detection rules.

    This function evaluates multiple account-related indicators to determine
    whether a user is likely a bot, possibly a bot, or a legitimate user.
    The classification logic is implemented using vectorized operations.

    Parameters:
        dataset (pandas.DataFrame):
            Input DataFrame containing user metadata. The DataFrame must
            include the following columns:
                - has_avatar (bool): Indicates whether the user has a custom profile image.
                - has_description (bool): Indicates whether the user has a profile description.
                - date_follow (datetime or NaN): Follow date of the streamer,
                  or NaN if the user does not follow the streamer.

    Returns:
        pandas.DataFrame:
            The original DataFrame with an additional column:
                - is_bot (str): Bot classification result with values
                  "Yes", "Possible", or "No".

    Notes:
        - Missing follow information must be represented as NaN.
        - The function operates fully vectorized and is suitable for
          large datasets.
        - The original DataFrame is modified in place and returned for
          convenience.

    """
    conditions_is_bot = [
          (dataset["has_avatar"] == False) & (dataset["has_description"] == False) & (dataset["date_follow"].isna()),
          (dataset["has_avatar"] == False) & (dataset["date_follow"].isna())
    ]
    
    results_is_bot = [
         "Yes"
        ,"Possible"
    ]

    dataset["is_bot"] = numpy.select(
         conditions_is_bot
        ,results_is_bot
        ,default="No"
    )
    
    return dataset
