import pathlib

import click

import altendpy.processtemplates


@click.command()
@click.option(
    '--root',
    default='.', type=click.Path(file_okay=False),
    help='Recursively search this directory for templates',
    show_default=True,
)
@click.option(
    '--suffix',
    default='_template',
    help='Extension suffix used to identify templates',
    show_default=True,
    type=str,
)
@click.option(
    '--output-dir',
    default=None, type=click.Path(file_okay=False),
    help='Generated source code in this directory',
    show_default=True,
)
def processtemplates(root, suffix, output_dir):
    """Search for and process templates"""

    root = pathlib.Path(root)
    output_dir = pathlib.Path(output_dir)
    altendpy.processtemplates.process_root(
        root=root,
        suffix=suffix,
        output_dir=output_dir,
        output=click.echo,
    )
