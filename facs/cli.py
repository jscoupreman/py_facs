import click
from facs.command.acquisition import AcquisitionCommand
from facs.command.logs import LogsCommand
from facs.command.resources import ResourcesCommand
from facs.command.extraction import ExtractionCommand
from facs.command.systems import SystemsCommand


cli = click.Group('cli', context_settings=dict(terminal_width=120))
cli.add_command(AcquisitionCommand().get_commands())
cli.add_command(LogsCommand().get_commands())
cli.add_command(ResourcesCommand().get_commands())
cli.add_command(ExtractionCommand().get_commands())
cli.add_command(SystemsCommand().get_commands())

if __name__ == '__main__':
    cli()
