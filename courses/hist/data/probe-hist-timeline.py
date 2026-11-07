# Runs the hist-timeline probe on several data sets (3, 12, 30 events, long labels, 1787-89 demo, bad attributes).
import re, subprocess, io, sys
ch = io.open('chapters/hist.eu.france.2.md', encoding='utf-8').read()
m = re.search(r'<div class="widget" data-w="hist-timeline" (.*?)></div>', ch, re.S)
chapter_attrs = m.group(1)

demo = ('data-title="The road to 1789, 1787–89" data-lanes="Politics,Economy,People" data-events="'
 '1787-02-22 | Assembly of Notables opens | Calonne asks 144 notables to approve his reform plan. | Politics ;; '
 '1787-04-08 | Calonne dismissed | The Notables reject the land tax and the king dismisses him. | People ;; '
 '1788-07-13 | Hailstorm | Crops around Paris are destroyed. | Economy ;; '
 '1788-08-08 | Estates-General called | The king summons it for May 1789. | Politics ;; '
 '1789-05-05 | Estates-General opens | About 1,200 deputies meet at Versailles. | Politics ;; '
 '1789-07-14 | Bastille stormed | Crowds take the fortress for its gunpowder. | People"')

def gen(n, long=False):
    ev = []
    lanes = ['A', 'B', 'C']
    for i in range(n):
        y = 1700 + i * 7
        label = ('A very long label that goes on and on about an event that happened in the year ' + str(y) + ' in a distant place') if long else 'Event ' + str(i + 1)
        detail = ('A long detail sentence, repeated. ' * 6) if long else 'Detail of event ' + str(i + 1) + '.'
        ev.append('%d-%02d-%02d | %s | %s | %s' % (y, i % 12 + 1, i % 28 + 1, label, detail, lanes[i % 3]))
    return 'data-title="Generated %d" data-lanes="A,B,C" data-events="%s"' % (n, ' ;; '.join(ev))

sets = {
  'chapter(27)': chapter_attrs,
  'demo 1787-89': demo,
  '3 events': gen(3),
  '12 events': gen(12),
  '30 long': gen(30, True),
  'same date': 'data-title="Same" data-events="1789 | A | x ;; 1789 | B | y"',
  'one event': 'data-events="1789-07-14 | Only | one"',
  'bad: none': '',
  'bad: junk': 'data-events="hello ;; 12 | x" data-lanes=",,"',
  'bad: half': 'data-events="1789-07-14 | Good | ok ;; nonsense | x"',
}
only = sys.argv[1:]
for name, attrs in sets.items():
    if only and not any(o in name for o in only): continue
    r = subprocess.run(['node', 'kit/zta.js', 'widget', 'hist-timeline', attrs, '--probe'], capture_output=True, text=True, encoding='utf-8')
    print('==', name, '==')
    print((r.stdout + r.stderr).strip()[-900:])
