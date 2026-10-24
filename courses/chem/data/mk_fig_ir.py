import sys; sys.path.insert(0, 'data'); sys.stdout.reconfigure(encoding='utf-8')
from mk_fig_synthesis import *
specs = {
 'ethanol': ([(3350,110,0.8),(2930,35,0.55),(2880,25,0.4),(1450,30,0.2),(1380,25,0.2),(1060,35,0.9),(880,30,0.25)],
             [(3350,'O–H',122),(2910,'C–H',104),(1060,'C–O',132)]),
 'acid': ([(2750,280,0.65),(2930,30,0.3),(1710,28,0.95),(1420,30,0.35),(1280,40,0.8),(930,60,0.4)],
             [(2750,'O–H',116),(1850,'C=O',137),(1225,'C–O',122)]),
 'propanone': ([(2960,35,0.4),(2900,30,0.3),(1715,28,0.97),(1430,25,0.25),(1360,30,0.3),(1220,40,0.25)],
             [(2930,'C–H',96),(1850,'C=O',138)]),
}
for k,(dips,labels) in specs.items():
    svg,bad,ymin = ir_svg(k,dips,labels)
    print(k,'bad',bad,'ymax',ymin,len(svg))
    open('scratch/ir_%s.svg.txt'%k,'w',encoding='utf-8').write(svg)
