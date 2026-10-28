@chapter bio.oxygen
@title Transport of oxygen and carbon dioxide
@level as
@paper CAIE 9700 Papers 1 and 2
@time 4–5 hours
@summary Red blood cells carry oxygen on haemoglobin and help to carry carbon dioxide. You will learn the oxygen dissociation curve and why it is S-shaped, how carbonic anhydrase, haemoglobinic acid, carbaminohaemoglobin and the chloride shift move carbon dioxide, the role of plasma, and how the Bohr shift delivers more oxygen to active tissues.

:::why
A resting adult needs about a quarter of a litre of oxygen every minute, and an athlete needs ten times as much, yet oxygen dissolves very poorly in water. Haemoglobin solves the problem: it picks oxygen up in the lungs and gives it up exactly where it is needed. The same red blood cells carry most of the carbon dioxide made by the tissues back to the lungs. Examiners love the oxygen dissociation curve, because it joins structure (the shape of haemoglobin), graphs (reading and describing a curve) and physiology (what the lungs and the muscles need).
:::

**Before you start**, you should know the structure of haemoglobin from [Proteins](#bio.proteins), enzymes from [Enzymes](#bio.enzymes), diffusion and facilitated diffusion from [Movement into and out of cells](#bio.movement), and the red blood cell from [Blood vessels, blood and tissue fluid](#bio.mammaltransport).

:::try Warm-up
Q: How many polypeptide chains does a molecule of haemoglobin have, and what does each chain carry? (from [Proteins](#bio.proteins))
A: Four chains (two α and two β). Each chain carries one haem group, which contains an iron ion (\(\ce{Fe^2+}\)) that can bind one oxygen molecule.
Q: What does an enzyme do to the activation energy of a reaction, and is the enzyme used up? (from [Enzymes](#bio.enzymes))
A: It lowers the activation energy by providing an alternative route through the enzyme–substrate complex. The enzyme is not used up.
Q: Name the process by which oxygen crosses a capillary wall, and state what makes it happen. (from [Movement into and out of cells](#bio.movement))
A: Diffusion, down a concentration gradient: net movement from a higher to a lower concentration, with no energy needed from the cell.
:::

## Oxygen and haemoglobin

Oxygen is not very soluble in water, and the blood plasma is mostly water. If the blood carried oxygen only in solution, a mammal would need a heart pumping dozens of times as much blood. Instead, each red blood cell is packed with hundreds of millions of molecules of haemoglobin, and haemoglobin carries about 98% of the oxygen in the blood.

Haemoglobin has four polypeptide chains, and each chain has a **haem** group with an iron ion. One oxygen molecule \(\ce{O2}\) binds to each haem group, so one haemoglobin molecule can carry up to four oxygen molecules (eight oxygen atoms). The binding is reversible:

\[\ce{Hb + 4O2 <=> HbO8}\]

Haemoglobin (Hb) is dark red. With oxygen bound it is **oxyhaemoglobin** (\(\ce{HbO8}\)), which is bright red. In the lungs the reaction goes to the right (oxygen is **loaded**, or the haemoglobin **associates** with oxygen). In respiring tissues it goes to the left (oxygen is **unloaded**, or the haemoglobin **dissociates**).

### Partial pressure

Air is a mixture of gases, and each gas contributes to the total pressure in proportion to its share of the molecules. The part contributed by one gas is its partial pressure.

:::def Partial pressure of oxygen (pO₂)
The pressure that oxygen alone would exert in a mixture of gases. It is a measure of the concentration of oxygen, measured in kilopascals (kPa). A gas diffuses from a region of higher partial pressure to a region of lower partial pressure.
:::

Atmospheric pressure is about 101 kPa and air is about 21% oxygen, so the pO₂ of air is about 21 kPa. By the time air has reached the alveoli it has mixed with air already in the lungs, and the alveolar pO₂ is about 13 kPa. In the tissues, the cells use oxygen, so the pO₂ there is much lower: around 4–5 kPa in a resting muscle and lower in an active one. Oxygen therefore moves **down a partial pressure gradient** from the alveolar air into the blood, and from the blood into the tissue fluid and into the cells.

:::def Percentage saturation of haemoglobin
The percentage of the haem groups of the haemoglobin in the blood that are combined with oxygen. A sample of blood with all of its haem groups carrying oxygen is 100% saturated.
:::

:::def Affinity (of haemoglobin for oxygen)
How readily haemoglobin binds oxygen. A high affinity means haemoglobin picks up oxygen easily and holds it at low partial pressures; a low affinity means it releases oxygen easily.
:::

## The oxygen dissociation curve

The **oxygen dissociation curve** shows how the percentage saturation of haemoglobin depends on the partial pressure of oxygen. The curve is found by exposing blood to different partial pressures of oxygen and measuring the saturation. The graph below is a **model curve** that illustrates the shape for adult human haemoglobin; use it to learn the pattern and not as a source of exact values.

:::plot Model oxygen dissociation curve of adult haemoglobin. At the pO₂ of the lungs (about 13 kPa) it is almost fully saturated; in a resting tissue (about 4 kPa) it is about 61% saturated.
--f "100*x**2.7/(3.4**2.7+x**2.7)" --x 0 16 --y 0 135 --hline 100 --xlabel "partial pressure of oxygen / kPa" --ylabel "saturation of haemoglobin / %" --label "adult haemoglobin" --pt "13,97.4,lungs@s" --pt "4,60.8,resting tissue@se" --legend tr --alt "An S-shaped curve. It rises slowly from 0% at 0 kPa, then steeply between about 2 and 6 kPa, and then flattens as it approaches 100% saturation. At 13 kPa, the pressure in the lungs, the saturation is about 97%. At 4 kPa it is about 61%."
:::

### Describing the curve

Three parts, in this order:
1. **At low pO₂ (0 to about 2 kPa)** the curve is shallow: haemoglobin picks up oxygen slowly at first.
2. **In the middle (about 2 to 6 kPa)** the curve is steep: a **small change in pO₂** gives a **large change in saturation**.
3. **At high pO₂ (above about 8 kPa)** the curve flattens and approaches 100%: increasing the pO₂ barely raises the saturation.

A graph of this shape is called **sigmoid** (S-shaped).

### Explaining the S-shape: cooperative binding

The shape comes from the way the four haem groups of one molecule affect each other.

:::html
<figure class="fig small"><svg viewBox="0 0 300 440" role="img" aria-label="Four stages of oxygen loading onto haemoglobin, shown as four subunits each with a haem group. Stage 1: all four haem groups are empty and the first oxygen molecule binds slowly. Stage 2: one oxygen is bound, the subunits have changed shape and the second and third oxygen molecules bind easily. Stage 3: three oxygen molecules are bound and the fourth binds slowly because few sites are left. Stage 4: all four haem groups carry oxygen."><text class="tl tb" x="10" y="16">1  First O₂ binds slowly</text><path class="fm s-acc sw2" d="M61 78L60.8 81L60.2 84L59.2 86.8L57.9 89.5L56.2 92L54.3 94.3L52 96.2L49.5 97.9L46.8 99.2L44 100.2L41 100.8L38 101L35 100.8L32 100.2L29.2 99.2L26.5 97.9L24 96.2L21.7 94.3L19.8 92L18.1 89.5L16.8 86.8L15.8 84L15.2 81L15 78L15.2 75L15.8 72L16.8 69.2L18.1 66.5L19.8 64L21.7 61.7L24 59.8L26.5 58.1L29.2 56.8L32 55.8L35 55.2L38 55L41 55.2L44 55.8L46.8 56.8L49.5 58.1L52 59.8L54.3 61.7L56.2 64L57.9 66.5L59.2 69.2L60.2 72L60.8 75Z"/><text class="tl" x="38" y="82" text-anchor="middle">haem</text><path class="fm s-acc sw2" d="M119 78L118.8 81L118.2 84L117.2 86.8L115.9 89.5L114.2 92L112.3 94.3L110 96.2L107.5 97.9L104.8 99.2L102 100.2L99 100.8L96 101L93 100.8L90 100.2L87.2 99.2L84.5 97.9L82 96.2L79.7 94.3L77.8 92L76.1 89.5L74.8 86.8L73.8 84L73.2 81L73 78L73.2 75L73.8 72L74.8 69.2L76.1 66.5L77.8 64L79.7 61.7L82 59.8L84.5 58.1L87.2 56.8L90 55.8L93 55.2L96 55L99 55.2L102 55.8L104.8 56.8L107.5 58.1L110 59.8L112.3 61.7L114.2 64L115.9 66.5L117.2 69.2L118.2 72L118.8 75Z"/><text class="tl" x="96" y="82" text-anchor="middle">haem</text><path class="fm s-acc sw2" d="M177 78L176.8 81L176.2 84L175.2 86.8L173.9 89.5L172.2 92L170.3 94.3L168 96.2L165.5 97.9L162.8 99.2L160 100.2L157 100.8L154 101L151 100.8L148 100.2L145.2 99.2L142.5 97.9L140 96.2L137.7 94.3L135.8 92L134.1 89.5L132.8 86.8L131.8 84L131.2 81L131 78L131.2 75L131.8 72L132.8 69.2L134.1 66.5L135.8 64L137.7 61.7L140 59.8L142.5 58.1L145.2 56.8L148 55.8L151 55.2L154 55L157 55.2L160 55.8L162.8 56.8L165.5 58.1L168 59.8L170.3 61.7L172.2 64L173.9 66.5L175.2 69.2L176.2 72L176.8 75Z"/><text class="tl" x="154" y="82" text-anchor="middle">haem</text><path class="fm s-acc sw2" d="M235 78L234.8 81L234.2 84L233.2 86.8L231.9 89.5L230.2 92L228.3 94.3L226 96.2L223.5 97.9L220.8 99.2L218 100.2L215 100.8L212 101L209 100.8L206 100.2L203.2 99.2L200.5 97.9L198 96.2L195.7 94.3L193.8 92L192.1 89.5L190.8 86.8L189.8 84L189.2 81L189 78L189.2 75L189.8 72L190.8 69.2L192.1 66.5L193.8 64L195.7 61.7L198 59.8L200.5 58.1L203.2 56.8L206 55.8L209 55.2L212 55L215 55.2L218 55.8L220.8 56.8L223.5 58.1L226 59.8L228.3 61.7L230.2 64L231.9 66.5L233.2 69.2L234.2 72L234.8 75Z"/><text class="tl" x="212" y="82" text-anchor="middle">haem</text><path class="c1 sw2" d="M38 35L38 49" marker-end="url(#ah)"/><text class="tl" x="46" y="47">O₂</text><text class="tl tb" x="10" y="124">2  Shape changes: 2nd, 3rd bind easily</text><path class="f2 s-acc2 sw2" d="M64 186L63.8 189.4L63.1 192.7L62 195.9L60.5 199L58.6 201.8L56.4 204.4L53.8 206.6L51 208.5L47.9 210L44.7 211.1L41.4 211.8L38 212L34.6 211.8L31.3 211.1L28.1 210L25 208.5L22.2 206.6L19.6 204.4L17.4 201.8L15.5 199L14 195.9L12.9 192.7L12.2 189.4L12 186L12.2 182.6L12.9 179.3L14 176.1L15.5 173L17.4 170.2L19.6 167.6L22.2 165.4L25 163.5L28.1 162L31.3 160.9L34.6 160.2L38 160L41.4 160.2L44.7 160.9L47.9 162L51 163.5L53.8 165.4L56.4 167.6L58.6 170.2L60.5 173L62 176.1L63.1 179.3L63.8 182.6Z"/><text class="tl" x="38" y="190" text-anchor="middle">O₂</text><path class="fm s-acc sw2" d="M122 186L121.8 189.4L121.1 192.7L120 195.9L118.5 199L116.6 201.8L114.4 204.4L111.8 206.6L109 208.5L105.9 210L102.7 211.1L99.4 211.8L96 212L92.6 211.8L89.3 211.1L86.1 210L83 208.5L80.2 206.6L77.6 204.4L75.4 201.8L73.5 199L72 195.9L70.9 192.7L70.2 189.4L70 186L70.2 182.6L70.9 179.3L72 176.1L73.5 173L75.4 170.2L77.6 167.6L80.2 165.4L83 163.5L86.1 162L89.3 160.9L92.6 160.2L96 160L99.4 160.2L102.7 160.9L105.9 162L109 163.5L111.8 165.4L114.4 167.6L116.6 170.2L118.5 173L120 176.1L121.1 179.3L121.8 182.6Z"/><text class="tl" x="96" y="190" text-anchor="middle">haem</text><path class="fm s-acc sw2" d="M180 186L179.8 189.4L179.1 192.7L178 195.9L176.5 199L174.6 201.8L172.4 204.4L169.8 206.6L167 208.5L163.9 210L160.7 211.1L157.4 211.8L154 212L150.6 211.8L147.3 211.1L144.1 210L141 208.5L138.2 206.6L135.6 204.4L133.4 201.8L131.5 199L130 195.9L128.9 192.7L128.2 189.4L128 186L128.2 182.6L128.9 179.3L130 176.1L131.5 173L133.4 170.2L135.6 167.6L138.2 165.4L141 163.5L144.1 162L147.3 160.9L150.6 160.2L154 160L157.4 160.2L160.7 160.9L163.9 162L167 163.5L169.8 165.4L172.4 167.6L174.6 170.2L176.5 173L178 176.1L179.1 179.3L179.8 182.6Z"/><text class="tl" x="154" y="190" text-anchor="middle">haem</text><path class="fm s-acc sw2" d="M238 186L237.8 189.4L237.1 192.7L236 195.9L234.5 199L232.6 201.8L230.4 204.4L227.8 206.6L225 208.5L221.9 210L218.7 211.1L215.4 211.8L212 212L208.6 211.8L205.3 211.1L202.1 210L199 208.5L196.2 206.6L193.6 204.4L191.4 201.8L189.5 199L188 195.9L186.9 192.7L186.2 189.4L186 186L186.2 182.6L186.9 179.3L188 176.1L189.5 173L191.4 170.2L193.6 167.6L196.2 165.4L199 163.5L202.1 162L205.3 160.9L208.6 160.2L212 160L215.4 160.2L218.7 160.9L221.9 162L225 163.5L227.8 165.4L230.4 167.6L232.6 170.2L234.5 173L236 176.1L237.1 179.3L237.8 182.6Z"/><text class="tl" x="212" y="190" text-anchor="middle">haem</text><path class="c1 sw2" d="M96 140L96 154" marker-end="url(#ah)"/><text class="tl" x="104" y="152">O₂</text><path class="c1 sw2" d="M154 140L154 154" marker-end="url(#ah)"/><text class="tl" x="162" y="152">O₂</text><text class="tl tb" x="10" y="232">3  Fourth O₂ binds slowly</text><path class="f2 s-acc2 sw2" d="M64 294L63.8 297.4L63.1 300.7L62 303.9L60.5 307L58.6 309.8L56.4 312.4L53.8 314.6L51 316.5L47.9 318L44.7 319.1L41.4 319.8L38 320L34.6 319.8L31.3 319.1L28.1 318L25 316.5L22.2 314.6L19.6 312.4L17.4 309.8L15.5 307L14 303.9L12.9 300.7L12.2 297.4L12 294L12.2 290.6L12.9 287.3L14 284.1L15.5 281L17.4 278.2L19.6 275.6L22.2 273.4L25 271.5L28.1 270L31.3 268.9L34.6 268.2L38 268L41.4 268.2L44.7 268.9L47.9 270L51 271.5L53.8 273.4L56.4 275.6L58.6 278.2L60.5 281L62 284.1L63.1 287.3L63.8 290.6Z"/><text class="tl" x="38" y="298" text-anchor="middle">O₂</text><path class="f2 s-acc2 sw2" d="M122 294L121.8 297.4L121.1 300.7L120 303.9L118.5 307L116.6 309.8L114.4 312.4L111.8 314.6L109 316.5L105.9 318L102.7 319.1L99.4 319.8L96 320L92.6 319.8L89.3 319.1L86.1 318L83 316.5L80.2 314.6L77.6 312.4L75.4 309.8L73.5 307L72 303.9L70.9 300.7L70.2 297.4L70 294L70.2 290.6L70.9 287.3L72 284.1L73.5 281L75.4 278.2L77.6 275.6L80.2 273.4L83 271.5L86.1 270L89.3 268.9L92.6 268.2L96 268L99.4 268.2L102.7 268.9L105.9 270L109 271.5L111.8 273.4L114.4 275.6L116.6 278.2L118.5 281L120 284.1L121.1 287.3L121.8 290.6Z"/><text class="tl" x="96" y="298" text-anchor="middle">O₂</text><path class="f2 s-acc2 sw2" d="M180 294L179.8 297.4L179.1 300.7L178 303.9L176.5 307L174.6 309.8L172.4 312.4L169.8 314.6L167 316.5L163.9 318L160.7 319.1L157.4 319.8L154 320L150.6 319.8L147.3 319.1L144.1 318L141 316.5L138.2 314.6L135.6 312.4L133.4 309.8L131.5 307L130 303.9L128.9 300.7L128.2 297.4L128 294L128.2 290.6L128.9 287.3L130 284.1L131.5 281L133.4 278.2L135.6 275.6L138.2 273.4L141 271.5L144.1 270L147.3 268.9L150.6 268.2L154 268L157.4 268.2L160.7 268.9L163.9 270L167 271.5L169.8 273.4L172.4 275.6L174.6 278.2L176.5 281L178 284.1L179.1 287.3L179.8 290.6Z"/><text class="tl" x="154" y="298" text-anchor="middle">O₂</text><path class="fm s-acc sw2" d="M238 294L237.8 297.4L237.1 300.7L236 303.9L234.5 307L232.6 309.8L230.4 312.4L227.8 314.6L225 316.5L221.9 318L218.7 319.1L215.4 319.8L212 320L208.6 319.8L205.3 319.1L202.1 318L199 316.5L196.2 314.6L193.6 312.4L191.4 309.8L189.5 307L188 303.9L186.9 300.7L186.2 297.4L186 294L186.2 290.6L186.9 287.3L188 284.1L189.5 281L191.4 278.2L193.6 275.6L196.2 273.4L199 271.5L202.1 270L205.3 268.9L208.6 268.2L212 268L215.4 268.2L218.7 268.9L221.9 270L225 271.5L227.8 273.4L230.4 275.6L232.6 278.2L234.5 281L236 284.1L237.1 287.3L237.8 290.6Z"/><text class="tl" x="212" y="298" text-anchor="middle">haem</text><path class="c1 sw2" d="M212 248L212 262" marker-end="url(#ah)"/><text class="tl" x="220" y="260">O₂</text><text class="tl tb" x="10" y="340">4  Fully saturated: 4 O₂ bound</text><path class="f2 s-acc2 sw2" d="M64 402L63.8 405.4L63.1 408.7L62 411.9L60.5 415L58.6 417.8L56.4 420.4L53.8 422.6L51 424.5L47.9 426L44.7 427.1L41.4 427.8L38 428L34.6 427.8L31.3 427.1L28.1 426L25 424.5L22.2 422.6L19.6 420.4L17.4 417.8L15.5 415L14 411.9L12.9 408.7L12.2 405.4L12 402L12.2 398.6L12.9 395.3L14 392.1L15.5 389L17.4 386.2L19.6 383.6L22.2 381.4L25 379.5L28.1 378L31.3 376.9L34.6 376.2L38 376L41.4 376.2L44.7 376.9L47.9 378L51 379.5L53.8 381.4L56.4 383.6L58.6 386.2L60.5 389L62 392.1L63.1 395.3L63.8 398.6Z"/><text class="tl" x="38" y="406" text-anchor="middle">O₂</text><path class="f2 s-acc2 sw2" d="M122 402L121.8 405.4L121.1 408.7L120 411.9L118.5 415L116.6 417.8L114.4 420.4L111.8 422.6L109 424.5L105.9 426L102.7 427.1L99.4 427.8L96 428L92.6 427.8L89.3 427.1L86.1 426L83 424.5L80.2 422.6L77.6 420.4L75.4 417.8L73.5 415L72 411.9L70.9 408.7L70.2 405.4L70 402L70.2 398.6L70.9 395.3L72 392.1L73.5 389L75.4 386.2L77.6 383.6L80.2 381.4L83 379.5L86.1 378L89.3 376.9L92.6 376.2L96 376L99.4 376.2L102.7 376.9L105.9 378L109 379.5L111.8 381.4L114.4 383.6L116.6 386.2L118.5 389L120 392.1L121.1 395.3L121.8 398.6Z"/><text class="tl" x="96" y="406" text-anchor="middle">O₂</text><path class="f2 s-acc2 sw2" d="M180 402L179.8 405.4L179.1 408.7L178 411.9L176.5 415L174.6 417.8L172.4 420.4L169.8 422.6L167 424.5L163.9 426L160.7 427.1L157.4 427.8L154 428L150.6 427.8L147.3 427.1L144.1 426L141 424.5L138.2 422.6L135.6 420.4L133.4 417.8L131.5 415L130 411.9L128.9 408.7L128.2 405.4L128 402L128.2 398.6L128.9 395.3L130 392.1L131.5 389L133.4 386.2L135.6 383.6L138.2 381.4L141 379.5L144.1 378L147.3 376.9L150.6 376.2L154 376L157.4 376.2L160.7 376.9L163.9 378L167 379.5L169.8 381.4L172.4 383.6L174.6 386.2L176.5 389L178 392.1L179.1 395.3L179.8 398.6Z"/><text class="tl" x="154" y="406" text-anchor="middle">O₂</text><path class="f2 s-acc2 sw2" d="M238 402L237.8 405.4L237.1 408.7L236 411.9L234.5 415L232.6 417.8L230.4 420.4L227.8 422.6L225 424.5L221.9 426L218.7 427.1L215.4 427.8L212 428L208.6 427.8L205.3 427.1L202.1 426L199 424.5L196.2 422.6L193.6 420.4L191.4 417.8L189.5 415L188 411.9L186.9 408.7L186.2 405.4L186 402L186.2 398.6L186.9 395.3L188 392.1L189.5 389L191.4 386.2L193.6 383.6L196.2 381.4L199 379.5L202.1 378L205.3 376.9L208.6 376.2L212 376L215.4 376.2L218.7 376.9L221.9 378L225 379.5L227.8 381.4L230.4 383.6L232.6 386.2L234.5 389L236 392.1L237.1 395.3L237.8 398.6Z"/><text class="tl" x="212" y="406" text-anchor="middle">O₂</text></svg><figcaption>Cooperative binding. The first oxygen to bind changes the shape of haemoglobin (the circles widen), so the second and third bind easily; the fourth binds slowly because there is only one vacant haem group to find.</figcaption></figure>
:::

:::steps
1. **The first oxygen molecule binds with difficulty.** The haem groups are tucked into the folded polypeptides, so at low pO₂ an oxygen molecule rarely finds one. This is the shallow start of the curve.
2. **Binding changes the shape.** When the first oxygen molecule binds, the **tertiary and quaternary structure** of the haemoglobin changes slightly, and the other haem groups become easier to reach.
3. **The second and third oxygen molecules bind more easily.** A small rise in pO₂ now fills many more sites. This is **cooperative binding**: each oxygen that binds makes the next one bind more easily. It gives the steep part of the curve.
4. **The fourth binds with difficulty again.** Only one site is left, so there is a low chance that an oxygen molecule collides with it the right way round. The curve flattens as it approaches 100%.
:::

:::def Cooperative binding
The binding of one oxygen molecule to haemoglobin changes the shape of the molecule so that the next oxygen molecules bind more easily.
:::

### Why the curve is S-shaped: what it does for the body

:::key Using the shape of the curve
- **In the lungs** (pO₂ about 13 kPa) the curve is on its flat top: haemoglobin is about **97% saturated**, so it **loads** nearly all the oxygen it can. Even if the pO₂ falls a little, the saturation hardly changes, which gives a safety margin.
- **In respiring tissues** (low pO₂, in a resting muscle about 4 kPa, in a very active one lower) the curve is on its **steep** part: a **small fall in pO₂ releases a large amount of oxygen**. The tissues that use oxygen fastest, and so have the lowest pO₂, get the most.
- The haemoglobin does not give up all of its oxygen: in a resting muscle it is still about 61% saturated when it leaves, which is a reserve for exercise.
:::

:::exam Describe, then explain, a curve
"Describe" the curve: quote the saturation at named values of pO₂ with units ("at 13 kPa the saturation is about 97%, and at 4 kPa it is 61%") and say that it rises steeply between about 2 and 6 kPa. "Explain" it: use cooperative binding, the change of shape and the fourth molecule. Never write that haemoglobin "wants" or "needs" oxygen.
:::

:::eg Blood is 100% saturated when each 100 cm³ of it carries 20 cm³ of oxygen. Haemoglobin in the blood leaving the lungs at a pO₂ of 13 kPa is 97% saturated. In a respiring tissue where the pO₂ is 5 kPa, the saturation is 74%. Calculate the volume of oxygen unloaded from each 100 cm³ of blood.
**Step 1: percentage points unloaded.** The saturation falls from 97% to 74%.

\[\begin{aligned} \text{unloaded} &= 97 - 74 \\ &= 23\ \text{percentage points} \end{aligned}\] [M1] [A1]

**Step 2: volume.** That is 23% of the oxygen capacity of 20 cm³ per 100 cm³.

\[\begin{aligned} \text{volume} &= \frac{23}{100} \times 20 \\ &= 4.6\,\mathrm{cm^3\ per\ 100\,cm^3\ of\ blood} \end{aligned}\] [M1] [A1]

**Step 3: express as a share of what was loaded.** The blood carried \(0.97 \times 20 = 19.4\,\mathrm{cm^3}\), so it gave up \(4.6 \div 19.4 = 24\%\) of its oxygen, and it still carries 74% of 20, which is 14.8 cm³. This reserve is why the blood returning to the lungs is still about three-quarters saturated.
:::

:::eg Explain why the oxygen dissociation curve of haemoglobin is S-shaped.
A full-mark answer follows the four stages in order.

A haemoglobin molecule has four haem groups, and each one can bind one oxygen molecule. [B1]

At a low partial pressure of oxygen, the first oxygen molecule binds slowly (with difficulty), because the haem groups are not easily reached, so the curve is shallow. [B1]

Binding of the first oxygen changes the shape (tertiary and quaternary structure) of the haemoglobin so that the other haem groups bind oxygen more easily (cooperative binding), which makes the curve steep. [B1]

The fourth oxygen molecule binds with difficulty, because there are few vacant haem groups left for it to collide with, so the curve flattens as it approaches 100% saturation. [B1]

A weaker answer says "haemoglobin takes up oxygen quickly, then slows down because it is full". That describes the shape and does not explain why the middle is steep: there is no change of shape and no cooperative binding.
:::

:::eg Real context, a climb to altitude: at high altitude the air pressure is lower, so the pO₂ of the air in the alveoli of a climber falls from 13 kPa to 8 kPa. At 8 kPa haemoglobin is 91% saturated. Compare this with sea level and explain why a climber can still load a lot of oxygen.
The alveolar pO₂ falls from 13 to 8 kPa, a fall of \(5 \div 13 = 38\%\), but the saturation falls only from 97% to 91%, a fall of 6 percentage points.

At 8 kPa the saturation of the haemoglobin is still about 91%, so the blood is still nearly full of oxygen. [B1]

This is because at these partial pressures the dissociation curve is on its flat top, where a large fall in pO₂ makes little difference to the saturation. [B1]

So the blood still carries almost as much oxygen as at sea level: 91% of its capacity compared with 97%. [B1]

A climber still feels breathless, because the tissues' pO₂ is lower and the reserve of oxygen in the blood is smaller. Over days, the body makes more red blood cells to carry more haemoglobin, which restores the oxygen delivered.
:::

## Carbon dioxide transport

The cells of a respiring tissue make carbon dioxide, and it must be carried to the lungs. Carbon dioxide is carried in three ways. The percentages are approximate textbook figures.

| Form | Where | Approximate share |
|---|---|---|
| hydrogen carbonate ions (\(\ce{HCO3-}\)) | made inside red blood cells, carried in the plasma | about 85% |
| carbaminohaemoglobin | on haemoglobin inside red blood cells | about 10% |
| dissolved carbon dioxide | in the plasma | about 5% |

Both the red blood cell and the plasma are therefore involved.

### Inside the red blood cell

:::def Carbonic anhydrase
An enzyme in red blood cells that catalyses the reaction between carbon dioxide and water to form carbonic acid, \(\ce{H2CO3}\), and so speeds up the transport of carbon dioxide.
:::

In a respiring tissue the steps are:

:::steps
1. **Carbon dioxide diffuses** from the respiring cells into the tissue fluid, into the blood plasma and into the **red blood cell**, down its partial pressure gradient.
2. **Carbonic anhydrase** in the red blood cell catalyses the reaction of carbon dioxide with water to make carbonic acid. The acid then dissociates into hydrogen ions and hydrogen carbonate ions:

\[\ce{CO2 + H2O <=>[\text{carbonic anhydrase}] H2CO3}\]

\[\ce{H2CO3 <=> H+ + HCO3-}\]

3. **Haemoglobin takes up the hydrogen ions.** The \(\ce{H+}\) ions bind to haemoglobin and form **haemoglobinic acid** (HHb). This stops the pH of the red blood cell falling too far, so haemoglobin acts as a **buffer**. It also changes the shape of haemoglobin so that it releases oxygen more easily (the Bohr shift, below).
4. **Hydrogen carbonate ions leave the red cell.** \(\ce{HCO3-}\) is charged, so it cannot cross the phospholipid bilayer: it leaves by **facilitated diffusion** through a transport protein in the cell surface membrane, down its concentration gradient, into the plasma. The plasma carries it to the lungs.
5. **Chloride ions move in.** Each \(\ce{HCO3-}\) that leaves would make the inside of the cell more positive, so chloride ions \(\ce{Cl-}\) move **into** the red blood cell from the plasma. This movement is the **chloride shift**.
6. **Some carbon dioxide binds to haemoglobin.** It combines directly with the **amine groups** (–NH₂) at the ends of the polypeptide chains of haemoglobin, not with the haem group, to form **carbaminohaemoglobin**.
:::

:::def Haemoglobinic acid
The compound formed when hydrogen ions released from carbonic acid in a red blood cell combine with haemoglobin. Its formation removes hydrogen ions from the cell, so it helps to maintain the pH.
:::

:::def Carbaminohaemoglobin
The compound formed when carbon dioxide binds directly to the amine groups of the polypeptide chains of haemoglobin.
:::

:::def Chloride shift
The movement of chloride ions into red blood cells from the plasma as hydrogen carbonate ions move out of the red blood cells into the plasma, so that the electrical balance across the cell surface membrane is maintained.
:::

:::html
<figure class="fig"><svg viewBox="0 0 600 296" role="img" aria-label="A red blood cell in a respiring tissue. Carbon dioxide diffuses into the cell. Inside, carbonic anhydrase catalyses carbon dioxide plus water forming carbonic acid, which dissociates into hydrogen ions and hydrogen carbonate ions. Hydrogen ions combine with haemoglobin to form haemoglobinic acid. Some carbon dioxide combines with haemoglobin to form carbaminohaemoglobin. Hydrogen carbonate ions leave the cell into the plasma and chloride ions move in, the chloride shift. Oxygen is unloaded from oxyhaemoglobin."><path class="fm s-acc sw2" d="M440 150L438.8 162.4L435.2 174.6L429.3 186.4L421.2 197.5L411.1 207.8L399 217.2L385.2 225.4L370 232.3L353.6 237.8L336.2 241.8L318.3 244.2L300 245L281.7 244.2L263.8 241.8L246.4 237.8L230 232.3L214.8 225.4L201 217.2L188.9 207.8L178.8 197.5L170.7 186.4L164.8 174.6L161.2 162.4L160 150L161.2 137.6L164.8 125.4L170.7 113.6L178.8 102.5L188.9 92.2L201 82.8L214.8 74.6L230 67.7L246.4 62.2L263.8 58.2L281.7 55.8L300 55L318.3 55.8L336.2 58.2L353.6 62.2L370 67.7L385.2 74.6L399 82.8L411.1 92.2L421.2 102.5L429.3 113.6L435.2 125.4L438.8 137.6Z"/><text class="tl" x="300" y="100" text-anchor="middle">CO₂ + H₂O ⇌ H₂CO₃</text><text class="tl" x="300" y="114" text-anchor="middle">(carbonic anhydrase)</text><text class="tl" x="300" y="140" text-anchor="middle">H₂CO₃ ⇌ H⁺ + HCO₃⁻</text><text class="tl" x="300" y="166" text-anchor="middle">H⁺ + Hb → HHb</text><text class="tl" x="300" y="180" text-anchor="middle">(haemoglobinic acid)</text><text class="tl" x="300" y="204" text-anchor="middle">CO₂ + Hb → HbCO₂</text><text class="tl" x="300" y="218" text-anchor="middle">(carbaminohaemoglobin)</text><text class="tl tb" x="20" y="24">red blood cell</text><path class="ln-m thin" d="M72 32L186 94"/><text class="tl" x="590" y="24" text-anchor="end">plasma carries HCO₃⁻ and some dissolved CO₂</text><path class="c3 sw2" d="M20 132L146 132" marker-end="url(#ah)"/><text class="tl" x="20" y="120">CO₂ from the tissue</text><path class="c3 sw2" d="M452 124L570 124" marker-end="url(#ah)"/><text class="tl" x="452" y="112">HCO₃⁻ to plasma</text><path class="c4 sw2" d="M570 176L452 176" marker-end="url(#ah)"/><text class="tl" x="580" y="198" text-anchor="end">Cl⁻ moves in</text><text class="tl" x="580" y="212" text-anchor="end">(chloride shift)</text><path class="c1 sw2" d="M212 228L160 268" marker-end="url(#ah)"/><text class="tl" x="10" y="284">O₂ unloaded from oxyhaemoglobin</text></svg><figcaption>Carbon dioxide transport in the tissues. In the lungs every step runs in reverse: hydrogen carbonate ions enter the cell, chloride ions leave, and carbon dioxide is released and diffuses into the alveolus.</figcaption></figure>
:::

:::key Why the chloride shift matters
- It keeps the **charge balanced** across the membrane, so hydrogen carbonate ions can **keep leaving** the cell.
- This keeps the concentration of \(\ce{HCO3-}\) inside the red cell low, so the carbonic anhydrase reaction keeps going to the right and the cell can take up **more carbon dioxide**.
- So more carbon dioxide is carried (as \(\ce{HCO3-}\) in the plasma) than the red cell alone could hold.
:::

### The role of plasma

The plasma carries carbon dioxide in two ways. Most of the carbon dioxide made by the tissues is carried as hydrogen carbonate ions dissolved in the plasma (the ions made in the red cell, above), and a small share (about 5%) is carried simply **dissolved** in the plasma as \(\ce{CO2}\) molecules. Plasma has no carbonic anhydrase, so it makes little carbonic acid by itself, which is why the red blood cell is essential.

### In the lungs

In the lungs the pCO₂ of the plasma is higher than in the alveolar air, so the changes run in **reverse**.
- Dissolved carbon dioxide diffuses out of the plasma into the alveolus, down its partial pressure gradient.
- \(\ce{HCO3-}\) re-enters the red blood cell, and chloride ions leave (the reverse chloride shift).
- Haemoglobinic acid releases its \(\ce{H+}\) ions, which combine with \(\ce{HCO3-}\) to make carbonic acid, and carbonic anhydrase splits it into carbon dioxide and water. The carbon dioxide diffuses out.
- Carbaminohaemoglobin releases its carbon dioxide too. As the haemoglobin gives up hydrogen ions and carbon dioxide, it binds oxygen more easily.

### The tissues and the lungs compared

Everything in this chapter is one set of reversible reactions that run in opposite directions in two places. Use the table to check that you can say both columns.

| | respiring tissue | lungs |
|---|---|---|
| pO₂ and pCO₂ | pO₂ low, pCO₂ high | pO₂ high (about 13 kPa), pCO₂ low |
| oxygen and haemoglobin | oxyhaemoglobin unloads oxygen (steep part of the curve; curve shifted right, the Bohr shift) | haemoglobin loads oxygen (flat top of the curve; curve shifted left) |
| carbonic anhydrase | CO₂ + H₂O → H₂CO₃ → H⁺ + HCO₃⁻ | H⁺ + HCO₃⁻ → H₂CO₃ → CO₂ + H₂O |
| hydrogen carbonate ions | leave the red cell into the plasma | enter the red cell from the plasma |
| chloride ions | move into the red cell (chloride shift) | move out of the red cell |
| hydrogen ions | bind to haemoglobin: haemoglobinic acid forms | released from haemoglobinic acid |
| carbon dioxide on haemoglobin | carbaminohaemoglobin forms | carbaminohaemoglobin releases CO₂, which diffuses into the alveolus |

:::warn Where does the carbon dioxide bind to haemoglobin?
Carbaminohaemoglobin is formed when carbon dioxide binds to the **amine groups** of the globin chains. Oxygen binds to the **haem** groups. Do not write that carbon dioxide "binds to the haem group", which is where carbon monoxide and oxygen bind. Also, the chloride shift moves \(\ce{Cl-}\) **into** the red cell, in the tissues.
:::

:::eg Describe the roles of the red blood cell in the transport of carbon dioxide from respiring tissue to the lungs.
Six marking points, in the order they happen.

Carbon dioxide diffuses from the tissue into the red blood cell, down a concentration gradient. [B1]

Carbonic anhydrase catalyses the reaction of carbon dioxide and water to form carbonic acid. [B1]

Carbonic acid dissociates into hydrogen ions and hydrogen carbonate ions. [B1]

The hydrogen ions bind to haemoglobin to form haemoglobinic acid, which acts as a buffer and prevents a large fall in pH. [B1]

Hydrogen carbonate ions diffuse out of the red cell into the plasma by facilitated diffusion, and chloride ions move into the cell (the chloride shift) to keep the charge balanced. [B1]

Some carbon dioxide binds to the amine groups of haemoglobin to form carbaminohaemoglobin. [B1]

(Also credit: carbonic anhydrase speeds up the reaction; carbon dioxide is also carried dissolved in the plasma.)

A weaker answer says "carbon dioxide is carried in the blood as hydrogen carbonate". It does not say where the ions are made, what makes them, or what happens to the hydrogen ions.
:::

:::eg Spot the error: describe how carbon dioxide is carried from the tissues to the lungs. [3]
A student wrote this answer.

Line 1: Most of the carbon dioxide is carried as hydrogen carbonate ions in the plasma.
Line 2: Some carbon dioxide binds to the haem group of haemoglobin to form carbaminohaemoglobin.
Line 3: A small amount of carbon dioxide is carried dissolved in the plasma.

Line 1 is correct [B1]. **Line 2 is wrong: carbaminohaemoglobin is formed when carbon dioxide binds to the amine groups of the globin chains. The haem groups are where oxygen binds. That mark is lost [B0].** Line 3 is correct [B1].

Correct Line 2: "Some carbon dioxide binds to the amine groups of haemoglobin to form carbaminohaemoglobin." With that change the answer scores 3 marks.
:::

## The Bohr shift

When tissues respire faster, they produce more carbon dioxide. A rise in pCO₂ has an effect on the haemoglobin.

:::def Bohr shift
The shift of the oxygen dissociation curve to the right when the partial pressure of carbon dioxide rises. At any partial pressure of oxygen, haemoglobin has a lower affinity for oxygen and is less saturated, so it releases more oxygen.
:::

The cause is the chemistry of the red blood cell. A higher pCO₂ means more carbon dioxide enters the red blood cell, and carbonic anhydrase makes more carbonic acid, so there are more hydrogen ions. These bind to haemoglobin to form haemoglobinic acid, which **changes the shape of the haemoglobin molecule** so that its **affinity for oxygen falls**. Oxygen is released more readily.

:::plot Model oxygen dissociation curves of adult haemoglobin at a normal pCO₂ and at a high pCO₂ (the Bohr shift). At 4 kPa the saturation falls from about 61% to about 41%.
--f "100*x**2.7/(3.4**2.7+x**2.7)" --f "100*x**2.7/(4.575**2.7+x**2.7)" --label "lower pCO₂ (5.3 kPa)" --label "higher pCO₂ (10 kPa)" --x 0 16 --y 0 135 --xlabel "partial pressure of oxygen / kPa" --ylabel "saturation of haemoglobin / %" --pt "4,60.8,61%@nw" --pt "4,41.0,41%@se" --legend tr --alt "Two S-shaped curves. The curve for the higher pCO₂ lies to the right of the curve for the lower pCO₂, so that at a pO₂ of 4 kPa the saturation is about 41% instead of about 61%. Both curves approach 100% saturation at high pO₂."
:::

:::key The Bohr shift and why it matters
- **Active tissues** (respiring fast) have a **high pCO₂** and a **low pO₂**. The curve shifts **right**: haemoglobin has a **lower affinity**, so at the same pO₂ it **unloads more oxygen** (in the example, 20 percentage points more at 4 kPa). The tissues that most need oxygen receive more.
- **In the lungs** the pCO₂ is **low**, so the curve is **further to the left**: haemoglobin has a **higher affinity** and **loads oxygen** fully, even though the pO₂ is only 13 kPa.
- The shift is **useful**: it matches the oxygen delivery to the oxygen use, without the need for any change in the blood flow.
:::

Try it: drag the **pCO₂** slider and watch the curve move right. Drag the **lungs** and **tissue** markers to read the saturation at each pO₂, and the percentage unloaded.

:::html
<div class="widget" data-w="bio-odc" data-pco2="5.3"></div>
:::

:::warn Which way does the curve move?
A shift **to the right** means a **lower affinity** and **more oxygen released**. It does **not** mean that the haemoglobin carries more oxygen. Say "at the same pO₂ the saturation is lower" and quote the numbers. Also remember that the Bohr shift is caused by **carbon dioxide** (through hydrogen ions), not by the oxygen.
:::

:::note Beyond the syllabus
Myoglobin (in muscle) and fetal haemoglobin both have curves to the **left** of adult haemoglobin: they hold oxygen more tightly. You do not need them for this syllabus; they are an example of how the shape of a curve depends on the protein.
:::

:::eg Blood is 100% saturated when 100 cm³ of it carries 18 cm³ of oxygen. It leaves the lungs 97% saturated. In a muscle at a pO₂ of 4 kPa the saturation is 61% at a normal pCO₂ and 41% at a raised pCO₂. Calculate how much more oxygen each 100 cm³ of blood unloads at the raised pCO₂.
The Bohr shift changes the saturation at the **same** pO₂, so compare the two unloaded amounts.

**Step 1: percentage points unloaded.** Take the saturation in the muscle away from the saturation leaving the lungs.

\[\begin{aligned} \text{normal pCO}_2 &: 97 - 61 = 36\ \text{percentage points} \\ \text{raised pCO}_2 &: 97 - 41 = 56\ \text{percentage points} \end{aligned}\] [M1] [A1]

**Step 2: the extra, as a volume.** The extra is \(56 - 36 = 20\) percentage points of the capacity of 18 cm³.

\[\begin{aligned} \text{extra oxygen} &= \frac{20}{100} \times 18 \\ &= 3.6\,\mathrm{cm^3\ per\ 100\,cm^3\ of\ blood} \end{aligned}\] [M1] [A1]

Check with the two volumes: \(0.36 \times 18 = 6.48\,\mathrm{cm^3}\) at the normal pCO₂ and \(0.56 \times 18 = 10.08\,\mathrm{cm^3}\) at the raised pCO₂, a difference of 3.60 cm³. The active muscle gets about 1.6 times as much oxygen from each 100 cm³ of blood, with no extra blood flow.
:::

:::eg Explain the Bohr shift and its importance to a running mammal.
Six marking points.

During exercise, the muscle cells respire faster, so they produce more carbon dioxide and the pCO₂ of the blood rises. [B1]

The carbon dioxide enters the red blood cells, where carbonic anhydrase makes carbonic acid that dissociates into hydrogen ions and hydrogen carbonate ions. [B1]

The hydrogen ions bind to haemoglobin, forming haemoglobinic acid, which changes the shape of haemoglobin so that its affinity for oxygen decreases. [B1]

The oxygen dissociation curve shifts to the right (the Bohr shift): at the same partial pressure of oxygen, the haemoglobin is less saturated and releases more oxygen. [B1]

So more oxygen is unloaded in the active muscles, where it is needed for aerobic respiration. [B1]

In the lungs the pCO₂ is lower, so the curve shifts back to the left and haemoglobin loads oxygen fully again. [B1]

(Also credit: the effect is greater at a low pO₂.)

A weaker answer says "carbon dioxide makes haemoglobin let go of oxygen faster". It never says the curve shifts, never mentions hydrogen ions or the change in shape, and does not link the shift to the tissue's needs.
:::

## Practice

:::try Start easy, finish at exam standard
Q: Write an equation for the reversible reaction between haemoglobin and oxygen.
A: \(\ce{Hb + 4O2 <=> HbO8}\) (haemoglobin plus four oxygen molecules gives oxyhaemoglobin).
Q: State what is meant by the partial pressure of oxygen.
A: The pressure exerted by oxygen alone in a mixture of gases; it is a measure of the concentration of oxygen, in kPa.
Q: In the lungs the haemoglobin is almost fully saturated. State where on the curve this is and why it is useful.
A: On the flat top of the curve (high pO₂). The haemoglobin loads nearly all the oxygen it can, and the saturation changes little if the pO₂ falls a little.
Q: Explain why the curve is steep between about 2 kPa and 6 kPa.
A: The binding of the first oxygen molecules changes the shape of haemoglobin, so the second and third bind more easily (cooperative binding). A small rise in pO₂ gives a large rise in saturation.
Q: Name the enzyme in red blood cells that makes carbonic acid from carbon dioxide and water.
A: Carbonic anhydrase.
Q: A sample of blood carries 15 cm³ of oxygen per 100 cm³ when 100% saturated. Calculate the volume of oxygen in 100 cm³ of blood that is 80% saturated.
A: \(80 \div 100 \times 15 = 12\,\mathrm{cm^3}\).
Q: State the approximate percentage of carbon dioxide carried as hydrogen carbonate ions and the percentage carried dissolved in the plasma.
A: About 85% as hydrogen carbonate ions and about 5% dissolved in the plasma (about 10% is carbaminohaemoglobin).
Q: Explain why haemoglobinic acid forms in the red blood cell.
A: Carbonic acid dissociates to \(\ce{H+}\) and \(\ce{HCO3-}\); the \(\ce{H+}\) ions bind to haemoglobin. This prevents the pH of the cell from falling, so haemoglobin acts as a buffer.
Q: Explain why chloride ions move into red blood cells when hydrogen carbonate ions move out.
A: \(\ce{HCO3-}\) is a negative ion, so when it leaves the cell it would leave a positive charge inside. \(\ce{Cl-}\) ions move in to keep the charge balanced, so that more \(\ce{HCO3-}\) can leave.
Q: At rest the blood leaving a muscle is still 61% saturated. Suggest why it is an advantage that haemoglobin does not give up all of its oxygen.
A: The remaining oxygen is a reserve. When the muscle starts to work harder, the pO₂ falls and the haemoglobin can unload more oxygen at once.
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ State two ways in which carbon dioxide is carried in the blood, other than as hydrogen carbonate ions.
A: Dissolved in the plasma. [B1]
Combined with haemoglobin as carbaminohaemoglobin. [B1]
Q: [4 marks] ★★ The table shows the percentage saturation of the haemoglobin of two mammals, a large mammal and a small mammal, at different partial pressures of oxygen. The data are for the question.

| pO₂ / kPa | large mammal / % | small mammal / % |
|---|---|---|
| 2 | 29 | 7 |
| 4 | 72 | 32 |
| 6 | 89 | 58 |
| 9 | 96 | 81 |
| 13 | 98 | 92 |

(a) Describe the differences between the two sets of data. (b) A small mammal has a much higher metabolic rate than a large mammal. Suggest how the haemoglobin of the small mammal is suited to its needs.
H: For (a), compare the saturations at the same pO₂, quoting figures.
H: For (b), where would the oxygen be released: at a high pO₂ or a low pO₂?
A: (a) At every pO₂ the saturation of the large mammal's haemoglobin is higher than that of the small mammal. [B1] For example, at 4 kPa it is 72% compared with 32%. [B1]
(b) The small mammal's haemoglobin has a lower affinity for oxygen (the curve is to the right), so it unloads oxygen more readily at the pO₂ in its tissues. [B1] This supplies the large amount of oxygen that the fast aerobic respiration of a small mammal needs. [B1]
Q: [3 marks] ★★ Use the table above. At the lungs the pO₂ is 13 kPa and in a working muscle it is 4 kPa. Calculate the percentage saturation of the haemoglobin that is unloaded in the muscle for the small mammal, and the volume of oxygen released from each 100 cm³ of its blood, when 100% saturated blood carries 15 cm³ of oxygen per 100 cm³.
H: Subtract the saturation at 4 kPa from the saturation at 13 kPa.
H: Then take that percentage of 15 cm³.
A: Percentage unloaded \(= 92 - 32\) [M1] \(= 60\) percentage points. [A1]
Volume \(= 60 \div 100 \times 15 = 9.0\,\mathrm{cm^3}\) per 100 cm³ [A1]
Q: [4 marks] ★★ (a) Explain the importance of the chloride shift. (b) Explain why haemoglobin is important in preventing a large fall in the pH of the red blood cells.
A: (a) Chloride ions move into the red blood cell as hydrogen carbonate ions move out. [B1] This keeps the electrical charge balanced, so more hydrogen carbonate ions can leave, and more carbon dioxide can be carried. [B1]
(b) Hydrogen ions are released when carbonic acid dissociates. [B1] They bind to haemoglobin to form haemoglobinic acid, so the concentration of free hydrogen ions stays low (haemoglobin acts as a buffer). [B1]
Q: [4 marks] ★★ The table shows the percentage saturation of haemoglobin from a sample of human blood at two values of pCO₂ and three values of pO₂.

| pO₂ / kPa | pCO₂ 4 kPa / % | pCO₂ 9 kPa / % |
|---|---|---|
| 3 | 45 | 25 |
| 6 | 85 | 68 |
| 10 | 96 | 90 |

(a) Describe the effect of an increase in pCO₂ on the saturation of the haemoglobin. (b) Name the effect and explain what causes it.
H: Quote the saturation at 3 kPa for both pCO₂ values.
H: For (b), name the ion that binds to haemoglobin.
A: (a) At each pO₂ the saturation is lower at the higher pCO₂. [B1] For example, at 3 kPa it falls from 45% to 25%, and the effect is smaller at a higher pO₂ (96% to 90% at 10 kPa). [B1]
(b) It is the Bohr shift. Carbon dioxide forms carbonic acid, whose hydrogen ions bind to haemoglobin and reduce its affinity for oxygen, so the curve shifts to the right. [B1] [B1]
Q: [6 marks] (#bio.movement) ★★★ Hydrogen carbonate ions made in the red blood cell enter the plasma. (a) Explain why they cannot cross the cell surface membrane by simple diffusion. (b) Describe how they cross the membrane. (c) Explain how the movement of chloride ions affects the movement of hydrogen carbonate ions. (d) State where in the red cell carbonic anhydrase is found.
H: Think about the structure of the phospholipid bilayer.
H: For (c), consider the charge on each ion.
A: (a) Hydrogen carbonate ions are charged, and the hydrophobic fatty acid tails in the middle of the bilayer repel them. [B1]
(b) They move through a transport protein (a channel or carrier) by facilitated diffusion. [B1] They move down a concentration gradient, so no ATP is needed. [B1]
(c) Chloride ions move into the cell as hydrogen carbonate ions move out. [B1] This keeps the charge balanced, so the hydrogen carbonate ions can continue to leave. [B1]
(d) In the cytoplasm of the red blood cell. [B1]
Q: [6 marks] (#bio.proteins) ★★★ Haemoglobin is a protein with four polypeptide chains. (a) Explain, using the term cooperative binding, why the dissociation curve is steeper between 2 kPa and 6 kPa than below 2 kPa. (b) Explain why the haemoglobin of a person who lives at high altitude is advantaged by a curve that is further to the left. (c) A mutation changes one amino acid in the globin chain so that the haem group is held more tightly. Suggest how this would change the curve.
H: For (b), think about the low pO₂ in the air at high altitude.
A: (a) The binding of the first oxygen molecule changes the shape of haemoglobin. [B1] This makes it easier for the second and third to bind, so a small increase in pO₂ gives a large rise in saturation. [B1]
(b) At high altitude, the pO₂ of the alveoli is low. [B1] A curve further to the left (a higher affinity) means the haemoglobin is more saturated at the same low pO₂, so it loads more oxygen. [B1]
(c) The curve would shift to the left (higher affinity), because the haemoglobin would hold oxygen more tightly. [B1] The haemoglobin would release less oxygen at the tissues. [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ Carbon monoxide binds to the haem groups of haemoglobin much more strongly than oxygen does, and it is released very slowly. A person breathes in air containing carbon monoxide, and half of the haem groups in the blood become bound to carbon monoxide. The person's blood still has the normal number of red blood cells. (a) Explain why the person receives less oxygen even though the lungs are working normally. (b) The remaining oxygen is held more tightly by the haemoglobin than usual. Explain this, using cooperative binding, and say what effect it has on the unloading of oxygen in the tissues. (c) Suggest why the first aid for this person is to give pure oxygen to breathe.
H: For (b), what does a carbon monoxide molecule on one haem group do to the shape of the molecule?
H: For (c), think about the competition between oxygen and carbon monoxide at the haem group.
A: (a) Haem groups occupied by carbon monoxide cannot bind oxygen, so the blood can carry only about half as much oxygen. [B1]
(b) The binding of carbon monoxide changes the shape of the haemoglobin molecule in the same way as binding oxygen, so the other haem groups bind oxygen more strongly (a higher affinity). [B1] The curve shifts to the left, so haemoglobin releases less oxygen at a given pO₂ in the tissues. [B1] The tissues get even less oxygen than the lower amount carried. [B1]
(c) A high pO₂ in the lungs raises the proportion of haem groups that are bound to oxygen, which helps to displace carbon monoxide. [B1] More oxygen is carried in the plasma in solution as well. [B1]
Q: [5 marks] ★★★ A child has anaemia, so the blood contains only half as much haemoglobin as normal. The shape of the dissociation curve is the same as normal. Normal blood carries 16 cm³ of oxygen per 100 cm³ when 100% saturated. The haemoglobin leaving the lungs is 98% saturated, and the haemoglobin leaving a muscle during exercise is 42% saturated (data for the question). (a) Calculate the volume of oxygen that normal blood unloads in the muscle per 100 cm³. (b) Calculate the volume that the anaemic blood unloads. (c) Suggest how the child's body might compensate.
H: Unloaded saturation \(= 98 - 42\), then take that percentage of the capacity.
H: The anaemic blood has the same percentages but half the capacity.
A: (a) Unloaded \(= 98 - 42 = 56\) percentage points \(= 0.56 \times 16\) [M1] \(= 9.0\,\mathrm{cm^3}\) per 100 cm³ [A1]
(b) Capacity is \(8\,\mathrm{cm^3}\), so \(0.56 \times 8 = 4.5\,\mathrm{cm^3}\) per 100 cm³. [A1]
(c) A faster heart rate (or faster blood flow) so that more blood passes the muscle each minute. [B1] Breathing faster does not raise the saturation much, because the blood is already almost fully saturated, so a greater cardiac output is the better compensation. [B1]
:::

:::quiz
? In the lungs, haemoglobin is on the top of its dissociation curve. Which statement explains why this is useful?
+ The curve is flat here, so the saturation changes little if the pO₂ falls a little.
- The curve is steepest here, so a small change in pO₂ loads a lot of oxygen.
- Haemoglobin releases its oxygen here.
- Haemoglobin has its lowest affinity for oxygen here.
> At high pO₂ the curve is flat, so haemoglobin loads nearly all it can and has a safety margin. The steep part is at lower pO₂, where oxygen is unloaded.
? Which statement describes cooperative binding?
+ The binding of one oxygen molecule makes it easier for the next to bind.
- Each haem group binds an oxygen molecule at a different pO₂.
- Oxygen binds to the globin and not to the haem group.
- The four chains of haemoglobin bind oxygen at the same time.
> The first oxygen changes the shape of haemoglobin so that the others bind more easily. That gives the steep middle of the S-shaped curve.
? In the Bohr shift, what causes the curve to move to the right?
+ an increase in the partial pressure of carbon dioxide
- a decrease in the partial pressure of carbon dioxide
- an increase in the partial pressure of oxygen
- an increase in the number of red blood cells
> More carbon dioxide gives more hydrogen ions, which bind to haemoglobin and reduce its affinity for oxygen. The shift is not caused by the oxygen or the number of cells.
? What is the effect of a shift of the curve to the right?
+ at the same pO₂, more oxygen is released
- at the same pO₂, less oxygen is released
- haemoglobin can carry more oxygen at 100% saturation
- haemoglobin loads oxygen more easily at the lungs
> A shift to the right means lower affinity: the haemoglobin is less saturated at any given pO₂, so more oxygen is released in the tissues.
? Where does carbon dioxide bind to form carbaminohaemoglobin?
+ the amine groups of the polypeptide chains
- the iron ion of the haem group
- the carboxyl group of haem
- the phospholipid of the cell surface membrane
> Carbon dioxide binds to the amine groups (–NH₂) of the globin chains. The iron ion of the haem group binds oxygen, and carbon monoxide.
? What is the main form in which carbon dioxide is carried in the blood?
+ as hydrogen carbonate ions in the plasma
- as carbaminohaemoglobin in the red blood cells
- as dissolved carbon dioxide in the plasma
- as carbonic acid in the plasma
> About 85% is carried as \(\ce{HCO3-}\) in the plasma. About 10% is carbaminohaemoglobin and about 5% is dissolved. Carbonic acid is made in the red cell and dissociates at once.
? What is the chloride shift?
+ chloride ions move into red blood cells as hydrogen carbonate ions move out
- chloride ions move out of red blood cells as hydrogen carbonate ions move in
- chloride ions move from the plasma into the alveoli
- chloride ions bind to haemoglobin in place of oxygen
> In the tissues, hydrogen carbonate ions leave the red cell, and chloride ions enter to keep the electrical balance.
? What does carbonic anhydrase do?
+ it speeds up the reaction between carbon dioxide and water
- it carries carbon dioxide from the tissues to the lungs
- it binds hydrogen ions
- it releases oxygen from haemoglobin
> Carbonic anhydrase is an enzyme: it catalyses \(\ce{CO2 + H2O <=> H2CO3}\) in the red blood cell. Haemoglobin binds hydrogen ions and carries gases.
? Why is haemoglobinic acid important?
+ the formation of it removes hydrogen ions and so helps to keep the pH of the red blood cell stable
- it carries oxygen from the lungs to the tissues
- it carries carbon dioxide from the tissues to the lungs
- it is made by haemoglobin to release hydrogen ions into the plasma
> When hydrogen ions bind to haemoglobin, they are no longer free, so the pH does not fall as much. It does not carry the gases.
? Which statement about respiring tissues is correct?
+ pO₂ is low and haemoglobin unloads oxygen
- pO₂ is high and haemoglobin loads oxygen
- pCO₂ is low and haemoglobin binds oxygen more tightly
- pCO₂ is high and haemoglobin has a higher affinity for oxygen
> Tissues use oxygen, so the pO₂ is low, and haemoglobin unloads oxygen. High pCO₂ lowers the affinity.
:::

:::checklist What you can now do
- [ ] I can describe the roles of red blood cells and haemoglobin in transporting oxygen, and of carbonic anhydrase, haemoglobinic acid and carbaminohaemoglobin in transporting carbon dioxide.
- [ ] I can describe the chloride shift and explain why it is important.
- [ ] I can describe the role of the plasma in carrying carbon dioxide.
- [ ] I can describe and explain the oxygen dissociation curve of adult haemoglobin, including cooperative binding.
- [ ] I can explain why the shape of the curve suits the partial pressures of oxygen in the lungs and in respiring tissues.
- [ ] I can describe and explain the Bohr shift and its importance.
- [ ] I can read saturation values from a curve, calculate the oxygen unloaded, and describe data on two curves with figures and units.
:::

:::recap
- Haemoglobin has four haem groups, each binding one oxygen molecule: \(\ce{Hb + 4O2 <=> HbO8}\). It loads oxygen in the lungs (high pO₂) and unloads it in the tissues (low pO₂).
- The oxygen dissociation curve is **S-shaped**: first oxygen binds with difficulty; it changes the shape and the next two bind more easily (cooperative binding); the fourth is hard again.
- In the lungs (about 13 kPa) the curve is flat: nearly full loading. In respiring tissues the curve is steep: a small fall in pO₂ releases a lot of oxygen.
- Carbon dioxide: about 85% as hydrogen carbonate ions (in the plasma), about 10% as carbaminohaemoglobin (on the amine groups of globin) and about 5% dissolved in the plasma.
- Carbonic anhydrase in the red cell makes carbonic acid; it dissociates to \(\ce{H+}\) and \(\ce{HCO3-}\). \(\ce{H+}\) binds to haemoglobin (haemoglobinic acid: a buffer). \(\ce{HCO3-}\) leaves by facilitated diffusion; chloride ions move in (chloride shift) to keep the charge balanced.
- The Bohr shift: a higher pCO₂ lowers the affinity of haemoglobin, and the curve moves right, so more oxygen is released in active tissues. In the lungs the pCO₂ is low, so loading is full.
:::

:::links
- read: [CAIE A Level Biology: transport in mammals notes and topic questions](https://www.physicsandmathstutor.com/biology-revision/a-level-cie/transport-in-mammals/) · Physics & Maths Tutor · free revision notes and past-paper questions sorted by topic
- practise: [Transport in mammals (9700, exams from 2025)](https://www.savemyexams.com/a-level/biology/cie/25/topics/8-transport-in-mammals/) · Save My Exams · notes and exam questions with mark schemes, some free [paid]
- watch: [Amoeba Sisters videos](https://www.youtube.com/@AmoebaSisters/videos) · Amoeba Sisters (YouTube) · a friendly first explanation of haemoglobin and gas transport
- watch: [CAIE A Level Biology videos](https://cognito.org/specifications/alevel/biology/cie) · Cognito · short videos and questions matched to the syllabus
- read: [Circulatory and respiratory systems](https://openstax.org/books/biology-2e/pages/39-introduction) · OpenStax Biology 2e · free university textbook chapter on gas exchange and transport, beyond the syllabus in places
- papers: [Paper 2 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-biology/cie-paper-2/) · Physics & Maths Tutor · find the dissociation curve questions in real papers [unofficial]

Links checked 24 October 2026.
:::

Next: [The heart and the cardiac cycle](#bio.heart) shows how the heart pumps the blood that carries these gases.
