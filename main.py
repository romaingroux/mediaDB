import lib.models.constants as const
import lib.models.medias as medias


if __name__ == "__main__":
    
    movie = medias.Movie(title="Il faut sauver le soldat ryan",
                         type=const.VideoType.SERIE)
    print(movie)
    
    
    serie = medias.Serie(title="Friends",
                         season=1,
                         episode=1,
                         type=const.VideoType.MOVIE)
    print(serie)