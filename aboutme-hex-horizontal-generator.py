#!/usr/bin/env python3

# :.,.+2s/ \+/ /g | Tabularize / /l0
raw = '''

email googleplus disqus  stumbleupon pinterest flattr   newgrounds gamejolt    grooveshark soundcloud imgur       flickr instagram stylish     stackoverflow   stackoverflowcareers
blog  twitter    aboutme angellist   paypal    gratipay steam      kongregate  drawception deviantart openclipart slides codepen   github      curriculumvitae
skype facebook   vk      tumblr      ello      myspace  alvanista  backloggery playfire    youtube    twitch      hitbox reddit    userscripts bitbucket       linkedin

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
            print('  - [{x:.1f}, {y:2.0f}, {id}]'.format(
                x=(x + x_offset),
                y=y_position,
                id=cells[y][x]
            ))
