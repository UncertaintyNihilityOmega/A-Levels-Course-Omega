# REVIEW: Physics

Findings for the Writer, newest review at the bottom. One item per line:
`- [ ] <chapter-id>: <exactly what to change>`. The Writer fixes it and changes `[ ]` to `[x]`.
While any `- [ ]` line is open, `status` says FIX.

## REVIEW P1, P2 (2026-10-13)
Already fixed by the reviewer: figure labels and layout in all four chapters, g from data 9.78 (not 9.79), parcel v_y 99.0, dynamics quiz/spot-the-error mark wording, forces window-force sentence, units and phys-collide widget formatting. Open items:
- [x] phys.units: in the `:::def Derived unit` card, replace "(and possibly using no other units)" with ", such as \(\mathrm{m\,s^{-1}}\) or \(\mathrm{kg\,m^{-3}}\)" so the definition reads cleanly.
- [x] phys.units: in the `:::warn mm and m s` box, replace "the capital T (tera, \(10^{12}\), not the tesla)" with "the capital T (as a prefix it is tera, \(10^{12}\); on its own, T is the tesla)".
- [x] phys.kinematics: in the "100 km h⁻¹ in 8.0 s" worked example give the [A1] answer as \(3.5\,\mathrm{m\,s^{-2}}\) (2 s.f., like the data) on the display line, and keep 3.47 only as the unrounded value in the sentence below it.
- [x] phys.forces: steering-wheel worked example: the data (12 N, 0.36 m) are 2 s.f., so give the torque as \(4.3\,\mathrm{N\,m}\) on the [A1] line (keep 4.32 as the unrounded value in the check by moments) and update checks/phys.forces.py.
- [x] phys.dynamics: in "Impulse and the force–time graph", replace "Cambridge only states force as rate of change of momentum, but impulse is a quick way to think." with "The 9702 syllabus defines force as the rate of change of momentum and does not name impulse, but impulse is a quick way to think."
- [x] phys.dynamics: skydiver v–t figure: make the start of the curve follow the dashed gradient-g line (first segment from (60,250) with gradient about 4.3 px per px, e.g. L70 207L82 165, before bending over), so "1: gradient = g" is visibly true.
