dotlink helps you keep track of symlinks to your dotfiles

# Dotfile Location

Dotfiles are assumed to be in `~/.dotfiles`.

# Catalog

Catalog your symlinks in `~/.dotfiles/catalog` like so:

```
~/.zshrc <- zshrc
```

On the left is the absolute path to where the file should be linked, on the right is the relative path to the source file within `~/.dotfiles`.

# Commands

Run `python dotlink.py status` to see the status of your links:

* Green: File is linked according to your catalog.
* Blue: Target does not exist yet.
* Red: Another file than the expected symlink is present at the target location.

Note the number (#) of the entry that you want to link or unlink and run `python dotlink.py [un]link #` to to do so. Sequences like `1, 4, 5:9` are supported.
