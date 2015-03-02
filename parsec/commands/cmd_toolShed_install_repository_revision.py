import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('toolShed_install_repository_revision')
@options.galaxy_instance()
@click.argument("tool_shed_url", type=str)
@click.argument("name", type=str)
@click.argument("owner", type=str)
@click.argument("changeset_revision", type=str)

@click.option(
    "--install_tool_dependencies",
    help="Whether or not to automatically handle tool dependencies (see http://wiki.galaxyproject.org/AToolOrASuitePerRepository for more details)",
    type=bool
)
@click.option(
    "--install_repository_dependencies",
    help="Whether or not to automatically handle repository dependencies (see http://wiki.galaxyproject.org/DefiningRepositoryDependencies for more details)",
    type=bool
)
@click.option(
    "--tool_panel_section_id",
    help="The ID of the Galaxy tool panel section where the tool should be insterted under. Note that you should specify either this parameter or the ``new_tool_panel_section_label``. If both are specified, this one will take precedence.",
    type=str
)
@click.option(
    "--new_tool_panel_section_label",
    help="The name of a Galaxy tool panel section that should be created and the repository installed into.",
    type=str
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, tool_shed_url, name, owner, changeset_revision, install_tool_dependencies=False, install_repository_dependencies=False, tool_panel_section_id="", new_tool_panel_section_label=""):
    """Install a specified repository revision from a specified Tool Shed into this Galaxy instance. This example demonstrates installation of a repository that contains valid tools, loading them into a section of the Galaxy tool panel or creating a new tool panel section. You can choose if tool dependencies or repository dependencies should be installed, use ``install_tool_dependencies`` or ``install_repository_dependencies``.
    """
    return ctx.gi.toolShed.install_repository_revision(tool_shed_url, name, owner, changeset_revision, install_tool_dependencies=install_tool_dependencies, install_repository_dependencies=install_repository_dependencies, tool_panel_section_id=tool_panel_section_id, new_tool_panel_section_label=new_tool_panel_section_label)
