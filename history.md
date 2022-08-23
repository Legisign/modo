# `modo` History

## modo

*   2022-07-08    Added a check that all files == `*.po`.
*   2022-07-03    Fixed a bug in `-v`, `--verbose` and increased the verbosity in some places.
*   2021-10-01    `-v`, `--verbose` switches.
*   2021-07-22    Added check for `*.po` pattern.
*   2021-07-21    Enhanced command line handling including `-h`, `--help`.
*   2021-03-22    Bug fixes in the `.qm` target branch: `lconvert` requires `-target-language`.
*   2020-10-24    Added `-d`, `--destination` for giving the target dir.
*   2020-08-12    Files with names ending `_qt` need a intermediate `.ts` file.
*   2018-08-24    More small changes.
*   2017-01-05    Small changes.
*   2016-10-03    More stylistic changes.
*   2016-09-18    Stylistic changes.
*   2016-09-03    More `${var:t}` and `${var:r}` fixes.
*   2016-08-19    Using also `${var:r}`.
*   2016-08-08    `${0***/}` is more easily `${0:t}` in zsh.
*   2016-01-27    Added `--` to every `print`.
*   2015-10-13    Creating the target dir instead of giving up.
*   2015-06-05    More bug fixes.
*   2015-06-01    Bug fixed and stylistic changes.
*   2015-05-31    Bug fix: `pofiles=($@)` is required to keep `pofiles` an array.
*   2015-05-16    Bug fix: given source path, `.mo` couldn’t be found.
*   2015-04-24    New functionless structure.
*   2015-01-10    Stylistic changes; better backups.
*   2014-02-26    Bug fix: no globbing inside `[[...]]`.
*   2014-01-10    Script language changed to zsh.
*   2011-10-07    Temp dir moved to `/tmp`.
*   2011-08-14    Using a temp dir for the `.mo` files because of NFS issues.
*   2011-05-01    Fixed the automatic selection of the target directory.
*   2010-09-14    Added automatic selection of the target directory.
*   2009-10-13    Added forcing file update.
*   2009-07-11    Added (for the second time) handling of new files.
*   2008-08-06    Bug fix.

## `l10nrestore` (previously `morestore`)

* 2022-06-29    Bug fix: not giving `-s`, `--step` resulted in an error. Also `~` written as `\~` to avoid extended patterns.
* 2021-11-13    Small changes.
* 2021-07-21    Added `-h` which was actually missing.
* 2021-07-19    Long switches (including new `-h`, `--help`).
* 2020-01-15    Conversion to zsh.
* 2016-09-13    Added support for `.qm` files and renamed to `l10nrestore`.
* 2016-09-04    Finally a functional implementation.
* 2016-01-18    Back to the project after many a long year.
* 2008-06-18    An initial sketch.

## `qmdo` (previously `tsdo`)

* 2021-10-02    `-v`, `--verbose` switch.
* 2021-07-21    Enhanced command line handling including `-h`, `--help`.
* 2020-01-17    Qt4 to Qt5; stylistic changes.
* 2017-05-27    `lrelease` can be a symlink, so `$(whence lrelease)` is not enough.
* 2017-01-05    Bug fix, stylistic changes.
* 2016-10-03    More `modo`-style changes.
* 2016-09-24    Renamed to `qmdo`.
* 2016-09-13    Long overdue `modo`-style changes.
* 2016-05-03    Added `--` to every `print`.
* 2016-01-24    Port to zsh.
* 2009-07-12    Project started.

## `podo`

* 2022-08-24    With only one parameter, use current dir as the destination.
* 2021-07-21    Added `-h`, `--help`. Signals error if used as root.
* 2020-10-28    Allow multiple sources.
* 2019-02-21    `$argv` changed to `$@`.
* 2016-09-17    New handling of command line parameters.
* 2016-09-16    Small stylistic changes.
* 2016-04-23    Created to complement `modo`.

## `install_modos`

* 2020-01-15    `l10nrestore` is now a zsh script.
* 2017-03-07    Simplifications.
* 2017-03-07    Getting rid of csh-like syntax.
* 2017-02-17    Bug fix.
* 2017-01-30    Added `$localgroup` handling.
* 2016-10-01    Bug fix: of course one needs to check if the files exist
* 2016-09-18    No need to install unless source is newer.
* 2016-09-17    `podo` added. `do_install` function.
* 2016-09-13    Ready.

