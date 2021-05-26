import click
from facs.command.abstract import AbstractCommand


class AcquisitionCommand(AbstractCommand):
    def __init__(self):
        super().__init__('acquisition.yaml')

    def get_commands(self):
        group = click.Group(
            'acquisition',
            help='cheat sheets related to data acquisition (info, dump, mount)',
            context_settings=dict(terminal_width=120)
        )

        group.add_command(click.Command(
            name='checklist', help='reminders to ensure chain of custody when performing an acquisition',
            callback=self.checklist
        ))

        group.add_command(click.Command(
            name='collect', help='cheat sheet to collect info about a disk',
            callback=self.collect_info,
        ))

        group.add_command(click.Command(
            name='dump', help='cheat sheet to dump disk or memory',
            callback=self.dump,
        ))

        group.add_command(click.Command(
            name='mount', help='cheat sheet to mount partitions',
            callback=self.mount
        ))

        return group

    def checklist(self):
        checkpoints = self._data['chain_of_custody']
        self._print_text('Check list for chain of custody', checkpoints)

    def collect_info(self):
        glossary = []
        for elt in self._data['info']['glossary']:
            line = '{:15}: {}'.format(elt['name'], ', '.join(elt['examples']))
            glossary.append(line)
        self._print_text('Glossary', glossary)

        tools = self._data['info']['tools']
        tools.sort()
        self._print_text('Tools', tools)

        cheat_sheet = []
        for elt in self._data['info']['cheat_sheet']:
            line = '{:80}: {}'.format(elt['description'], elt['command'])
            cheat_sheet.append(line)
        self._print_text('Cheat Sheet', cheat_sheet)

    def dump(self):
        glossary = []
        for elt in self._data['dump']['glossary']:
            line = '{:15}: {}'.format(elt['name'], ', '.join(elt['examples']))
            glossary.append(line)
        self._print_text('Glossary', glossary)

        tools = self._data['dump']['tools']
        tools.sort()
        self._print_text('Tools', tools)

        cheat_sheet = []
        for elt in self._data['dump']['cheat_sheet']:
            line = '{:80}: {}'.format(elt['description'], elt['command'])
            cheat_sheet.append(line)
        self._print_text('Cheat Sheet', cheat_sheet)

    def mount(self):
        glossary = []
        for elt in self._data['mount']['glossary']:
            line = '{:15}: {}'.format(elt['name'], ', '.join(elt['examples']))
            glossary.append(line)
        self._print_text('Glossary', glossary)

        tools = self._data['mount']['tools']
        tools.sort()
        self._print_text('Tools', tools)

        cheat_sheet = []
        for elt in self._data['mount']['cheat_sheet']:
            line = '{:80}: {}'.format(elt['description'], elt['command'])
            cheat_sheet.append(line)
        self._print_text('Cheat Sheet', cheat_sheet)
