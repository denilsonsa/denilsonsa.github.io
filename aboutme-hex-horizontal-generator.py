#!/usr/bin/env python3

# Not listed:

# :.,.+2s/ \+/ /g | Tabularize / /l0
raw = '''

email googleplus reddit   disqus   pocket    stumbleupon pinterest kickstarter newgrounds  gamejolt  kongregate  steam       bandcamp   tunein      soundcloud  imgur   flickr    instagram  coderwall   regexcrossword devpost    pluralsight hackhands stackexchange   stackoverflowcv
blog  twitter    aboutme  gravatar angellist paypal      flattr    gratipay    changetip   patreon   itchio      drawception deviantart opengameart openclipart behance slides    slideshare speakerdeck topcoder       hackerrank codepen     linkedin  curriculumvitae
skype telegram   facebook tumblr   ello      snapchat    vk        myspace     livejournal alvanista backloggery playfire    hitbox     twitch      vimeo       youtube asciinema ifttt      shadertoy   stylish        greasyfork userscripts bitbucket githubgist      github

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
