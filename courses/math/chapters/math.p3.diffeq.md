@chapter math.p3.diffeq
@title Differential equations
@level a2
@paper CAIE P3 · Edexcel IAL P4 · AQA/OCR/Edexcel Pure Year 2
@time 7–9 hours
@summary How to turn a rate statement such as "the rate of change of \(N\) is proportional to \(N\)" into a differential equation, how to solve it by separating the variables, how to find a particular solution from an initial condition, and how to read the answer in context: growth, decay, cooling and a population that levels off.

:::why
Most real change is described by a rate. A population grows at a rate that depends on how many there are; a cup of tea cools at a rate that depends on how much hotter it is than the room; a tank drains at a rate that depends on the depth. These statements are differential equations, and solving one gives the whole story: the number, the temperature or the depth at every moment. This is how the exponential function \(e^{kt}\) first appears in modelling, and why it appears so often.
:::

**Before you start**, you need integration from [Further integration](#math.p3.integ) and [Integration techniques](#math.p3.inttech), and exponentials and logarithms from [Exponentials and logarithms](#math.p3.logs).

## What a differential equation is

:::def Differential equation
A differential equation (DE) is an equation that contains a derivative such as \(\dfrac{dy}{dx}\) or \(\dfrac{dN}{dt}\). To **solve** it is to find the function \(y\) (or \(N\)) that satisfies it.
:::

:::def General and particular solutions
The **general solution** contains an arbitrary constant, so it describes a whole family of curves. A **particular solution** is the one curve of that family that passes through a given point, found by using an **initial condition** such as \(y = 5\) when \(x = 0\) to fix the constant.
:::

## Forming a differential equation

"Proportional to" is the key phrase: it means "equals a constant times". The constant of proportionality is usually called \(k\). A **rate of change** of \(x\) with respect to time \(t\) is \(\dfrac{dx}{dt}\), and "decreasing" means a minus sign in front of \(k\) when \(k > 0\).

| Statement | Differential equation |
|---|---|
| The rate of increase of \(N\) is proportional to \(N\) | \(\dfrac{dN}{dt} = kN\) |
| The mass \(m\) decreases at a rate proportional to \(m\) | \(\dfrac{dm}{dt} = -km\) |
| The depth \(h\) decreases at a rate proportional to \(\sqrt h\) | \(\dfrac{dh}{dt} = -k\sqrt h\) |
| The gradient at each point is the product of its coordinates | \(\dfrac{dy}{dx} = xy\) |
| The temperature \(\theta\) falls at a rate proportional to its excess over \(20\) | \(\dfrac{d\theta}{dt} = -k(\theta - 20)\) |

## Separating the variables

If the DE can be arranged so that all the \(y\) terms are on one side with \(dy\) and all the \(x\) terms on the other with \(dx\), integrate both sides.

:::key Separation of variables
For \(\dfrac{dy}{dx} = f(x)\,g(y)\), rearrange and integrate:
\[\int \frac{1}{g(y)}\,dy = \int f(x)\,dx\]
Add **one** constant \(c\), on one side only. Then use the initial condition to find \(c\), and solve for \(y\) if the question asks for \(y\) in terms of \(x\).
:::

The integrals on each side may need any technique from [Integration techniques](#math.p3.inttech): reverse chain rule, partial fractions or parts.

:::eg (a) Solve \(\dfrac{dy}{dx} = 3y\), given that \(y = 5\) when \(x = 0\). (b) Solve \(\dfrac{dy}{dx} = \dfrac xy\), given that \(y = 2\) when \(x = 0\) and \(y > 0\).
(a) Separate: \(\displaystyle\int \frac1y\,dy = \int 3\,dx\), so \(\ln|y| = 3x + c\). At \(x = 0\), \(y = 5\): \(c = \ln 5\). Then \(\ln y - \ln 5 = 3x\), so \(\ln\dfrac y5 = 3x\) and \(y = 5e^{3x}\).

(b) Separate: \(\displaystyle\int y\,dy = \int x\,dx\), so \(\tfrac12y^2 = \tfrac12x^2 + c\), or \(y^2 = x^2 + A\) with \(A = 2c\). At \(x = 0\), \(y = 2\): \(A = 4\). So \(y^2 = x^2 + 4\), and since \(y > 0\), \(y = \sqrt{x^2 + 4}\).
:::

:::eg Solve \(\dfrac{dy}{dx} = 2xe^{-y}\), given that \(y = 0\) when \(x = 0\). Express \(y\) in terms of \(x\).
Since \(e^{-y} = \dfrac1{e^y}\), separate to \(\displaystyle\int e^y\,dy = \int 2x\,dx\). So \(e^y = x^2 + c\). At \(x = 0\), \(y = 0\): \(1 = c\). So \(e^y = x^2 + 1\) and \(y = \ln(x^2 + 1)\).

Check: \(\dfrac{dy}{dx} = \dfrac{2x}{x^2 + 1}\), and \(2xe^{-y} = \dfrac{2x}{x^2 + 1}\). They agree.
:::

:::warn Separating slips
Put the constant in once, at the integration step, **before** you rearrange. A constant added after taking the exponential is the classic slip: \(\ln y = 3x + c\) means \(y = Ae^{3x}\) with \(A = e^c\), not \(y = e^{3x} + c\). Also keep \(dx\) and \(dy\) with their own variables: if a \(y\) is left on the \(x\) side, you have not separated.
:::

## Growth, decay and cooling

When the rate is proportional to the quantity, \(\dfrac{dN}{dt} = kN\) separates to \(\ln N = kt + c\), so \(N = Ae^{kt}\): **exponential growth** if \(k > 0\), **decay** if \(k < 0\). The constant \(A\) is the starting value.

:::eg A population of insects is modelled by \(\dfrac{dN}{dt} = kN\), where \(N\) is the number after \(t\) years and \(k\) is a positive constant. Initially \(N = 2000\), and the population doubles in 5 years. Find (a) \(k\), (b) \(N\) after 12 years, to 3 significant figures, and (c) when \(N\) reaches 10 000.
\(N = Ae^{kt}\) with \(A = 2000\), so \(N = 2000e^{kt}\).
(a) At \(t = 5\), \(N = 4000\): \(e^{5k} = 2\), so \(k = \dfrac{\ln 2}{5} = 0.139\).
(b) \(N = 2000e^{12k} = 2000\times 2^{12/5} = 10\,600\) (3 s.f.).
(c) \(2000 \times 2^{t/5} = 10\,000\) gives \(2^{t/5} = 5\), so \(t = \dfrac{5\ln 5}{\ln 2} = 11.6\) years.
:::

:::eg A drink at \(90^\circ\text{C}\) is left in a room at \(20^\circ\text{C}\). Its temperature \(\theta\) after \(t\) minutes satisfies \(\dfrac{d\theta}{dt} = -k(\theta - 20)\), where \(k > 0\). After 5 minutes the temperature is \(60^\circ\text{C}\). Find the temperature after 10 minutes and the time for it to fall to \(40^\circ\text{C}\).
Separate: \(\displaystyle\int\frac{1}{\theta - 20}\,d\theta = -k\int dt\), so \(\ln(\theta - 20) = -kt + c\) (\(\theta > 20\)). Hence \(\theta = 20 + Ae^{-kt}\). At \(t = 0\), \(\theta = 90\): \(A = 70\). At \(t = 5\), \(\theta = 60\): \(40 = 70e^{-5k}\), so \(e^{-5k} = \tfrac47\) and \(k = \tfrac15\ln\tfrac74 = 0.112\).

At \(t = 10\): \(e^{-10k} = \left(\tfrac47\right)^2 = \tfrac{16}{49}\), so \(\theta = 20 + 70\times\tfrac{16}{49} = 42.9^\circ\text{C}\) (3 s.f.).

For \(\theta = 40\): \(20 = 70e^{-kt}\), so \(e^{-kt} = \tfrac27\) and \(t = \dfrac{\ln 3.5}{k} = 11.2\) minutes.

The drink never falls below \(20^\circ\text{C}\): as \(t \to \infty\), \(e^{-kt} \to 0\) and \(\theta \to 20\), the room temperature.
:::

:::eg (Exam style) Water drains from a tank. The depth \(h\) cm after \(t\) minutes satisfies \(\dfrac{dh}{dt} = -k\sqrt h\), where \(k\) is a positive constant. Initially \(h = 100\), and after 10 minutes \(h = 64\). Find \(k\) and the time for the tank to empty.
Separate: \(\displaystyle\int h^{-1/2}\,dh = -k\int dt\). [M1]
Integrate: \(2\sqrt h = -kt + c\). [A1] At \(t = 0\), \(h = 100\): \(c = 20\). [B1]
At \(t = 10\), \(h = 64\): \(2\times 8 = -10k + 20\), so \(k = 0.4\). [M1 A1]
The tank is empty when \(h = 0\): \(0 = -0.4t + 20\), so \(t = 50\) minutes. [A1]

Unlike exponential decay, this depth reaches zero in a finite time, because \(\sqrt h\) does not shrink in proportion to itself.
:::

## When growth levels off

An unlimited exponential cannot go on for ever, because food, space or money runs out. A model where the rate of growth depends on both the amount present and the room left uses a product such as \(P(10 - P)\). Separating the variables then needs partial fractions.

:::eg A population \(P\) (in thousands) satisfies \(\dfrac{dP}{dt} = 0.05P(10 - P)\), where \(t\) is in years and \(P = 1\) when \(t = 0\). Solve the DE, find when \(P = 5\), and describe what happens in the long term.
Separate: \(\displaystyle\int\frac{1}{P(10 - P)}\,dP = \int 0.05\,dt\). Partial fractions: \(\dfrac{1}{P(10 - P)} = \dfrac1{10}\left(\dfrac1P + \dfrac1{10 - P}\right)\). Integrate:
\[\tfrac1{10}\big(\ln P - \ln(10 - P)\big) = 0.05t + c \quad\Longrightarrow\quad \ln\frac{P}{10 - P} = 0.5t + c'\]
At \(t = 0\), \(P = 1\): \(c' = \ln\tfrac19\). So \(\dfrac{P}{10 - P} = \tfrac19e^{0.5t}\). Rearranging for \(P\):
\[P = \frac{10e^{0.5t}}{9 + e^{0.5t}} = \frac{10}{1 + 9e^{-0.5t}}\]
When \(P = 5\): \(1 + 9e^{-0.5t} = 2\), so \(e^{-0.5t} = \tfrac19\) and \(t = 2\ln 9 = 4.39\) years.

As \(t \to \infty\), \(e^{-0.5t} \to 0\) and \(P \to 10\): the population levels off at 10 thousand.
:::

:::plot The solution of \(\dfrac{dP}{dt} = 0.05P(10 - P)\) with \(P = 1\) at \(t = 0\). The growth is slow at first, fastest at \(P = 5\), then levels off at \(10\).
--f "10/(1+9*exp(-0.5*x))" --label "P(t)" --x 0 14 --y 0 11 --hline 10 --pt "4.394,5,P = 5 at t = 4.39@se" --xlabel "t (years)" --ylabel "P (thousands)" --legend br
:::

The graph is the S-shaped curve typical of limited growth. The line \(P = 10\) is a limit the curve approaches but never crosses. You can also read this from the DE itself: \(\dfrac{dP}{dt} = 0\) at \(P = 10\) (and at \(P = 0\)), and \(\dfrac{dP}{dt} > 0\) for \(0 < P < 10\), so a population starting between them rises towards \(10\).

## Harder separations

:::eg (Exam style) The variables \(x\) and \(y\) satisfy \(\dfrac{dy}{dx} = xy\ln x\) for \(x > 0\), and \(y = 1\) when \(x = 1\). Solve the equation, and find \(y\) when \(x = e\), giving 3 significant figures.
Separate: \(\displaystyle\int\frac1y\,dy = \int x\ln x\,dx\). [M1]
The right-hand side needs parts, with \(u = \ln x\) and \(\dfrac{dv}{dx} = x\): \(\displaystyle\int x\ln x\,dx = \tfrac12x^2\ln x - \tfrac14x^2\). [M1 A1]
So \(\ln y = \tfrac12x^2\ln x - \tfrac14x^2 + c\). At \(x = 1\), \(y = 1\): \(0 = 0 - \tfrac14 + c\), so \(c = \tfrac14\). [M1]
\[\ln y = \tfrac12x^2\ln x - \tfrac14x^2 + \tfrac14\]
At \(x = e\): \(\ln y = \tfrac12e^2 - \tfrac14e^2 + \tfrac14 = \tfrac14(e^2 + 1) = 2.097\), so \(y = e^{2.097} = 8.14\) (3 s.f.). [A1]
:::

:::exam What earns marks
- **Separate** (a mark), **integrate both sides** (usually two marks), then **find the constant** from the initial condition (a mark). Exams reward each step separately.
- Forming the DE from words: write the derivative with the right variable and the correct sign, and include \(k\). Check that "decreasing" gives \(-k\) with \(k > 0\).
- State the answer in the form asked: \(y\) in terms of \(x\) (rearrange), or leave the relationship if only "solve" is requested. Give the constant to the accuracy requested, usually 3 significant figures.
- A final mark often asks you to interpret: what happens as \(t \to \infty\)? Say it in context (the temperature tends to the room temperature, the population tends to the limit), not just \(\to 10\).
:::

:::board Other boards
Edexcel IAL P4 and the Year 2 Pure courses (AQA, OCR, Edexcel) all include first-order DEs by separating variables, with rate statements to form the equation. The logistic model \(\dfrac{dP}{dt} = kP(M - P)\) is solved by partial fractions on some courses and used as a context on others. Check your own specification for the contexts it lists.
:::

:::try Start easy, finish at exam standard
Q: The number \(N\) of bacteria increases at a rate proportional to \(N\). Write down a differential equation for \(N\) in terms of \(t\).
A: \(\dfrac{dN}{dt} = kN\), with \(k > 0\).
Q: Solve \(\dfrac{dy}{dx} = 4y^2\), given that \(y = 1\) when \(x = 0\).
A: \(\displaystyle\int y^{-2}\,dy = \int 4\,dx\), so \(-\dfrac1y = 4x + c\). At \(x = 0\), \(y = 1\): \(c = -1\). So \(\dfrac1y = 1 - 4x\) and \(y = \dfrac{1}{1 - 4x}\).
Q: Solve \(\dfrac{dy}{dx} = e^{2x - y}\), given that \(y = 0\) when \(x = 0\). Give \(y\) in terms of \(x\).
A: \(e^{2x - y} = e^{2x}e^{-y}\), so \(\displaystyle\int e^y\,dy = \int e^{2x}\,dx\), giving \(e^y = \tfrac12e^{2x} + c\). At \(x = 0\): \(1 = \tfrac12 + c\), so \(c = \tfrac12\). So \(y = \ln\left(\dfrac{e^{2x} + 1}{2}\right)\).
Q: Solve \(\dfrac{dy}{dx} = xy\cos x\), given that \(y = 1\) when \(x = 0\).
A: \(\displaystyle\int\frac1y\,dy = \int x\cos x\,dx\). By parts the right side is \(x\sin x + \cos x\). So \(\ln y = x\sin x + \cos x + c\). At \(x = 0\): \(0 = 1 + c\), so \(c = -1\). Then \(y = e^{x\sin x + \cos x - 1}\).
Q: A radioactive substance decays at a rate proportional to its mass \(m\). The initial mass is 40 g and the half-life is 8 days. Find the mass after 20 days, to 3 significant figures.
A: \(m = 40e^{-kt}\); half-life gives \(e^{-8k} = \tfrac12\), so \(m = 40\times 2^{-t/8}\). At \(t = 20\): \(m = 40\times 2^{-2.5} = 7.07\) g.
Q: A hot drink at \(80^\circ\text{C}\) cools in a room at \(20^\circ\text{C}\) so that \(\dfrac{d\theta}{dt} = -0.1(\theta - 20)\). Find \(\theta\) after 6 minutes, to 3 significant figures.
A: \(\theta = 20 + Ae^{-0.1t}\), and \(t = 0\), \(\theta = 80\) give \(A = 60\). At \(t = 6\): \(\theta = 20 + 60e^{-0.6} = 52.9^\circ\text{C}\).
Q: The depth \(h\) m of water in a tank satisfies \(\dfrac{dh}{dt} = -0.5\sqrt h\), where \(t\) is in hours, and \(h = 36\) when \(t = 0\). Find the depth after 8 hours and the time to empty the tank.
A: \(\displaystyle\int h^{-1/2}\,dh = -0.5\int dt\), so \(2\sqrt h = -0.5t + c\). At \(t = 0\): \(c = 12\). At \(t = 8\): \(2\sqrt h = 8\), so \(h = 16\) m. Empty when \(-0.5t + 12 = 0\): \(t = 24\) hours.
Q: Solve \(\dfrac{dy}{dx} = \dfrac{y}{x(x + 1)}\), given that \(y = 2\) when \(x = 1\), and \(x > 0\). Give \(y\) in terms of \(x\).
A: \(\displaystyle\int\frac1y\,dy = \int\frac{1}{x(x + 1)}\,dx = \int\left(\frac1x - \frac1{x + 1}\right)dx\). So \(\ln y = \ln x - \ln(x + 1) + c = \ln\dfrac{x}{x + 1} + c\). At \(x = 1\): \(\ln 2 = \ln\tfrac12 + c\), so \(c = \ln 4\). Then \(y = \dfrac{4x}{x + 1}\).
Q: (Exam style) A population satisfies \(\dfrac{dP}{dt} = P(8 - P)\) with \(P > 0\). Without solving, say what value \(P\) approaches if \(P = 3\) when \(t = 0\), and why.
A: The rate is zero when \(P = 8\), and it is positive for \(0 < P < 8\), so \(P\) increases towards \(8\) but cannot cross it. So \(P \to 8\) as \(t \to \infty\).
:::

:::quiz
? The mass \(m\) of a substance decreases at a rate proportional to \(m\). Which DE models this (with \(k > 0\))?
- \(\dfrac{dm}{dt} = km\)
+ \(\dfrac{dm}{dt} = -km\)
- \(\dfrac{dm}{dt} = -k\)
- \(\dfrac{dm}{dt} = -\dfrac km\)
> "Proportional to \(m\)" gives \(km\), and "decreases" gives the minus sign. A constant rate would be \(-k\), and \(-k/m\) would be proportional to \(1/m\).
? Which is the correct separated form of \(\dfrac{dy}{dx} = \dfrac{x}{y^2}\)?
- \(\displaystyle\int y^2\,dx = \int x\,dy\)
+ \(\displaystyle\int y^2\,dy = \int x\,dx\)
- \(\displaystyle\int \frac1{y^2}\,dy = \int x\,dx\)
- \(\displaystyle\int y\,dy = \int x\,dx\)
> Multiply by \(y^2\) and by \(dx\): \(y^2\,dy = x\,dx\). Each variable ends up with its own differential.
? What is the general solution of \(\dfrac{dy}{dx} = 2y\)?
- \(y = e^{2x} + c\)
+ \(y = Ae^{2x}\)
- \(y = 2e^x\)
- \(y = \tfrac12x^2 + c\)
> \(\ln y = 2x + c\), so \(y = e^{2x + c} = Ae^{2x}\) with \(A = e^c\). The constant multiplies the exponential; it is not added.
? A population satisfies \(\dfrac{dP}{dt} = 0.05P(10 - P)\) with \(P(0) = 1\). What does \(P\) approach as \(t \to \infty\)?
- \(0\)
- \(5\)
+ \(10\)
- It grows without limit.
> The rate is zero at \(P = 10\) and positive below it, so \(P\) rises to \(10\) and levels off.
? Why does a tank with \(\dfrac{dh}{dt} = -k\sqrt h\) empty in finite time, whereas \(\dfrac{dm}{dt} = -km\) never reaches zero?
- Because \(k\) is larger in the first.
+ The first solution, \(2\sqrt h = c - kt\), is linear in \(t\) and reaches zero; the second is an exponential, which only tends to zero.
- Because depth is measured in metres.
- It does not: both stay positive for ever.
> Setting \(2\sqrt h = c - kt\) equal to zero gives a finite time \(t = c/k\). An exponential \(Ae^{-kt}\) is positive for every \(t\).
:::

:::recap
- A DE contains a derivative. "Proportional to" means "equals \(k\) times"; "decreasing" puts a minus sign in front of \(k\).
- Separate the variables: \(\displaystyle\int\frac1{g(y)}\,dy = \int f(x)\,dx\). Add one constant, then use the initial condition to find it.
- \(\dfrac{dN}{dt} = kN\) gives \(N = Ae^{kt}\): growth if \(k > 0\), decay if \(k < 0\). \(\dfrac{d\theta}{dt} = -k(\theta - a)\) gives \(\theta = a + Ae^{-kt}\), which tends to \(a\).
- A product such as \(P(M - P)\) needs partial fractions and gives an S-shaped curve that levels off at \(M\).
- Check the solution by differentiating, and say what happens in the long term in the words of the context.
:::

:::note Learn more online
- **Watch:** [Differential equations, studying the unsolvable](https://www.3blue1brown.com/lessons/differential-equations) · 3Blue1Brown · what a differential equation describes
- **Watch:** [General and particular solutions](https://www.examsolutions.net/tutorials/finding-general-solution-particular-solution/) · ExamSolutions · separating variables and using a condition
- **Watch:** [Exam questions: forming differential equations](https://www.examsolutions.net/tutorials/exam-questions-forming-differential-equations/) · ExamSolutions · turning a rate statement into an equation
- **Practise:** [CAIE Pure 3 differential equations exam questions](https://www.savemyexams.com/a-level/maths/cie/20/pure-3/topic-questions/integration/differential-equations/exam-questions/) · Save My Exams · with mark schemes *(some content paid)*
- **Read:** [Separable equations](https://tutorial.math.lamar.edu/Classes/DE/Separable.aspx) · Paul's Online Notes · worked examples

These sites open in your browser and need the internet. Links checked 3 October 2026.
:::

Next: [Vectors](#math.p3.vectors).
