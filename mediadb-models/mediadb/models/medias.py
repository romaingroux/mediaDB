from pydantic import BaseModel, field_validator, model_validator
import typing as tp
import typing_extensions as tp_ext
import abc
import mediadb.models.constants as const


class VideoMedia(BaseModel, abc.ABC):
    """
    An abstract base model for any video media.
    """

    """the media title"""
    title: str
    """the media audio language"""
    language: const.Language = const.Language.UNKNOWN
    """the media subtitle language, None if no subtitles"""
    subtitles: tp.Optional[const.Language] = None
    """the media type"""
    type: const.VideoType = const.VideoType.UNKNOWN
    
    @field_validator("title")
    @classmethod
    def check_notempty(cls, value: str) \
        -> str:
        """
        Checks that the fields are not empty 
        nor None.
        Args:
            title: the value to check.
        Returns: the given value.
        """
        # if value is None:
        #     raise ValueError("value cannot be None")
        if value == "":
            raise ValueError("value cannot be empty")
        return value

    
class Movie(VideoMedia):
    """
    A class modeling a movie.
    """
    
    @model_validator(mode="after")
    def set_type(self) \
        -> tp_ext.Self:
        """
        Forces type to MOVIE.
        Returns: the instance itself.
        """
        self.type = const.VideoType.MOVIE
        return self


class Documentary(VideoMedia):
    """
    A class modeling a documentary.
    """
    
    @model_validator(mode="after")
    def set_type(self) \
        -> tp_ext.Self:
        """
        Forces type to DOCUMENTARY.
        Returns: the instance itself.
        """
        self.type = const.VideoType.DOCUMENTARY
        return self


class Serie(VideoMedia):
    """
    A class modeling a serie episode
    """
    
    @model_validator(mode="after")
    def set_type(self) \
        -> tp_ext.Self:
        """
        Forces type to SERIE.
        Returns: the instance itself.
        """
        self.type = const.VideoType.SERIE
        return self
    
    @field_validator("season", "episode")
    @classmethod
    def is_bigger_zero(cls, value: int) \
        -> int:
        """
        Checks that the given int is 
        non 0 and positive.
        """
        if value > 0:
            return value
        else:
            raise ValueError("value must be > 0 ({value})")
    
    @field_validator("episode_name")
    @classmethod
    def check_notempty_serie(cls, value: str) \
        -> str:
        """
        Checks that the value is not empty.
        Args:
            value: the value to check
        Returns: the given value.
        """
        if value == "":
            raise ValueError("value cannot be empty")
        return value
    
    """The season number, must be > 0"""
    season: int
    """The episode number, must be > 0"""
    episode: int
    """The episode name, optionnal"""
    episode_name: tp.Optional[str] = None

