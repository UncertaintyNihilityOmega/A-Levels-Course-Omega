# data/titration_model.py: the titration-curve model used by widgets/chem-titration.js and by the chapter checks.
# Charge balance  [H+] + [Na+ or BH+] = [OH-] + [A-],  solved for [H+] by bisection on log10([H+]).
from math import log10, sqrt
KW = 1.00e-14
PKA_DEFAULT = 4.76          # weak acid, like ethanoic acid
PKB_WEAK_BASE = 4.75        # weak base, like ammonia

def ph_at(vb, acid_strong=True, base_strong=True, ca=0.100, va=25.0, cb=0.100, pka=PKA_DEFAULT, pkb=PKB_WEAK_BASE):
    """pH after vb cm3 of base (conc cb) has been added to va cm3 of acid (conc ca)."""
    V = (va + vb) / 1000.0
    ta = ca * va / 1000.0 / V          # total acid concentration after mixing
    tb = cb * vb / 1000.0 / V          # total base concentration after mixing
    Ka = 10 ** (-pka)
    KaBH = KW / 10 ** (-pkb)           # Ka of the conjugate acid of the weak base
    def f(lh):
        h = 10 ** lh
        a = ta if acid_strong else ta * Ka / (Ka + h)
        b = tb if base_strong else tb * h / (h + KaBH)
        return h + b - KW / h - a
    lo, hi = -16.0, 2.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(mid) > 0: hi = mid
        else: lo = mid
    return -(lo + hi) / 2

def veq(ca=0.100, va=25.0, cb=0.100): return ca * va / cb
