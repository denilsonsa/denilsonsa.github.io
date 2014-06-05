#!/usr/bin/env python3

import math
import re
import sys


re_svg = re.compile(r'^(\s*<svg\s+viewBox=")[-0-9. ]+(")$', re.M)
re_centralpicture = re.compile(r'^(<g\s+class="centralpicture">\s+<image\s+x=")[-0-9.]+("\s+y=")[-0-9.]+("\s+width=")[0-9.]+("\s+height=")[0-9.]+(")$', re.M)
re_item = re.compile(r'^(\s*<g\s+transform="translate\()[-0-9., ]+(\)"\s+class="item[^>]*>\s*)$', re.M)


def count_items(data):
    return len(re_item.findall(data))
    #return sum(1 for line in data if re_item.match(line))


def calculate(radius, circles, deg_offset):
    if (circles <= 1):
        return [
            {'r': 0, 'x': 0, 'y': 0, 'deg': 0}
        ]

    deg_step = 360 / circles
    rad_step = 2 * math.pi / circles
    rad_offset = deg_offset * 2 * math.pi / 360
    ret = []

    # r is the distance from the center.
    r = radius / math.sin(rad_step / 2)

    for i in range(circles):
        deg = (deg_offset + deg_step * i) % 360
        rad = (rad_offset + rad_step * i) % (2 * math.pi)
        ret.append({
            'r': r,
            'x': r * math.cos(rad),
            'y': r * math.sin(rad),
            'deg': deg,
        })

    return ret


def s(number, decimals=1):
    return str(round(number, decimals))

def main():
    data = sys.stdin.read()
    num_circles = count_items(data)

    radius = 20  # Hard-coded
    coords = calculate(radius, num_circles, 270)

    inner_radius = coords[0]['r'] - radius
    outer_radius = coords[0]['r'] + radius
    inner_diameter = inner_radius * 2
    outer_diameter = outer_radius * 2

    def translate_replace(match):
        # Destructive to coords list.
        coord = coords.pop(0)
        return match.group(1) + s(coord['x']) + ' ' + s(coord['y']) + match.group(2)

    data = re_svg.sub(r'\g<1>-{0} -{0} {1} {1}\g<2>'.format(s(outer_radius), s(outer_diameter)), data)
    data = re_centralpicture.sub(r'\g<1>-{0}\g<2>-{0}\g<3>{1}\g<4>{1}\g<5>'.format(s(inner_radius), s(inner_diameter)), data)
    data = re_item.sub(translate_replace, data)

    sys.stdout.write(''.join(data))


if __name__ == '__main__':
    main()
