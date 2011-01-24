from bottle import redirect

def cmd_fl(term):
    """Search among Flickr photos under Creative Commons license."""
    redirect('http://www.flickr.com/search/?q=%s&l=cc&ss=0&ct=0&mt=all&w=all&adv=1' % term)

def cmd_dj(term):
    """Django documentation search."""
    redirect(
        'http://docs.djangoproject.com/en/dev/search/?cx=009763561546736975936:e88ek0eurf4&'
        'cof=FORID:11&q=%s&siteurl=docs.djangoproject.com/en/dev/topics/db/models/' % term
    )

def cmd_tr(term):
    """Translates the text using Google Translate."""
    if len(term.decode('utf-8')) < len(term):
        direction = 'ru|en'
    else:
        direction = 'en|ru'
    redirect('http://translate.google.com/#%s|%s' % (direction, term))
