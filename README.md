# README

`modo` is a collection of zsh scripts dealing with day-to-day tasks of GNU Gettext (`.po`) and Qt (`.ts`) localization files.

*   `install_modos`: simple script installer
*   `modo`: compile and install a GNU Gettext-format `.po` file (as `.mo`)
*   `qmdo`: compile and install a Qt-format `.ts` file (as `.qm`)
*   `l10nrestore`: restore a previous version of a `.mo` or `.qm` file
*   `podo`: reverse-compile a `.mo` file as `.po` to allow editing

## Notes on some of the scripts

### `install_modos`

Installs `modo` and `qmdo` to `/usr/local/sbin` (since they require root privileges in order to install the target files) and `l10nrestore` and `podo` to `/usr/local/bin` (since they don’t).

### `modo`

Usage is basically `modo pofile...`, but the target directory needs consideration. Unless given in a `modo.def` file (consisting solely of a target directory name) or with the `-d` switch of the script, `modo` uses either `/usr/share/locale/fi/LC_MESSAGES` in distros other than Ubuntu, or `/usr/share/locale-langpack/fi/LC_MESSAGES` in Ubuntu.

**NOTE** the language code! It’s inferred from $LANG without the country code and encoding parts (i.e., `LANG=fi_FI.UTF-8` yields “fi”).

### `qmdo`

Usage is `qmdo tsfile...` and the target directory is OBLIGATORILY set in a `qmdo.def` file (consisting solely of a target directory name).

### `l10nrestore`

As `modo` and `qmdo` create numbered backups, `l10nrestore` allows reverting to an older file. This is the only script having an actual usage screen (`-h` or `--help`).
