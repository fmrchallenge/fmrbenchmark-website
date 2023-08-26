Source code for the website of the fmrbenchmark project
=======================================================

https://fmrchallenge.org




Building and deploying
----------------------

The source code and issue tracker are available at
https://github.com/fmrchallenge/fmrbenchmark-website/
The repository uses [Git LFS](https://git-lfs.github.com), which is required to
checkout some of the large files that are used in the website.

The server-side is built using [Django](https://www.djangoproject.com/) and
[Celery](https://docs.celeryproject.org/en/stable/). The client-side is based on
[HTML5 Boilerplate](http://html5boilerplate.com) templates. Deployment is
achieved with [Ansible](https://docs.ansible.com/ansible/latest/index.html).


Organization
------------

* img-gen/ - directory containing sources from some of the figures on the
  website are generated.


Licenses
--------

In summary, new code is released under the [Apache 2.0 license](
https://www.apache.org/licenses/LICENSE-2.0.html). Read below for other open
source licenses that may apply.

Some of the source code for the site originates from the Middleman, HTML5
Boilerplate, and Bootstrap projects. Copies of their respective licenses are
included as LICENSE-Middleman.md, LICENSE-html5boilerplate.md, and
LICENSE-Bootstrap. They are all the standard [MIT License](
http://opensource.org/licenses/MIT).

Any code that is original site content, and thus not covered by the
aforementioned copyrights, is released under the [Apache 2.0 license](
https://www.apache.org/licenses/LICENSE-2.0.html). Any non-code content
is released under the Creative Commons Attribution 4.0 International License. To
get a copy of this license, visit https://creativecommons.org/licenses/by/4.0/
or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
If there is ambiguity about which license applies, then assume the relevant
license is [Apache 2.0 license](https://www.apache.org/licenses/LICENSE-2.0.html).
