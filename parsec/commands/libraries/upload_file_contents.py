import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('upload_file_contents')
@click.argument("library_id", type=str)
@click.argument("pasted_content", type=str)

@click.option(
    "--folder_id",
    help="id of the folder where to place the uploaded file. If not provided, the root folder will be used",
    type=str
)
@click.option(
    "--file_type",
    help="Galaxy file format name",
    default="auto",
    type=str
)
@click.option(
    "--dbkey",
    help="Dbkey",
    default="?",
    type=str
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, library_id, pasted_content, folder_id="", file_type="auto", dbkey="?"):
    """Upload pasted_content to a data library as a new file.
    """
    return ctx.gi.libraries.upload_file_contents(library_id, pasted_content, folder_id=folder_id, file_type=file_type, dbkey=dbkey)
