import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('users_show_user')
@options.galaxy_instance()
@click.argument("user_id", type=str)

@click.option(
    "--deleted",
    help="Include deleted users in listing",
    type=bool
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, user_id, deleted=False):
    """Display information about a user. If ``deleted`` is set to ``True``, display information about a deleted user.
    """
    return ctx.gi.users.show_user(user_id, deleted=deleted)
