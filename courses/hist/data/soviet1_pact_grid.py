# data/soviet1_pact_grid.py (review of P34): builds and checks the two-column satellite-state grid for hist.d.soviet.1.
# Run: py data/soviet1_pact_grid.py > data/soviet1_pact_grid.svg.txt  (checks print to stderr)
import sys
W=340; CW=7.0  # estimated px per character at 12 px (bold a little wider)
boxes=[  # (col,row,cls,title,line2,line3)
 (0,0,'fm','East Germany','Ulbricht 1950–71','1953 rising; Wall 1961'),
 (1,0,'fm','Poland','Bierut, then Gomułka','Poznań, October 1956'),
 (0,1,'fm','Czechoslovakia','Novotný; Dubček 1968','Prague Spring 1968'),
 (1,1,'fm','Hungary','Rákosi, Nagy, Kádár','Uprising 1956'),
 (0,2,'fp','Bulgaria','Zhivkov from 1954','A loyal ally'),
 (1,2,'fp','Romania','Gheorghiu-Dej to 1965','Kept its distance'),
]
X=[6,172]; BW=162; BH=70; RY=[8,86,164]
out=[]; texts=[]
def t(x,y,s,bold=False):
    out.append(f'<text class="tl{" tb" if bold else ""} tc" x="{x}" y="{y}">{s}</text>')
    w=len(s)*CW*(1.08 if bold else 1); texts.append((x-w/2,x+w/2,y,s))
for c,r,cls,a,b,d in boxes:
    x,y=X[c],RY[r]
    out.append(f'<rect class="{cls} s-acc sw2" x="{x}" y="{y}" width="{BW}" height="{BH}" rx="5"/>')
    cx=x+BW//2; t(cx,y+22,a,True); t(cx,y+41,b); t(cx,y+59,d)
    for x0,x1,yy,s in texts[-3:]:
        assert x+3<=x0 and x1<=x+BW-3, ('too wide',s,x0,x1)
out.append('<rect class="fp s-acc sw2" x="6" y="242" width="328" height="30" rx="5"/>')
t(170,262,'Albania left in 1968; Yugoslavia never joined')
out.append('<rect class="fm2 s-acc sw2" x="6" y="280" width="328" height="88" rx="5"/>')
t(170,302,'USSR (to the east)',True); t(170,321,'Stalin to 1953; Khrushchev 1953–64;'); t(170,339,'Brezhnev 1964–82'); t(170,358,'Joint Command of the Warsaw Pact in Moscow')
for x0,x1,yy,s in texts[-5:]:
    assert 12<=x0 and x1<=328, ('too wide',s,x0,x1)
H=376
aria=("Schematic diagram of the Soviet bloc in eastern Europe, not a map. Six boxes in three rows of two: East Germany, led by Ulbricht 1950 to 1971, with the 1953 rising and the Wall of 1961; "
 "Poland, led by Bierut and then Gomulka, with Poznan and the Polish October of 1956; Czechoslovakia, led by Novotny then Dubcek in 1968, with the Prague Spring of 1968; "
 "Hungary, led by Rakosi, Nagy and Kadar, with the uprising of 1956; Bulgaria, led by Zhivkov from 1954, a loyal ally; Romania, led by Gheorghiu-Dej to 1965, which kept its distance. "
 "Below them, a note that Albania left the Pact in 1968 and Yugoslavia never joined. At the bottom, a wide box for the USSR, to the east: Stalin to 1953, Khrushchev 1953 to 1964 and Brezhnev 1964 to 1982, with the Joint Command of the Warsaw Pact in Moscow.")
print(f'<figure class="fig small"><svg viewBox="0 0 {W} {H}" role="img" aria-label="{aria}">'+''.join(out)+'</svg>')

print('checks ok:',len(texts),'labels inside their boxes; height',H,file=sys.stderr)
