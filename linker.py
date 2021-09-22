import os
import os.path


def determine_link_status(target, source):

    target_expanded = os.path.expanduser(target)
    source_expanded = os.path.expanduser(source)

    if not os.path.exists(target_expanded):
        return 'clear'

    if not os.path.islink(target_expanded):
        return 'taken'

    if os.path.realpath(target_expanded) != source_expanded:
        return 'taken'

    return 'linked'


def link(target, source):

    target_expanded = os.path.expanduser(target)
    source_expanded = os.path.expanduser(source)

    if determine_link_status(target, source) == 'clear':
        return os.symlink(source_expanded, target_expanded)


def unlink(target, source):

    target_expanded = os.path.expanduser(target)
    source_expanded = os.path.expanduser(source)

    if determine_link_status(target, source) == 'linked':
        if os.path.isdir(target_expanded):
            return os.rmdir(target_expanded)
        else:
            return os.remove(target_expanded)

