import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('datasets_show_dataset')
@options.galaxy_instance()
@click.argument("dataset_id", type=str)

@click.option(
    "--deleted",
    help="Whether to return results for a deleted dataset",
    type=bool
)
@click.option(
    "--hda_ldda",
    help="Whether to show a history dataset ('hda' - the default) or library dataset ('ldda').",
    type=str
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, dataset_id, deleted=False, hda_ldda=""):
    """Display information about and/or content of a dataset. This can be a history or a library dataset.
    """
    return ctx.gi.datasets.show_dataset(dataset_id, deleted=deleted, hda_ldda=hda_ldda)
