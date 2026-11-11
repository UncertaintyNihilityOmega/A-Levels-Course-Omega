# data/malaysia1_states_fig.py (P38): builds and checks the schematic of the three groupings of British-ruled territory in Malaya before 1941.
# Run: py data/malaysia1_states_fig.py > data/malaysia1_states_fig.svg.txt  (checks print to stderr)
import sys
W=340; CW=7.0
out=[]; texts=[]
def t(x,y,s,bold=False):
    out.append(f'<text class="tl{" tb" if bold else ""} tc" x="{x}" y="{y}">{s}</text>')
    w=len(s)*CW*(1.08 if bold else 1); texts.append((x-w/2,x+w/2,y,s))
def box(y,h,cls,lines):
    out.append(f'<rect class="{cls} s-acc sw2" x="6" y="{y}" width="328" height="{h}" rx="5"/>')
    for i,s in enumerate(lines):
        t(170,y+22+i*19,s,i==0)
    for x0,x1,yy,s in texts[-len(lines):]:
        assert 12<=x0 and x1<=328, ('too wide',s,x0,x1)
    assert 22+(len(lines)-1)*19+8<=h, ('too tall',lines)
box(8,50,'fm2',['High Commissioner for the Malay States','(also Governor of the Straits Settlements)'])
out.append('<line class="ln-m thin dash" x1="170" y1="58" x2="170" y2="72"/>')
box(72,70,'fp',['Straits Settlements (Crown colony)','Singapore, Penang, Malacca','Ruled directly by British officials'])
out.append('<line class="ln-m thin dash" x1="170" y1="142" x2="170" y2="156"/>')
box(156,90,'fm',['Federated Malay States (1895)','Perak, Selangor, Negeri Sembilan, Pahang','A British Resident in each state;','Chief Secretary at Kuala Lumpur'])
out.append('<line class="ln-m thin dash" x1="170" y1="246" x2="170" y2="260"/>')
box(260,108,'fm2',['Unfederated Malay States','Perlis, Kedah, Kelantan, Terengganu:','under British protection from 1909;','Johor took a General Adviser in 1914','Most internal self-government kept'])
H=376
aria=("Schematic diagram of British rule in Malaya before 1941, not a map. At the top, one official: the High Commissioner for the Malay States, who was also Governor of the Straits Settlements. "
 "Below, three groups of territory in three stacked boxes. First, the Straits Settlements, a Crown colony of Singapore, Penang and Malacca, ruled directly by British officials. "
 "Second, the Federated Malay States of 1895: Perak, Selangor, Negeri Sembilan and Pahang, each with a British Resident and a Chief Secretary at Kuala Lumpur. "
 "Third, the Unfederated Malay States: Perlis, Kedah, Kelantan and Terengganu, which came under British protection in 1909, and Johor, which accepted a General Adviser in 1914; they kept most internal self-government.")
print(f'<figure class="fig small"><svg viewBox="0 0 {W} {H}" role="img" aria-label="{aria}">'+''.join(out)+'</svg>')
print('checks ok:',len(texts),'labels; height',H,file=sys.stderr)
