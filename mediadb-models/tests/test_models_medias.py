import pytest
import mediadb.models.medias as medias
import mediadb.models.constants as const


class TestMovie:
    """
    A test suite for mediadb.models.medias.Movie
    """
    
    def test_default(self):
        """
        Tests contruction of an instance without arguments.
        Expected to raise ValueError.
        """
        with pytest.raises(ValueError):
            medias.Movie()
    
    def test_complete(self):
        """
        Tests construction with all arguments given with all possible 
        combinations of languages and types.
        Expected to work.
        """
        
        title = "Alien"
        for l1 in const.Language:
            for l2 in const.Language:
                for t in const.VideoType:
                    movie = medias.Movie(title="Alien",
                                        language=l1,
                                        subtitles=l2,
                                        type=t)
                    assert(movie.title == title)
                    assert(movie.language == l1)
                    assert(movie.subtitles == l2)
                    assert(movie.type == const.VideoType.MOVIE) # invariant
    
    def test_minimal(self):
        """"
        Tests construction with only the minimal arguments (title only).
        Expected to work.
        """
        title = "Alien"
        movie = medias.Movie(title=title)
        assert(movie.title == title)
        assert(movie.language == const.Language.UNKNOWN)
        assert(movie.subtitles == None)
        assert(movie.type == const.VideoType.MOVIE)
    
    def test_no_title(self):
        """
        Test construction with all arguments but title.
        Expected to raise ValueError
        """
        with pytest.raises(ValueError):
            medias.Movie(language=const.Language.ENGLISH,
                         subtitles=const.Language.FRENCH,
                         type=const.VideoType.MOVIE)

    def test_no_language(self):
        """
        Tests construction without language argument.
        Expected to work
        """
        title = "Alien"
        subtitles = const.Language.ENGLISH
        t = const.VideoType.MOVIE
        movie = medias.Movie(title=title,
                             subtitles=subtitles,
                             type=t)
        assert(movie.title == title)
        assert(movie.language == const.Language.UNKNOWN)
        assert(movie.subtitles == subtitles)
        assert(movie.type == t) # invariant

    def test_no_subtitles(self):
        """
        Tests construction without subtitles argument.
        Expected to work
        """
        title = "Alien"
        language = const.Language.ENGLISH
        t = const.VideoType.MOVIE
        movie = medias.Movie(title=title,
                             language=language,
                             type=t)
        assert(movie.title == title)
        assert(movie.language == language)
        assert(movie.subtitles == None)
        assert(movie.type == t) # invariant
    
    def test_no_type(self):
        """
        Tests construction without language argument.
        Expected to work
        """
        title = "Alien"
        language = const.Language.ENGLISH
        subtitles = const.Language.ENGLISH
        movie = medias.Movie(title=title,
                             language=language,
                             subtitles=subtitles)
        assert(movie.title == title)
        assert(movie.language == language)
        assert(movie.subtitles == subtitles)
        assert(movie.type == const.VideoType.MOVIE) # invariant
        
class TestDocumentary:
    """
    A test suite for mediadb.models.medias.Documentary
    """
    
    def test_default(self):
        """
        Tests contruction of an instance without arguments.
        Expected to raise ValueError.
        """
        with pytest.raises(ValueError):
            medias.Documentary()
    
    def test_complete(self):
        """
        Tests construction with all arguments given with all possible 
        combinations of languages and types.
        Expected to work.
        """
        
        title = "Bowling for Columbine"
        for l1 in const.Language:
            for l2 in const.Language:
                for t in const.VideoType:
                    doc = medias.Documentary(title=title,
                                             language=l1,
                                             subtitles=l2,
                                             type=t)
                    assert(doc.title == title)
                    assert(doc.language == l1)
                    assert(doc.subtitles == l2)
                    assert(doc.type == const.VideoType.DOCUMENTARY) # invariant
    
    def test_minimal(self):
        """"
        Tests construction with only the minimal arguments (title only).
        Expected to work.
        """
        title = "Bowling for Columbine"
        doc = medias.Documentary(title=title)
        assert(doc.title == title)
        assert(doc.language == const.Language.UNKNOWN)
        assert(doc.subtitles == None)
        assert(doc.type == const.VideoType.DOCUMENTARY)
    
    def test_no_title(self):
        """
        Test construction with all arguments but title.
        Expected to raise ValueError
        """
        with pytest.raises(ValueError):
            medias.Documentary(language=const.Language.ENGLISH,
                               subtitles=const.Language.FRENCH,
                               type=const.VideoType.DOCUMENTARY)

    def test_no_language(self):
        """
        Tests construction without language argument.
        Expected to work
        """
        title = "Bowling for Columbine"
        subtitles = const.Language.ENGLISH
        t = const.VideoType.DOCUMENTARY
        doc = medias.Documentary(title=title,
                                 subtitles=subtitles,
                                 type=t)
        assert(doc.title == title)
        assert(doc.language == const.Language.UNKNOWN)
        assert(doc.subtitles == subtitles)
        assert(doc.type == t) # invariant

    def test_no_subtitles(self):
        """
        Tests construction without subtitles argument.
        Expected to work
        """
        title = "Bowling for Columbine"
        language = const.Language.ENGLISH
        t = const.VideoType.DOCUMENTARY
        doc = medias.Documentary(title=title,
                                 language=language,
                                 type=t)
        assert(doc.title == title)
        assert(doc.language == language)
        assert(doc.subtitles == None)
        assert(doc.type == t) # invariant
    
    def test_no_type(self):
        """
        Tests construction without language argument.
        Expected to work
        """
        title = "Bowling for Columbine"
        language = const.Language.ENGLISH
        subtitles = const.Language.ENGLISH
        doc = medias.Documentary(title=title,
                                 language=language,
                                 subtitles=subtitles)
        assert(doc.title == title)
        assert(doc.language == language)
        assert(doc.subtitles == subtitles)
        assert(doc.type == const.VideoType.DOCUMENTARY) # invariant

class TestSerie:
    """
    A test suite for mediadb.models.medias.Serie
    """
    
    def test_default(self):
        """
        Tests contruction of an instance without arguments.
        Expected to raise ValueError.
        """
        with pytest.raises(ValueError):
            medias.Serie()

    def test_complete(self):
        """
        Tests construction with all arguments given with all possible 
        combinations of languages and types.
        Expected to work.
        """
        
        title = "Generation Kill"
        season = 1
        episode = 3
        episode_name = "Screwby"
        for l1 in const.Language:
            for l2 in const.Language:
                for t in const.VideoType:
                    serie = medias.Serie(title=title,
                                         language=l1,
                                         subtitles=l2,
                                         season=season,
                                         episode=episode,
                                         episode_name=episode_name,
                                         type=t)
                    assert(serie.title == title)
                    assert(serie.language == l1)
                    assert(serie.subtitles == l2)
                    assert(serie.season == season)
                    assert(serie.episode == episode)
                    assert(serie.episode_name == episode_name)
                    assert(serie.type == const.VideoType.SERIE) # invariant
    
    def test_minimal(self):
        """"
        Tests construction with only the minimal arguments (title, season, 
        episode).
        Expected to raise ValueError.
        """
        title = "Generation Kill"
        season = 1
        episode = 3
        serie = medias.Serie(title="Generation Kill",
                             season=season,
                             episode=episode)
        assert(serie.title == title)
        assert(serie.language == const.Language.UNKNOWN)
        assert(serie.subtitles == None)
        assert(serie.season == season)
        assert(serie.episode == episode)
        assert(serie.episode_name == None)
        assert(serie.type == const.VideoType.SERIE) # invariant
    
    def test_no_title(self):
        """
        Tests construction without title argument.
        Expected to raise ValueError.
        """
        with pytest.raises(ValueError):
            medias.Serie(language=const.Language.ENGLISH,
                         subtitles=const.Language.ENGLISH,
                         type=const.VideoType.SERIE,
                         season=1,
                         episode=3,
                         episode_name="Screwby")
    
    def test_no_language(self):
        """
        Tests construction without language argument.
        Expected to work
        """
        title = "Generation Kill"
        subtitles = const.Language.ENGLISH
        t = const.VideoType.SERIE
        season = 1
        episode = 3
        episode_name = "Screwby"
        serie = medias.Serie(title=title,
                             subtitles=subtitles,
                             type=t,
                             season=season,
                             episode=episode,
                             episode_name=episode_name)
        assert(serie.title == title)
        assert(serie.language == const.Language.UNKNOWN)
        assert(serie.subtitles == subtitles)
        assert(serie.type == t) # invariant
        assert(serie.episode == episode) 
        assert(serie.season == season) 
        assert(serie.episode_name == episode_name)

    def test_no_subtitles(self):
        """
        Tests construction without subtitles argument.
        Expected to work
        """
        title = "Generation Kill"
        language = const.Language.ENGLISH
        t = const.VideoType.SERIE
        season = 1
        episode = 3
        episode_name = "Screwby"
        serie = medias.Serie(title=title,
                             language=language,
                             type=t,
                             season=season,
                             episode=episode,
                             episode_name=episode_name)
        assert(serie.title == title)
        assert(serie.language == language)
        assert(serie.subtitles == None)
        assert(serie.type == t) # invariant
        assert(serie.episode == episode) 
        assert(serie.season == season) 
        assert(serie.episode_name == episode_name)
    
    def test_no_type(self):
        """
        Tests construction without language argument.
        Expected to work
        """
        title = "Generation Kill"
        language = const.Language.ENGLISH
        subtitles = const.Language.ENGLISH
        season = 1
        episode = 3
        episode_name = "Screwby"
        serie = medias.Serie(title=title,
                             language=language,
                             subtitles=subtitles,
                             season=season,
                             episode=episode,
                             episode_name=episode_name)
        assert(serie.title == title)
        assert(serie.language == language)
        assert(serie.subtitles == subtitles)
        assert(serie.type == const.VideoType.SERIE) # invariant
        assert(serie.episode == episode) 
        assert(serie.season == season) 
        assert(serie.episode_name == episode_name)
    
    def test_no_season(self):
        """
        Tests construction without season argument.
        Expected to raise ValueError.
        """
        with pytest.raises(ValueError):
            medias.Serie(title="Generation Kill",
                         language=const.Language.ENGLISH,
                         subtitles=const.Language.ENGLISH,
                         type=const.VideoType.SERIE,
                         episode=3,
                         episode_name="Screwby")
    
    def test_no_episode(self):
        """
        Tests construction without episode argument.
        Expected to raise ValueError.
        """
        with pytest.raises(ValueError):
            medias.Serie(title="Generation Kill",
                         language=const.Language.ENGLISH,
                         subtitles=const.Language.ENGLISH,
                         type=const.VideoType.SERIE,
                         season=1,
                         episode_name="Screwby")
    
    def test_no_episode_name(self):
        """
        Test construction without episode name argument.
        Expected to work.
        """
        title = "Generation Kill"
        language = const.Language.ENGLISH
        subtitles = const.Language.ENGLISH
        t = const.VideoType.SERIE
        season = 1
        episode = 3
        serie = medias.Serie(title=title,
                             language=language,
                             subtitles=subtitles,
                             type=t,
                             season=season,
                             episode=episode)
        assert(serie.title == title)
        assert(serie.language == language)
        assert(serie.subtitles == subtitles)
        assert(serie.type == t) # invariant
        assert(serie.season == season)
        assert(serie.episode == episode)
        assert(serie.episode_name == None)
