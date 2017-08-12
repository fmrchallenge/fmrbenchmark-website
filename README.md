Source code for the website of the fmrbenchmark project
=======================================================

https://fmrchallenge.org

The site is built using [Middleman](https://middlemanapp.com/) and is based on
the [HTML5 Boilerplate](http://html5boilerplate.com) template.

Preparations, building, testing
-------------------------------

The source code and issue tracker are available at
https://github.com/fmrchallenge/fmrbenchmark-website/
The repository uses [Git LFS](https://git-lfs.github.com), which is required to
checkout some of the large files that are used in the website.

If you do not already have them, install [Ruby](http://www.ruby-lang.org) and
[bundle](http://gembundler.com). Then, from the root of this source tree,

    bundle install
    bundle exec middleman build

to build the site. Contents of the output directory build/ can be copied
directly onto the server for deployment.

Use `middleman server` for local testing. It updates the output automatically
when source files change. Beware that the default configuration may allow other
hosts on your local network to view the site.

We use Travis CI and [Sauce Labs](https://saucelabs.com/open-source) to build
and test the site from the current source code in the repository.
[![Build status](https://api.travis-ci.org/fmrchallenge/fmrbenchmark-website.svg?branch=master)](https://travis-ci.org/fmrchallenge/fmrbenchmark-website)


Deploying
---------

After building as described in the previous section, use `deploy.sh`. The script
must be provided a host and path as would be used with `rsync`.


Organization
------------

* img-gen/ - directory containing sources from some of the figures on the
  website are generated.


Licenses
--------

Some of the source code for the site originates from the Middleman, HTML5
Boilerplate, and Bootstrap projects. Copies of their respective licenses are
included as LICENSE-Middleman.md, LICENSE-html5boilerplate.md, and
LICENSE-Bootstrap. They are all the standard [MIT License](
http://opensource.org/licenses/MIT).

Anything that is original site content, and thus not covered by the
aforementioned copyrights, is released under the Creative Commons
Attribution 4.0 International License. To get a copy of this license,
visit http://creativecommons.org/licenses/by/4.0/ or send a letter to
Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
