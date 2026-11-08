# data/p4-figcheck.py <chapter-id> ...: checks hand-SVG label fit and spacing in P4 chapters
import re, sys

def parse(svg):
    rects = []
    for m in re.finditer(r'<rect class="([^"]*)" x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"', svg):
        c, x, y, w, h = m.group(1), *map(float, m.groups()[1:])
        rects.append((c, x, y, w, h))
    texts = []
    for m in re.finditer(r'<text class="([^"]*)" x="([\d.]+)" y="([\d.]+)">([^<]*)</text>', svg):
        texts.append((m.group(1), float(m.group(2)), float(m.group(3)), m.group(4)))
    lines = []
    for m in re.finditer(r'<line class="([^"]*)" x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)"', svg):
        lines.append((m.group(1), *map(float, m.groups()[1:])))
    return rects, texts, lines

def run(cid):
    s = open(f'chapters/{cid}.md', encoding='utf-8').read()
    bad = 0
    for sm in re.finditer(r'<svg viewBox="0 0 (\d+) (\d+)".*?</svg>', s, re.S):
        W, H = int(sm.group(1)), int(sm.group(2))
        rects, texts, lines = parse(sm.group(0))
        print(cid, 'svg', W, H, len(rects), 'rects', len(texts), 'texts')
        for c, x, y, w, h in rects:
            if x < 0 or y < 0 or x + w > W or y + h > H:
                print('  OUT OF VIEWBOX', c, x, y, w, h); bad += 1
        for c, x, y, t in [(a, b, d, e) for a, b, d, e in texts]:
            bold = 'tb' in c.split()
            cw = 7.4 if bold else 6.9
            tw = len(t) * cw
            if 'tc' in c.split():
                x0, x1 = x - tw / 2, x + tw / 2
            else:
                x0, x1 = x, x + tw
            top, bot = y - 10, y + 3
            if x0 < 0 or x1 > W or bot > H:
                print('  TEXT OUTSIDE', repr(t), round(x0), round(x1)); bad += 1
            # containing rect: smallest rect with centre-anchor inside
            cont = [r for r in rects if r[1] <= x <= r[1] + r[3] and r[2] <= y <= r[2] + r[4] + 2]
            if cont:
                r = min(cont, key=lambda r: r[3] * r[4])
                if x0 < r[1] + 3 or x1 > r[1] + r[3] - 3 or top < r[2] + 1 or bot > r[2] + r[4]:
                    print('  TEXT DOES NOT FIT', repr(t), 'text', round(x0), round(x1), round(top), round(bot), 'rect', r[1:]); bad += 1
            # overlap with lines
            for lc, x1l, y1l, x2l, y2l in lines:
                if abs(y1l - y2l) < 0.1:  # horizontal
                    if top - 4 < y1l < bot + 4 and not (x1 < min(x1l, x2l) or x0 > max(x1l, x2l)):
                        print('  TEXT NEAR HORIZONTAL LINE', repr(t), y1l); bad += 1
                elif abs(x1l - x2l) < 0.1:
                    if x0 - 4 < x1l < x1 + 4 and not (bot < min(y1l, y2l) or top > max(y1l, y2l)):
                        print('  TEXT NEAR VERTICAL LINE', repr(t), x1l); bad += 1
        # text-text overlap
        boxes = []
        for c, x, y, t in texts:
            bold = 'tb' in c.split()
            tw = len(t) * (7.4 if bold else 6.9)
            x0 = x - tw / 2 if 'tc' in c.split() else x
            boxes.append((x0, x0 + tw, y - 10, y + 3, t))
        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes)):
                a, b = boxes[i], boxes[j]
                if not (a[1] + 2 < b[0] or b[1] + 2 < a[0] or a[3] + 2 < b[2] or b[3] + 2 < a[2]):
                    print('  TEXT OVERLAP', a[4], '|', b[4]); bad += 1
        # rect overlaps (non-nested)
        for i in range(len(rects)):
            for j in range(i + 1, len(rects)):
                a, b = rects[i], rects[j]
                ax0, ay0, ax1, ay1 = a[1], a[2], a[1] + a[3], a[2] + a[4]
                bx0, by0, bx1, by1 = b[1], b[2], b[1] + b[3], b[2] + b[4]
                inter = not (ax1 <= bx0 or bx1 <= ax0 or ay1 <= by0 or by1 <= ay0)
                nested = (ax0 <= bx0 and ay0 <= by0 and ax1 >= bx1 and ay1 >= by1) or (bx0 <= ax0 and by0 <= ay0 and bx1 >= ax1 and by1 >= ay1)
                if inter and not nested:
                    print('  RECT OVERLAP', a[1:], b[1:]); bad += 1
        # arrows
        for lc, x1l, y1l, x2l, y2l in lines:
            L = ((x2l - x1l) ** 2 + (y2l - y1l) ** 2) ** .5
            if L < 20 and 'ln-m' not in lc:
                print('  SHORT LINE', lc, round(L)); bad += 1
    print(cid, 'figure problems:', bad)
    return bad

if __name__ == '__main__':
    tot = sum(run(a) for a in sys.argv[1:])
    sys.exit(1 if tot else 0)
