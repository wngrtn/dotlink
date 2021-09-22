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

