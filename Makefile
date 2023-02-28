# Makefile

PREFIX = /usr/local
.SECONDEXPANSION:
INSTALL = echo install -m 755 -g $$(ADMINS)

install: modo qmdo l10nrestore podo
	ADMINS := $(shell grep '^wheel:' | cut -d: -f1)
	ifneq ($(ADMINS),wheel)
		ADMINS := staff
	endif
	$(INSTALL) modo $(PREFIX)/sbin
	$(INSTALL) qmdo $(PREFIX)/sbin
	$(INSTALL) l10nrestore $(PREFIX)/sbin
	$(INSTALL) podo $(PREFIX)/bin
