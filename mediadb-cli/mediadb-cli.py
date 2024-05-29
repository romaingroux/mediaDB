import click
import mediadb.models.constants as const
import mediadb.models.medias as medias
# from lib.models import medias as medias


# the language value list
lang_list = [x.value for x in const.Language]
# the language value set
lang_set = set(lang_list)
# a str with a coma separated language list
lang_str = (", ").join(lang_list)


# def validate_language(ctx,
#                       param, 
#                       value: str) \
#     -> str:
#     """
#     Checks that value is a valid const.Language element.
#     Args:
#         ctx: click stuff
#         param: click stuff
#         value: the value to check.
#     Returns:
#         The value to check if the test passes.
#     Raises:
#         click.BadParameter if the test fails.
#     """
#     if value in lang_set:
#         return value
#     else:
#         raise click.BadParameter(f"language is not accepted ({value})")


# def validate_subtitles(ctx,
#                        param, 
#                        value: str) \
#     -> str:
#     """
#     Checks that value is a valid const.Language element or None (which 
#     is an accepted subtitle value in Movie, Documentary and Serie)
#     Args:
#         ctx: click stuff
#         param: click stuff
#         value: the value to check.
#     Returns:
#         The value to check if the test passes.
#     Raises:
#         click.BadParameter if the test fails.
#     """
#     if value is None:
#         return None
#     else:
#         return validate_language(ctx, param, value)


# def validate_season(ctx,
#                     para,
#                     value: int) \
#     -> int:
#     """
#     Checks that the season number is > 0.
#     Args:
#         ctx: click stuff
#         param: click stuff
#         value: the value to check.
#      Returns:
#         The value to check if the test passes.
#     Raises:
#         click.BadParameter if the test fails.
#     """
#     if value > 0:
#         return value
#     else:
#         raise click.BadParameters(f"Season number must be > 0 ({value})")
    

# def validate_episode(ctx,
#                      para,
#                      value: int) \
#     -> int:
#     """
#     Checks that the episode number is > 0.
#     Args:
#         ctx: click stuff
#         param: click stuff
#         value: the value to check.
#      Returns:
#         The value to check if the test passes.
#     Raises:
#         click.BadParameter if the test fails.
#     """
#     if value > 0:
#         return value
#     else:
#         raise click.BadParameters(f"Season episode must be > 0 ({value})")


@click.group()
def cli():
    """
    CLI entry point for other commands.
    """
    pass


@click.command()
@click.option("--title", 
              required=True,
              type=str,
              help="The movie title")
@click.option("--language",
              required=True,
              help=f"The movie language, accepted values are: {lang_str}")
@click.option("--subtitles",
              type=str,
              default=None,
              help=f"The movie subtitle language, accepted values are: " \
                  f"{lang_str}")
def create_movie_document(title: str,
                          language: str,
                          subtitles: str):
    """
    Prints a Movie document in JSON format on stdout. 
    """
    click.echo(medias.Movie(title=title,
                            language=language,
                            subtitles=subtitles).model_dump_json())


@click.command()
@click.option("--title", 
              required=True,
              type=str,
              help="The movie title")
@click.option("--language",
              required=True,
              help=f"The movie language, accepted values are: {lang_str}")
@click.option("--subtitles",
              type=str,
              default=None,
              help=f"The movie subtitle language, accepted values are: " \
                   f"{lang_str}")
def create_documentary_document(title: str,
                                language: str,
                                subtitles: str):
    """
    Prints a Movie document in JSON format on stdout. 
    """
    click.echo(medias.Documentary(title=title,
                                  language=language,
                                  subtitles=subtitles).model_dump_json())


@click.command()
@click.option("--title", 
              required=True,
              type=str,
              help="The movie title")
@click.option("--language",
              required=True,
              help=f"The movie language, accepted values are: {lang_str}")
@click.option("--subtitles",
              type=str,
              default=None,
              help=f"The movie subtitle language, accepted values are: " \
                  f"{lang_str}")
@click.option("--season", 
              type=int,
              required=True,
              help="The season number")
@click.option("--episode", 
              type=int,
              required=True,
              help="The episode number")
@click.option("--name",
              type=str,
              default=None,
              help="Episode name.")
def create_serie_document(title: str,
                          language: str,
                          subtitles: str,
                          season: int,
                          episode: int,
                          name: str):
    """
    Prints a Serie document in JSON format on stdout. 
    """
    click.echo(medias.Serie(title=title,
                            language=language,
                            subtitles=subtitles,
                            season=season,
                            episode=episode,
                            episode_name=name).model_dump_json())


# @click.command()
# def check_document():
#     click.echo("checking document")


cli.add_command(create_movie_document)
cli.add_command(create_documentary_document)
cli.add_command(create_serie_document)
# cli.add_command(check_document)


# if __name__ == "__main__":
#     cli()

if __name__ == "__main__":
    cli()
    # create_movie_document()