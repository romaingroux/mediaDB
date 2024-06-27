import pytest
import mediadb.models.medias as medias
import mediadb.models.constants as const
import pathlib as path


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
        file = path.Path("/dir/file.media")

        for l1 in const.Language:
            for l2 in const.Language:
                for t in const.VideoType:
                    movie = medias.Movie(title="Alien",
                                        language=l1,
                                        subtitles=l2,
                                        type=t,
                                        file=file)
                    assert(movie.title == title)
                    assert(movie.language == l1)
                    assert(movie.subtitles == l2)
                    assert(movie.type == const.VideoType.MOVIE) # invariant
                    assert(movie.file == file)
    
    def test_minimal(self):
        """"
        Tests construction with only the minimal arguments (title only).
        Expected to work.
        """
        title = "Alien"
        file = path.Path("/dir/file.media")

        movie = medias.Movie(title=title, file=file)
        assert(movie.title == title)
        assert(movie.language == const.Language.UNKNOWN)
        assert(movie.subtitles == None)
        assert(movie.type == const.VideoType.MOVIE)
        assert(movie.file == file)
    
    def test_no_title(self):
        """
        Test construction with all arguments but title.
        Expected to raise ValueError
        """
        with pytest.raises(ValueError):
            medias.Movie(language=const.Language.ENGLISH,
                         subtitles=const.Language.FRENCH,
                         type=const.VideoType.MOVIE,
                         file=path.Path("/dir/file.media"))
    
    def test_empty_title(self):
        """
        Test construction with all arguments and empty string title.
        Expected to raise ValueError.
        """
        with pytest.raises(ValueError):
            medias.Movie(title="",
                         language=const.Language.ENGLISH,
                         subtitles=const.Language.FRENCH,
                         type=const.VideoType.MOVIE,
                         file=path.Path("/dir/file.media"))

    def test_no_language(self):
        """
        Tests construction without language argument.
        Expected to work.
        """
        title = "Alien"
        file = path.Path("/dir/file.media")
        subtitles = const.Language.ENGLISH
        t = const.VideoType.MOVIE
        movie = medias.Movie(title=title,
                             subtitles=subtitles,
                             type=t,
                             file=file)
        assert(movie.title == title)
        assert(movie.language == const.Language.UNKNOWN)
        assert(movie.subtitles == subtitles)
        assert(movie.type == t) # invariant
        assert(movie.file == file)


    def test_no_subtitles(self):
        """
        Tests construction without subtitles argument.
        Expected to work.
        """
        title = "Alien"
        file = path.Path("/dir/file.media")
        language = const.Language.ENGLISH
        t = const.VideoType.MOVIE
        movie = medias.Movie(title=title,
                             language=language,
                             type=t,
                             file=file)
        assert(movie.title == title)
        assert(movie.language == language)
        assert(movie.subtitles == None)
        assert(movie.type == t) # invariant
        assert(movie.file == file)
    
    def test_no_type(self):
        """
        Tests construction without language argument.
        Expected to work.
        """
        title = "Alien"
        file = path.Path("/dir/file.media")
        language = const.Language.ENGLISH
        subtitles = const.Language.ENGLISH
        movie = medias.Movie(title=title,
                             language=language,
                             subtitles=subtitles,
                             file=file)
        assert(movie.title == title)
        assert(movie.language == language)
        assert(movie.subtitles == subtitles)
        assert(movie.type == const.VideoType.MOVIE) # invariant
        assert(movie.file == file)
    
    def test_no_file(self):
        """
        Tests construction without file argument.
        Expected to fail.
        """
        title = "Alien"
        language = const.Language.ENGLISH
        subtitles = const.Language.ENGLISH
        t = const.VideoType.MOVIE
        with pytest.raises(ValueError):
            medias.Movie(title=title,
                         language=language,
                         subtitles=subtitles,
                         type=t)


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
        file = path.Path("/dir/file.media")

        for l1 in const.Language:
            for l2 in const.Language:
                for t in const.VideoType:
                    doc = medias.Documentary(title=title,
                                             language=l1,
                                             subtitles=l2,
                                             type=t,
                                             file=file)
                    assert(doc.title == title)
                    assert(doc.language == l1)
                    assert(doc.subtitles == l2)
                    assert(doc.type == const.VideoType.DOCUMENTARY) # invariant
                    assert(doc.file == file)
    
    def test_minimal(self):
        """"
        Tests construction with only the minimal arguments (title only).
        Expected to work.
        """
        title = "Bowling for Columbine"
        file = path.Path("/dir/file.media")
        doc = medias.Documentary(title=title, file=file)
        

        assert(doc.title == title)
        assert(doc.language == const.Language.UNKNOWN)
        assert(doc.subtitles == None)
        assert(doc.type == const.VideoType.DOCUMENTARY)
        assert(doc.file == file)
    
    def test_no_title(self):
        """
        Test construction with all arguments but title.
        Expected to raise ValueError.
        """
        with pytest.raises(ValueError):
            medias.Documentary(language=const.Language.ENGLISH,
                               subtitles=const.Language.FRENCH,
                               type=const.VideoType.DOCUMENTARY,
                               file=path.Path("/dir/file.media"))
    
    def test_empty_title(self):
        """
        Test construction with all arguments and empty string title.
        Expected to raise ValueError.
        """
        with pytest.raises(ValueError):
            medias.Documentary(title="",
                               language=const.Language.ENGLISH,
                               subtitles=const.Language.FRENCH,
                               type=const.VideoType.DOCUMENTARY,
                               file=path.Path("/dir/file.media"))

    def test_no_language(self):
        """
        Tests construction without language argument.
        Expected to work.
        """
        title = "Bowling for Columbine"
        file = path.Path("/dir/file.media")
        subtitles = const.Language.ENGLISH
        t = const.VideoType.DOCUMENTARY
        doc = medias.Documentary(title=title,
                                 subtitles=subtitles,
                                 type=t,
                                 file=file)
        assert(doc.title == title)
        assert(doc.language == const.Language.UNKNOWN)
        assert(doc.subtitles == subtitles)
        assert(doc.type == t) # invariant
        assert(doc.file == file)


    def test_no_subtitles(self):
        """
        Tests construction without subtitles argument.
        Expected to work.
        """
        title = "Bowling for Columbine"
        file = path.Path("/dir/file.media")
        language = const.Language.ENGLISH
        t = const.VideoType.DOCUMENTARY
        doc = medias.Documentary(title=title,
                                 language=language,
                                 type=t,
                                 file=file)
        assert(doc.title == title)
        assert(doc.language == language)
        assert(doc.subtitles == None)
        assert(doc.type == t) # invariant
        assert(doc.file == file)
    
    def test_no_type(self):
        """
        Tests construction without language argument.
        Expected to work.
        """
        title = "Bowling for Columbine"
        file = path.Path("/dir/file.media")
        language = const.Language.ENGLISH
        subtitles = const.Language.ENGLISH
        doc = medias.Documentary(title=title,
                                 language=language,
                                 subtitles=subtitles,
                                 file=file)
        assert(doc.title == title)
        assert(doc.language == language)
        assert(doc.subtitles == subtitles)
        assert(doc.type == const.VideoType.DOCUMENTARY) # invariant
        assert(doc.file == file)
    
    def test_no_file(self):
        """
        Tests construction without file argument.
        Expected to fail.
        """
        title = "Bowling for Columbine"
        language = const.Language.ENGLISH
        subtitles = const.Language.ENGLISH
        t = const.VideoType.DOCUMENTARY
        with pytest.raises(ValueError):
            medias.Documentary(title=title,
                               language=language,
                               subtitles=subtitles,
                               type=t)
    

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
        file = path.Path("/dir/file.media")

        for l1 in const.Language:
            for l2 in const.Language:
                for t in const.VideoType:
                    serie = medias.Serie(title=title,
                                         language=l1,
                                         subtitles=l2,
                                         season=season,
                                         episode=episode,
                                         episode_name=episode_name,
                                         type=t,
                                         file=file)
                    assert(serie.title == title)
                    assert(serie.language == l1)
                    assert(serie.subtitles == l2)
                    assert(serie.season == season)
                    assert(serie.episode == episode)
                    assert(serie.episode_name == episode_name)
                    assert(serie.type == const.VideoType.SERIE) # invariant
                    assert(serie.file == file)
    
    def test_minimal(self):
        """"
        Tests construction with only the minimal arguments (title, season, 
        episode).
        Expected to raise ValueError.
        """
        title = "Generation Kill"
        season = 1
        episode = 3
        file = path.Path("/dir/file.media")
        serie = medias.Serie(title="Generation Kill",
                             season=season,
                             episode=episode,
                             file=file)
        assert(serie.title == title)
        assert(serie.language == const.Language.UNKNOWN)
        assert(serie.subtitles == None)
        assert(serie.season == season)
        assert(serie.episode == episode)
        assert(serie.episode_name == None)
        assert(serie.type == const.VideoType.SERIE) # invariant
        assert(serie.file == file)
    
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
                         episode_name="Screwby",
                         file=path.Path("/dir/file.media"))
    
    def test_empty_title(self):
        """
        Tests construction with empty title string.
        Expected to raise ValueError.
        """
        with pytest.raises(ValueError):
            medias.Serie(title="",
                         language=const.Language.ENGLISH,
                         subtitles=const.Language.ENGLISH,
                         type=const.VideoType.SERIE,
                         season=1,
                         episode=3,
                         episode_name="Screwby",
                         file=path.Path("/dir/file.media"))
    
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
        file = path.Path("/dir/file.media")
        serie = medias.Serie(title=title,
                             subtitles=subtitles,
                             type=t,
                             season=season,
                             episode=episode,
                             episode_name=episode_name,
                             file=file)
        assert(serie.title == title)
        assert(serie.language == const.Language.UNKNOWN)
        assert(serie.subtitles == subtitles)
        assert(serie.type == t) # invariant
        assert(serie.episode == episode) 
        assert(serie.season == season) 
        assert(serie.episode_name == episode_name)
        assert(serie.file == file)

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
        file = path.Path("/dir/file.media")
        serie = medias.Serie(title=title,
                             language=language,
                             type=t,
                             season=season,
                             episode=episode,
                             episode_name=episode_name,
                             file=file)
        assert(serie.title == title)
        assert(serie.language == language)
        assert(serie.subtitles == None)
        assert(serie.type == t) # invariant
        assert(serie.episode == episode) 
        assert(serie.season == season) 
        assert(serie.episode_name == episode_name)
        assert(serie.file == file)
    
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
        file = path.Path("/dir/file.media")
        serie = medias.Serie(title=title,
                             language=language,
                             subtitles=subtitles,
                             season=season,
                             episode=episode,
                             episode_name=episode_name,
                             file=file)
        assert(serie.title == title)
        assert(serie.language == language)
        assert(serie.subtitles == subtitles)
        assert(serie.type == const.VideoType.SERIE) # invariant
        assert(serie.episode == episode) 
        assert(serie.season == season) 
        assert(serie.episode_name == episode_name)
        assert(serie.file == file)
    
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
                         episode_name="Screwby",
                         file=path.Path("/dir/file.media"))
    
    def test_0_season(self):
        """
        Tests construction with 0 value season argument.
        Expected to raise ValueError.
        """
        with pytest.raises(ValueError):
            medias.Serie(title="Generation Kill",
                         language=const.Language.ENGLISH,
                         subtitles=const.Language.ENGLISH,
                         type=const.VideoType.SERIE,
                         season=0,
                         episode=3,
                         episode_name="Screwby",
                         file=path.Path("/dir/file.media"))
    
    def test_neg_season(self):
        """
        Tests construction with negative value season argument.
        Expected to raise ValueError.
        """
        with pytest.raises(ValueError):
            medias.Serie(title="Generation Kill",
                         language=const.Language.ENGLISH,
                         subtitles=const.Language.ENGLISH,
                         type=const.VideoType.SERIE,
                         season=-1,
                         episode=3,
                         episode_name="Screwby",
                         file=path.Path("/dir/file.media"))
    
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
                         episode_name="Screwby",
                         file=path.Path("/dir/file.media"))
    
    def test_0_episode(self):
        """
        Tests construction with 0 value episode argument.
        Expected to raise ValueError.
        """
        with pytest.raises(ValueError):
            medias.Serie(title="Generation Kill",
                         language=const.Language.ENGLISH,
                         subtitles=const.Language.ENGLISH,
                         type=const.VideoType.SERIE,
                         season=1,
                         episode=0,
                         episode_name="Screwby",
                         file=path.Path("/dir/file.media"))
    
    def test_neg_episode(self):
        """
        Tests construction with negative value episode argument.
        Expected to raise ValueError.
        """
        with pytest.raises(ValueError):
            medias.Serie(title="Generation Kill",
                         language=const.Language.ENGLISH,
                         subtitles=const.Language.ENGLISH,
                         type=const.VideoType.SERIE,
                         season=1,
                         episode=-1,
                         episode_name="Screwby",
                         file=path.Path("/dir/file.media"))
    
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
        file = path.Path("/dir/file.media")
        serie = medias.Serie(title=title,
                             language=language,
                             subtitles=subtitles,
                             type=t,
                             season=season,
                             episode=episode,
                             file=file)
        assert(serie.title == title)
        assert(serie.language == language)
        assert(serie.subtitles == subtitles)
        assert(serie.type == t) # invariant
        assert(serie.season == season)
        assert(serie.episode == episode)
        assert(serie.episode_name == None)
        assert(serie.file == file)

    def test_empty_episode_name(self):
        """
        Test construction with an empty episode name string argument.
        Expected to fail.
        """
        title = "Generation Kill"
        language = const.Language.ENGLISH
        subtitles = const.Language.ENGLISH
        t = const.VideoType.SERIE
        season = 1
        episode = 3
        file = path.Path("/dir/file.media")
        with pytest.raises(ValueError):
            serie = medias.Serie(title=title,
                                language=language,
                                subtitles=subtitles,
                                type=t,
                                season=season,
                                episode=episode,
                                episode_name="",
                                file=file)
    
    def test_no_file(self):
        """
        Tests construction without file argument.
        Expected to fail.
        """
        title = "Generation Kill"
        language = const.Language.ENGLISH
        subtitles = const.Language.ENGLISH
        t = const.VideoType.SERIE
        season = 1
        episode = 3
        episode_name = "Screwby"
        with pytest.raises(ValueError):
            medias.Serie(title=title,
                         language=language,
                         subtitles=subtitles,
                         season=season,
                         episode=episode,
                         episode_name=episode_name,
                         type=t)
