# Make commands
#
#
# This is part of https://fmrchallenge.org
# Copyright (c) 2020
#
# This is free software, released under the Apache License, Version 2.0.
# You may obtain a copy of the License at https://www.apache.org/licenses/LICENSE-2.0


.PHONY: test-preconditions
test-preconditions:
	test ! -d build/
	@python3 -c 'import fmrweb.settings; assert fmrweb.settings.DEBUG, "For testing, DEBUG should be True!"'


check: test-preconditions
	pylint --load-plugins pylint_django -E fmrweb
	python3 -Wall manage.py test -v 2 --failfast


.PHONY: deploy-preconditions
deploy-preconditions:
	test ! -d build/
	test ! -d static_to_deploy
	@python3 -c 'import fmrweb.settings; assert not fmrweb.settings.DEBUG, "For deploying, DEBUG should be False!"'


buildstatic: deploy-preconditions distclean
	./manage.py collectstatic

deploy: buildstatic
	mkdir -p build/main_etc
	cp etc/snakeoil.pem build/main_etc/
	cp etc/snakeoil.key build/main_etc/
	cp etc/django-secret.key build/main_etc/
	cp etc/nginx.conf build/main_etc/
	cp etc/supervisord.conf build/
	cp manage.py build/
	cp -r fmrweb build/


clean:
	rm -f -v db.sqlite3
	rm -r -f build/
	rm -f -v django.*.log

distclean: clean
	rm -f -v `find . -name \*~`
	rm -f -v `find . -name \*.pyc`
	rm -r -f static_to_deploy
