import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('libraries_set_library_permissions')
@options.galaxy_instance()
@click.argument("library_id", type=str)

@click.option(
    "--access_in",
    help="list of user ids",
    type=list
)
@click.option(
    "--modify_in",
    help="list of user ids",
    type=list
)
@click.option(
    "--add_in",
    help="list of user ids",
    type=list
)
@click.option(
    "--manage_in",
    help="list of user ids",
    type=list
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, library_id, access_in="", modify_in="", add_in="", manage_in=""):
    """Sets the permissions for a library.  Note: it will override all security for this library even if you leave out a permission type.
    """
    return ctx.gi.libraries.set_library_permissions(library_id, access_in=access_in, modify_in=modify_in, add_in=add_in, manage_in=manage_in)
