Source code for the website of the fmrbenchmark project
=======================================================

https://fmrchallenge.org

The site is built using [Middleman](https://middlemanapp.com/) and is based on
the [HTML5 Boilerplate](http://html5boilerplate.com) template.

Preparations, building, testing
-------------------------------

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


Organization
------------

* img-gen/ - directory containing sources from some of the figures on the
  website are generated.


Licenses
--------

Some of the source code for the site originates from the Middleman and HTML5
Boilerplate projects. Copies of their respective licenses are included as
LICENSE-Middleman.md and LICENSE-html5boilerplate.md. They are both the standard
[MIT License](http://opensource.org/licenses/MIT).

Anything that is original site content, and thus not covered by the
aforementioned copyrights, is released under the Creative Commons
Attribution-ShareAlike 4.0 International License. To get a copy of this license,
visit http://creativecommons.org/licenses/by-sa/4.0/ or send a letter to
Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
