import enum


class StrEnum(str, enum.Enum):
    """
    A string enumeration class.
    """
    pass


class Language(StrEnum):
    """
    The possible video languages.
    """
    ENGLISH = "EN"
    FRENCH = "FR"
    GERMAN = "DE"
    UNKNOWN = "unknown"


class VideoType(StrEnum):
    """
    The possible video types.
    """
    SERIE = "serie"
    MOVIE = "movie"
    DOCUMENTARY = "documentary"
    UNKNOWN = "unknown"
