# data/crit.py: critical values for the 9700 statistical tests, computed in pure Python (no scipy).
# Use in a check script:
#   import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'data'))
#   from crit import chi2_crit, t_crit, r_crit
# chi2_crit(df, p=0.05): chi-squared critical value (upper tail p).
# t_crit(df, p=0.05): two-tailed t critical value.
# r_crit(n, p=0.05): two-tailed critical value of Pearson's r for n pairs (from t with n - 2 df).
from math import lgamma, exp, log, sqrt, pi, erf

def _simpson(f, a, b, n=2000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3

def chi2_cdf(x, df):
    # regularised lower incomplete gamma P(df/2, x/2) by its power series
    if x <= 0:
        return 0.0
    k, y = df / 2, x / 2
    term = exp(-y + k * log(y) - lgamma(k + 1))
    total, n = term, 0
    while term > 1e-15 * total:
        n += 1
        term *= y / (k + n)
        total += term
    return total

def t_cdf(x, df):
    c = exp(lgamma((df + 1) / 2) - lgamma(df / 2)) / sqrt(df * pi)
    return 0.5 + _simpson(lambda t: c * (1 + t * t / df) ** (-(df + 1) / 2), 0, x)

def _solve(f, target, lo, hi):
    for _ in range(60):
        mid = (lo + hi) / 2
        if f(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

def chi2_crit(df, p=0.05):
    return _solve(lambda x: chi2_cdf(x, df), 1 - p, 0.0, 100.0)

def t_crit(df, p=0.05):
    return _solve(lambda x: t_cdf(x, df), 1 - p / 2, 0.0, 200.0)

def r_crit(n, p=0.05):
    t = t_crit(n - 2, p)
    return t / sqrt(n - 2 + t * t)

if __name__ == '__main__':
    print('chi2 p=0.05 df1-10:', ' '.join(f'{chi2_crit(d):.2f}' for d in range(1, 11)))
    print('chi2 p=0.01 df1-5:', ' '.join(f'{chi2_crit(d, 0.01):.2f}' for d in range(1, 6)))
    print('t p=0.05 df1-30:', ' '.join(f'{t_crit(d):.2f}' for d in range(1, 31)))
    print('t p=0.01 df1-30:', ' '.join(f'{t_crit(d, 0.01):.2f}' for d in range(1, 31)))
    print('Pearson r p=0.05 n5-20:', ' '.join(f'{n}:{r_crit(n):.3f}' for n in range(5, 21)))
