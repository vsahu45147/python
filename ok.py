import colorsys
from gettext import npgettext


def draw_ellipses(gmm, ax):
    for n, color in enumerate(colorsys):
        covariances = gmm.covariances_[n] [:2, :2]
        v, w = npgettext.linalg.eigh(covariances)
        u = w[0] / np.linalg.norm(w[0])
        