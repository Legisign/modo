#!/usr/bin/env python3
'''l10nrestore -- restore an .mo or .qm file from numbered backup

  2016-09-13  0.9.91  Added support for .qm files and renamed the program
                      to l10nrestore. (TN)
  2018-02-20  0.9.92  Getting rid of separate init(). (TN)

'''

import sys
import os
import getopt
import glob

# Constants
version = '0.9.92'
short_opts = 'l:s:v'
long_opts = ('l10ndir=',                # -l
             'steps=',                  # -s
             'verbose',                 # -v
             'help')

# Global variables
l10ndir = '/usr/share/locale/fi/LC_MESSAGES'
steps = 1
verbose = False

def warn(msg):
    print('{}: {}'.format(os.path.basename(sys.argv[0]), msg), file=sys.stderr)

def die(msg):
    warn(msg)
    sys.exit(1)

def usage():
    global l10ndir, steps
    print('''{prg} -- palauta kotoistustiedosto varmuuskopiosta

Käyttö:
    {prg} [VALITSIMET] TIEDOSTO…

Palauttaa kotoistustiedostot (.mo, .qm) varmuuskopioistaan.

Valitsimet (suluissa oletukset):
    -l KANSIO, --l10ndir=KANSIO     kansio, josta tiedostoja etsitään
    -s N, --steps=N                 palautusaskelten määrä
    --help                          näytä tämä ohje ja lopeta

Oletukset:
    --l10ndir={l10n}
    --steps={steps}
'''.format(prg=os.path.basename(sys.argv[0]), l10n=l10ndir, steps=steps))

def restore(pathname, steps=1, verbose=False):
    dirname, filename = os.path.split(pathname)
    backups = glob.glob(os.path.join(dirname, filename + '.~[0-9]*~'))
    if len(backups) < steps:
        raise ValueError(filename, len(backups))
    # Any of the following operations may raise an exception
    if verbose:
        print('{name} -> {name}.restore'.format(name=filename))
    os.rename(pathname, os.path.join(dirname, filename + '.restore'))
    if verbose:
        print('{name}.~1~ -> {name}'.format(name=filename))
    os.rename(filename + '.~1~', filename)
    for gen in range(2, len(backups)):
        if verbose:
            print('{name}.~{old}~ -> {name}.~{new}~'.format(name=filename,
                                                            old=gen,
                                                            new=gen - 1))
        os.rename(filename + '.~{}~'.format(gen),
                  filename + '.~{}~'.format(gen - 1))
    if verbose:
        print('{}.~{}~ poistetaan'.format(filename, len(backups)))
    os.remove('{}.~{}~'.format(filename, len(backups)))
    if verbose:
        print('{}.restore poistetaan'.format(filename))
    os.remove(filename + '.restore')

## MAIN

try:
    opts, args = getopt.getopt(sys.argv[1:], short_opts, long_opts)
except getopt.GetoptError:
    die('virhe komentorivillä (kokeile "--help")')
for opt, val in opts:
    if opt in ('-l', '--l10ndir'):
        l10ndir = val
    if opt in ('-s', '--steps'):
        try:
            steps = int(val)
        except ValueError:
            die('virheellinen parametri "{}"'.format(val))
    if opt in ('-v', '--verbose'):
        verbose = True
    elif opt == '--help':
        usage()
        sys.exit(0)
if not args:
    die('ei parametreja (kokeile "-help")')
if not os.path.isdir(l10ndir):
    die('kansio puuttuu: "{}"'.format(l10ndir))
for arg in args:
    if not os.path.exists(os.path.join(l10ndir, arg)):
        warn('Tiedostoa ei ole, ohitetaan: "{}"'.format(arg))
        continue
    filename = os.path.join(l10ndir, arg)
    try:
        restore(filename, steps, verbose)
    except FileNotFoundError:
        die('tiedostoa ei löydy: {}'.format(filename))
    except PermissionError:
        die('ei käyttöoikeuksia: {}'.format(filename))
    except IOError:
        die('muu I/O-virhe: {}'.format(filename))
    except ValueError as exc:
        name, gens = exc.args
        noun = 'sukupolvea' if gens > 1 else 'sukupolvi'
        die('tiedostosta "{}" on vain {} palautus{}'.format(name, gens, noun))
