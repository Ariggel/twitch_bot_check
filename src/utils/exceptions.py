class TwitchAPIError(Exception):
    """base class for exceptions"""

class TwitchUserNotFound(TwitchAPIError):
    pass

class TwitchAuthError(TwitchAPIError):
    pass

class TwitchRateLimitError(TwitchAPIError):
    pass

class TwitchBadResponse(TwitchAPIError):
    pass