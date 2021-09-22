import os.path
import sys
from printer import print_color
from linker import determine_link_status


PATH_DOTFILES = '~/.dotfiles/'

STATUS_COLORS = {
    'taken':  'red',
    'clear':  'blue',
    'linked': 'green',
}


# Load Catalog
# ------------------------------------------------------------------------------
with open(os.path.expanduser(PATH_DOTFILES + 'catalog')) as f:
    catalog_lines = f.readlines()

catalog = {}

for line in catalog_lines:
    chunks = line.split('<-')
    catalog[chunks[0].strip()] = chunks[1].strip()


# Print Catalog
# ------------------------------------------------------------------------------
if sys.argv[1:] == ['status']:

    maxlength_target = max([len(target) for target in catalog.keys()])

    for target, source in catalog.items():
        status = determine_link_status(target, PATH_DOTFILES + source)
        entry = f'{target.ljust(maxlength_target)} <- {source}'
        print_color(entry, STATUS_COLORS[status])

