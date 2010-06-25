
.PHONY: help doc

help:
	@echo "Usage: make <target>"
	@echo "Possible targets:"
	@echo "  docs            Make HTML documentation"
	@echo "  upload          upload_sdist, upload_doc"

clean:
	cd doc; $(MAKE) $(MFLAGS) clean
	python setup.py clean
	-rm -rf build/docs

tag_version:
	@echo "Checking for uncommitted changed..."
	hg summary | grep -q 'commit: (clean)'
	@echo "Clean!"
	hg tag `python -c 'from qslaunch import get_version; print get_version().replace(" ", "-")'`

upload: upload_sdist upload_doc

upload_sdist:
	python setup.py sdist upload --identity="Serge Emond" --sign

upload_doc: docs
	python setup.py upload_docs

docs:
	cd doc; $(MAKE) $(MFLAGS) html
	-rm -rf build/docs
	cp -a doc/_build/html build/docs
	-rm -f build/docs/.buildinfo

