def sequence_to_list(str):

    chunks = str.split(',')

    elements = []

    for chunk in chunks:

        limits = [ int(x) for x in chunk.split(':') ]

        if len(limits) == 1:
            elements.append(limits[0])
        elif len(limits) == 2:
            elements.extend(range(limits[0], limits[1] + 1))
        else:
            raise ValueError(f'Malformed sequence at {chunk}')

    return list(set(elements))

