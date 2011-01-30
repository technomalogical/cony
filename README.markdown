Shared Smart Bookmarks Server
=============================

"Cony" is a tool to write [smart bookmarks][smart-bm] in the python and
to share them across all your browsers and with other developers
on the GitHub. This project is inspired by Facebook's [bunny1][].

What the difference between Cony and Bunny1?
--------------------------------------------

* Cony has no other dependencies other than Bottle, which itself is a
  micro web framework without dependencies.
* Cony could be easily extended. You have no need to inherit any classes like
  you do with Bunny1. With Cony, you place you commands in a separate
  file and fire `./cony.py`.

Introduction
------------

Smart bookmarks is a fast way to retrive information from the web.
For example, you could write a `w smart bookmarks` in the browser's
location bar and it will open a Wikipedia article about [smart bookmarks][smart-bm].

If you use more than one browser or device, then you are in trouble,
because you have to sync the browsers settings releated to smart bookmarks.

Cony not only solves this problem, creating one place were you store you
smart bookmarks, but also, it makes your bookmarks MUCH MUCH SMARTER.

For example, you could create this bookmark which will choose the
text translation mode depending on language:

    def cmd_tr(term):
        """Translates the text using Google Translate."""
        if len(term.decode('utf-8')) < len(term):
            direction = 'ru|en'
        else:
            direction = 'en|ru'
        redirect('http://translate.google.com/#%s|%s' % (direction, term))

This bookmarks trying to figure out if query contains only ASCII
characters and then translates text from English to Russian. Otherwise
it translates in other direction.

There are many other applications of this small webserver.


Installation
------------

Few ways to install Cony:

* Just clone the repository and to run `./cony.py`.
* `easy_install cony; cony.py`
* `pip install cony; cony.py`

Now you have server up and running. It binds to the localhost:8080 by
default. Open the <http://localhost:8080> in your browser to see the help.

### Firefox

Type `about:config` into your location bar in Firefox.
Set the value of `keyword.URL` to be `http://localhost/?s=`
Now, type `pypi cony` into your location bar and hit enter.

### Google Chrome

Choose `Options` from the wrench menu to the right of the location bar in Chrome,
then under the section `Default Search`, click the `Manage` button. Click the
`Add` button and then fill in the fields `name`, `keyword`, and `URL` with `Cony`, `c`,
and `http://localhost:8080/?s=%s`. Hit `OK` and then select `Cony` from the list
of search engines and hit the `Make Default` button to make it your default search
engine. Now, type `pypi cony` into your location bar and hit enter.

### Safari

For Safari you could try to install [Keywurl][] plugin. And add a `Cony` as default
search.


[smart-bm]: http://en.wikipedia.org/wiki/Smart_bookmark
[bunny1]: https://github.com/facebook/bunny1
[Keywurl]: http://alexstaubo.github.com/keywurl/
