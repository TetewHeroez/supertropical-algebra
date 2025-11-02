# Makefile for Sphinx documentation

SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

.PHONY: help html clean

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"
	@echo "  clean      to remove build files"

html:
	$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)"
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html/."

clean:
	rm -rf $(BUILDDIR)
	@echo "Build files cleaned."
