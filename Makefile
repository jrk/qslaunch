
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

