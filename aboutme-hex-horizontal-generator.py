#!/usr/bin/env python3

# Not listed: italki, crunchyroll

# :.,.+2s/ \+/ /g | Tabularize / /l0
raw = '''

email    reddit   pinterest kickstarter indiegogo newgrounds gamejolt     kongregate  steam  alvanista     backloggd   backloggery retroachievements imgur       flickr  instagram coderwall  regexcrossword devpost    stackexchange curriculumvitae linkedin
blog     gravatar disqus    angellist   paypal    kofi       buymeacoffee patreon     itchio interference  drawception deviantart  opengameart       openclipart behance slides    slideshare speakerdeck    shadertoy  topcoder      hackerrank      codepen
telegram twitter  facebook  tumblr      snapchat  vk         myspace      livejournal medium instructables bandcamp    tunein      soundcloud        twitch      vimeo   youtube   asciinema  usercss        greasyfork userscripts   bitbucket       githubgist github

'''

cells = [
    [id.strip() for id in line.strip().split() ]
    for line in raw.strip().splitlines()
]
assert len(cells) == 3

max_x = max(len(line) for line in cells)
for x in range(max_x, -1, -1):
    for y, (x_offset, y_position) in [(1, (0.5, 0)), (0, (0, -1)), (2, (0, 1))]:
        if len(cells[y]) > x:  # If the element exists.
            assert float(y_position).is_integer()  # If it is not, must change the format string below.
            id = cells[y][x]
            if id != 'none':
                print('  - [{x:.1f}, {y:2.0f}, {id}]'.format(
                    x=(x + x_offset),
                    y=y_position,
                    id=id
                ))
