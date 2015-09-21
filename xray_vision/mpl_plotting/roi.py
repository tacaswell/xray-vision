from __future__ import absolute_import, division, print_function
import copy
import matplotlib.cm as mcm
from matplotlib.colors import LogNorm


def show_label_array(ax, label_array, cmap=None, **kwargs):
    """
    Display a labeled array nicely

    Additional kwargs are passed through to `ax.imshow`.
    If `vmin` is in kwargs, it is clipped to minimum of 0.5.

    Parameters
    ----------
    ax : Axes
        The `Axes` object to add the artist too

    label_array : ndarray
        Expected to be an unsigned integer array.  0 is background,
        positive integers label region of interest

    cmap : str or colormap, optional
        Color map to use, defaults to 'Paired'


    Returns
    -------
    img : AxesImage
        The artist added to the axes
    """
    if cmap is None:
        cmap = 'Paired'

    _cmap = copy.copy((mcm.get_cmap(cmap)))
    _cmap.set_under('w', 0)
    vmin = max(.5, kwargs.pop('vmin', .5))

    ax.set_aspect('equal')
    im = ax.imshow(label_array, cmap=cmap,
                   interpolation='nearest',
                   vmin=vmin,
                   **kwargs)

    return im


def show_label_array_on_image(ax, image, label_array, cmap=None, vmax=None,
                              **kwargs):
    """""
    This will plot the required ROI's(labeled array on the image

    Additional kwargs are passed through to `ax.imshow`.

    Parameters
    ----------
    ax : Axes
        The `Axes` object to add the artist too

    image : array
        The image array

    label_array : array
        Expected to be an unsigned integer array.  0 is background,
        positive integers label region of interest

    cmap : str or colormap, optional
        Color map to use, defaults to 'Paired'


    Returns
    -------
    im : AxesImage
        The artist added to the axes

    im_label : AxesImage
        The artist added to the axes
    """
    if cmap is None:
        cmap = 'Paired'

    _cmap = copy.copy((mcm.get_cmap(cmap)))
    _cmap.set_under('w', 0)

    if vmax is None:
        vmax = np.percentile(image, [80, 100])

    ax.set_aspect('equal')
    im = ax.imshow(image, cmap='gray', interpolation='none', norm=LogNorm(),
                   vmax=vmax, **kwargs)
    im_label = ax.imshow(label_array, cmap=cmap,  interpolation='none',
                         norm=LogNorm(), **kwargs)

    return im, im_label