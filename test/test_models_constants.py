import pytest
import lib.models.constants as const



class TestLanguage:
    """
    A test suite for the lib.models.Language class.
    """
    
    def test_values(self):
        assert(len(const.Language) == 4)
        assert(const.Language.ENGLISH == "EN")
        assert(const.Language.FRENCH == "FR")
        assert(const.Language.GERMAN == "DE")
        assert(const.Language.UNKNOWN == "unknown")


class TestVideoType:
    """
    A test suite for the lib.models.VideoType class.
    """
    
    def test_values(self):
        assert(len(const.VideoType) == 4)
        assert(const.VideoType.SERIE == "serie")
        assert(const.VideoType.MOVIE == "movie")
        assert(const.VideoType.DOCUMENTARY == "documentary")
        assert(const.VideoType.UNKNOWN == "unknown")
