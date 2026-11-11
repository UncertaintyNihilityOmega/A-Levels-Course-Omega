# data/malaysia2_seats_fig.py (P38): builds and checks the seat-bar schematic of the Federation of Malaysia in 1963 for hist.d.malaysia.2.
# Run: py data/malaysia2_seats_fig.py > data/malaysia2_seats_fig.svg.txt  (checks print to stderr)
import sys
W=340; CW=7.0; SC=1.5
rows=[('Malaya (11 states)',104,'f1'),('Singapore',15,'f1'),('Sarawak',24,'f1'),('Sabah',16,'f1')]
assert sum(r[1] for r in rows)==159
out=[]; texts=[]
def t(x,y,s,bold=False,anchor=''):
    out.append(f'<text class="tl{" tb" if bold else ""}{anchor}" x="{x}" y="{y}">{s}</text>')
    w=len(s)*CW*(1.08 if bold else 1)
    x0=x-w/2 if 'tc' in anchor else x
    texts.append((x0,x0+w,y,s))
t(170,22,'Seats in the Dewan Rakyat, 1963: 159',True,' tc')
y=44
BX=140
for name,n,cls in rows:
    t(6,y+17,name)
    out.append(f'<rect class="{cls} s-acc sw2" x="{BX}" y="{y}" width="{n*SC:.1f}" height="24" rx="3"/>')
    t(BX+n*SC+6,y+17,str(n))
    assert texts[-1][1]<=334,('number too wide',name)
    assert texts[-2][1]<=BX-4,('label too wide',name)
    y+=36
t(170,y+14,'Brunei stayed out.',False,' tc')
t(170,y+33,'Singapore left on 9 August 1965.',False,' tc')
for x0,x1,yy,s_ in texts[-2:]:
    assert x0>=6 and x1<=334,'note too wide'
H=y+48
aria=("Bar chart of the 159 seats in the Dewan Rakyat, the lower house of the Federation of Malaysia, when it was formed on 16 September 1963. "
 "Malaya, 11 states: 104 seats. Singapore: 15 seats. Sarawak: 24 seats. Sabah: 16 seats. Below the bars, a note that Brunei stayed out and that Singapore left on 9 August 1965.")
print(f'<figure class="fig small"><svg viewBox="0 0 {W} {H}" role="img" aria-label="{aria}">'+''.join(out)+'</svg>')
print('checks ok:',len(texts),'labels; height',H,file=sys.stderr)
