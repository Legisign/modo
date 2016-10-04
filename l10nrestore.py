#!/usr/bin/env python3
'''l10nrestore -- restore an .mo or .qm file from numbered backup

  2016-09-13  0.9.91  Added support for .qm files and renamed the program
                      to l10nrestore. (TN)

'''

import sys
import os
import getopt
import glob

# Constants
version = '0.9.91'
short_opts = 'l:s:v'
long_opts = ('l10ndir=',                # -l
             'steps=',                  # -s
             'verbose',                 # -v
             'help')

class ProgramError(Exception):
    pass

def warn(msg):
    print('{}: {}'.format(os.path.basename(sys.argv[0]), msg), file=sys.stderr)

def die(msg):
    warn(msg)
    sys.exit(1)

def usage():
    print('''l10nrestore -- palauta kotoistustiedosto varmuuskopiosta

Käyttö:

    l10nrestore [VALITSIMET] TIEDOSTO…
    
Palauttaa kotoistustiedostot (GNU gettextin .mo tai Qt:n .qm) 
varmuuskopioistaan.

Valitsimet:

    -l KANSIO  --l10ndir=KANSIO
        kansio, josta tiedostoja etsitään (oletus nykykansio)
    
    -s N  --steps=N     
        palautusaskelten määrä
    
    --help              
        näytä tämä ohje ja lopeta.
''')

def l10n_restore(l10ndir, l10nfile, steps=1, verbose=False):
    backups = glob.glob(os.path.join(l10ndir, l10nfile + '.~[0-9]*~'))
    if len(backups) < steps:
        raise ProgramError
    # Any of the following operations may raise an exception
    if verbose:
        print('{l10n} -> {l10n}.l10nrestore'.format(l10n=l10nfile))
    os.rename(l10nfile, l10nfile + '.l10nrestore')
    if verbose:
        print('{l10n}.~1~ -> {l10n}'.format(l10n=l10nfile))
    os.rename(l10nfile + '.~1~', l10nfile)
    for gen in range(2, len(backups)):
        if verbose:
            print('{l10n}.~{old}~ -> {l10n}.~{new}~'.format(l10n=l10nfile,
                                                            old=gen,
                                                            new=gen - 1))
        os.rename(l10nfile + '.~{}~'.format(gen),
                  l10nfile + '.~{}~'.format(gen - 1))
    if verbose:
        print('{}.~{}~ poistetaan'.format(l10nfile, len(backups)))
    os.remove('{}.~{}~'.format(l10nfile, len(backups)))
    if verbose:
        print('{}.l10nrestore poistetaan'.format(l10nfile))
    os.remove(l10nfile + '.l10nrestore')

def init(args):
    global short_opts, long_opts
    steps = 1
    verbose = False
    opts, args = getopt.getopt(sys.argv[1:], short_opts, long_opts)
    for opt, val in opts:
        if opt in ('-l', '--l10ndir'):
            l10n = val
        if opt in ('-s', '--steps'):
            steps = int(val)
        if opt in ('-v', '--verbose'):
            verbose = True
        elif opt == '--help':
            usage()
            sys.exit(0)
    if not args:
        raise ProgramError
    return args, l10n, steps, verbose

l10ndir = '.'
try:
    args, l10ndir, steps, verbose = init(sys.argv[1:])
except getopt.GetoptError:
    die('Virhe komentorivillä (kokeile "--help")')
except ValueError:
    die('Virheellinen -s, --steps -arvo')
except ProgramError:
    die('Käyttö: l10nrestore [valitsimet] tsto... (kokeile "--help")')
if not os.path.isdir(l10n):
    die('Kansiota ei ole, lopetetaan: "{}"'.format(l10ndir))
for arg in args:
    if not os.path.exists(os.path.join(l10ndir, arg)):
        warn('Tiedostoa ei ole, ohitetaan: "{}"'.format(arg))
        continue
    try:
        l10n_restore(l10ndir, arg, steps, verbose)
    except (FileNotFoundError, PermissionError, IOError):
        die('palautus ei onnistu: {}'.format(arg))
    except ProgramError:
        die('ei voi palauttaa niin montaa sukupolvea')
