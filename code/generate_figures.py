import math
import numpy as np
import matplotlib.pyplot as plt


def quantities(n, a=10, mM=2, mMR=2, mD=2, phi=0.8):
    qII = (a - mM) / (2 - n)
    denom = 3 - n * (1 + phi)
    qMR = (a + mD - 2 * mMR + n * phi * (mMR - mD)) / denom
    qDR = (a + mMR - 2 * mD + n * (mD - mMR)) / denom
    QR = qMR + qDR
    return qII, qMR, qDR, QR


def welfare(n, a=10, mM=2, mMR=2, mD=2, phi=0.8, K=30, tauM=0, tauR=0):
    qII, qMR, qDR, QR = quantities(n, a, mM, mMR, mD, phi)
    swii = 0.5 * qII**2 + tauM * qII
    swr = 0.5 * QR**2 + tauR * qMR + qDR**2 - K
    return swii, swr, swr - swii


def bisect_root(f, lo=0.0, hi=0.999999, tol=1e-10, max_iter=200):
    flo = f(lo)
    fhi = f(hi)
    if flo >= 0:
        return 0.0
    if fhi <= 0:
        return math.nan
    for _ in range(max_iter):
        mid = (lo + hi) / 2
        fm = f(mid)
        if abs(fm) < tol or (hi - lo) < tol:
            return mid
        if flo * fm <= 0:
            hi = mid
            fhi = fm
        else:
            lo = mid
            flo = fm
    return (lo + hi) / 2


def threshold(a=10, mM=2, mMR=2, mD=2, phi=0.8, K=30):
    return bisect_root(lambda n: welfare(n, a, mM, mMR, mD, phi, K)[2])


def main():
    n_grid = np.linspace(0, 0.999, 500)
    swii_vals = []
    swr_vals = []
    delta_vals = []

    for n in n_grid:
        swii, swr, delta = welfare(n)
        swii_vals.append(swii)
        swr_vals.append(swr)
        delta_vals.append(delta)

    n_star = threshold()

    plt.figure()
    plt.plot(n_grid, swii_vals, label='Unconditional clearance')
    plt.plot(n_grid, swr_vals, label='Access remedy')
    plt.axvline(n_star, linestyle='--', label=f'Threshold n* = {n_star:.3f}')
    plt.xlabel('Network effect parameter n')
    plt.ylabel('Home welfare')
    plt.legend()
    plt.tight_layout()
    plt.savefig('../figures/figure_1_welfare_comparison.pdf')
    plt.close()

    plt.figure()
    plt.plot(n_grid, delta_vals, label='SW_R - SW_II')
    plt.axhline(0, linestyle='--')
    plt.axvline(n_star, linestyle='--', label=f'Threshold n* = {n_star:.3f}')
    plt.xlabel('Network effect parameter n')
    plt.ylabel('Welfare difference')
    plt.legend()
    plt.tight_layout()
    plt.savefig('../figures/figure_2_welfare_difference.pdf')
    plt.close()

    phi_values = np.linspace(0.3, 1.0, 50)
    threshold_phi = [threshold(phi=phi) for phi in phi_values]

    plt.figure()
    plt.plot(phi_values, threshold_phi)
    plt.xlabel('Access quality phi')
    plt.ylabel('Threshold n*')
    plt.tight_layout()
    plt.savefig('../figures/figure_3_access_quality_threshold.pdf')
    plt.close()

    mD_values = np.linspace(2.0, 4.0, 50)
    threshold_mD = [threshold(mD=mD) for mD in mD_values]

    plt.figure()
    plt.plot(mD_values, threshold_mD)
    plt.xlabel('Entrant effective marginal cost m_D')
    plt.ylabel('Threshold n*')
    plt.tight_layout()
    plt.savefig('../figures/figure_4_entrant_cost_threshold.pdf')
    plt.close()

    print(f'Baseline threshold n* = {n_star:.6f}')


if __name__ == '__main__':
    main()
