# data/cs.dns_fig.py: writes the DNS lookup figure into chapters/cs.internet.md (replaces the old figure).
# Numbers only on the arrows; the numbered steps are listed under the figure.
import pathlib

box = lambda x, y, name, cls: f'<rect class="{cls} s-acc sw2" x="{x}" y="{y}" width="84" height="34"/><text class="tl tc" x="{x + 42}" y="{y + 22}">{name}</text>'
parts = [
    box(14, 20, "Browser", "fm"), box(242, 20, "Resolver", "fm"), box(14, 136, "Web server", "f1"), box(242, 136, "DNS servers", "fm"),
    '<line class="c1 sw2" x1="106" y1="30" x2="234" y2="30" marker-end="url(#ah)"/><text class="tl tc" x="170" y="22">1</text>',
    '<line class="ln-m dash" x1="234" y1="46" x2="106" y2="46" marker-end="url(#ahm)"/><text class="tl tc" x="170" y="62">4</text>',
    '<line class="c1 sw2" x1="268" y1="62" x2="268" y2="128" marker-end="url(#ah)"/><text class="tl te" x="259" y="99">2</text>',
    '<line class="ln-m dash" x1="300" y1="128" x2="300" y2="62" marker-end="url(#ahm)"/><text class="tl" x="308" y="99">3</text>',
    '<line class="c1 sw2" x1="28" y1="62" x2="28" y2="128" marker-end="url(#ah)"/><text class="tl te" x="20" y="99">5</text>',
    '<line class="ln-m dash" x1="70" y1="128" x2="70" y2="62" marker-end="url(#ahm)"/><text class="tl" x="78" y="99">6</text>',
]
label = ("A DNS lookup drawn as six numbered arrows between four boxes. 1: the browser asks the resolver for the IP address of the name. "
         "2: the resolver asks the DNS servers. 3: the DNS servers reply with the IP address. 4: the resolver passes the IP address to the browser. "
         "5: the browser requests the page from the web server. 6: the web server sends the page back. Solid arrows are requests and dashed arrows are replies.")
fig = (f'<figure class="fig small"><svg viewBox="0 0 340 185" role="img" aria-label="{label}">' + "".join(parts) +
       '</svg><figcaption>The six steps of a DNS lookup. The numbers match the list below; solid arrows are requests and dashed arrows are replies.</figcaption></figure>')
p = pathlib.Path("chapters/cs.internet.md")
s = p.read_text(encoding="utf-8")
a = s.index('<figure class="fig"><svg viewBox="0 0 625 345"')
b = s.index("</figure>", a) + len("</figure>")
s = s[:a] + fig + s[b:]
with open(p, "w", encoding="utf-8", newline="") as f:
    f.write(s)
print("replaced")
