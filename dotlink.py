import os.path
import sys
from printer import print_color
from linker import determine_link_status, link, unlink
from sequencer import sequence_to_list

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
if len(sys.argv) == 1:
    sys.argv[1:] = ['status']

if sys.argv[1:] == ['status']:

    maxlength_target = max([len(target) for target in catalog.keys()])
    maxlength_counter = len(str(len(catalog)))

    for i, (target, source) in enumerate(catalog.items()):
        status = determine_link_status(target, PATH_DOTFILES + source)
        i_f = str(i + 1).rjust(maxlength_counter)
        target_f = target.ljust(maxlength_target)
        entry = f'{i_f} {target_f} <- {source}'
        print_color(entry, STATUS_COLORS[status])

if sys.argv[1] in ['link', 'unlink']:

    entries = sequence_to_list(','.join(sys.argv[2:]))

    for i, (target, source) in enumerate(catalog.items()):
        if i+1 in entries:
            locals()[sys.argv[1]](target, PATH_DOTFILES + source)

