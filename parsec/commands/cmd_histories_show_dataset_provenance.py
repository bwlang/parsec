import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('histories_show_dataset_provenance')
@options.galaxy_instance()
@click.argument("history_id", type=str)
@click.argument("dataset_id", type=str)

@click.option(
    "--follow",
    help="If ``follow`` is ``True``, recursively fetch dataset provenance information for all inputs and their inputs, etc....",
    type=bool
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, history_id, dataset_id, follow=False):
    """Get details related to how dataset was created (``id``, ``job_id``, ``tool_id``, ``stdout``, ``stderr``, ``parameters``, ``inputs``, etc...).
    """
    return ctx.gi.histories.show_dataset_provenance(history_id, dataset_id, follow=follow)
