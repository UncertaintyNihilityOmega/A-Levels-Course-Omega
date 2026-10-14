@chapter phys.efields
@title Electric fields
@level a2
@paper CAIE P4 (A Level)
@time 6–8 hours
@summary Electric field strength and field lines, uniform fields between parallel plates and the motion of charged particles in them, Coulomb's law, the field of a point charge, and electric potential and potential energy, which follow the same pattern as gravitational fields.

:::why
A television tube, an inkjet printer, a lightning conductor and the nucleus of every atom all depend on electric fields. This chapter shows how a charge changes the space around it, how that field pushes other charges, and how much energy it takes to move them. If you have met [Gravitational fields](#phys.gravity), the ideas will feel familiar: the laws are both inverse-square laws, with one big difference, because electric forces can repel as well as attract.
:::

**Before you start**, you need field strength and potential from [Gravitational fields](#phys.gravity), charge and p.d. from [Electricity](#phys.electricity), and projectile motion from [Kinematics](#phys.kinematics).

:::try Warm-up
Q: The gravitational field strength at the Earth's surface is \(9.81\,\mathrm{N\,kg^{-1}}\). What is it at a point twice as far from the centre of the Earth? (from [Gravitational fields](#phys.gravity))
A: Field strength follows an inverse-square law, \(g \propto 1/r^2\). Doubling \(r\) divides \(g\) by 4: \(9.81/4 = 2.45\,\mathrm{N\,kg^{-1}}\).
Q: A ball is thrown horizontally at \(12\,\mathrm{m\,s^{-1}}\) from the top of a cliff \(20\,\mathrm{m}\) high. How far from the foot of the cliff does it land? (from [Kinematics](#phys.kinematics))
A: Vertically, \(s = \tfrac12 gt^2\) gives \(t = \sqrt{2 \times 20/9.81} = 2.02\,\mathrm{s}\). Horizontally the speed is constant, so the distance is \(12 \times 2.02 = 24\,\mathrm{m}\).
Q: A p.d. of \(12\,\mathrm{V}\) moves \(3.0\,\mathrm{C}\) of charge between two points. How much energy is transferred? (from [Electricity](#phys.electricity))
A: \(V = W/Q\), so \(W = QV = 3.0 \times 12 = 36\,\mathrm{J}\).
:::

## Electric fields and field strength

Rub a balloon on your hair and it sticks to the wall. The balloon has gained **charge**, and charged objects push or pull on each other without touching. There are two kinds of charge: like charges repel and unlike charges attract. As with gravity, physicists describe this action at a distance with a **field**.

:::def Electric field
A region of space in which a charge experiences a force.
:::

A big charge makes a strong field, and a big test charge feels a big force. To describe the field itself, divide out the size of the charge you test it with, as you did for gravity.

:::def Electric field strength
The force per unit positive charge acting on a small stationary test charge placed at that point in the field.
:::

:::formula Electric field strength and the force on a charge
\[E = \frac{F}{q} \qquad\qquad F = qE\]
\(E\): electric field strength (\(\mathrm{N\,C^{-1}}\) or \(\mathrm{V\,m^{-1}}\)) · \(F\): force on the charge (N) · \(q\): the charge (C), with its sign.
:::

Field strength is a **vector**. Its direction is the direction of the force on a **positive** charge. A negative charge feels a force in the **opposite** direction to the field. The test charge must be small, so that it does not move the charges that make the field.

The unit is the newton per coulomb. In the next section you will see that this is the same as the volt per metre.

:::eg A uniform electric field has strength \(3.0 \times 10^{4}\,\mathrm{N\,C^{-1}}\). Find the force on (a) a charge of \(+2.0\,\mu\mathrm{C}\) and (b) an electron.
(a) \(F = qE = 2.0 \times 10^{-6} \times 3.0 \times 10^{4}\) [C1] \(= 6.0 \times 10^{-2}\,\mathrm{N}\) in the direction of the field. [A1]

(b) The electron's charge is \(-1.60 \times 10^{-19}\,\mathrm{C}\), so \(F = 1.60 \times 10^{-19} \times 3.0 \times 10^{4} = 4.8 \times 10^{-15}\,\mathrm{N}\), directed **opposite** to the field. [A1]

The force on the electron is tiny in newtons, but its mass is only \(9.11 \times 10^{-31}\,\mathrm{kg}\), so its acceleration is huge.
:::

### Field lines

A **field line** is a line drawn so that its direction at each point is the direction of the force on a small positive charge, with an arrow to show it. The pattern tells you the field at a glance.

- Field lines start on positive charges and end on negative charges (or go off to infinity).
- Lines never cross, because the field has only one direction at each point.
- Where the lines are closer together, the field is stronger.
- Lines meet the surface of a conductor at right angles.

:::html
<figure class="fig wide"><svg viewBox="0 0 600 462" role="img" aria-label="Four electric field line patterns: straight lines pointing away from an isolated positive charge, straight lines pointing into an isolated negative charge, curved lines running from a positive charge to a negative charge beside it, and lines from two positive charges that bend away from each other."><path class="c1" d="M159 105L235 105"/><path class="c1" d="M200 105L210 105" marker-end="url(#ah-phys)"/><path class="c1" d="M156.4 111.4L210.1 165.1"/><path class="c1" d="M185.4 140.4L192.4 147.4" marker-end="url(#ah-phys)"/><path class="c1" d="M150 114L150 190"/><path class="c1" d="M150 155L150 165" marker-end="url(#ah-phys)"/><path class="c1" d="M143.6 111.4L89.9 165.1"/><path class="c1" d="M114.6 140.4L107.6 147.4" marker-end="url(#ah-phys)"/><path class="c1" d="M141 105L65 105"/><path class="c1" d="M100 105L90 105" marker-end="url(#ah-phys)"/><path class="c1" d="M143.6 98.6L89.9 44.9"/><path class="c1" d="M114.6 69.6L107.6 62.6" marker-end="url(#ah-phys)"/><path class="c1" d="M150 96L150 20"/><path class="c1" d="M150 55L150 45" marker-end="url(#ah-phys)"/><path class="c1" d="M156.4 98.6L210.1 44.9"/><path class="c1" d="M185.4 69.6L192.4 62.6" marker-end="url(#ah-phys)"/><circle class="fp s-ink sw2" cx="150" cy="105" r="9"/><text class="tb tc" x="150" y="109.5">+</text><text class="tl tc" x="150" y="220">(a) isolated positive charge</text><path class="c1" d="M535 105L459 105"/><path class="c1" d="M510 105L500 105" marker-end="url(#ah-phys)"/><path class="c1" d="M510.1 165.1L456.4 111.4"/><path class="c1" d="M492.4 147.4L485.4 140.4" marker-end="url(#ah-phys)"/><path class="c1" d="M450 190L450 114"/><path class="c1" d="M450 165L450 155" marker-end="url(#ah-phys)"/><path class="c1" d="M389.9 165.1L443.6 111.4"/><path class="c1" d="M407.6 147.4L414.6 140.4" marker-end="url(#ah-phys)"/><path class="c1" d="M365 105L441 105"/><path class="c1" d="M390 105L400 105" marker-end="url(#ah-phys)"/><path class="c1" d="M389.9 44.9L443.6 98.6"/><path class="c1" d="M407.6 62.6L414.6 69.6" marker-end="url(#ah-phys)"/><path class="c1" d="M450 20L450 96"/><path class="c1" d="M450 45L450 55" marker-end="url(#ah-phys)"/><path class="c1" d="M510.1 44.9L456.4 98.6"/><path class="c1" d="M492.4 62.6L485.4 69.6" marker-end="url(#ah-phys)"/><circle class="fp s-ink sw2" cx="450" cy="105" r="9"/><text class="tb tc" x="450" y="109.5">−</text><text class="tl tc" x="450" y="220">(b) isolated negative charge</text><path class="c1" d="M105 335L112.5 335L120 335L127.5 335L135 335L142.5 335L150 335L157.5 335L165 335L172.5 335L180 335L187.5 335L195 335L196.5 335"/><path class="c1" d="M145.8 335L155.8 335" marker-end="url(#ah-phys)"/><path class="c1" d="M102.1 342.1L107.5 347.3L113 352.3L118.9 357L125.1 361.2L131.7 364.7L138.8 367.2L146.2 368.6L153.6 368.6L161 367.3L168.1 364.8L174.7 361.3L180.9 357.1L186.8 352.4L192.4 347.4L197.8 342.2L198.8 341.2"/><path class="c1" d="M145.6 368.6L155.6 368.6" marker-end="url(#ah-phys)"/><path class="c1" d="M95 345L95.1 352.5L95.5 360L96.2 367.5L97.3 374.9L98.9 382.2L101 389.4L103.7 396.4L107.1 403.1L111.1 409.4L115.9 415.2L121.4 420.3L127.5 424.6L134.3 427.8L141.5 429.9L148.9 430.8L156.4 430.3L163.7 428.6L170.6 425.6L176.9 421.6L182.6 416.7L187.6 411.1L191.8 405L195.4 398.4L198.3 391.4L200.6 384.3L202.3 377L203.5 369.6L204.3 362.2L204.8 354.7L205 347.2L205 344.2"/><path class="c1" d="M109.6 407.5L115.9 415.2" marker-end="url(#ah-phys)"/><path class="c1" d="M87.9 342.1L82.7 347.4L77.5 352.9L72.5 358.4L67.5 364L62.7 369.8L58 375.7L53.5 381.6L49.1 387.7L44.9 394L40.9 400.3L37 406.7L33.4 413.2L29.9 419.9L26.5 426.6L23.4 433.4"/><path class="c1" d="M54.2 380.6L48.4 388.8" marker-end="url(#ah-phys)"/><path class="c1" d="M85 335L77.5 335L70 335L62.5 335L55 335L47.5 335L40 335L32.5 335L25 335L17.5 335L10 335L5.5 335"/><path class="c1" d="M50.2 335L40.2 335" marker-end="url(#ah-phys)"/><path class="c1" d="M87.9 327.9L82.7 322.6L77.5 317.1L72.5 311.6L67.5 306L62.7 300.2L58 294.3L53.5 288.4L49.1 282.3L44.9 276L40.9 269.7L37 263.3L33.4 256.8L29.9 250.1L26.5 243.4L23.4 236.6"/><path class="c1" d="M54.2 289.4L48.4 281.2" marker-end="url(#ah-phys)"/><path class="c1" d="M95 325L95.1 317.5L95.5 310L96.2 302.5L97.3 295.1L98.9 287.8L101 280.6L103.7 273.6L107.1 266.9L111.1 260.6L115.9 254.8L121.4 249.7L127.5 245.4L134.3 242.2L141.5 240.1L148.9 239.2L156.4 239.7L163.7 241.4L170.6 244.4L176.9 248.4L182.6 253.3L187.6 258.9L191.8 265L195.4 271.6L198.3 278.6L200.6 285.7L202.3 293L203.5 300.4L204.3 307.8L204.8 315.3L205 322.8L205 325.8"/><path class="c1" d="M109.6 262.5L115.9 254.8" marker-end="url(#ah-phys)"/><path class="c1" d="M102.1 327.9L107.5 322.7L113 317.7L118.9 313L125.1 308.8L131.7 305.3L138.8 302.8L146.2 301.4L153.6 301.4L161 302.7L168.1 305.2L174.7 308.7L180.9 312.9L186.8 317.6L192.4 322.6L197.8 327.8L198.8 328.8"/><path class="c1" d="M145.6 301.4L155.6 301.4" marker-end="url(#ah-phys)"/><circle class="fp s-ink sw2" cx="95" cy="335" r="9"/><text class="tb tc" x="95" y="339.5">+</text><circle class="fp s-ink sw2" cx="205" cy="335" r="9"/><text class="tb tc" x="205" y="339.5">−</text><text class="tl tc" x="150" y="450">(c) a positive and a negative charge</text><path class="c1" d="M409.2 338.8L416.1 341.8L422.9 345L429.4 348.7L435.3 353.4L439.7 359.4L442.3 366.4L443.7 373.8L444.5 381.2L444.9 388.7L445.1 396.2L445.1 403.7L445.1 411.2L445 418.7L444.9 426.2L444.8 433.7"/><path class="c1" d="M441.4 361.5L443.3 371.4" marker-end="url(#ah-phys)"/><path class="c1" d="M403.8 344.2L406.5 351.2L408.9 358.4L410.8 365.6L412.2 373L412.9 380.4L413.2 387.9L412.9 395.4L412.3 402.9L411.4 410.3L410.2 417.8L408.9 425.1L407.4 432.5L407.1 434"/><path class="c1" d="M412.3 374.6L413.4 384.5" marker-end="url(#ah-phys)"/><path class="c1" d="M396.2 344.2L393.2 351.1L390 357.9L386.6 364.6L383.1 371.2L379.3 377.7L375.4 384.1L371.3 390.4L367.1 396.6L362.8 402.7L358.3 408.8L353.8 414.8L349.3 420.7L344.6 426.6L339.9 432.5L339 433.6"/><path class="c1" d="M379.3 377.8L374 386.3" marker-end="url(#ah-phys)"/><path class="c1" d="M390.8 338.8L383.8 341.7L376.8 344.4L369.9 347.1L362.8 349.8L355.8 352.4L348.8 355L341.7 357.5L334.6 359.9L327.5 362.4L320.4 364.8L313.3 367.1L306.2 369.5"/><path class="c1" d="M361.9 350.1L352.5 353.6" marker-end="url(#ah-phys)"/><path class="c1" d="M390.8 331.2L383.8 328.3L376.8 325.6L369.9 322.9L362.8 320.2L355.8 317.6L348.8 315L341.7 312.5L334.6 310.1L327.5 307.6L320.4 305.2L313.3 302.9L306.2 300.5"/><path class="c1" d="M361.9 319.9L352.5 316.4" marker-end="url(#ah-phys)"/><path class="c1" d="M396.2 325.8L393.2 318.9L390 312.1L386.6 305.4L383.1 298.8L379.3 292.3L375.4 285.9L371.3 279.6L367.1 273.4L362.8 267.3L358.3 261.2L353.8 255.2L349.3 249.3L344.6 243.4L339.9 237.5L339 236.4"/><path class="c1" d="M379.3 292.2L374 283.7" marker-end="url(#ah-phys)"/><path class="c1" d="M403.8 325.8L406.5 318.8L408.9 311.6L410.8 304.4L412.2 297L412.9 289.6L413.2 282.1L412.9 274.6L412.3 267.1L411.4 259.7L410.2 252.2L408.9 244.9L407.4 237.5L407.1 236"/><path class="c1" d="M412.3 295.4L413.4 285.5" marker-end="url(#ah-phys)"/><path class="c1" d="M409.2 331.2L416.1 328.2L422.9 325L429.4 321.3L435.3 316.6L439.7 310.6L442.3 303.6L443.7 296.2L444.5 288.8L444.9 281.3L445.1 273.8L445.1 266.3L445.1 258.8L445 251.3L444.9 243.8L444.8 236.3"/><path class="c1" d="M441.4 308.5L443.3 298.6" marker-end="url(#ah-phys)"/><path class="c1" d="M509.2 338.8L516.2 341.7L523.2 344.4L530.1 347.1L537.2 349.8L544.2 352.4L551.2 355L558.3 357.5L565.4 359.9L572.5 362.4L579.6 364.8L586.7 367.1L593.8 369.5"/><path class="c1" d="M538.1 350.1L547.5 353.6" marker-end="url(#ah-phys)"/><path class="c1" d="M503.8 344.2L506.8 351.1L510 357.9L513.4 364.6L516.9 371.2L520.7 377.7L524.6 384.1L528.7 390.4L532.9 396.6L537.2 402.7L541.7 408.8L546.2 414.8L550.7 420.7L555.4 426.6L560.1 432.5L561 433.6"/><path class="c1" d="M520.7 377.8L526 386.3" marker-end="url(#ah-phys)"/><path class="c1" d="M496.2 344.2L493.5 351.2L491.1 358.4L489.2 365.6L487.8 373L487.1 380.4L486.8 387.9L487.1 395.4L487.7 402.9L488.6 410.3L489.8 417.8L491.1 425.1L492.6 432.5L492.9 434"/><path class="c1" d="M487.7 374.6L486.6 384.5" marker-end="url(#ah-phys)"/><path class="c1" d="M490.8 338.8L483.9 341.8L477.1 345L470.6 348.7L464.7 353.4L460.3 359.4L457.7 366.4L456.3 373.8L455.5 381.2L455.1 388.7L454.9 396.2L454.9 403.7L454.9 411.2L455 418.7L455.1 426.2L455.2 433.7"/><path class="c1" d="M458.6 361.5L456.7 371.4" marker-end="url(#ah-phys)"/><path class="c1" d="M490.8 331.2L483.9 328.2L477.1 325L470.6 321.3L464.7 316.6L460.3 310.6L457.7 303.6L456.3 296.2L455.5 288.8L455.1 281.3L454.9 273.8L454.9 266.3L454.9 258.8L455 251.3L455.1 243.8L455.2 236.3"/><path class="c1" d="M458.6 308.5L456.7 298.6" marker-end="url(#ah-phys)"/><path class="c1" d="M496.2 325.8L493.5 318.8L491.1 311.6L489.2 304.4L487.8 297L487.1 289.6L486.8 282.1L487.1 274.6L487.7 267.1L488.6 259.7L489.8 252.2L491.1 244.9L492.6 237.5L492.9 236"/><path class="c1" d="M487.7 295.4L486.6 285.5" marker-end="url(#ah-phys)"/><path class="c1" d="M503.8 325.8L506.8 318.9L510 312.1L513.4 305.4L516.9 298.8L520.7 292.3L524.6 285.9L528.7 279.6L532.9 273.4L537.2 267.3L541.7 261.2L546.2 255.2L550.7 249.3L555.4 243.4L560.1 237.5L561 236.4"/><path class="c1" d="M520.7 292.2L526 283.7" marker-end="url(#ah-phys)"/><path class="c1" d="M509.2 331.2L516.2 328.3L523.2 325.6L530.1 322.9L537.2 320.2L544.2 317.6L551.2 315L558.3 312.5L565.4 310.1L572.5 307.6L579.6 305.2L586.7 302.9L593.8 300.5"/><path class="c1" d="M538.1 319.9L547.5 316.4" marker-end="url(#ah-phys)"/><circle class="fp s-ink sw2" cx="400" cy="335" r="9"/><text class="tb tc" x="400" y="339.5">+</text><circle class="fp s-ink sw2" cx="500" cy="335" r="9"/><text class="tb tc" x="500" y="339.5">+</text><text class="tl tc" x="450" y="450">(d) two positive charges</text><circle class="fi" cx="450" cy="335" r="3"/></svg><figcaption>Field lines of (a) an isolated positive charge, (b) an isolated negative charge, (c) a positive and a negative charge, and (d) two equal positive charges. The dot in (d) marks the neutral point, where the resultant field is zero. Lines are closer together where the field is stronger.</figcaption></figure>
:::

Near a single point charge the lines are straight and radial, and spread out as you move away, so the field weakens. Between a positive and a negative charge, many lines run from one to the other. Between two positive charges the lines push each other apart, and midway between two equal charges there is a **neutral point**, where the fields of the two charges are equal and opposite and so the resultant field is zero.

:::warn A field line is not the path of a particle
A field line gives the direction of the **force** at each point. A charge released from rest starts to move along the line. If the line is curved, the charge gains speed and its inertia carries it off the line. Only in a straight line field does the charge stay on the line.
:::

## Uniform fields between parallel plates

Connect two flat metal plates to opposite terminals of a power supply. The plates become equally and oppositely charged, and between them the field lines are straight, parallel and equally spaced. That is a **uniform field**: the same strength and direction at every point.

:::html
<figure class="fig"><svg viewBox="0 24 560 212" role="img" aria-label="Two horizontal parallel plates, the upper positive and the lower negative, with fifteen field lines running down between them, equally spaced in the middle and bulging outwards at the two ends. A dimension arrow shows the plate separation d."><rect class="fi" x="110" y="47" width="360" height="8"/><rect class="fi" x="110" y="195" width="360" height="8"/><path class="c1" d="M122 55L116.7 64.1L111.3 73.1L106.5 82.4L102.6 92.2L99.6 102.2L97.8 112.5L97 123L97.3 133.5L98.8 143.9L101.4 154.1L104.9 163.9L109.4 173.4L114.6 182.5L120.1 191.5L122.3 195.5"/><path class="c1" d="M96.9 121.3L97.2 129.3" marker-end="url(#ah-phys)"/><path class="c1" d="M146 55L143 65.1L140.1 75.2L137.4 85.3L135.2 95.6L133.5 105.9L132.5 116.4L132.3 126.9L132.8 137.4L134 147.8L135.9 158.1L138.3 168.3L141.1 178.4L144.1 188.5L146.2 195.7"/><path class="c1" d="M132.4 121.4L132.2 129.4" marker-end="url(#ah-phys)"/><path class="c1" d="M170 55L168.1 65.3L166.4 75.7L164.8 86.1L163.5 96.5L162.5 106.9L162 117.4L161.9 127.9L162.3 138.4L163 148.9L164.2 159.3L165.7 169.7L167.4 180.1L169.2 190.4L170.2 196.3"/><path class="c1" d="M162 121.7L161.9 129.7" marker-end="url(#ah-phys)"/><path class="c1" d="M194 55L192.8 65.4L191.7 75.9L190.7 86.3L189.9 96.8L189.4 107.3L189 117.8L189 128.3L189.2 138.8L189.7 149.3L190.4 159.7L191.3 170.2L192.4 180.6L193.5 191.1L194.1 195.6"/><path class="c1" d="M189 121.3L189 129.3" marker-end="url(#ah-phys)"/><path class="c1" d="M218 55L217.2 65.5L216.5 75.9L215.9 86.4L215.5 96.9L215.1 107.4L214.9 117.9L214.9 128.4L215 138.9L215.3 149.4L215.8 159.9L216.3 170.4L217 180.9L217.7 191.3L218.1 195.8"/><path class="c1" d="M214.9 121.4L214.9 129.4" marker-end="url(#ah-phys)"/><path class="c1" d="M242 55L241.5 65.5L241.1 76L240.8 86.5L240.5 97L240.3 107.5L240.2 118L240.2 128.5L240.3 139L240.4 149.5L240.7 160L241 170.5L241.4 181L241.8 191.4L242 195.9"/><path class="c1" d="M240.2 121.5L240.2 129.5" marker-end="url(#ah-phys)"/><path class="c1" d="M266 55L265.8 65.5L265.6 76L265.4 86.5L265.3 97L265.2 107.5L265.2 118L265.2 128.5L265.2 139L265.3 149.5L265.4 160L265.5 170.5L265.7 181L265.9 191.5L266 196"/><path class="c1" d="M265.2 121.5L265.2 129.5" marker-end="url(#ah-phys)"/><path class="c1" d="M290 55L290 65.5L290 76L290 86.5L290 97L290 107.5L290 118L290 128.5L290 139L290 149.5L290 160L290 170.5L290 181L290 191.5L290 196"/><path class="c1" d="M290 121.5L290 129.5" marker-end="url(#ah-phys)"/><path class="c1" d="M314 55L314.2 65.5L314.4 76L314.6 86.5L314.7 97L314.8 107.5L314.8 118L314.8 128.5L314.8 139L314.7 149.5L314.6 160L314.5 170.5L314.3 181L314.1 191.5L314 196"/><path class="c1" d="M314.8 121.5L314.8 129.5" marker-end="url(#ah-phys)"/><path class="c1" d="M338 55L338.5 65.5L338.9 76L339.2 86.5L339.5 97L339.7 107.5L339.8 118L339.8 128.5L339.7 139L339.6 149.5L339.3 160L339 170.5L338.6 181L338.2 191.4L338 195.9"/><path class="c1" d="M339.8 121.5L339.8 129.5" marker-end="url(#ah-phys)"/><path class="c1" d="M362 55L362.8 65.5L363.5 75.9L364.1 86.4L364.5 96.9L364.9 107.4L365.1 117.9L365.1 128.4L365 138.9L364.7 149.4L364.2 159.9L363.7 170.4L363 180.9L362.3 191.3L361.9 195.8"/><path class="c1" d="M365.1 121.4L365.1 129.4" marker-end="url(#ah-phys)"/><path class="c1" d="M386 55L387.2 65.4L388.3 75.9L389.3 86.3L390.1 96.8L390.6 107.3L391 117.8L391 128.3L390.8 138.8L390.3 149.3L389.6 159.7L388.7 170.2L387.6 180.6L386.5 191.1L385.9 195.6"/><path class="c1" d="M391 121.3L391 129.3" marker-end="url(#ah-phys)"/><path class="c1" d="M410 55L411.9 65.3L413.6 75.7L415.2 86.1L416.5 96.5L417.5 106.9L418 117.4L418.1 127.9L417.7 138.4L417 148.9L415.8 159.3L414.3 169.7L412.6 180.1L410.8 190.4L409.8 196.3"/><path class="c1" d="M418 121.7L418.1 129.7" marker-end="url(#ah-phys)"/><path class="c1" d="M434 55L437 65.1L439.9 75.2L442.6 85.3L444.8 95.6L446.5 105.9L447.5 116.4L447.7 126.9L447.2 137.4L446 147.8L444.1 158.1L441.7 168.3L438.9 178.4L435.9 188.5L433.8 195.7"/><path class="c1" d="M447.6 121.4L447.8 129.4" marker-end="url(#ah-phys)"/><path class="c1" d="M458 55L463.3 64.1L468.7 73.1L473.5 82.4L477.4 92.2L480.4 102.2L482.2 112.5L483 123L482.7 133.5L481.2 143.9L478.6 154.1L475.1 163.9L470.6 173.4L465.4 182.5L459.9 191.5L457.7 195.5"/><path class="c1" d="M483.1 121.3L482.8 129.3" marker-end="url(#ah-phys)"/><path class="ln thin dash" d="M474 55H528M474 195H528"/><path class="c1" d="M520 125V57" marker-end="url(#ah-phys)"/><path class="c1" d="M520 125V193" marker-end="url(#ah-phys)"/><text class="tl ti" x="529" y="129">d</text><text class="tl tc" x="290" y="40">positive plate</text><text class="tl tc" x="290" y="224">negative plate</text><text class="tl te" x="86" y="129">edge effect</text></svg><figcaption>Field lines between two parallel plates. In the middle the lines are parallel and equally spaced, so the field is uniform, with E = V/d. Near the ends the lines bulge outwards and the field is weaker.</figcaption></figure>
:::

Close to the edges, the lines bulge outwards and the field is weaker, so the field is only uniform in the middle of the gap. Where an exam question says "uniform field", it means you may ignore the edges.

:::formula Uniform field between parallel plates
\[E = \frac{\Delta V}{\Delta d}\]
\(E\): field strength (\(\mathrm{V\,m^{-1}}\)) · \(\Delta V\): p.d. between the plates (V) · \(\Delta d\): separation of the plates (m). The field points from the plate at higher potential (positive) to the plate at lower potential (negative).
:::

:::proof Why E = V/d for a uniform field
Move a charge \(q\) across the gap from one plate to the other.
By the definition of p.d., the work done on the charge is \(W = qV\).
The force on the charge is \(F = qE\) and it is the same everywhere, because the field is uniform. The distance moved along the field is \(d\), so \(W = Fd = qEd\).
Equate the two expressions: \(qV = qEd\), so \(E = V/d\).
The charge \(q\) cancels, so the result does not depend on the charge you use to find it.
:::

This also shows that the volt per metre and the newton per coulomb are the same unit:
\[1\,\mathrm{V\,m^{-1}} = 1\,\mathrm{J\,C^{-1}\,m^{-1}} = 1\,\mathrm{N\,m\,C^{-1}\,m^{-1}} = 1\,\mathrm{N\,C^{-1}}\]
using \(1\,\mathrm{V} = 1\,\mathrm{J\,C^{-1}}\) and \(1\,\mathrm{J} = 1\,\mathrm{N\,m}\).

:::eg A p.d. of \(2.0\,\mathrm{kV}\) is applied across two plates \(5.0\,\mathrm{mm}\) apart. Find the field strength, and the force on a charge of \(+1.60 \times 10^{-19}\,\mathrm{C}\) between them.
\[E = \frac{V}{d} = \frac{2.0 \times 10^{3}}{5.0 \times 10^{-3}} = 4.0 \times 10^{5}\,\mathrm{V\,m^{-1}}\] [C1] [A1]
\[F = qE = 1.60 \times 10^{-19} \times 4.0 \times 10^{5} = 6.4 \times 10^{-14}\,\mathrm{N}\] [A1]
Change the millimetres into metres first, or the unit comes out wrong. With the same p.d., halving the separation would double the field.
:::

:::eg An oil drop of mass \(3.3 \times 10^{-15}\,\mathrm{kg}\) is held stationary between two horizontal plates \(1.5\,\mathrm{cm}\) apart, with a p.d. of \(600\,\mathrm{V}\) across them and the upper plate positive. Find the charge on the drop and say whether it is positive or negative.
:::html
<figure class="fig small"><svg viewBox="28 0 308 196" role="img" aria-label="Two horizontal plates with the upper one positive. An oil drop between them is held still by an upward electric force and a downward weight of equal length, each labelled 3.2 times ten to the minus fourteen newtons. The field E points down."><rect class="fi" x="40" y="20" width="270" height="8"/><rect class="fi" x="40" y="170" width="270" height="8"/><text class="tl" x="40" y="14">+600 V</text><text class="tl" x="40" y="192">0 V</text><path class="c2" d="M80 48V98" marker-end="url(#ah2-phys)"/><text class="tl ti" x="90" y="78">E</text><circle class="fp s-ink sw2" cx="180" cy="99" r="14"/><text class="tl te" x="160" y="103">oil drop</text><path class="c1" d="M180 83V40" marker-end="url(#ah-phys)"/><text class="tl" x="190" y="62">F = qE = 3.2 × 10⁻¹⁴ N</text><path class="c1" d="M180 115V158" marker-end="url(#ah-phys)"/><text class="tl" x="190" y="142">W = mg = 3.2 × 10⁻¹⁴ N</text></svg><figcaption>The forces on the drop. The electric force acts upwards, opposite to the field, which is why the drop must be negative. It balances the weight, so the drop is stationary.</figcaption></figure>
:::
\[E = \frac{V}{d} = \frac{600}{1.5 \times 10^{-2}} = 4.0 \times 10^{4}\,\mathrm{V\,m^{-1}}\] [C1]
The drop is stationary, so the upward electric force balances its weight: \(qE = mg\). [B1]
\[q = \frac{mg}{E} = \frac{3.3 \times 10^{-15} \times 9.81}{4.0 \times 10^{4}} = 8.1 \times 10^{-19}\,\mathrm{C}\] [A1]
The field points downwards (from the positive upper plate), and the force on the drop points upwards, so the charge is **negative**. [B1] The charge is about 5 times \(e\): charge always comes in whole multiples of \(1.60 \times 10^{-19}\,\mathrm{C}\), a fact first shown by experiments of this kind.
:::

## Charged particles in a uniform field

A charge \(q\) in a uniform field feels a constant force \(qE\), so it has a constant acceleration \(a = qE/m\). You already know how to deal with constant acceleration. Two cases cover every question: the particle moves **along** the field lines, or **across** them.

### Along the field: gaining kinetic energy

A positive particle released from rest between two plates speeds up towards the negative plate. The field does work \(qV\) on it, and the work becomes kinetic energy:

:::key Energy gained in an electric field
\[qV = \tfrac12 mv^2 - \tfrac12 mu^2\]
For a particle starting from rest, \(qV = \tfrac12 mv^2\), so \(v = \sqrt{2qV/m}\). This works for any path between two points with p.d. \(V\), but only if you know the p.d. If you know the distance instead, use \(a = qE/m\) and the equations of motion.
:::

:::eg A proton is released from rest at the positive plate of a pair of plates with a p.d. of \(2.0\,\mathrm{kV}\) across them. Find its kinetic energy and speed when it reaches the negative plate.
\[E_K = qV = 1.60 \times 10^{-19} \times 2.0 \times 10^{3} = 3.2 \times 10^{-16}\,\mathrm{J}\] [C1] [A1]
\[v = \sqrt{\frac{2E_K}{m}} = \sqrt{\frac{2 \times 3.2 \times 10^{-16}}{1.67 \times 10^{-27}}} = 6.2 \times 10^{5}\,\mathrm{m\,s^{-1}}\] [A1]
:::

A particle with the charge of one electron that falls through 1 V gains \(1.60 \times 10^{-19}\,\mathrm{J}\). This amount of energy is called one **electronvolt**, which you will use in [Quantum physics](#phys.quantum). The proton above gained 2.0 keV.

:::eg An electron gun in an old television tube accelerates electrons from rest through \(2.0\,\mathrm{kV}\). Find the speed of the electrons as they leave the gun.
\[\tfrac12 mv^2 = eV \quad\Rightarrow\quad v = \sqrt{\frac{2 \times 1.60 \times 10^{-19} \times 2.0 \times 10^{3}}{9.11 \times 10^{-31}}}\] [C1]
\[v = 2.7 \times 10^{7}\,\mathrm{m\,s^{-1}}\] [A1]
This is about 9% of the speed of light. The formula \(\tfrac12 mv^2\) is accurate at this speed, and it is only at much higher speeds that relativity changes the answer. The electron has the same energy as the proton in the last example, but a speed over 40 times larger, because its mass is nearly 2000 times smaller.
:::

If the particle moves against the field (a positive charge moving towards the positive plate) it slows down and may stop. The same equation works, with a negative work done by the field.

### Across the field: a parabolic path

Now let a particle enter the field at right angles to the field lines. Take the field as vertical. Then:

- **Horizontally** there is no force, so the horizontal velocity \(v\) stays constant.
- **Vertically** there is a constant force \(qE\), so the vertical acceleration is \(a = qE/m\), starting from zero vertical velocity.

This is exactly a horizontal projectile, and the path is a **parabola**. The only difference from the cliff in the warm-up is that the force is electric, not gravitational.

:::html
<figure class="fig"><svg viewBox="0 14 480 180" role="img" aria-label="An electron enters at the middle of the gap between a positive upper plate and a negative lower plate, travelling horizontally. Its path curves upwards in a parabola towards the positive plate, and after leaving the plates it travels in a straight line, still rising. A dimension arrow shows the vertical deflection y at the exit."><rect class="fi" x="60" y="34" width="300" height="8"/><rect class="fi" x="60" y="162" width="300" height="8"/><path class="c1" d="M15 102H58" marker-end="url(#ah-phys)"/><path class="c3 sw2" d="M60 102Q210 102 360 65.4L440 45.9" marker-end="url(#ahr)"/><path class="ln thin dash" d="M360 102H400M360 65.4H400"/><path class="c2" d="M395 102V67.4" marker-end="url(#ah2-phys)"/><text class="tl" x="403" y="88">y = 6.1 mm</text><path class="c2" d="M300 132V158" marker-end="url(#ah2-phys)"/><text class="tl ti" x="310" y="150">E</text><text class="tl" x="70" y="124">electron, v = 3.0 × 10⁷ m s⁻¹</text><text class="tl tc" x="210" y="28">positive plate</text><text class="tl tc" x="210" y="190">negative plate</text></svg><figcaption>The path of an electron through the plates of the next example, drawn to scale. It keeps a constant speed along the plates and accelerates towards the positive plate, so the path is a parabola. Once it leaves the field it travels in a straight line.</figcaption></figure>
:::

:::eg Electrons travelling at \(3.0 \times 10^{7}\,\mathrm{m\,s^{-1}}\) enter midway between two horizontal plates \(2.0\,\mathrm{cm}\) apart and \(5.0\,\mathrm{cm}\) long, with a p.d. of \(500\,\mathrm{V}\) between them. Find the acceleration of an electron, the deflection as it leaves the plates, and its direction of motion on leaving.
Field: \(E = V/d = 500/(2.0 \times 10^{-2}) = 2.5 \times 10^{4}\,\mathrm{V\,m^{-1}}\). Force: \(F = eE = 1.60 \times 10^{-19} \times 2.5 \times 10^{4} = 4.0 \times 10^{-15}\,\mathrm{N}\). [C1]
\[a = \frac{F}{m} = \frac{4.0 \times 10^{-15}}{9.11 \times 10^{-31}} = 4.4 \times 10^{15}\,\mathrm{m\,s^{-2}}\] [A1]
Time in the plates: \(t = \dfrac{L}{v} = \dfrac{5.0 \times 10^{-2}}{3.0 \times 10^{7}} = 1.7 \times 10^{-9}\,\mathrm{s}\). [C1]
Vertical deflection (starting from zero vertical velocity): \(y = \tfrac12 at^2 = \tfrac12 \times 4.39 \times 10^{15} \times (1.67 \times 10^{-9})^2 = 6.1 \times 10^{-3}\,\mathrm{m}\). [A1]
The deflection is 6.1 mm, less than the 10 mm from the middle to a plate, so the electron leaves the plates. The vertical velocity is \(v_y = at = 7.3 \times 10^{6}\,\mathrm{m\,s^{-1}}\), so the angle above the original direction is
\[\tan\theta = \frac{v_y}{v_x} = \frac{7.3 \times 10^{6}}{3.0 \times 10^{7}} \quad\Rightarrow\quad \theta = 14^\circ\] [A1]
The electron moves towards the **positive** plate, as a negative charge must. After leaving the plates, there is no force and it travels in a straight line.
:::

Putting the steps together in symbols gives a result worth knowing:

:::key Deflection in a uniform field
\[y = \frac{qE}{2m}\left(\frac{L}{v}\right)^2 = \frac{qEL^2}{2mv^2}\]
\(y\): deflection after travelling a distance \(L\) along the plates (m) · \(v\): the constant speed along the plates. The deflection is proportional to the field strength, so doubling the p.d. doubles \(y\).
:::

:::eg Show that gravity can be ignored for the electron in the last example.
Weight: \(mg = 9.11 \times 10^{-31} \times 9.81 = 8.9 \times 10^{-30}\,\mathrm{N}\).
Electric force: \(eE = 4.0 \times 10^{-15}\,\mathrm{N}\).
The electric force is about \(4.5 \times 10^{14}\) times bigger, so gravity has no measurable effect. [B1] The same is true of protons and ions. For a charged oil drop or a dust particle (see the oil-drop example) the weight is comparable to the electric force and must be included.
:::

Charged particles in uniform fields are used to steer beams. In an oscilloscope the electron beam passes between two pairs of plates, one pair to deflect it up and down and the other sideways. In an inkjet printer, tiny drops of ink are given a charge and pass between plates, and the p.d. decides how far each lands from the centre of the character being printed.

:::lab Investigating the deflection of an electron beam
:::steps
1. Use a deflection tube (an evacuated glass tube with an electron gun and a pair of horizontal plates, and a scale on the screen). Set the accelerating p.d. \(V_a\) between the gun's cathode and anode to a fixed value, such as \(2.6\,\mathrm{kV}\), so that the electrons enter the plates at a constant speed.
2. Connect a variable supply across the plates. For at least six values of the plate p.d. \(V\), measure the deflection \(y\) of the spot on the screen and record it.
3. Plot \(y\) (\(y\)-axis) against \(V\) (\(x\)-axis). The graph is a straight line through the origin, since \(y\) is proportional to \(V\).
4. For a second graph, keep \(V\) fixed and change \(V_a\). Plot \(y\) against \(1/V_a\): this is also a straight line through the origin.
:::
The two results come from the same equation. With \(a = eV/(md)\), \(t = L/v\) and \(\tfrac12 mv^2 = eV_a\), the deflection at the end of the plates is
\[y = \frac{VL^2}{4dV_a}\]
so the gradient of the \(y\)–\(V\) graph is \(L^2/(4dV_a)\). Notice that the charge and the mass of the electron have cancelled, so every charged particle with the same charge-to-mass ratio would give the same line. For the tube of the earlier example (\(L = 5.0\,\mathrm{cm}\), \(d = 2.0\,\mathrm{cm}\)) and \(V_a = 2.56\,\mathrm{kV}\) (the p.d. that gives the electrons a speed of \(3.0 \times 10^{7}\,\mathrm{m\,s^{-1}}\)), the expected gradient is \(1.22 \times 10^{-5}\,\mathrm{m\,V^{-1}}\), so a plate p.d. of 500 V gives a deflection of 6.1 mm.
:::

## Coulomb's law

Two small charges exert forces on each other. The size of the force follows an inverse-square law, like Newton's law of gravitation.

:::def Coulomb's law
The force between two point charges is proportional to the product of the charges and inversely proportional to the square of their separation.
:::

:::formula Coulomb's law
\[F = \frac{Q_1 Q_2}{4\pi\varepsilon_0 r^2}\]
\(F\): force on each charge (N) · \(Q_1, Q_2\): the charges (C) · \(r\): separation of the charges (m) · \(\varepsilon_0\): permittivity of free space, \(8.85 \times 10^{-12}\,\mathrm{F\,m^{-1}}\). The constant \(\dfrac{1}{4\pi\varepsilon_0} = 8.99 \times 10^{9}\,\mathrm{m\,F^{-1}}\). The formula is for point charges in free space (air is close enough).
:::

The two charges exert forces of equal size on each other, in opposite directions, by Newton's third law. The force is **repulsive** between like charges and **attractive** between unlike ones. The usual exam method is to put the sizes of the charges into the formula without signs, which gives the size of the force, and then to say the direction from the signs.

The law is for **point charges**, but real charged objects are not points. A conducting sphere is the exception: from outside, the charge on a charged spherical conductor behaves as if it were all at the sphere's centre. That is why \(r\) is the distance between the **centres** of two charged spheres, however large they are.

:::eg Two small spheres carrying \(+2.0\,\mathrm{nC}\) each are \(30\,\mathrm{mm}\) apart in air. Find the force between them.
\[F = \frac{Q_1Q_2}{4\pi\varepsilon_0 r^2} = \frac{8.99 \times 10^{9} \times (2.0 \times 10^{-9})^2}{(30 \times 10^{-3})^2}\] [C1]
\[F = 4.0 \times 10^{-5}\,\mathrm{N}\] [A1]
The charges are alike, so the force is repulsive: each sphere is pushed directly away from the other. [B1]
:::

:::eg The force between two point charges is \(F\). Find the new force if the distance between them is trebled and one of the charges is doubled.
\(F \propto Q_1Q_2/r^2\). Doubling one charge multiplies \(F\) by 2. Trebling \(r\) divides \(F\) by \(3^2 = 9\).
The new force is \(\dfrac{2}{9}F\). [A1]
:::

:::warn r is the distance between the centres
For a charged sphere, \(r\) is measured from its **centre**, not from its surface. If a sphere of radius 4.0 cm carries a charge and you want its field at 6.0 cm from the surface, put \(r = 10\,\mathrm{cm}\) into the formula.
:::

### Electric and gravitational forces compared

The law \(F = Q_1Q_2/(4\pi\varepsilon_0r^2)\) has the same shape as \(F = Gm_1m_2/r^2\). Both fall with the square of the distance, and both are proportional to the product of the "charges" (masses in gravity). The big differences are that charge comes in two signs, so the electric force can **repel**, and that the electric force is far stronger.

:::eg Compare the electric force with the gravitational force between two protons. Use \(m_p = 1.67 \times 10^{-27}\,\mathrm{kg}\) and \(e = 1.60 \times 10^{-19}\,\mathrm{C}\).
\[\frac{F_\text{electric}}{F_\text{gravitational}} = \frac{e^2/(4\pi\varepsilon_0r^2)}{Gm_p^2/r^2} = \frac{e^2}{4\pi\varepsilon_0 G m_p^2}\] [C1]
The separation \(r\) cancels, so the ratio is the same at any distance:
\[\frac{8.99 \times 10^{9} \times (1.60 \times 10^{-19})^2}{6.67 \times 10^{-11} \times (1.67 \times 10^{-27})^2} = 1.2 \times 10^{36}\] [A1]
Gravity is utterly negligible between particles. It only matters for astronomical bodies because they are huge and nearly neutral, so their electric forces cancel but their gravitational forces always add up.
:::

## The field of a point charge

Put a small positive test charge \(q\) at distance \(r\) from a point charge \(Q\). The force on it is given by Coulomb's law, and the field strength is the force per unit charge.

:::formula Electric field strength of a point charge
\[E = \frac{Q}{4\pi\varepsilon_0 r^2}\]
\(Q\): the charge producing the field (C) · \(r\): distance from the point charge, or from the centre of a charged sphere (m). The field points **away** from a positive \(Q\) and **towards** a negative \(Q\). It is an inverse-square law: doubling \(r\) divides \(E\) by 4.
:::

:::proof Why E = Q/(4πε₀r²)
The force on a small test charge \(q\) at distance \(r\) from the point charge \(Q\) is \(F = \dfrac{Qq}{4\pi\varepsilon_0 r^2}\) (Coulomb's law).
The field strength is the force per unit charge, \(E = F/q\).
Divide the force by \(q\): the charge \(q\) cancels, leaving \(E = \dfrac{Q}{4\pi\varepsilon_0 r^2}\).
:::

:::eg A small sphere carries a charge of \(+5.0\,\mathrm{nC}\). Find the field strength \(0.10\,\mathrm{m}\) from its centre, with its direction.
\[E = \frac{Q}{4\pi\varepsilon_0 r^2} = \frac{8.99 \times 10^{9} \times 5.0 \times 10^{-9}}{(0.10)^2}\] [C1]
\[E = 4.5 \times 10^{3}\,\mathrm{N\,C^{-1}}\] [A1]
The sphere is positive, so the field points directly away from the centre. [B1]
:::

### Adding the fields of several charges

Each charge makes its own field, and the field at a point is the **vector sum** of the fields due to each charge. Draw each field as an arrow first, and decide the directions by thinking about the force on a positive test charge. Fields along the same line add or subtract; fields at an angle need Pythagoras or components.

:::eg Two point charges, \(+3.0\,\mathrm{nC}\) and \(-3.0\,\mathrm{nC}\), are \(0.20\,\mathrm{m}\) apart. Find the field strength at the midpoint between them.
Each charge is \(0.10\,\mathrm{m}\) from the midpoint, and each field has strength
\[E_1 = E_2 = \frac{8.99 \times 10^{9} \times 3.0 \times 10^{-9}}{(0.10)^2} = 2.7 \times 10^{3}\,\mathrm{N\,C^{-1}}\] [C1]
The positive charge pushes a test charge away from itself, towards the negative charge. The negative charge pulls it towards itself, also towards the negative charge. Both fields point in the **same** direction, so they add. [B1]
\[E = 2 \times 2.70 \times 10^{3} = 5.4 \times 10^{3}\,\mathrm{N\,C^{-1}}\] [A1]
directed from the positive charge towards the negative charge.
:::

:::eg A charge \(+4Q\) and a charge \(+Q\) are \(0.30\,\mathrm{m}\) apart, with \(Q = 2.0\,\mathrm{nC}\). Find the point on the line between them where the field is zero.
Between two positive charges, the fields point in opposite directions, so they can cancel. Let the point be \(x\) from the \(+4Q\) charge. [B1]
The fields are equal in size there: \(\dfrac{4Q}{4\pi\varepsilon_0 x^2} = \dfrac{Q}{4\pi\varepsilon_0 (0.30 - x)^2}\). [M1]
Cancel the common factors and take square roots: \(\dfrac{2}{x} = \dfrac{1}{0.30 - x}\), so \(2(0.30 - x) = x\) and \(x = 0.20\,\mathrm{m}\). [A1]
The point is \(0.20\,\mathrm{m}\) from \(+4Q\) and \(0.10\,\mathrm{m}\) from \(+Q\): the distances are in the ratio \(2 : 1\), the square root of the ratio of the charges. Check: the field of each charge there is \(1.8 \times 10^{3}\,\mathrm{N\,C^{-1}}\), equal and opposite.
:::

## Electric potential

Just as a mass has gravitational potential energy in a gravitational field, a charge has **electric potential energy** in an electric field. Dividing the energy by the charge gives a property of the field alone, the **electric potential**. The zero is chosen at infinity, where the field has faded away.

:::def Electric potential
At a point, the work done per unit positive charge in bringing a small test charge from infinity to that point.
:::

:::formula Electric potential of a point charge
\[V = \frac{Q}{4\pi\varepsilon_0 r}\]
\(V\): electric potential (V, or \(\mathrm{J\,C^{-1}}\)) · \(Q\): the charge producing the field, **with its sign** (C) · \(r\): distance from the point charge or from the centre of a charged sphere (m). The potential is zero at infinity.
:::

Unlike gravitational potential, the sign depends on the source. Near a **positive** charge, a positive test charge is repelled, so you must do work on it to bring it in, and the potential is positive. Near a **negative** charge, the test charge is attracted and the field does the work, so the work done by you is negative and the potential is negative.

:::proof Why V = Q/(4πε₀r)
Bring a small positive charge \(q\) from infinity to distance \(r\) from a point charge \(Q\). At distance \(x\) the electric force on \(q\) is \(Qq/(4\pi\varepsilon_0 x^2)\).
To move \(q\) slowly, you push against this force with an equal force. The work you do is the area under the force–distance graph from \(x = \infty\) to \(x = r\):
\[W = \int_{\infty}^{r} \left(-\frac{Qq}{4\pi\varepsilon_0 x^2}\right)dx = \frac{Qq}{4\pi\varepsilon_0 r}\]
The work done per unit charge is \(V = W/q = \dfrac{Q}{4\pi\varepsilon_0 r}\).
For \(Q > 0\) the result is positive (you pushed against a repulsion), and for \(Q < 0\) it is negative.
:::

:::eg Find the electric potential \(0.10\,\mathrm{m}\) from the centre of a sphere carrying \(+5.0\,\mathrm{nC}\), and the work needed to bring a charge of \(+2.0\,\mathrm{nC}\) from infinity to that point.
\[V = \frac{Q}{4\pi\varepsilon_0 r} = \frac{8.99 \times 10^{9} \times 5.0 \times 10^{-9}}{0.10} = 4.5 \times 10^{2}\,\mathrm{V}\] [C1] [A1]
The work done is the charge times the potential: \(W = qV = 2.0 \times 10^{-9} \times 449.5 = 9.0 \times 10^{-7}\,\mathrm{J}\). [A1]
:::

:::eg A Van de Graaff generator has a spherical dome of radius \(0.15\,\mathrm{m}\) carrying a charge of \(1.0\,\mu\mathrm{C}\). Find the potential of the dome and the field strength at its surface.
The charge on the dome acts as a point charge at its centre, so the surface is at \(r = 0.15\,\mathrm{m}\).
\[V = \frac{8.99 \times 10^{9} \times 1.0 \times 10^{-6}}{0.15} = 6.0 \times 10^{4}\,\mathrm{V}\] [C1] [A1]
\[E = \frac{Q}{4\pi\varepsilon_0 r^2} = \frac{V}{r} = \frac{5.99 \times 10^{4}}{0.15} = 4.0 \times 10^{5}\,\mathrm{V\,m^{-1}}\] [A1]
Sixty kilovolts sounds dangerous, but the charge is tiny, so very little energy is stored.
:::

### Potential is a scalar

The potential at a point near several charges is the **sum** of the potentials due to each charge, with their signs. There are no directions to worry about.

:::eg For the two charges in the midpoint example (\(+3.0\,\mathrm{nC}\) and \(-3.0\,\mathrm{nC}\), \(0.20\,\mathrm{m}\) apart) find the electric potential at the midpoint.
\[V = \frac{1}{4\pi\varepsilon_0}\left(\frac{+3.0 \times 10^{-9}}{0.10} + \frac{-3.0 \times 10^{-9}}{0.10}\right) = 0\] [A1]
The potential is zero at the midpoint, yet the field strength there is \(5.4 \times 10^{3}\,\mathrm{N\,C^{-1}}\). Zero potential does not mean zero field: potential tells you the energy per unit charge, not how steeply it changes.
:::

:::warn Field is a vector, potential is a scalar
Add fields as vectors, with directions. Add potentials as numbers, with signs. Two equal and opposite charges can give zero potential at a point where the field is not zero, as the last example shows. Two equal positive charges give zero field at the midpoint, where the potential is double that of one charge.
:::

### Equipotentials

An **equipotential** joins points of equal potential. Round a point charge the equipotentials are spheres (circles in a diagram). The surface of a conductor in equilibrium is an equipotential.

:::def Equipotential
A surface on which every point has the same potential.
:::

:::html
<figure class="fig small"><svg viewBox="5 5 340 340" role="img" aria-label="Field lines and equipotentials of a positive point charge. Eight straight field lines point away from the charge. Three dashed circles centred on the charge, at 0.10, 0.20 and 0.40 metres, are the equipotentials at 450, 225 and 112 volts. The field lines cross every circle at right angles."><path class="c1" d="M186.1 179.6L330.2 239.3"/><path class="c1" d="M271.1 214.8L282.2 219.4" marker-end="url(#ah-phys)"/><path class="c1" d="M179.6 186.1L239.3 330.2"/><path class="c1" d="M214.8 271.1L219.4 282.2" marker-end="url(#ah-phys)"/><path class="c1" d="M170.4 186.1L110.7 330.2"/><path class="c1" d="M135.2 271.1L130.6 282.2" marker-end="url(#ah-phys)"/><path class="c1" d="M163.9 179.6L19.8 239.3"/><path class="c1" d="M78.9 214.8L67.8 219.4" marker-end="url(#ah-phys)"/><path class="c1" d="M163.9 170.4L19.8 110.7"/><path class="c1" d="M78.9 135.2L67.8 130.6" marker-end="url(#ah-phys)"/><path class="c1" d="M170.4 163.9L110.7 19.8"/><path class="c1" d="M135.2 78.9L130.6 67.8" marker-end="url(#ah-phys)"/><path class="c1" d="M179.6 163.9L239.3 19.8"/><path class="c1" d="M214.8 78.9L219.4 67.8" marker-end="url(#ah-phys)"/><path class="c1" d="M186.1 170.4L330.2 110.7"/><path class="c1" d="M271.1 135.2L282.2 130.6" marker-end="url(#ah-phys)"/><circle class="ln dash" cx="175" cy="175" r="40"/><circle class="ln dash" cx="175" cy="175" r="80"/><circle class="ln dash" cx="175" cy="175" r="160"/><circle class="fp s-ink sw2" cx="175" cy="175" r="9"/><text class="tb tc" x="175" y="179.5">+</text><text class="tl tc halo" x="220" y="179">450 V</text><text class="tl tc halo" x="95" y="179">225 V</text><text class="tl tc halo" x="175" y="339">112 V</text></svg><figcaption>Field lines (solid) and equipotentials (dashed) of a +5.0 nC point charge, at 0.10 m, 0.20 m and 0.40 m from it. The equipotentials are circles round the charge, and they cross every field line at right angles. Each circle here has half the potential of the one inside it, at twice the distance; equipotentials drawn at equal steps of potential get further apart as the field gets weaker.</figcaption></figure>
:::

Equipotentials have two important properties:
- They cross field lines at **right angles**. If the field had a component along the surface, moving a charge along it would involve work, and the potential would not be constant.
- No work is done in moving a charge along an equipotential, since \(\Delta V = 0\).

Where the equipotentials are close together, the potential changes quickly with distance, so the field is strong. In the figure, the equipotentials for equal steps of potential would be closer near the charge. A maps-and-contours picture is helpful: potential is height, equipotentials are contour lines, and the field points downhill.

### Work done between points

The work done on a charge \(q\) in moving it from a point at potential \(V_1\) to a point at potential \(V_2\) is the charge times the change in potential. If the work is done by an outside agent, moving the charge slowly, this is the change in its electric potential energy:

:::formula Work done in moving a charge
\[W = q\,\Delta V = q(V_2 - V_1)\]
\(W\): work done on the charge by the external force (J) · \(q\): the charge, with its sign (C). It is also the increase in the charge's electric potential energy. A negative answer means the field does the work and the charge's kinetic energy increases if it is free to move.
:::

:::eg A charge of \(+2.0\,\mathrm{nC}\) moves from the equipotential at \(450\,\mathrm{V}\) to the equipotential at \(225\,\mathrm{V}\) in the figure above. Find the change in its electric potential energy and say what happens if it is free to move.
\(\Delta V = V_2 - V_1 = 224.8 - 449.5 = -224.8\,\mathrm{V}\) (using the unrounded potentials). [C1]
\(\Delta E_P = q\Delta V = 2.0 \times 10^{-9} \times (-224.8) = -4.5 \times 10^{-7}\,\mathrm{J}\). [A1]
The potential energy falls, so the field does \(4.5 \times 10^{-7}\,\mathrm{J}\) of work on the charge. If it is free to move, the charge speeds up away from the positive source, and its kinetic energy increases by this amount. [B1]
:::

### Field strength as potential gradient

The field and the potential describe the same thing. The field is the **negative of the potential gradient**:

:::formula Field strength and potential gradient
\[E = -\frac{\Delta V}{\Delta x} \qquad\text{or, at a point,}\qquad E = -\frac{dV}{dx}\]
\(E\): field strength in the direction of \(x\) (\(\mathrm{V\,m^{-1}}\)) · \(\Delta V/\Delta x\): the gradient of a graph of \(V\) against distance. The minus sign means the field points in the direction in which the potential **falls**.
:::

For a uniform field, the gradient is the same everywhere, which gives back \(E = V/d\). Between the two plates in the earlier example, the potential falls steadily from \(800\,\mathrm{V}\) at the positive plate to \(0\) at the negative plate.

:::plot Potential between two plates \(2.0\,\mathrm{cm}\) apart with a p.d. of \(800\,\mathrm{V}\). The graph is a straight line, and its gradient is minus the field strength.
--f "800-400*x+0*sqrt(2-x)" --x 0 2.3 --y 0 900 --pt "0.5,600,(0.5 cm, 600 V)@ne" --pt "1.5,200,(1.5 cm, 200 V)@ne" --xlabel "x / cm" --ylabel "V / V" --xstep 0.5
:::

The gradient is \(\dfrac{0 - 800}{2.0 - 0} = -400\,\mathrm{V\,cm^{-1}} = -4.0 \times 10^{4}\,\mathrm{V\,m^{-1}}\), so \(E = 4.0 \times 10^{4}\,\mathrm{V\,m^{-1}}\), pointing along \(+x\), from high to low potential. Convert the centimetres to metres before you quote the field.

For a point charge, \(V = Q/(4\pi\varepsilon_0 r)\), and the gradient is \(dV/dr = -Q/(4\pi\varepsilon_0 r^2)\). Minus this is \(E = Q/(4\pi\varepsilon_0 r^2)\), which agrees with the field of a point charge. For a non-uniform field you find \(E\) at a point by drawing a **tangent** to the \(V\)–\(r\) graph at that point and measuring its gradient. Steeper tangent, stronger field.

### Charged conducting spheres

A conducting sphere carries its charge on its surface. Inside the conductor the field is zero, so no work is done in moving a charge about inside, and the potential is **constant** and equal to its value at the surface. Outside, the sphere acts as a point charge at its centre. For a sphere of radius 10 cm carrying \(5.0\,\mathrm{nC}\):

:::html
<figure class="fig wide"><svg viewBox="0 0 600 250" role="img" aria-label="Two graphs for a conducting sphere of radius 10 centimetres carrying 5.0 nanocoulombs. Left, potential against distance from the centre: constant at 450 volts inside and at the surface, then falling as 1 over r. Right, field strength against distance: zero inside, jumping to 4.5 kilovolts per metre at the surface, then falling as 1 over r squared."><path class="ax" d="M60 34V210H281"/><path class="ax" d="M60 210v4"/><text class="ts tc" x="60" y="226">0</text><path class="ax" d="M113.8 210v4"/><text class="ts tc" x="113.8" y="226">10</text><path class="ax" d="M167.5 210v4"/><text class="ts tc" x="167.5" y="226">20</text><path class="ax" d="M221.2 210v4"/><text class="ts tc" x="221.2" y="226">30</text><path class="ax" d="M275 210v4"/><text class="ts tc" x="275" y="226">40</text><path class="ax" d="M60 210h-4"/><text class="ts te" x="53" y="214">0</text><path class="ax" d="M60 176h-4"/><text class="ts te" x="53" y="180">100</text><path class="ax" d="M60 142h-4"/><text class="ts te" x="53" y="146">200</text><path class="ax" d="M60 108h-4"/><text class="ts te" x="53" y="112">300</text><path class="ax" d="M60 74h-4"/><text class="ts te" x="53" y="78">400</text><path class="ax" d="M60 40h-4"/><text class="ts te" x="53" y="44">500</text><path class="c1 sw2" d="M60 57.1L113.8 57.1L116.4 64.4L119.1 71L121.8 77.1L124.5 82.6L127.2 87.7L129.9 92.4L132.6 96.8L135.2 100.8L137.9 104.6L140.6 108.1L143.3 111.4L146 114.5L148.7 117.4L151.4 120.1L154.1 122.6L156.8 125.1L159.4 127.4L162.1 129.5L164.8 131.6L167.5 133.6L170.2 135.4L172.9 137.2L175.6 138.9L178.2 140.5L180.9 142.1L183.6 143.5L186.3 145L189 146.3L191.7 147.6L194.4 148.9L197.1 150.1L199.8 151.2L202.4 152.3L205.1 153.4L207.8 154.4L210.5 155.4L213.2 156.4L215.9 157.3L218.6 158.2L221.2 159L223.9 159.9L226.6 160.7L229.3 161.5L232 162.2L234.7 163L237.4 163.7L240.1 164.4L242.8 165L245.4 165.7L248.1 166.3L250.8 166.9L253.5 167.5L256.2 168.1L258.9 168.7L261.6 169.2L264.2 169.8L266.9 170.3L269.6 170.8L272.3 171.3L275 171.8"/><path class="ln thin dash" d="M113.8 210V57.1"/><text class="tl" x="65.4" y="49.1">V = 450 V inside</text><text class="tl" x="172.9" y="127.2">V ∝ 1/r</text><text class="tl te" x="281" y="245">r / cm</text><text class="tl" x="22" y="28">V / V</text><path class="ax" d="M370 34V210H591"/><path class="ax" d="M370 210v4"/><text class="ts tc" x="370" y="226">0</text><path class="ax" d="M423.8 210v4"/><text class="ts tc" x="423.8" y="226">10</text><path class="ax" d="M477.5 210v4"/><text class="ts tc" x="477.5" y="226">20</text><path class="ax" d="M531.2 210v4"/><text class="ts tc" x="531.2" y="226">30</text><path class="ax" d="M585 210v4"/><text class="ts tc" x="585" y="226">40</text><path class="ax" d="M370 210h-4"/><text class="ts te" x="363" y="214">0</text><path class="ax" d="M370 176h-4"/><text class="ts te" x="363" y="180">1</text><path class="ax" d="M370 142h-4"/><text class="ts te" x="363" y="146">2</text><path class="ax" d="M370 108h-4"/><text class="ts te" x="363" y="112">3</text><path class="ax" d="M370 74h-4"/><text class="ts te" x="363" y="78">4</text><path class="ax" d="M370 40h-4"/><text class="ts te" x="363" y="44">5</text><path class="c1 sw3" d="M370 210H423.8"/><path class="c1 sw2" d="M423.8 57.1L426.4 71.4L429.1 83.7L431.8 94.4L434.5 103.8L437.2 112.2L439.9 119.5L442.6 126.1L445.2 132L447.9 137.3L450.6 142.1L453.3 146.4L456 150.3L458.7 153.9L461.4 157.1L464.1 160.1L466.8 162.8L469.4 165.3L472.1 167.7L474.8 169.8L477.5 171.8L480.2 173.6L482.9 175.3L485.6 176.9L488.2 178.4L490.9 179.8L493.6 181.1L496.3 182.3L499 183.5L501.7 184.5L504.4 185.5L507.1 186.5L509.8 187.4L512.4 188.2L515.1 189L517.8 189.8L520.5 190.5L523.2 191.2L525.9 191.8L528.6 192.4L531.2 193L533.9 193.6L536.6 194.1L539.3 194.6L542 195.1L544.7 195.5L547.4 196L550.1 196.4L552.8 196.8L555.4 197.2L558.1 197.5L560.8 197.9L563.5 198.2L566.2 198.5L568.9 198.8L571.6 199.1L574.2 199.4L576.9 199.7L579.6 199.9L582.3 200.2L585 200.4"/><path class="ln thin dash" d="M423.8 210V57.1"/><text class="tl" x="375.4" y="200">E = 0</text><text class="tl" x="445.2" y="118">E ∝ 1/r²</text><text class="tl te" x="591" y="245">r / cm</text><text class="tl" x="332" y="28">E / kV m⁻¹</text></svg><figcaption>Potential V (left) and field strength E (right) against distance r from the centre of a conducting sphere of radius 10 cm carrying 5.0 nC. Inside, V is constant and E is zero. Outside, V falls as 1/r and E falls as 1/r². At every point E is minus the gradient of the V graph.</figcaption></figure>
:::

The potential is a flat \(450\,\mathrm{V}\) up to the surface and then falls as \(1/r\). The field is zero inside, jumps to \(4.5\,\mathrm{kV\,m^{-1}}\) at the surface and then falls as \(1/r^2\). The field is the negative of the gradient of the potential graph: flat potential inside means zero field; steepest gradient at the surface means the largest field.

:::eg The potential at distance \(r\) from the centre of the sphere above (\(r\) in cm) is \(V = 4495/r\) volts for \(r \geq 10\). Use the gradient to find the field strength at \(r = 20\,\mathrm{cm}\), and check with the formula for a point charge.
The gradient of \(V = 4495\,r^{-1}\) is \(dV/dr = -4495/r^2\). At \(r = 20\) this is \(-11.24\,\mathrm{V\,cm^{-1}}\) or \(-1124\,\mathrm{V\,m^{-1}}\). [C1]
\(E = -\dfrac{dV}{dr} = 1.1 \times 10^{3}\,\mathrm{V\,m^{-1}}\), directed away from the sphere. [A1]
Check: \(E = \dfrac{8.99 \times 10^{9} \times 5.0 \times 10^{-9}}{(0.20)^2} = 1.1 \times 10^{3}\,\mathrm{N\,C^{-1}}\). [B1]
On an exam graph without an equation you would draw the tangent at \(r = 20\,\mathrm{cm}\) and measure its gradient between two points far apart on the tangent, as you did for the gradient of a straight line.
:::

## Electric potential energy

The potential energy of a charge \(q\) at a point where the potential is \(V\) is \(qV\). For a charge \(q\) at distance \(r\) from a point charge \(Q\), this gives the energy of the pair.

:::formula Electric potential energy of two point charges
\[E_P = qV = \frac{Qq}{4\pi\varepsilon_0 r}\]
\(E_P\): electric potential energy of the pair (J) · \(Q\), \(q\): the two charges, **with signs** · \(r\): their separation (m). Zero at infinite separation. Positive for like charges (they repel, so work was done to bring them together). Negative for unlike charges (they attract).
:::

Plotted against separation, \(E_P\) is a curve like \(1/r\), above the axis for like charges and below it for unlike charges. Two protons, or a proton and an electron, \(1.0 \times 10^{-10}\,\mathrm{m}\) apart (about the size of an atom) have potential energies of \(+2.3 \times 10^{-18}\,\mathrm{J}\) and \(-2.3 \times 10^{-18}\,\mathrm{J}\).

:::plot Electric potential energy against separation for two like charges (a pair of protons) and two unlike charges (a proton and an electron). The gradient is minus the force.
--f "2.30/x+0*sqrt(2.6-x)" --f "-2.30/x+0*sqrt(2.6-x)" --x 0.4 3 --y -6 6 --label "like charges" --label "unlike charges" --xlabel "r / 10⁻¹⁰ m" --ylabel "Eₚ / 10⁻¹⁸ J" --legend tr
:::

The gradient of this graph is minus the force on the charges: \(F = -dE_P/dr\). For like charges the gradient is negative, so the force is positive, meaning repulsion; for unlike charges the gradient is positive, so the force is attractive. When a free charge moves in a field, the total of electric potential energy and kinetic energy is constant, as long as no other forces do work. That is how you find the speed at a different point, or how close a charge gets before it is stopped.

:::eg An α-particle (charge \(+2e\)) with kinetic energy \(5.5\,\mathrm{MeV}\) is fired straight at a gold nucleus (charge \(+79e\)), which stays at rest. Find the distance of closest approach. Take \(1\,\mathrm{eV} = 1.60 \times 10^{-19}\,\mathrm{J}\).
The kinetic energy is \(5.5 \times 10^{6} \times 1.60 \times 10^{-19} = 8.8 \times 10^{-13}\,\mathrm{J}\). [C1]
At closest approach the α-particle is momentarily at rest, so all its kinetic energy has become electric potential energy: \(E_K = \dfrac{Qq}{4\pi\varepsilon_0 r}\). [B1]
\[r = \frac{Qq}{4\pi\varepsilon_0 E_K} = \frac{8.99 \times 10^{9} \times (79 \times 1.60 \times 10^{-19}) \times (2 \times 1.60 \times 10^{-19})}{8.8 \times 10^{-13}}\] [C1]
\[r = 4.1 \times 10^{-14}\,\mathrm{m}\] [A1]
The α-particle was stopped by the repulsion at \(4.1 \times 10^{-14}\,\mathrm{m}\) from the centre of the nucleus, so the nucleus must be smaller than this. This is how scattering experiments, described in [Particle physics](#phys.particles), set an upper limit for the size of a nucleus.
:::

:::eg In a model of the hydrogen atom, an electron orbits a proton at a radius of \(5.3 \times 10^{-11}\,\mathrm{m}\). Find the electric potential energy of the pair, the kinetic energy of the electron, and the total energy, in electronvolts.
\[E_P = \frac{(+e)(-e)}{4\pi\varepsilon_0 r} = -\frac{8.99 \times 10^{9} \times (1.60 \times 10^{-19})^2}{5.3 \times 10^{-11}} = -4.3 \times 10^{-18}\,\mathrm{J} = -27\,\mathrm{eV}\] [C1] [A1]
The Coulomb force provides the centripetal force (from [Motion in a circle](#phys.circular)): \(\dfrac{e^2}{4\pi\varepsilon_0 r^2} = \dfrac{mv^2}{r}\), so \(mv^2 = \dfrac{e^2}{4\pi\varepsilon_0 r}\) and
\[E_K = \tfrac12 mv^2 = \frac{e^2}{8\pi\varepsilon_0 r} = +2.2 \times 10^{-18}\,\mathrm{J} = +13.6\,\mathrm{eV}\] [M1] [A1]
The total energy is \(-27.14 + 13.57 = -13.57 \approx -13.6\,\mathrm{eV}\) (add the unrounded values: the rounded ones would give \(-13.5\)): it is negative because the electron is bound, and \(13.6\,\mathrm{eV}\) is the energy needed to ionise the atom. [A1]
:::

## Electric and gravitational fields

You have now met two fields that obey inverse-square laws. Everything that you learned for one transfers to the other, with the substitutions \(m \to Q\) and \(G \to -1/(4\pi\varepsilon_0)\) (the minus sign because masses always attract, and like charges repel).

| | Gravitational field | Electric field |
|---|---|---|
| Source | mass \(M\) | charge \(Q\) (positive or negative) |
| Force law | \(F = \dfrac{GMm}{r^2}\) | \(F = \dfrac{Qq}{4\pi\varepsilon_0 r^2}\) |
| Field strength | \(g = F/m = \dfrac{GM}{r^2}\) | \(E = F/q = \dfrac{Q}{4\pi\varepsilon_0 r^2}\) |
| Unit of field | \(\mathrm{N\,kg^{-1}}\) | \(\mathrm{N\,C^{-1}}\) or \(\mathrm{V\,m^{-1}}\) |
| Direction | always towards the mass | away from + and towards −, so it can point either way |
| Potential | \(\phi = -\dfrac{GM}{r}\) (always negative) | \(V = \dfrac{Q}{4\pi\varepsilon_0 r}\) (sign of \(Q\)) |
| Potential energy | \(-\dfrac{GMm}{r}\) | \(\dfrac{Qq}{4\pi\varepsilon_0 r}\) |
| Field from potential | \(g = -d\phi/dr\) | \(E = -dV/dr\) |
| Force | always attractive | attractive or repulsive |
| Strength between two protons | negligible | about \(10^{36}\) times larger |

Gravitational fields cannot be screened, because there is no negative mass to cancel them. Electric fields can be, which is why a metal box shields its contents from an external electric field.

:::board
AQA and OCR use the same Coulomb law and the same definition of electric potential as Cambridge. Many textbooks shorten \(1/(4\pi\varepsilon_0)\) to \(k\) and write \(F = kQ_1Q_2/r^2\); on a Cambridge paper write \(1/(4\pi\varepsilon_0)\) or use its value \(8.99 \times 10^{9}\,\mathrm{m\,F^{-1}}\), because \(k\) is the Boltzmann constant on the data sheet.
:::

:::eg Spot the error: find the electric field strength at the midpoint between a charge of \(+5.0\,\mathrm{nC}\) and a charge of \(-5.0\,\mathrm{nC}\), which are \(0.40\,\mathrm{m}\) apart.
A student wrote this answer.

Line 1: \(E_1 = E_2 = \dfrac{8.99 \times 10^{9} \times 5.0 \times 10^{-9}}{0.20^2} = 1.1 \times 10^{3}\,\mathrm{N\,C^{-1}}\)
Line 2: the charges are equal and opposite, so the fields cancel
Line 3: \(E = 0\)

Line 1 is correct. [C1] **Lines 2 and 3 are wrong. At the midpoint, the positive charge pushes a test charge away from it and the negative charge pulls the test charge towards it, so the two fields point the same way and add. It is the potentials that cancel, not the fields.** [A0]

Correct working: \(E = 2 \times 1.12 \times 10^{3} = 2.2 \times 10^{3}\,\mathrm{N\,C^{-1}}\), directed towards the negative charge. [A1]

Check: the field of one charge alone is already \(1.1 \times 10^{3}\,\mathrm{N\,C^{-1}}\), and the second charge cannot make the field smaller when it pushes the same way.
:::

:::try Start easy, finish at exam standard
Q: An electron is in a uniform field of strength \(2.0 \times 10^{4}\,\mathrm{N\,C^{-1}}\). Find the force on it and state its direction relative to the field.
A: \(F = eE = 1.60 \times 10^{-19} \times 2.0 \times 10^{4} = 3.2 \times 10^{-15}\,\mathrm{N}\), in the direction **opposite** to the field, because the electron is negative.
Q: A p.d. of \(1.5\,\mathrm{kV}\) is applied across two parallel plates \(3.0\,\mathrm{cm}\) apart. Find the field strength between them.
A: \(E = V/d = 1500/(3.0 \times 10^{-2}) = 5.0 \times 10^{4}\,\mathrm{V\,m^{-1}}\).
Q: A proton is in a uniform field of strength \(1.2 \times 10^{5}\,\mathrm{N\,C^{-1}}\). Find its acceleration.
A: \(a = \dfrac{eE}{m_p} = \dfrac{1.60 \times 10^{-19} \times 1.2 \times 10^{5}}{1.67 \times 10^{-27}} = 1.1 \times 10^{13}\,\mathrm{m\,s^{-2}}\).
Q: Two point charges of \(+3.0\,\mu\mathrm{C}\) and \(+5.0\,\mu\mathrm{C}\) are \(0.50\,\mathrm{m}\) apart. Find the force between them.
A: \[F = \dfrac{8.99 \times 10^{9} \times 3.0 \times 10^{-6} \times 5.0 \times 10^{-6}}{0.50^2} = 0.54\,\mathrm{N}\] The force is repulsive.
Q: Find the field strength and the potential at \(0.30\,\mathrm{m}\) from a point charge of \(-2.0\,\mathrm{nC}\).
A: \(E = \dfrac{8.99 \times 10^{9} \times 2.0 \times 10^{-9}}{0.30^2} = 2.0 \times 10^{2}\,\mathrm{N\,C^{-1}}\), directed towards the charge. \(V = \dfrac{8.99 \times 10^{9} \times (-2.0 \times 10^{-9})}{0.30} = -60\,\mathrm{V}\).
Q: A proton is released from rest and accelerated through a p.d. of \(1.0\,\mathrm{kV}\). Find its final speed.
A: \(\tfrac12 mv^2 = eV\), so \(v = \sqrt{\dfrac{2 \times 1.60 \times 10^{-19} \times 1.0 \times 10^{3}}{1.67 \times 10^{-27}}} = 4.4 \times 10^{5}\,\mathrm{m\,s^{-1}}\).
Q: Find the electric potential energy of a charge of \(+2.0\,\mathrm{nC}\) and a charge of \(-3.0\,\mathrm{nC}\) that are \(5.0\,\mathrm{cm}\) apart.
A: \[E_P = \dfrac{8.99 \times 10^{9} \times (2.0 \times 10^{-9}) \times (-3.0 \times 10^{-9})}{5.0 \times 10^{-2}} = -1.1 \times 10^{-6}\,\mathrm{J}\] It is negative because the charges attract.
Q: A proton of kinetic energy \(8.0 \times 10^{-17}\,\mathrm{J}\) moves directly against a uniform field of strength \(2.0 \times 10^{4}\,\mathrm{V\,m^{-1}}\). How far does it travel before it stops?
A: The force is \(eE = 1.60 \times 10^{-19} \times 2.0 \times 10^{4} = 3.2 \times 10^{-15}\,\mathrm{N}\), opposing the motion. The work done by the force equals the kinetic energy lost, \(Fd = 8.0 \times 10^{-17}\), so \(d = \dfrac{8.0 \times 10^{-17}}{3.2 \times 10^{-15}} = 0.025\,\mathrm{m}\), that is 2.5 cm.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] (#phys.gravity) ★ (a) Define electric field strength at a point. (b) State Coulomb's law.
A: (a) The force per unit positive charge [B1] acting on a small stationary test charge at that point. (b) The force between two point charges is proportional to the product of the charges [B1] and inversely proportional to the square of their separation. [B1]
Q: [3 marks] ★★ Sketch the electric field pattern for two equal positive point charges, a short distance apart.
A: Lines leave each charge radially outwards, with arrows pointing away from the charges. [B1] The lines from the two charges do not cross; they bend away from each other and the pattern is symmetrical about the line midway between the charges. [B1] There is a point midway between the charges where no line passes, and the field is zero. [B1]
Q: [4 marks] ★★ Two horizontal metal plates are \(12\,\mathrm{mm}\) apart, with a p.d. of \(450\,\mathrm{V}\) across them. A charged oil drop of mass \(2.4 \times 10^{-15}\,\mathrm{kg}\) is held stationary between the plates. (a) Calculate the electric field strength between the plates. (b) Calculate the charge on the drop.
A: (a) \(E = V/d = 450/(12 \times 10^{-3})\) [C1] \(= 3.8 \times 10^{4}\,\mathrm{V\,m^{-1}}\). [A1] (b) The drop is stationary, so \(qE = mg\), giving \(q = \dfrac{2.4 \times 10^{-15} \times 9.81}{3.75 \times 10^{4}}\) [C1] \(= 6.3 \times 10^{-19}\,\mathrm{C}\). [A1]
Q: [4 marks] ★★ A point P is \(0.20\,\mathrm{m}\) from a point charge of \(+4.0\,\mathrm{nC}\) and \(0.30\,\mathrm{m}\) from a point charge of \(-2.0\,\mathrm{nC}\). Calculate the electric potential at P, and the work needed to bring a charge of \(+0.50\,\mathrm{nC}\) from infinity to P.
A: \[V = \dfrac{8.99 \times 10^{9} \times 4.0 \times 10^{-9}}{0.20} + \dfrac{8.99 \times 10^{9} \times (-2.0 \times 10^{-9})}{0.30}\] [C1] \(V = 180 - 60 = 1.2 \times 10^{2}\,\mathrm{V}\). [A1] The work is \(W = qV = 0.50 \times 10^{-9} \times 119.9\) [C1] \(= 6.0 \times 10^{-8}\,\mathrm{J}\). [A1]
Q: [2 marks] ★★ Explain why the electric potential at a point near a negative charge is negative.
A: The potential is defined as the work done per unit positive charge in bringing a small test charge from infinity to the point. [B1] A negative charge attracts a positive test charge, so the field does the work as the test charge moves in, and the work done by the external agent is negative. [B1]
Q: [3 marks] ★★ The graph of electric potential \(V\) against distance \(r\) from a small charged sphere passes through \((0.10\,\mathrm{m}, 180\,\mathrm{V})\). A tangent drawn to the graph at this point passes through \((0.20\,\mathrm{m}, 0\,\mathrm{V})\). Find the electric field strength at \(r = 0.10\,\mathrm{m}\) and state its direction.
A: The gradient of the tangent is \(\dfrac{0 - 180}{0.20 - 0.10}\) [C1] \(= -1.8 \times 10^{3}\,\mathrm{V\,m^{-1}}\). [A1] \(E = -\) gradient \(= 1.8 \times 10^{3}\,\mathrm{V\,m^{-1}}\), directed away from the sphere, in the direction in which the potential falls. [B1]
Q: [7 marks] (#phys.kinematics) ★★★ Electrons travelling at \(2.5 \times 10^{7}\,\mathrm{m\,s^{-1}}\) enter midway between two horizontal parallel plates, which are \(2.0\,\mathrm{cm}\) apart and \(4.0\,\mathrm{cm}\) long. The p.d. between the plates is \(400\,\mathrm{V}\). (a) Calculate the acceleration of an electron between the plates. (b) Calculate the vertical deflection of an electron as it leaves the plates. (c) Calculate the angle between the electron's direction of motion as it leaves the plates and its original direction.
H: The path across the field is a parabola, like a projectile.
H: Find the time spent between the plates from the horizontal speed, then use \(y = \tfrac12 at^2\).
H: The angle comes from \(\tan\theta = v_y/v_x\).
A: (a) \(E = V/d = 400/(2.0 \times 10^{-2}) = 2.0 \times 10^{4}\,\mathrm{V\,m^{-1}}\), so \(a = \dfrac{eE}{m}\) [C1] \(= \dfrac{1.60 \times 10^{-19} \times 2.0 \times 10^{4}}{9.11 \times 10^{-31}} = 3.5 \times 10^{15}\,\mathrm{m\,s^{-2}}\). [A1] (b) The time between the plates is \(t = \dfrac{L}{v} = \dfrac{4.0 \times 10^{-2}}{2.5 \times 10^{7}} = 1.6 \times 10^{-9}\,\mathrm{s}\). [C1] \(y = \tfrac12 at^2 = \tfrac12 \times 3.51 \times 10^{15} \times (1.6 \times 10^{-9})^2\) [C1] \(= 4.5 \times 10^{-3}\,\mathrm{m}\). [A1] (c) \(v_y = at = 5.62 \times 10^{6}\,\mathrm{m\,s^{-1}}\), so \(\tan\theta = \dfrac{5.62 \times 10^{6}}{2.5 \times 10^{7}}\) [C1] and \(\theta = 13^\circ\). [A1]
Q: [5 marks] (#phys.particles) ★★★ An α-particle (charge \(+2e\)) of kinetic energy \(4.8\,\mathrm{MeV}\) is fired directly at a stationary silver nucleus (charge \(+47e\)). (a) Calculate the distance of closest approach. (b) State what this suggests about the radius of the silver nucleus.
H: Convert the energy to joules using \(1\,\mathrm{eV} = 1.60 \times 10^{-19}\,\mathrm{J}\).
H: At closest approach the α-particle is momentarily at rest.
A: (a) The kinetic energy is \(4.8 \times 10^{6} \times 1.60 \times 10^{-19} = 7.7 \times 10^{-13}\,\mathrm{J}\). [C1] At closest approach all of this has become electric potential energy. [B1] \[r = \dfrac{Qq}{4\pi\varepsilon_0 E_K} = \dfrac{8.99 \times 10^{9} \times (47 \times 1.60 \times 10^{-19}) \times (2 \times 1.60 \times 10^{-19})}{7.68 \times 10^{-13}}\] [C1] \(r = 2.8 \times 10^{-14}\,\mathrm{m}\). [A1] (b) The α-particle did not reach the nucleus, so the nuclear radius is less than \(2.8 \times 10^{-14}\,\mathrm{m}\). [B1]
:::

:::try Stretch for A*
Q: [8 marks] ★★★ Point P is at the origin. A point charge of \(+2.0\,\mathrm{nC}\) is on the \(x\)-axis at \(x = 0.30\,\mathrm{m}\), and a second point charge of \(+2.0\,\mathrm{nC}\) is on the \(y\)-axis at \(y = 0.40\,\mathrm{m}\). (a) Calculate the magnitude of the resultant electric field at P and its direction relative to the \(x\)-axis. (b) Calculate the electric potential at P. (c) Calculate the work needed to bring a charge of \(+1.0\,\mathrm{nC}\) from infinity to P.
H: Find the field due to each charge separately. The two fields are at right angles to each other.
H: Potential is a scalar: add the two values.
A: (a) The field due to the charge on the \(x\)-axis is \(E_x = \dfrac{8.99 \times 10^{9} \times 2.0 \times 10^{-9}}{0.30^2} = 2.0 \times 10^{2}\,\mathrm{N\,C^{-1}}\), pointing in the \(-x\) direction (away from the charge). [C1] The field due to the other is \(E_y = \dfrac{8.99 \times 10^{9} \times 2.0 \times 10^{-9}}{0.40^2} = 1.1 \times 10^{2}\,\mathrm{N\,C^{-1}}\), in the \(-y\) direction. [A1] The two fields are at right angles, so \(E = \sqrt{E_x^2 + E_y^2}\) [C1] \(= 2.3 \times 10^{2}\,\mathrm{N\,C^{-1}}\). [A1] The angle with the \(-x\) direction is \(\tan^{-1}(112/200) = 29^\circ\), towards the \(-y\) direction. [A1] (b) \(V = 8.99 \times 10^{9} \times 2.0 \times 10^{-9}\left(\dfrac{1}{0.30} + \dfrac{1}{0.40}\right)\) [C1] \(= 1.0 \times 10^{2}\,\mathrm{V}\). [A1] (c) \(W = qV = 1.0 \times 10^{-9} \times 104.9 = 1.0 \times 10^{-7}\,\mathrm{J}\). [A1]
Q: [6 marks] ★★★ A proton enters a region of uniform electric field of strength \(2.0 \times 10^{4}\,\mathrm{V\,m^{-1}}\), directed vertically downwards. Its speed is \(4.0 \times 10^{5}\,\mathrm{m\,s^{-1}}\) at \(30^\circ\) above the horizontal. (a) Find the acceleration of the proton. (b) Find the maximum height above its entry point. (c) Find the horizontal distance from the entry point at which it returns to the entry height.
H: Treat it as a projectile: the field replaces gravity. Resolve the velocity into horizontal and vertical components.
H: At the highest point the vertical velocity is zero.
A: (a) \(a = \dfrac{eE}{m_p} = \dfrac{1.60 \times 10^{-19} \times 2.0 \times 10^{4}}{1.67 \times 10^{-27}}\) [C1] \(= 1.9 \times 10^{12}\,\mathrm{m\,s^{-2}}\), directed downwards. [A1] (b) The initial vertical speed is \(u_y = 4.0 \times 10^{5} \sin 30^\circ = 2.0 \times 10^{5}\,\mathrm{m\,s^{-1}}\). At the top, \(0 = u_y^2 - 2ah\), so \(h = \dfrac{u_y^2}{2a}\) [C1] \(= 1.0 \times 10^{-2}\,\mathrm{m}\). [A1] (c) The time to return is \(t = 2u_y/a = 2.1 \times 10^{-7}\,\mathrm{s}\), and the horizontal speed is \(4.0 \times 10^{5}\cos 30^\circ = 3.46 \times 10^{5}\,\mathrm{m\,s^{-1}}\), so the distance is \(3.46 \times 10^{5} \times 2.09 \times 10^{-7}\) [C1] \(= 7.2 \times 10^{-2}\,\mathrm{m}\). [A1]
:::

:::quiz
? Which unit is equivalent to the newton per coulomb?
+ Volt per metre
- Joule per coulomb
- Newton metre
- Coulomb per volt
> A volt per metre is a joule per coulomb per metre, which is a newton metre per coulomb per metre, which is a newton per coulomb. The joule per coulomb is the volt, a unit of potential, not field strength.
? A uniform electric field points east. In which direction is the force on an electron?
+ West
- East
- Upwards
- There is no force, because the electron is so light
> A negative charge feels a force opposite to the field. The force is small in newtons, but the electron's mass is so small that the acceleration is large.
? The force between two small charged spheres is \(F\). One charge is doubled and the distance between them is doubled. What is the new force?
+ \(F/2\)
- \(F/4\)
- \(2F\)
- \(F\)
> Doubling one charge doubles the force. Doubling the distance divides it by 4. The two changes together give \(2/4 = \tfrac12\), so the force is \(F/2\).
? At the midpoint between a charge \(+Q\) and a charge \(-Q\), which statement is correct?
+ The potential is zero and the field strength is not zero.
- The potential is not zero and the field strength is zero.
- The potential and the field strength are both zero.
- The potential and the field strength are both not zero.
> Potential is a scalar: the two contributions are equal and opposite, so they cancel. The field is a vector: both point towards \(-Q\), so they add.
? The p.d. across two parallel plates stays the same while the distance between them is halved. What happens to the field strength between them?
+ It doubles.
- It halves.
- It stays the same.
- It quadruples.
> For a uniform field \(E = V/d\). Halving \(d\) at constant \(V\) doubles \(E\). Quadrupling would be for an inverse-square law, but this is not one.
? How much work is done in moving a charge along an equipotential?
+ None, because the potential difference is zero.
- A positive amount, equal to the charge times the potential.
- A negative amount, because the field points the opposite way.
- It depends on the length of the path.
> Work is \(q\Delta V\), and \(\Delta V = 0\) along an equipotential. The path does not matter: only the p.d. between the end points does.
? What does the gradient of a graph of potential \(V\) against distance \(r\) give?
+ Minus the electric field strength
- The electric field strength
- The electric potential energy
- The charge on the source
> The field is the negative of the potential gradient, \(E = -dV/dr\). Without the minus sign you would get the wrong direction for the field.
? Two protons are pushed closer together. What happens to their electric potential energy?
+ It increases.
- It decreases.
- It stays the same, because the charges are the same.
- It becomes negative.
> Like charges repel, so work must be done to push them together, and the potential energy \(Qq/(4\pi\varepsilon_0 r)\) increases as \(r\) falls. It is positive for like charges.
:::

:::checklist What you can now do
- [ ] I can define electric field strength, use \(F = qE\) and describe a field with field lines, including the pattern for one or two point charges and between parallel plates.
- [ ] I can use \(E = V/d\) for the uniform field between parallel plates.
- [ ] I can describe and calculate the motion of a charged particle along a uniform field (using \(qV = \tfrac12 mv^2\)) and across it (a parabola).
- [ ] I can state Coulomb's law and use it, knowing that a charged sphere acts as a point charge at its centre.
- [ ] I can use \(E = Q/(4\pi\varepsilon_0 r^2)\) and add the fields of several charges as vectors.
- [ ] I can define electric potential and use \(V = Q/(4\pi\varepsilon_0 r)\), adding potentials as scalars.
- [ ] I can use the fact that the field is the negative of the potential gradient, including from a tangent to a \(V\)–\(r\) graph.
- [ ] I can sketch and explain the graphs of \(E\) and \(V\) against \(r\) for a charged sphere, and describe equipotentials.
- [ ] I can use \(E_P = Qq/(4\pi\varepsilon_0 r)\) and energy conservation, for example to find a distance of closest approach.
- [ ] I can compare electric and gravitational fields.
:::

:::recap
- Electric field strength: force per unit positive charge, \(E = F/q\), in \(\mathrm{N\,C^{-1}} = \mathrm{V\,m^{-1}}\). A positive charge feels a force along the field, a negative one opposite to it.
- Field lines run from positive to negative charges, never cross, and are closer where the field is stronger. Parallel plates give a uniform field \(E = V/d\), except near the edges.
- Along a uniform field a charge gains \(qV = \tfrac12 mv^2\). Across it the path is a parabola: constant velocity along the plates, constant acceleration \(qE/m\) across them.
- Coulomb's law: \(F = Q_1Q_2/(4\pi\varepsilon_0 r^2)\). A charged sphere acts as a point charge at its centre. Field of a point charge: \(E = Q/(4\pi\varepsilon_0 r^2)\), added as vectors.
- Electric potential: the work done per unit positive charge in bringing a test charge from infinity. \(V = Q/(4\pi\varepsilon_0 r)\), a scalar, added with signs. Equipotentials cross field lines at right angles.
- \(E = -dV/dr\): the field is minus the potential gradient. For a conducting sphere, \(V\) is constant and \(E = 0\) inside.
- Electric potential energy of two point charges: \(E_P = Qq/(4\pi\varepsilon_0 r)\), positive for like charges. Work done on a charge: \(W = q\Delta V\).
- Compared with gravity: both are inverse-square laws, but electric forces can repel, and are about \(10^{36}\) times larger between protons.
:::

:::links
- explore: [Charges and Fields](https://phet.colorado.edu/en/simulations/charges-and-fields) · PhET · place charges, see the field and the equipotentials
- explore: [Coulomb's Law](https://phet.colorado.edu/en/simulations/coulombs-law) · PhET · see how the force changes with the charges and their separation
- papers: [9702 Paper 4 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-physics/cie-paper-4/) · Physics & Maths Tutor · find the electric fields questions in real papers [unofficial]

Links checked 13 October 2026.
:::
Next: [Capacitance](#phys.capacitance)
