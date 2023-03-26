# README

## Overview

`modo` is a collection of zsh scripts dealing with day-to-day tasks of GNU Gettext (`.po`) and Qt (`.ts`) localization files.

*   `modo`: compile and install a GNU Gettext-format `.po` file (as `.mo`)
*   `qmdo`: compile and install a Qt-format `.ts` file (as `.qm`)
*   `l10nrestore`: restore a previous version of a `.mo` or `.qm` file
*   `podo`: reverse-compile a `.mo` file as `.po` to allow editing

## Short descriptions of the scripts

### `modo`

Usage is basically `modo pofile...`.

Unless given in the command line with `-d`, `--destination` switch or in a config file name `modo.def` (whose contents are the destination directory), `modo` tries to locate an older version of the destination file. If not found and no `-f`, `--force` switch is given, the script gives up. With `-f`, `--force`, the default destination directory is used (`/usr/share/locale/LANGCODE/LC_MESSAGES`).

**NOTE:** LANGCODE is taken from `$LANG` without the country code and encoding parts (i.e., `LANG=fi_FI.UTF-8` yields “fi”).

### `qmdo`

Usage is `qmdo tsfile...` and the target directory is OBLIGATORILY set in a `qmdo.def` file (consisting solely of a target directory name).

### `l10nrestore`

As `modo` and `qmdo` create numbered backups, `l10nrestore` allows reverting to an older file. This is the only script having an actual usage screen (`-h` or `--help`).

Options: `-h`, `--help` to show usage; `-n`, `--dry-run` to show what would happen without actually doing anything; `-sN`, `--steps=N` to set the number of restoration steps taken; and `-v`, `--verbose` for more verbose output.

### `podo`

Reverse-compile an `.mo` file into a `.po` file. As the reverse-compiled files lack comments etc., they are not really suitable to work with, but they can provide some information to the translator (like, what is the version of the `.mo` file used in the current distribution).
