@chapter bio.hormones
@title Control and coordination in plants
@level a2
@paper CAIE 9700 Paper 4
@time 3–4 hours
@summary Plants have no nervous system, but they sense and respond with chemical signals. You will learn how guard cells open and close stomata and how abscisic acid closes them in a drought (with calcium ions as a second messenger), how a Venus fly trap snaps shut, how auxin stretches cell walls by acid growth, and how gibberellin switches on amylase in a germinating barley seed.

:::why
A plant cannot walk away from a drought, a shadow or a hungry insect, so it has to respond where it stands. It does this with hormones and with changes in cell shape that you can now explain in terms of ions, water potential, proton pumps and gene expression. These ideas also repeat across the course: guard cells use the transport and water potential of [Movement across membranes](#bio.movement), abscisic acid uses the second messenger idea of [Blood glucose, cell signalling and biosensors](#bio.glucose), and gibberellin links to the control of enzyme production. Paper 4 asks you to describe and explain each mechanism step by step.
:::

**Before you start**, you should know water potential and osmosis from [Movement across membranes](#bio.movement), the role of stomata in transpiration from [Transport in plants](#bio.planttransport), the cell wall from [Carbohydrates](#bio.carbs) and second messengers from [Blood glucose, cell signalling and biosensors](#bio.glucose).

:::try Warm-up
Q: What is the name for water moving from a region of higher water potential to a region of lower water potential through a partially permeable membrane? (from [Movement across membranes](#bio.movement))
A: Osmosis.
Q: Why does a plant lose water through its stomata, and what is this loss called? (from [Transport in plants](#bio.planttransport))
A: Water evaporates from the wet walls of the mesophyll cells into the air spaces, and the water vapour diffuses out through the open stomata down a water potential gradient. This is transpiration.
Q: What holds the glucose units of cellulose together in a microfibril, and what do the microfibrils do for the cell wall? (from [Carbohydrates](#bio.carbs))
A: β-1,4 glycosidic bonds within each chain, with hydrogen bonds between chains. The microfibrils give the wall great tensile strength.
:::

## Stomata: a balance between two needs

A leaf has a problem. It needs **carbon dioxide** for photosynthesis, and the carbon dioxide has to diffuse in through the stomata. But when a stoma is open, **water vapour diffuses out** (transpiration). A plant that kept its stomata open all the time would lose too much water; a plant that kept them shut would starve.

:::def Stoma and guard cells
A **stoma** is a pore in the epidermis of a leaf that allows gas exchange. Each stoma is surrounded by a pair of **guard cells**, which change shape to open and close it.
:::

:::key The trade-off
Stomata open: carbon dioxide diffuses in (for photosynthesis) but water vapour diffuses out (transpiration). Stomata closed: water is kept in, but no carbon dioxide gets in. A plant **regulates the stomatal aperture**, the width of the pore, to balance the need for carbon dioxide with the need to minimise water loss.
:::

In general, stomata are **open in the light**, when photosynthesis needs carbon dioxide, and **closed in the dark**, when there is no photosynthesis and no need to lose water. They also close in a **drought**, even in the light.

### Daily rhythms

:::def Circadian rhythm
A change in a process that repeats about every 24 hours, driven by an internal (endogenous) biological clock rather than directly by a change in the environment.
:::

Stomatal opening has a daily rhythm: open by day, closed by night. The rhythm is not just a direct response to light. If a plant is moved from a cycle of light and dark into **constant light**, its stomata continue to open and close with a period of about 24 hours for several days. So the plant has an **internal clock** that keeps time. Normally the clock is reset each day by the light and dark cycle, so that the stomata begin to open just before dawn.

:::plot Stomatal aperture of a plant kept in 12 hours of light and 12 hours of dark each day for 2 days, then in constant light from 48 h (dashed line). Time 0 is midnight at the start of the experiment. The data are invented to show the pattern.
--f "4.5-3.5*cos(2*pi*x/24)+0*sqrt(96-x)" --x 0 112 --y 0 10 --xstep 12 --vline 48 --xlabel "time / h" --ylabel "aperture / µm" --label "stomatal aperture" --legend tr --alt "Stomatal aperture rises and falls in smooth waves with a period of 24 hours. It is at a minimum of 1 micrometre at 0, 24, 48, 72 and 96 hours and a maximum of 8 micrometres at 12, 36, 60 and 84 hours. The pattern continues unchanged after the dashed line at 48 hours, when the plant was put in constant light."
:::

:::eg The graph shows the stomatal aperture of a plant. After 48 h the plant was kept in constant light. Describe the pattern and explain what it shows about the control of stomatal opening.
For the first two days the light and dark alternate; for the last two days the light is constant.

The aperture rises and falls in a regular cycle with a period of 24 h, from a minimum of 1 µm to a maximum of 8 µm. [B1]

The maximum of 8 µm is at 12 h and 36 h (midday), when the plant is in the light; the minimum is at 0, 24 and 48 h (midnight). [B1]

After 48 h, in constant light, the cycle continues: maxima at 60 h and 84 h, and minima at 72 h and 96 h, with the same period. [B1]

So the opening and closing of the stomata is not only a direct response to light: the plant has an internal (endogenous) biological clock that produces a circadian rhythm. [B1]

A weaker answer says "stomata open when it is light and close when it is dark". The graph shows the stomata closing at 72 h in constant light, so that answer cannot explain it, and scores no more than one mark.
:::

## Guard cells and the mechanism of opening

Guard cells are different from the other cells of the epidermis. Each has features that make it work as a valve.

:::steps
1. A **thick inner wall** (next to the pore) and a **thin outer wall**. The thin wall stretches more than the thick wall.
2. **Cellulose microfibrils arranged radially**, like hoops round a barrel, so the cell cannot get wider. When the cell takes in water it can only get longer.
3. **Chloroplasts**, so the cell can make ATP and sugars in the light. (Most other epidermal cells have none.)
4. **Proton pumps** and **K⁺ channels** in the cell surface membrane.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 340 326" role="img" aria-label="Top view of a pair of guard cells in two states. Top: stoma open. The two bean-shaped guard cells are turgid and curve apart, leaving a pore between them. Bottom: stoma closed. The guard cells are flaccid and straight, touching along the middle. Each guard cell has a thick inner wall next to the pore, a thin outer wall, cellulose microfibrils arranged across the cell like hoops, and chloroplasts."><text class="tl tb" x="170" y="22" text-anchor="middle">stoma open: guard cells turgid</text><path class="f1 s-acc sw2" d="M166.5 38L151.4 44L144.4 50L139.2 56L135.1 62L131.9 68L129.5 74L127.8 80L126.8 86L126.5 92L126.8 98L127.8 104L129.5 110L131.9 116L135.1 122L139.2 128L144.4 134L151.4 140L166.5 146L168.5 146L165.8 140L163.4 134L161.3 128L159.5 122L158.1 116L156.9 110L156.1 104L155.7 98L155.5 92L155.7 86L156.1 80L156.9 74L158.1 68L159.5 62L161.3 56L163.4 50L165.8 44L168.5 38Z"/><path class="ln sw3" d="M168.5 38L165.8 44L163.4 50L161.3 56L159.5 62L158.1 68L156.9 74L156.1 80L155.7 86L155.5 92L155.7 98L156.1 104L156.9 110L158.1 116L159.5 122L161.3 128L163.4 134L165.8 140L168.5 146"/><path class="ln-m thin" d="M159.5 62L135.1 62"/><path class="ln-m thin" d="M155.7 86L126.8 86"/><path class="ln-m thin" d="M156.1 104L127.8 104"/><path class="ln-m thin" d="M161.3 128L139.2 128"/><path class="fp ln" d="M148.2 73.1L148.2 73.5L148 73.9L147.8 74.3L147.5 74.7L147.2 75L146.7 75.4L146.2 75.6L145.7 75.9L145.1 76.1L144.5 76.2L143.9 76.3L143.2 76.3L142.5 76.3L141.9 76.2L141.3 76.1L140.7 75.9L140.2 75.6L139.7 75.4L139.2 75L138.9 74.7L138.6 74.3L138.4 73.9L138.2 73.5L138.2 73.1L138.2 72.7L138.4 72.3L138.6 71.9L138.9 71.5L139.2 71.2L139.7 70.8L140.2 70.6L140.7 70.3L141.3 70.1L141.9 70L142.5 69.9L143.2 69.9L143.9 69.9L144.5 70L145.1 70.1L145.7 70.3L146.2 70.6L146.7 70.8L147.2 71.2L147.5 71.5L147.8 71.9L148 72.3L148.2 72.7Z"/><path class="fp ln" d="M146 94.7L146 95.1L145.8 95.5L145.6 95.9L145.3 96.3L145 96.6L144.5 97L144 97.2L143.5 97.5L142.9 97.7L142.3 97.8L141.7 97.9L141 97.9L140.3 97.9L139.7 97.8L139.1 97.7L138.5 97.5L138 97.2L137.5 97L137 96.6L136.7 96.3L136.4 95.9L136.2 95.5L136 95.1L136 94.7L136 94.3L136.2 93.9L136.4 93.5L136.7 93.1L137 92.8L137.5 92.4L138 92.2L138.5 91.9L139.1 91.7L139.7 91.6L140.3 91.5L141 91.5L141.7 91.5L142.3 91.6L142.9 91.7L143.5 91.9L144 92.2L144.5 92.4L145 92.8L145.3 93.1L145.6 93.5L145.8 93.9L146 94.3Z"/><path class="fp ln" d="M150 116.3L150 116.7L149.8 117.1L149.6 117.5L149.3 117.9L149 118.2L148.5 118.6L148 118.8L147.5 119.1L146.9 119.3L146.3 119.4L145.7 119.5L145 119.5L144.3 119.5L143.7 119.4L143.1 119.3L142.5 119.1L142 118.8L141.5 118.6L141 118.2L140.7 117.9L140.4 117.5L140.2 117.1L140 116.7L140 116.3L140 115.9L140.2 115.5L140.4 115.1L140.7 114.7L141 114.4L141.5 114L142 113.8L142.5 113.5L143.1 113.3L143.7 113.2L144.3 113.1L145 113.1L145.7 113.1L146.3 113.2L146.9 113.3L147.5 113.5L148 113.8L148.5 114L149 114.4L149.3 114.7L149.6 115.1L149.8 115.5L150 115.9Z"/><path class="f1 s-acc sw2" d="M173.5 38L188.6 44L195.6 50L200.8 56L204.9 62L208.1 68L210.5 74L212.2 80L213.2 86L213.5 92L213.2 98L212.2 104L210.5 110L208.1 116L204.9 122L200.8 128L195.6 134L188.6 140L173.5 146L171.5 146L174.2 140L176.6 134L178.7 128L180.5 122L181.9 116L183.1 110L183.9 104L184.3 98L184.5 92L184.3 86L183.9 80L183.1 74L181.9 68L180.5 62L178.7 56L176.6 50L174.2 44L171.5 38Z"/><path class="ln sw3" d="M171.5 38L174.2 44L176.6 50L178.7 56L180.5 62L181.9 68L183.1 74L183.9 80L184.3 86L184.5 92L184.3 98L183.9 104L183.1 110L181.9 116L180.5 122L178.7 128L176.6 134L174.2 140L171.5 146"/><path class="ln-m thin" d="M180.5 62L204.9 62"/><path class="ln-m thin" d="M184.3 86L213.2 86"/><path class="ln-m thin" d="M183.9 104L212.2 104"/><path class="ln-m thin" d="M178.7 128L200.8 128"/><path class="fp ln" d="M201.8 73.1L201.8 73.5L201.6 73.9L201.4 74.3L201.1 74.7L200.8 75L200.3 75.4L199.8 75.6L199.3 75.9L198.7 76.1L198.1 76.2L197.5 76.3L196.8 76.3L196.1 76.3L195.5 76.2L194.9 76.1L194.3 75.9L193.8 75.6L193.3 75.4L192.8 75L192.5 74.7L192.2 74.3L192 73.9L191.8 73.5L191.8 73.1L191.8 72.7L192 72.3L192.2 71.9L192.5 71.5L192.8 71.2L193.3 70.8L193.8 70.6L194.3 70.3L194.9 70.1L195.5 70L196.1 69.9L196.8 69.9L197.5 69.9L198.1 70L198.7 70.1L199.3 70.3L199.8 70.6L200.3 70.8L200.8 71.2L201.1 71.5L201.4 71.9L201.6 72.3L201.8 72.7Z"/><path class="fp ln" d="M204 94.7L204 95.1L203.8 95.5L203.6 95.9L203.3 96.3L203 96.6L202.5 97L202 97.2L201.5 97.5L200.9 97.7L200.3 97.8L199.7 97.9L199 97.9L198.3 97.9L197.7 97.8L197.1 97.7L196.5 97.5L196 97.2L195.5 97L195 96.6L194.7 96.3L194.4 95.9L194.2 95.5L194 95.1L194 94.7L194 94.3L194.2 93.9L194.4 93.5L194.7 93.1L195 92.8L195.5 92.4L196 92.2L196.5 91.9L197.1 91.7L197.7 91.6L198.3 91.5L199 91.5L199.7 91.5L200.3 91.6L200.9 91.7L201.5 91.9L202 92.2L202.5 92.4L203 92.8L203.3 93.1L203.6 93.5L203.8 93.9L204 94.3Z"/><path class="fp ln" d="M200 116.3L200 116.7L199.8 117.1L199.6 117.5L199.3 117.9L199 118.2L198.5 118.6L198 118.8L197.5 119.1L196.9 119.3L196.3 119.4L195.7 119.5L195 119.5L194.3 119.5L193.7 119.4L193.1 119.3L192.5 119.1L192 118.8L191.5 118.6L191 118.2L190.7 117.9L190.4 117.5L190.2 117.1L190 116.7L190 116.3L190 115.9L190.2 115.5L190.4 115.1L190.7 114.7L191 114.4L191.5 114L192 113.8L192.5 113.5L193.1 113.3L193.7 113.2L194.3 113.1L195 113.1L195.7 113.1L196.3 113.2L196.9 113.3L197.5 113.5L198 113.8L198.5 114L199 114.4L199.3 114.7L199.6 115.1L199.8 115.5L200 115.9Z"/><text class="tl tb" x="170" y="192" text-anchor="middle">stoma closed: guard cells flaccid</text><path class="f1 s-acc sw2" d="M166.5 208L154.1 214L149.5 220L146.4 226L144.1 232L142.3 238L141 244L140.2 250L139.7 256L139.5 262L139.7 268L140.2 274L141 280L142.3 286L144.1 292L146.4 298L149.5 304L154.1 310L166.5 316L168.5 316L168.5 310L168.5 304L168.5 298L168.5 292L168.5 286L168.5 280L168.5 274L168.5 268L168.5 262L168.5 256L168.5 250L168.5 244L168.5 238L168.5 232L168.5 226L168.5 220L168.5 214L168.5 208Z"/><path class="ln sw3" d="M168.5 208L168.5 214L168.5 220L168.5 226L168.5 232L168.5 238L168.5 244L168.5 250L168.5 256L168.5 262L168.5 268L168.5 274L168.5 280L168.5 286L168.5 292L168.5 298L168.5 304L168.5 310L168.5 316"/><path class="ln-m thin" d="M168.5 232L144.1 232"/><path class="ln-m thin" d="M168.5 256L139.7 256"/><path class="ln-m thin" d="M168.5 274L140.2 274"/><path class="ln-m thin" d="M168.5 298L146.4 298"/><path class="fp ln" d="M159.8 243.1L159.8 243.5L159.6 243.9L159.4 244.3L159.1 244.7L158.8 245L158.3 245.4L157.8 245.6L157.3 245.9L156.7 246.1L156.1 246.2L155.5 246.3L154.8 246.3L154.1 246.3L153.5 246.2L152.9 246.1L152.3 245.9L151.8 245.6L151.3 245.4L150.8 245L150.5 244.7L150.2 244.3L150 243.9L149.8 243.5L149.8 243.1L149.8 242.7L150 242.3L150.2 241.9L150.5 241.5L150.8 241.2L151.3 240.8L151.8 240.6L152.3 240.3L152.9 240.1L153.5 240L154.1 239.9L154.8 239.9L155.5 239.9L156.1 240L156.7 240.1L157.3 240.3L157.8 240.6L158.3 240.8L158.8 241.2L159.1 241.5L159.4 241.9L159.6 242.3L159.8 242.7Z"/><path class="fp ln" d="M159 264.7L159 265.1L158.8 265.5L158.6 265.9L158.3 266.3L158 266.6L157.5 267L157 267.2L156.5 267.5L155.9 267.7L155.3 267.8L154.7 267.9L154 267.9L153.3 267.9L152.7 267.8L152.1 267.7L151.5 267.5L151 267.2L150.5 267L150 266.6L149.7 266.3L149.4 265.9L149.2 265.5L149 265.1L149 264.7L149 264.3L149.2 263.9L149.4 263.5L149.7 263.1L150 262.8L150.5 262.4L151 262.2L151.5 261.9L152.1 261.7L152.7 261.6L153.3 261.5L154 261.5L154.7 261.5L155.3 261.6L155.9 261.7L156.5 261.9L157 262.2L157.5 262.4L158 262.8L158.3 263.1L158.6 263.5L158.8 263.9L159 264.3Z"/><path class="fp ln" d="M160.4 286.3L160.4 286.7L160.2 287.1L160 287.5L159.7 287.9L159.4 288.2L158.9 288.6L158.4 288.8L157.9 289.1L157.3 289.3L156.7 289.4L156.1 289.5L155.4 289.5L154.7 289.5L154.1 289.4L153.5 289.3L152.9 289.1L152.4 288.8L151.9 288.6L151.4 288.2L151.1 287.9L150.8 287.5L150.6 287.1L150.4 286.7L150.4 286.3L150.4 285.9L150.6 285.5L150.8 285.1L151.1 284.7L151.4 284.4L151.9 284L152.4 283.8L152.9 283.5L153.5 283.3L154.1 283.2L154.7 283.1L155.4 283.1L156.1 283.1L156.7 283.2L157.3 283.3L157.9 283.5L158.4 283.8L158.9 284L159.4 284.4L159.7 284.7L160 285.1L160.2 285.5L160.4 285.9Z"/><path class="f1 s-acc sw2" d="M173.5 208L185.9 214L190.5 220L193.6 226L195.9 232L197.7 238L199 244L199.8 250L200.3 256L200.5 262L200.3 268L199.8 274L199 280L197.7 286L195.9 292L193.6 298L190.5 304L185.9 310L173.5 316L171.5 316L171.5 310L171.5 304L171.5 298L171.5 292L171.5 286L171.5 280L171.5 274L171.5 268L171.5 262L171.5 256L171.5 250L171.5 244L171.5 238L171.5 232L171.5 226L171.5 220L171.5 214L171.5 208Z"/><path class="ln sw3" d="M171.5 208L171.5 214L171.5 220L171.5 226L171.5 232L171.5 238L171.5 244L171.5 250L171.5 256L171.5 262L171.5 268L171.5 274L171.5 280L171.5 286L171.5 292L171.5 298L171.5 304L171.5 310L171.5 316"/><path class="ln-m thin" d="M171.5 232L195.9 232"/><path class="ln-m thin" d="M171.5 256L200.3 256"/><path class="ln-m thin" d="M171.5 274L199.8 274"/><path class="ln-m thin" d="M171.5 298L193.6 298"/><path class="fp ln" d="M190.2 243.1L190.2 243.5L190 243.9L189.8 244.3L189.5 244.7L189.2 245L188.7 245.4L188.2 245.6L187.7 245.9L187.1 246.1L186.5 246.2L185.9 246.3L185.2 246.3L184.5 246.3L183.9 246.2L183.3 246.1L182.7 245.9L182.2 245.6L181.7 245.4L181.2 245L180.9 244.7L180.6 244.3L180.4 243.9L180.2 243.5L180.2 243.1L180.2 242.7L180.4 242.3L180.6 241.9L180.9 241.5L181.2 241.2L181.7 240.8L182.2 240.6L182.7 240.3L183.3 240.1L183.9 240L184.5 239.9L185.2 239.9L185.9 239.9L186.5 240L187.1 240.1L187.7 240.3L188.2 240.6L188.7 240.8L189.2 241.2L189.5 241.5L189.8 241.9L190 242.3L190.2 242.7Z"/><path class="fp ln" d="M191 264.7L191 265.1L190.8 265.5L190.6 265.9L190.3 266.3L190 266.6L189.5 267L189 267.2L188.5 267.5L187.9 267.7L187.3 267.8L186.7 267.9L186 267.9L185.3 267.9L184.7 267.8L184.1 267.7L183.5 267.5L183 267.2L182.5 267L182 266.6L181.7 266.3L181.4 265.9L181.2 265.5L181 265.1L181 264.7L181 264.3L181.2 263.9L181.4 263.5L181.7 263.1L182 262.8L182.5 262.4L183 262.2L183.5 261.9L184.1 261.7L184.7 261.6L185.3 261.5L186 261.5L186.7 261.5L187.3 261.6L187.9 261.7L188.5 261.9L189 262.2L189.5 262.4L190 262.8L190.3 263.1L190.6 263.5L190.8 263.9L191 264.3Z"/><path class="fp ln" d="M189.6 286.3L189.6 286.7L189.4 287.1L189.2 287.5L188.9 287.9L188.6 288.2L188.1 288.6L187.6 288.8L187.1 289.1L186.5 289.3L185.9 289.4L185.3 289.5L184.6 289.5L183.9 289.5L183.3 289.4L182.7 289.3L182.1 289.1L181.6 288.8L181.1 288.6L180.6 288.2L180.3 287.9L180 287.5L179.8 287.1L179.6 286.7L179.6 286.3L179.6 285.9L179.8 285.5L180 285.1L180.3 284.7L180.6 284.4L181.1 284L181.6 283.8L182.1 283.5L182.7 283.3L183.3 283.2L183.9 283.1L184.6 283.1L185.3 283.1L185.9 283.2L186.5 283.3L187.1 283.5L187.6 283.8L188.1 284L188.6 284.4L188.9 284.7L189.2 285.1L189.4 285.5L189.6 285.9Z"/><text class="tl" x="112" y="70" text-anchor="end">thin outer wall</text><path class="ln-m thin" d="M116 66L131.4 68"/><text class="tl" x="112" y="124" text-anchor="end">chloroplast</text><path class="ln-m thin" d="M116 120L142 116.3"/><text class="tl" x="236" y="66">thick inner</text><text class="tl" x="236" y="80">wall</text><path class="ln-m thin" d="M232 72L181.5 62"/><text class="tl" x="236" y="120">cellulose</text><text class="tl" x="236" y="134">microfibrils</text><path class="ln-m thin" d="M232 126L189.8 128"/></svg><figcaption>Guard cells in a drawing. Because the inner wall is thick and the microfibrils run across the cell, a turgid guard cell lengthens and curves, so the pair move apart and open the stoma; flaccid guard cells straighten and close it.</figcaption></figure>
:::

Here is how a stoma opens in the light:

:::steps
1. Light is detected, and **proton pumps** in the cell surface membrane of the guard cell use **ATP** to pump **H⁺ ions out** of the cell into the cell wall.
2. This makes the inside of the cell **more negative** and the outside more positive, and **K⁺ channels open**. K⁺ ions move **into** the cell down this electrochemical gradient. (Negatively charged ions, such as chloride, enter too, and the cell makes malate.)
3. The concentration of solute in the guard cell rises, so its **water potential falls**.
4. **Water enters** the guard cells by **osmosis** from the neighbouring cells, down a water potential gradient.
5. The guard cells become **turgid**. Because their walls are thicker on the pore side and the microfibrils stop them getting wider, they get **longer** and **curve apart**, opening the stoma.
:::

To close the stoma, the process reverses: the proton pumps stop, K⁺ ions **leave** the guard cells (through channels), the water potential of the guard cells **rises**, water leaves by osmosis, the guard cells become **flaccid**, straighten and close the pore.

:::eg Explain how stomata open in the light.
The question asks for a mechanism: follow it from ATP to water movement to shape change.

In the light, proton pumps in the cell surface membrane of the guard cells use ATP to pump H⁺ ions out of the cells. [B1]

This lowers the H⁺ concentration inside the cells (the inside becomes more negative), so K⁺ channels open and K⁺ ions enter the guard cells. [B1]

The solute concentration inside the guard cells increases, so their water potential becomes lower than that of the surrounding cells. [B1]

Water enters the guard cells by osmosis, and they become turgid. [B1]

The thick inner walls and radially arranged cellulose microfibrils mean the cells lengthen and bend apart, so the stoma opens. [B1]

A weaker answer says "the guard cells fill with water, so the pore opens". It does not say what moves water in (the ions and water potential) or why the cell bends, and scores one mark.
:::

:::warn Turgid guard cells open the stoma
A common mistake is "stomata close because the guard cells lose turgor in the light" or "the guard cells swell and close the gap". **Turgid guard cells open the stoma; flaccid guard cells close it.** Also, K⁺ ions do not move by active transport here: it is the **proton pumps** that use ATP, and the K⁺ ions move through channels.
:::

## Abscisic acid and water stress

When a plant is short of water, closing the stomata is the fastest way to reduce water loss. The signal is a plant hormone, **abscisic acid (ABA)**.

:::def Abscisic acid (ABA)
A plant hormone made in response to water stress (and other stresses). It causes guard cells to lose turgor, so the stomata close.
:::

:::steps
1. In **water stress**, the leaf cells (and root cells) make more **ABA**, which is carried to the guard cells.
2. ABA **binds to receptors** on the cell surface membrane of the guard cells.
3. This causes **calcium ions (Ca²⁺)** to enter the cytoplasm (from outside the cell and from stores inside it). **Ca²⁺ is the second messenger** that carries the message on.
4. The Ca²⁺ ions cause **ion channels to open**: **K⁺ ions (and anions) leave** the guard cells, and the proton pumps are slowed.
5. The guard cells lose solute, so their **water potential rises** above that of the surrounding cells.
6. **Water leaves** the guard cells by **osmosis**; they become **flaccid** and the **stoma closes**.
7. Less water vapour is lost by transpiration, so the plant conserves water.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 340 460" role="img" aria-label="A flow chart of seven boxes with downward arrows. Water stress: the plant makes more abscisic acid. ABA binds to receptors on the guard cell membrane. Calcium ions enter the cytoplasm as a second messenger. Ion channels open and potassium ions leave the guard cells. The water potential of the guard cells rises and water leaves by osmosis. The guard cells become flaccid and the stoma closes. Less water is lost by transpiration."><rect class="f1 s-acc sw2" x="40" y="10" width="260" height="42"/><text class="tl" x="170" y="28.5" text-anchor="middle">water stress: the plant</text><text class="tl" x="170" y="43.5" text-anchor="middle">makes more abscisic acid</text><path class="c1 sw2" d="M170 52L170 74" marker-end="url(#ah)"/><rect class="f1 s-acc sw2" x="40" y="74" width="260" height="42"/><text class="tl" x="170" y="92.5" text-anchor="middle">ABA binds to receptors on</text><text class="tl" x="170" y="107.5" text-anchor="middle">the guard cell membrane</text><path class="c1 sw2" d="M170 116L170 138" marker-end="url(#ah)"/><rect class="f1 s-acc sw2" x="40" y="138" width="260" height="42"/><text class="tl" x="170" y="156.5" text-anchor="middle">calcium ions enter the</text><text class="tl" x="170" y="171.5" text-anchor="middle">cytoplasm (second messenger)</text><path class="c1 sw2" d="M170 180L170 202" marker-end="url(#ah)"/><rect class="f1 s-acc sw2" x="40" y="202" width="260" height="42"/><text class="tl" x="170" y="220.5" text-anchor="middle">ion channels open:</text><text class="tl" x="170" y="235.5" text-anchor="middle">K⁺ ions leave the guard cells</text><path class="c1 sw2" d="M170 244L170 266" marker-end="url(#ah)"/><rect class="f1 s-acc sw2" x="40" y="266" width="260" height="42"/><text class="tl" x="170" y="284.5" text-anchor="middle">water potential rises:</text><text class="tl" x="170" y="299.5" text-anchor="middle">water leaves by osmosis</text><path class="c1 sw2" d="M170 308L170 330" marker-end="url(#ah)"/><rect class="f1 s-acc sw2" x="40" y="330" width="260" height="42"/><text class="tl" x="170" y="348.5" text-anchor="middle">guard cells flaccid:</text><text class="tl" x="170" y="363.5" text-anchor="middle">stoma closes</text><path class="c1 sw2" d="M170 372L170 394" marker-end="url(#ah)"/><rect class="f2 s-acc2 sw2" x="40" y="394" width="260" height="42"/><text class="tl" x="170" y="412.5" text-anchor="middle">less water lost by</text><text class="tl" x="170" y="427.5" text-anchor="middle">transpiration</text></svg><figcaption>How abscisic acid closes a stoma. Calcium ions are the second messenger between the receptor at the surface and the ion channels.</figcaption></figure>
:::

:::eg Real context, a plant in a drought. A farmer's crop is short of water at midday. Explain how abscisic acid helps the plants to survive.
The roots and leaves of the plants make more abscisic acid when they are short of water. [B1]

ABA binds to receptors on the cell surface membranes of the guard cells. [B1]

This makes calcium ions enter the cytoplasm of the guard cells; they act as a second messenger. [B1]

The calcium ions open ion channels, so K⁺ ions leave the guard cells. The water potential of the guard cells rises and water leaves by osmosis. [B1]

The guard cells become flaccid, the stomata close and less water is lost by transpiration. [B1]

(Also credit: the closed stomata also reduce the carbon dioxide that enters, so photosynthesis is slower, but the plant survives.)
:::

:::eg Spot the error: describe how abscisic acid causes stomata to close. [3]
A student wrote this answer.

Line 1: ABA binds to receptors on the guard cell, which makes calcium ions enter the cytoplasm and act as a second messenger.
Line 2: The calcium ions open channels, so K⁺ ions leave the guard cell and its water potential rises.
Line 3: Water enters the guard cells by osmosis, so they become turgid and the stoma closes.

Line 1 is correct [B1]. Line 2 is correct [B1]. **Line 3 is wrong: when the water potential of the guard cells rises, water leaves by osmosis, and the guard cells become flaccid. Turgid guard cells open the stoma. That mark is lost [B0].** 

Correct Line 3: "Water leaves the guard cells by osmosis, so they become flaccid and the stoma closes." With that change the answer scores 3 marks.
:::

## The Venus fly trap: a rapid response

The Venus fly trap, *Dionaea muscipula*, grows in bogs where the soil has very little nitrate. It gets nitrogen by trapping and digesting insects. The trap is a **modified leaf** with two **lobes** joined by a midrib. Each lobe has three stiff **trigger hairs** on its inner surface. The edges of each lobe carry spikes that interlock when the trap shuts.

:::steps
1. An insect touches a **trigger hair**. The bending of the hair stimulates the sensory cells at its base, which produces an **action potential**. (You meet action potentials in [Neurones and action potentials](#bio.nerves).)
2. One touch is not enough. The trap closes only if a hair is touched **twice within about 20 seconds** (or two hairs are touched). This stops it closing for a raindrop or a falling piece of debris.
3. The action potentials **spread across the cells of the lobes**, and ions move rapidly, causing a change in the cells.
4. The cells in the **outer layer** of the lobes **expand quickly** (they take up water and their walls stretch), while the inner cells do not.
5. This makes the lobes **flip from a convex shape to a concave shape** and **snap shut** in a fraction of a second, trapping the insect.
6. If the prey keeps moving and stimulating the hairs, the trap seals and the glands on its surface secrete digestive enzymes; the products are absorbed.
:::

:::eg Describe how the closure of the trap of a Venus fly trap is brought about.
Trigger hairs on the lobes are touched by an insect, and the sensory cells at the base of the hair produce an action potential. [B1]

Two stimulations within about 20 seconds are needed before the trap closes. [B1]

The action potentials spread over the lobe, and the cells in the outer layer of the lobes expand rapidly. [B1]

The lobes change shape from convex to concave and snap shut, trapping the insect. [B1]

(Also credit: the advantage of needing two touches is that the trap does not waste energy closing for a non-living object such as a raindrop.)
:::

## Auxin and elongation growth

**Auxin** (indoleacetic acid, IAA) is a plant hormone made mainly in the **tips of shoots** (and in young leaves). It moves down the shoot to the zone just behind the tip, where cells are **elongating**.

:::def Auxin
A plant hormone, made in the shoot tip, that stimulates **elongation growth**: the permanent stretching of young cells so that the shoot gets longer. (It does not make cells divide in this role.)
:::

Plant cells are surrounded by a cellulose wall that is strong but, in young cells, can be loosened. The **acid growth hypothesis** explains how auxin loosens it.

:::steps
1. Auxin **binds to receptors** on the cells of the elongation zone.
2. It stimulates **proton pumps** (H⁺ pumps) in the cell surface membrane, which use ATP to pump **H⁺ ions into the cell wall**.
3. The **pH of the wall falls**: the wall becomes more **acidic**.
4. The low pH activates **expansins**, proteins in the wall.
5. Expansins **loosen the bonds** between the cellulose microfibrils, so the wall becomes more flexible and can stretch.
6. Water enters the cell by osmosis, and the **turgor pressure** pushes against the loosened wall and **stretches it**: the cell **elongates**.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 340 460" role="img" aria-label="A flow chart of seven boxes with downward arrows. Auxin made in the shoot tip moves to the cells behind it. Auxin binds to receptors on the cell surface membrane. Proton pumps, using ATP, pump hydrogen ions into the cell wall. The wall pH falls and expansins are activated. Expansins loosen the bonds between cellulose microfibrils. Water enters by osmosis and turgor stretches the loosened wall. The cell elongates."><rect class="f1 s-acc sw2" x="40" y="10" width="260" height="42"/><text class="tl" x="170" y="28.5" text-anchor="middle">auxin made in the shoot tip</text><text class="tl" x="170" y="43.5" text-anchor="middle">moves to cells behind it</text><path class="c1 sw2" d="M170 52L170 74" marker-end="url(#ah)"/><rect class="f1 s-acc sw2" x="40" y="74" width="260" height="42"/><text class="tl" x="170" y="92.5" text-anchor="middle">auxin binds to receptors</text><text class="tl" x="170" y="107.5" text-anchor="middle">on the cell surface membrane</text><path class="c1 sw2" d="M170 116L170 138" marker-end="url(#ah)"/><rect class="f1 s-acc sw2" x="40" y="138" width="260" height="42"/><text class="tl" x="170" y="156.5" text-anchor="middle">proton pumps (ATP) pump</text><text class="tl" x="170" y="171.5" text-anchor="middle">H⁺ ions into the cell wall</text><path class="c1 sw2" d="M170 180L170 202" marker-end="url(#ah)"/><rect class="f1 s-acc sw2" x="40" y="202" width="260" height="42"/><text class="tl" x="170" y="220.5" text-anchor="middle">wall pH falls:</text><text class="tl" x="170" y="235.5" text-anchor="middle">expansins are activated</text><path class="c1 sw2" d="M170 244L170 266" marker-end="url(#ah)"/><rect class="f1 s-acc sw2" x="40" y="266" width="260" height="42"/><text class="tl" x="170" y="284.5" text-anchor="middle">expansins loosen bonds between</text><text class="tl" x="170" y="299.5" text-anchor="middle">cellulose microfibrils</text><path class="c1 sw2" d="M170 308L170 330" marker-end="url(#ah)"/><rect class="f1 s-acc sw2" x="40" y="330" width="260" height="42"/><text class="tl" x="170" y="348.5" text-anchor="middle">water enters by osmosis: turgor</text><text class="tl" x="170" y="363.5" text-anchor="middle">stretches the loosened wall</text><path class="c1 sw2" d="M170 372L170 394" marker-end="url(#ah)"/><rect class="f2 s-acc2 sw2" x="40" y="394" width="260" height="42"/><text class="tl" x="170" y="420" text-anchor="middle">the cell elongates</text></svg><figcaption>The acid growth hypothesis. Elongation is permanent: the loosened wall is stretched by the turgor pressure and then re-formed.</figcaption></figure>
:::

:::eg Explain how auxin causes a plant cell to elongate.
Auxin binds to a receptor on the cell surface membrane of a cell in the zone of elongation. [B1]

It stimulates proton pumps in the membrane, which use ATP to pump H⁺ ions into the cell wall. [B1]

The pH of the wall falls, which activates the proteins called expansins. [B1]

The expansins loosen the bonds between the cellulose microfibrils, so the wall is more flexible. [B1]

Water enters the cell by osmosis, and the turgor pressure stretches the loosened wall, so the cell lengthens. [B1]

A weaker answer says "auxin makes the cells grow longer". It misses the proton pumps, the lower pH and the loosening of the wall, and scores one mark.
:::

:::note Auxin and the bending of shoots towards light
If light shines on a shoot from one side, auxin ends up on the **shaded side**. Cells on the shaded side elongate more than those on the lit side, so the shoot **bends towards the light**. This is a use of the elongation mechanism above: the same acid growth, with more of it on one side.
:::

## Gibberellin and the germination of barley

A barley grain contains a small **embryo** and a large store of **starch** in the **endosperm**, surrounded by a layer of cells called the **aleurone layer**. A dry seed is dormant. Germination starts when the seed takes in water, and it needs glucose for respiration and growth. The starch is insoluble and cannot be used until it is hydrolysed, so the seed needs the enzyme amylase.

:::def Gibberellin
A plant hormone made by the embryo of a germinating seed. It stimulates the cells of the aleurone layer to make amylase.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 352 224" role="img" aria-label="Section through a barley grain. The outer layer is the aleurone layer. Inside it is the large starchy endosperm. A small embryo sits at the bottom right. A dashed arrow shows gibberellin passing from the embryo to the aleurone layer. A solid arrow shows amylase passing from the aleurone layer into the endosperm. Starch in the endosperm is hydrolysed to maltose and then glucose, and an arrow carries the glucose to the embryo."><path class="fm s-acc sw2" d="M206 10L214.6 10.8L222.8 13.3L230.4 17.4L237.1 22.9L242.6 29.6L246.7 37.2L249.2 45.4L250 54L250 166L249.2 174.6L246.7 182.8L242.6 190.4L237.1 197.1L230.4 202.6L222.8 206.7L214.6 209.2L206 210L54 210L45.4 209.2L37.2 206.7L29.6 202.6L22.9 197.1L17.4 190.4L13.3 182.8L10.8 174.6L10 166L10 54L10.8 45.4L13.3 37.2L17.4 29.6L22.9 22.9L29.6 17.4L37.2 13.3L45.4 10.8L54 10Z"/><path class="f1 s-acc sw2" d="M204 24L210.2 24.6L216.2 26.4L221.8 29.4L226.6 33.4L230.6 38.2L233.6 43.8L235.4 49.8L236 56L236 164L235.4 170.2L233.6 176.2L230.6 181.8L226.6 186.6L221.8 190.6L216.2 193.6L210.2 195.4L204 196L56 196L49.8 195.4L43.8 193.6L38.2 190.6L33.4 186.6L29.4 181.8L26.4 176.2L24.6 170.2L24 164L24 56L24.6 49.8L26.4 43.8L29.4 38.2L33.4 33.4L38.2 29.4L43.8 26.4L49.8 24.6L56 24Z"/><path class="fr ln" d="M232 180L231.8 182.2L231 184.4L229.9 186.5L228.2 188.5L226.2 190.3L223.8 192L221 193.5L218 194.7L214.7 195.7L211.2 196.4L207.7 196.9L204 197L200.3 196.9L196.8 196.4L193.3 195.7L190 194.7L187 193.5L184.2 192L181.8 190.3L179.8 188.5L178.1 186.5L177 184.4L176.2 182.2L176 180L176.2 177.8L177 175.6L178.1 173.5L179.8 171.5L181.8 169.7L184.2 168L187 166.5L190 165.3L193.3 164.3L196.8 163.6L200.3 163.1L204 163L207.7 163.1L211.2 163.6L214.7 164.3L218 165.3L221 166.5L223.8 168L226.2 169.7L228.2 171.5L229.9 173.5L231 175.6L231.8 177.8Z"/><path class="c3 sw2 dash" d="M200 164L200 17" marker-end="url(#ah)"/><path class="c1 sw2" d="M76 17L76 112" marker-end="url(#ah)"/><text class="tl" x="84" y="52">amylase</text><text class="tl" x="194" y="94" text-anchor="end">gibberellin</text><text class="tl" x="34" y="142">starch hydrolysed to</text><text class="tl" x="34" y="156">maltose, then glucose</text><path class="c2 sw2" d="M116 168L172 182" marker-end="url(#ah)"/><text class="tl" x="262" y="26">aleurone</text><text class="tl" x="262" y="40">layer</text><path class="ln-m thin" d="M258 30L243 48"/><text class="tl" x="262" y="110">starchy</text><text class="tl" x="262" y="124">endosperm</text><path class="ln-m thin" d="M258 116L230 116"/><text class="tl" x="262" y="196">embryo</text><path class="ln-m thin" d="M258 192L230 186"/></svg><figcaption>Gibberellin from the embryo switches on amylase production in the aleurone layer. Amylase hydrolyses the starch of the endosperm, and the sugars feed the embryo.</figcaption></figure>
:::

:::steps
1. The seed **absorbs water**, and the **embryo** starts to make **gibberellin**.
2. Gibberellin **diffuses to the aleurone layer** and binds to receptors on its cells.
3. This starts a pathway that breaks down **DELLA proteins**, which normally stop the gene for amylase from being transcribed (see [Genes, phenotype and gene control](#bio.genecontrol)). With the DELLA proteins gone, the gene is **transcribed**, and the cells make **amylase**.
4. **Amylase** is secreted into the endosperm and **hydrolyses starch to maltose**, which is hydrolysed to glucose.
5. The **glucose** is carried to the embryo and used in **respiration** (for ATP) and for making cell walls and other materials, so the embryo grows.
:::

Gibberellin does not itself digest starch: it **switches on the production of amylase**. This is a link between a hormone and gene expression.

:::lab Investigating the effect of gibberellin on amylase production in barley
**Aim**: show that gibberellin makes barley seeds produce amylase.

:::steps
1. Prepare plates of agar containing starch. Soak barley seeds in water for several hours, then cut each in half across the middle and keep the half **without** the embryo.
2. Put the half-seeds, cut side down, on starch–agar plates: some with a little gibberellin solution on the agar, some with water, and some with **boiled** seeds on gibberellin.
3. Incubate at about 25 °C for 24–48 hours.
4. Flood each plate with iodine solution. Starch gives a blue-black colour; where amylase has hydrolysed the starch there is a **clear zone**.
5. Measure the diameter of each clear zone in mm. Repeat with several seeds and calculate the mean.
:::

**Typical results**: a large clear zone round the half-seeds on gibberellin; only a very small zone for water; none for boiled seeds.

**Variables**: the independent variable is gibberellin (present or absent); the dependent variable is the diameter of the clear zone. Standardise the number and size of half-seeds, the volume and concentration of starch agar, the temperature and the time.

**Why the half-seed has no embryo**: the embryo makes its own gibberellin, which would hide the effect.

**Safety**: iodine solution is an irritant and stains; wear eye protection. Wash hands after handling seeds and agar plates, and do not open plates that show unexpected microbial growth.
:::

:::eg Half-seeds of barley with no embryo were kept in water or in gibberellin solution, and the amylase activity was measured. Describe and explain the results.
The amylase activity is in arbitrary units. The data are invented.

| time / h | with gibberellin | in water |
|---|---|---|
| 0 | 0 | 0 |
| 12 | 4 | 1 |
| 24 | 18 | 2 |
| 36 | 40 | 3 |
| 48 | 62 | 3 |

(a) Describe the effect of gibberellin. (b) Calculate the mean rate of increase of amylase activity with gibberellin between 12 h and 36 h. (c) Explain the results.

**(a)** With gibberellin the amylase activity rises from 0 to 62 units in 48 h, but in water it reaches only 3 units. [B1]

**(b)** The change in activity is \(40 - 4 = 36\) units in \(36 - 12 = 24\) h.

\[\begin{aligned} \text{mean rate} &= \frac{40 - 4}{36 - 12} \\ &= 1.5\ \text{units h}^{-1} \end{aligned}\]

[M1] [A1]

**(c)** Gibberellin binds to receptors on the cells of the aleurone layer and stimulates them to make amylase (it switches on the amylase gene). [B1]

Without the embryo, the half-seeds in water have no source of gibberellin, so very little amylase is made. [B1]

(Also credit: amylase then hydrolyses starch in the endosperm to maltose, which is used by the embryo.)
:::

## Practice

:::try Start easy, finish at exam standard
Q: Name two features of a guard cell that are not found in most other epidermal cells.
A: Chloroplasts; a thicker inner wall (next to the pore) with radially arranged cellulose microfibrils; K⁺ channels and proton pumps in the cell surface membrane.
Q: State whether the guard cells are turgid or flaccid when a stoma is open, and what moves into the guard cells to make them so.
A: Turgid. Water enters by osmosis, because K⁺ ions have entered and lowered the water potential of the guard cells.
Q: Which hormone closes stomata in a drought, and which ion acts as the second messenger?
A: Abscisic acid (ABA); calcium ions (Ca²⁺).
Q: A plant kept in constant darkness for three days still opened its stomata a little at midday. What does this show?
A: The stomata are controlled by an internal (endogenous) biological clock, as well as responding directly to light.
Q: Why does a Venus fly trap not close when a raindrop lands on one hair?
A: The trap closes only after two stimulations within about 20 seconds. One touch produces an action potential that is not enough, which avoids closing for non-living objects.
Q: In which part of a shoot is auxin made, and what does it do to the cells just behind that part?
A: In the shoot tip. It makes the cells just behind it elongate.
Q: Put the steps in order: wall pH falls; auxin binds to receptor; expansins loosen the wall; proton pumps pump H⁺ into the wall; the cell elongates.
A: Auxin binds to receptor; proton pumps pump H⁺ into the wall; wall pH falls; expansins loosen the wall; the cell elongates.
Q: Which part of a barley seed makes gibberellin, and which part responds to it?
A: The embryo makes it. The aleurone layer responds by making amylase.
Q: A stoma has an aperture of 6.0 µm in the morning and 1.5 µm in the afternoon. Calculate the percentage decrease.
A: \((6.0 - 1.5) \div 6.0 \times 100 = 75\%\).
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Describe the structure of a guard cell and explain how it helps the stoma to open.
A: The cell wall is thicker on the side next to the pore (the inner wall) than on the outer side. [B1]
Cellulose microfibrils are arranged radially, so the cell cannot widen and only lengthens when it takes in water. [B1]
So when the guard cells are turgid they curve apart, opening the pore. [B1]
Q: [4 marks] ★★ The table shows the carbon dioxide uptake and water loss of a leaf at different stomatal apertures. The data are invented.

| aperture / µm | CO₂ uptake / units | water loss / units |
|---|---|---|
| 0 | 0 | 0 |
| 2 | 5 | 4 |
| 4 | 8 | 8 |
| 6 | 9 | 12 |
| 8 | 9.5 | 16 |

(a) Calculate the carbon dioxide uptake per unit of water lost at an aperture of 2 µm and at 8 µm. (b) Explain, using the data, why a plant regulates the stomatal aperture.
H: Divide the carbon dioxide uptake by the water loss for each aperture.
H: Compare how much each quantity changes between 4 µm and 8 µm.
A: (a) \(5 \div 4 = 1.25\) at 2 µm [M1] and \(9.5 \div 16 = 0.59\) at 8 µm [A1]
(b) Carbon dioxide uptake rises less and less as the aperture increases (from 8 units at 4 µm to 9.5 units at 8 µm), but water loss increases in proportion (from 8 to 16 units). [B1]
So wider apertures lose more water for little extra carbon dioxide; the plant balances the need for carbon dioxide for photosynthesis with the need to minimise water loss. [B1]
Q: [4 marks] ★★ Leaves were sprayed with abscisic acid at different concentrations and the stomatal aperture was measured. The data are invented.

| ABA / µmol dm⁻³ | aperture / µm |
|---|---|
| 0 | 9.0 |
| 1 | 7.5 |
| 10 | 4.0 |
| 100 | 1.5 |
| 1000 | 1.0 |

(a) Describe the effect of ABA concentration on the aperture. (b) Calculate the percentage decrease in aperture between 0 and 100 µmol dm⁻³.
H: For (a), give the trend with figures and say where it levels off.
A: (a) The aperture decreases as the ABA concentration increases, from 9.0 µm with no ABA to 1.0 µm at 1000 µmol dm⁻³. [B1]
Most of the decrease is below 100 µmol dm⁻³, and above that the aperture changes little (1.5 to 1.0 µm). [B1]
(b) \((9.0 - 1.5) \div 9.0 \times 100\) [M1] \(= 83\%\) [A1]
Q: [4 marks] ★★ A trap of a Venus fly trap was tested in an experiment. One trigger hair was touched once: the trap did not close. A hair was touched twice 10 s apart: it closed. A hair was touched twice 60 s apart: it did not close. (a) What do the results show about the stimulation needed to close the trap? (b) Explain the advantage to the plant of this response.
H: Think about what else might touch a trigger hair, and what the plant gets from an insect.
A: (a) Two stimulations within a short time (about 20 s) are needed to close the trap. [B1]
One touch, or two touches too far apart, are not enough. [B1]
(b) The trap does not close for a raindrop or debris, so energy is not wasted. [B1]
It closes only for a moving insect, which the plant digests to obtain nitrogen (as amino acids) that the bog soil lacks. [B1]
Q: [4 marks] ★★ A pot plant on a window sill grows with its shoot bending towards the light. Explain how auxin causes this.
H: Where is the auxin on the side of the shoot facing away from the light?
A: More auxin is on the shaded side of the shoot than on the lit side. [B1]
Auxin stimulates proton pumps that pump H⁺ into the cell walls, so the pH falls and expansins loosen the walls. [B1]
Cells on the shaded side elongate more, as water enters by osmosis and stretches the loosened walls. [B1]
So the shoot bends towards the light. [B1]
Q: [6 marks] (#bio.genecontrol) ★★★ A mutant barley plant makes DELLA proteins that cannot be broken down, even when gibberellin is present. (a) Predict the effect on the germination of the grains and explain. (b) The mutant is sprayed with a larger dose of gibberellin. Explain why this does not help.
H: What do DELLA proteins do to the gene for amylase?
H: For (b), at which step is the pathway blocked?
A: (a) The grains germinate poorly or not at all. [B1]
Gibberellin from the embryo binds to the aleurone cells, but the DELLA proteins are not broken down. [B1]
The gene for amylase stays switched off (is not transcribed), so little amylase is made. [B1]
So starch in the endosperm is not hydrolysed to maltose and glucose, and the embryo has too little glucose for respiration and growth. [B1]
(b) The block is after the binding of gibberellin: the proteins that stop transcription cannot be removed. [B1]
So more gibberellin does not switch on the gene. [B1]
Q: [5 marks] (#bio.photosynthesis) ★★★ A plant in a drought closes its stomata at midday. (a) Explain why this reduces the rate of photosynthesis. (b) Explain why closing the stomata is an advantage to the plant. (c) Name the hormone that causes the closure.
H: Which raw material for the light-independent stage can no longer get in?
A: (a) Carbon dioxide cannot diffuse in through the closed stomata, so less is available for the light-independent stage. [B1]
Less carbon dioxide combines with ribulose bisphosphate, so less glycerate 3-phosphate and triose phosphate is made. [B1]
(b) It reduces the water lost by transpiration, so the plant does not wilt or die. [B1]
Water is also needed for the light-dependent stage and for turgor. [B1]
(c) Abscisic acid. [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ Fusicoccin is a toxin made by a fungus. It keeps the proton pumps in the cell surface membranes of plant cells permanently active. Young stem segments were placed in a buffer solution, with or without fusicoccin. (a) Predict the effect of fusicoccin on the elongation of the segments, and explain. (b) The same toxin is applied to the leaves. Predict the effect on stomata in the light and in the dark, and explain.
H: What do the proton pumps do to the pH of the cell wall?
H: For (b), which ions move in when the proton pumps work, and what does that do to guard cell turgor?
A: (a) The segments elongate more (and faster) than in the buffer alone. [B1]
The active proton pumps pump H⁺ into the cell walls, so the pH falls and expansins loosen the bonds between cellulose microfibrils. [B1]
Water enters and the turgor pressure stretches the walls. [B1]
(b) The stomata stay open in the dark, and open fully in the light. [B1]
Active proton pumps in the guard cells let K⁺ ions enter through channels, lowering the water potential of the guard cells. [B1]
Water enters, the guard cells are turgid, and the stomata open. [B1]
Q: [5 marks] ★★★ A gardener sprays abscisic acid on potted plants before they are carried to a market in a hot van, and finds that the plants wilt less. (a) Explain why the plants wilt less. (b) Suggest one disadvantage of using abscisic acid in this way if the plants are kept sprayed for several days.
H: What does closing the stomata do to photosynthesis?
A: (a) ABA binds to receptors on guard cells, so Ca²⁺ ions enter as a second messenger. [B1]
K⁺ ions leave, water leaves by osmosis, the guard cells become flaccid and the stomata close. [B1]
Less water is lost by transpiration, so the cells keep their turgor and the plant does not wilt. [B1]
(b) Carbon dioxide cannot enter, so the rate of photosynthesis is reduced. [B1]
Less growth (less sugar made), so the plants may grow slowly or lose condition if sprayed for many days. [B1]
:::

:::quiz
? What happens to the guard cells when a stoma opens?
+ they take in water by osmosis and become turgid
- they lose water by osmosis and become flaccid
- they pump water in by active transport
- they divide to make the pore wider
> K⁺ ions enter, lowering the water potential, so water enters by osmosis. The thicker inner wall and radial microfibrils make the cells bend apart.
? Which ion acts as a second messenger in the response of guard cells to abscisic acid?
+ calcium ions
- potassium ions
- hydrogen ions
- chloride ions
> ABA binds at the surface and makes Ca²⁺ enter the cytoplasm; the Ca²⁺ then opens channels for K⁺ ions to leave.
? Why do guard cells open stomata in the light?
+ proton pumps use ATP to pump H⁺ out, and K⁺ ions then enter
- chlorophyll absorbs light and directly pushes the walls apart
- water is pumped in by active transport
- carbon dioxide enters and makes the cells turgid
> The pumps create an electrochemical gradient, K⁺ enters through channels, and water follows by osmosis.
? A plant kept in constant light still opens and closes its stomata about every 24 hours. What does this show?
+ the stomata are controlled by an internal biological clock
- stomata respond only to the light intensity
- stomata respond only to the concentration of carbon dioxide
- stomata are not controlled by the plant
> If the rhythm continues when the light is constant, the cycle must come from inside the plant: a circadian rhythm.
? How does the Venus fly trap avoid closing for a raindrop?
+ it closes only if a trigger hair is touched twice within about 20 seconds
- it closes only at night
- it has no trigger hairs
- it closes only when its stomata are open
> One touch, or two touches too far apart, do not produce enough stimulation. This saves energy.
? What does auxin do to proton pumps in the cell surface membrane of a young stem cell?
+ it stimulates them to pump H⁺ into the cell wall
- it stimulates them to pump H⁺ into the vacuole
- it stops them, so the cell wall becomes alkaline
- it makes them pump K⁺ ions out of the cell
> The lowered pH of the wall activates expansins, which loosen bonds between the cellulose microfibrils.
? What does auxin do in elongation growth?
+ makes cells in the shoot lengthen by stretching their walls
- makes cells in the shoot divide more quickly
- makes cell walls thicker so cells cannot grow
- makes the shoot tip produce gibberellin
> In this role auxin acts on elongation, not on cell division. The acid growth mechanism loosens the wall so that turgor can stretch it.
? What is the role of gibberellin in the germination of a barley grain?
+ it stimulates the aleurone layer to make amylase
- it digests the starch in the endosperm
- it makes the seed take up water
- it is made by the aleurone layer and acts on the embryo
> The embryo makes gibberellin. It switches on the amylase gene in the aleurone layer; the amylase then hydrolyses starch.
? A barley seed's embryo is removed. What happens to amylase production in the seed in water?
+ very little amylase is made, because no gibberellin is made
- the same amount is made, because the aleurone layer makes gibberellin
- more is made, because the starch is not used
- none is made, because the aleurone layer has no gene for amylase
> Without the embryo there is no gibberellin. The aleurone cells still have the gene and make amylase if gibberellin is added.
:::

:::checklist What you can now do
- [ ] I can explain that stomata open and close in response to environmental conditions to balance carbon dioxide uptake with water loss.
- [ ] I can explain that stomata have daily rhythms of opening and closing.
- [ ] I can describe the structure and function of guard cells and explain how they open and close a stoma.
- [ ] I can describe the role of abscisic acid in closing stomata in water stress, including calcium ions as a second messenger.
- [ ] I can describe how a Venus fly trap responds to stimulation of its trigger hairs and how the trap closes.
- [ ] I can explain the role of auxin in elongation growth, with proton pumping and acidification of the cell wall.
- [ ] I can describe the role of gibberellin in the germination of barley.
:::

:::recap
- Stomata balance carbon dioxide uptake against water loss. They are normally open in the light and closed in the dark; the rhythm continues in constant light, so there is an internal biological clock.
- Guard cells: thick inner wall, radial cellulose microfibrils, chloroplasts. In the light, proton pumps (ATP) pump H⁺ out, K⁺ channels open and K⁺ enters, water potential falls, water enters by osmosis, the cells become turgid and curve apart. Closing is the reverse.
- Abscisic acid (water stress) binds to receptors on guard cells; Ca²⁺ enters as a second messenger; ion channels open, K⁺ leaves, water leaves, guard cells flaccid, stoma closes.
- Venus fly trap: touch two trigger hairs (or one twice) within about 20 s; action potentials; outer cells of the lobes expand quickly; the lobes flip from convex to concave and snap shut.
- Auxin (made in the shoot tip): binds to receptors, stimulates proton pumps, H⁺ into the wall, pH falls, expansins loosen bonds between cellulose microfibrils, turgor stretches the wall, the cell elongates (acid growth).
- Gibberellin: embryo makes it; it acts on the aleurone layer (breaking down DELLA proteins) so amylase is made; amylase hydrolyses starch to maltose and glucose for the embryo.
:::

:::links
- read: [CAIE A Level Biology: control and coordination notes and topic questions](https://www.physicsandmathstutor.com/biology-revision/a-level-cie/control-and-coordination/) · Physics & Maths Tutor · free revision notes and past-paper questions sorted by topic
- practise: [Control and coordination (9700, exams from 2025)](https://www.savemyexams.com/a-level/biology/cie/25/topics/15-control-and-coordination/) · Save My Exams · notes and exam questions with mark schemes, some free [paid]
- watch: [Amoeba Sisters videos](https://www.youtube.com/@AmoebaSisters/videos) · Amoeba Sisters (YouTube) · a friendly first explanation of plant hormones
- read: [Plant form and physiology](https://openstax.org/books/biology-2e/pages/30-introduction) · OpenStax Biology 2e · free university textbook chapter on plant responses and hormones, beyond the syllabus in places
- papers: [Paper 4 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-biology/cie-paper-4/) · Physics & Maths Tutor · find the plant control questions in real papers [unofficial]

Links checked 24 October 2026.
:::

Next: [Meiosis and genetic variation](#bio.meiosis) begins the topic of inheritance by following the chromosomes through meiosis.
