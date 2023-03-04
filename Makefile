# Makefile

PREFIX = /usr/local
ADMINS = wheel
INSTALL = install -m 755 -g $(ADMINS)

install: modo qmdo l10nrestore podo
	$(INSTALL) modo $(PREFIX)/sbin
	$(INSTALL) qmdo $(PREFIX)/sbin
	$(INSTALL) l10nrestore $(PREFIX)/sbin
	$(INSTALL) podo $(PREFIX)/bin
