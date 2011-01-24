#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, debug, request, redirect

DEBUG = True


def cmd_g(term):
    """Google search."""
    redirect('http://www.google.com/search?q=%s' % term)


def cmd_pypi(term):
    """Python package index search.

    If there is exact match, then redirects right to the package's page.
    """
    import urllib
    try:
        direct_url = 'http://pypi.python.org/pypi/%s/' % term
        result = urllib.urlopen(direct_url)
    except Exception, e:
        pass
    else:
        if result.code == 200:
            redirect(direct_url)

    redirect('http://pypi.python.org/pypi?:action=search&term=%s&submit=search' % term)


def cmd_p(term):
    """Python documentation search."""
    redirect('http://docs.python.org/search.html?q=%s&check_keywords=yes&area=default' % term)


cmd_fallback = cmd_g


try:
    from local_commands import *
except ImportError:
    pass


def cmd_help(term):
    """Shows all available commands."""
    commands = []
    for name, obj in sorted(globals().items()):
        if name.startswith('cmd_') and callable(obj):
            commands.append('%s — %s' % (name[4:], obj.__doc__))
    return '<br/>'.join(commands)


@route('/')
def do_command():
    """Runs a command"""
    search_string = request.GET.get('s', 'help')

    tokens = search_string.split(' ', 1)
    command_name = tokens[0]
    term = len(tokens) == 2 and tokens[1] or ''

    command = globals().get('cmd_' + command_name, cmd_fallback)

    if command is cmd_fallback:
        term = search_string

    return command(term)


if __name__ == '__main__':
    debug(DEBUG)
    run(reloader = DEBUG)

