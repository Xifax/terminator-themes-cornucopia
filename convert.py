#!/usr/bin/env python
# coding: utf-8
import ConfigParser


def get_themes(theme_list='themes'):
    """Get availiable themes and colors from file"""
    themes = {}
    config = ConfigParser.ConfigParser()
    config.read(theme_list)
    for section in config.sections():
        theme = {}
        theme['palette'] = config.get(section, 'palette')
        theme['background'] = config.get(section, 'bg_color')
        theme['foreground'] = config.get(section, 'fg_color')
        theme['bold'] = config.get(section, 'bd_color')
        themes[section] = theme

    return themes


if __name__ == '__main__':
    """Convert themes"""
    template = '''
    [[%s]]
    palette="%s"
    background_color="%s"
    foreground_color="%s"
    '''

    with open('config', 'w') as config:
        for theme, options in get_themes().iteritems():
            config.write(template % (
                theme,
                options['palette'],
                options['background'],
                options['foreground'],
            ))
