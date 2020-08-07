# -*- coding: utf-8 -*-
from copy import deepcopy
from typing import List

import numpy as np

from nata.containers import ParticleDataset
from nata.plugins.register import register_container_plugin


@register_container_plugin(ParticleDataset, name="filter")
def filter_particle_dataset(
    dataset: ParticleDataset,
    mask: List[bool] = None,
    quantities: List[str] = None,
) -> ParticleDataset:
    """Filters a :class:`nata.containers.ParticleDataset` according to a\
       selection of quantities.

        Parameters
        ----------
        mask: ``np.ndarray``
            Array of booleans indicating the particles to be filtered. Particles
            with ``True`` (``False``) mask entries are selected (hidden). The
            shape of ``mask`` must match that of each particle quantity.

        quantities: ``list``
            List of quantities to be filtered, ordered by the way they should be
            sorted in the returned dataset.

        Returns
        ------
        :class:`nata.containers.ParticleDataset`:
            Filtered dataset with only the quantities selected in
            ``quantities``.

        Examples
        --------
        The filter plugin is used to get dataset with only a selection, say
        ``'x1'`` and ``'x2'``, of its quantities.

        >>> from nata.containers import ParticleDataset
        >>> ds = ParticleDataset("path/to"file")
        >>> ds_flt = ds.filter(quantities=["x1","p1"])

    """

    dataset_c = deepcopy(dataset)

    if quantities is not None:
        quants = {
            quant: dataset_c.quantities[quant]
            for quant in quantities
            if quant in dataset_c.quantities
        }
    else:
        quants = dataset_c.quantities

    if mask is not None:
        for name, quant in quants.items():
            quants[name].data[~mask] = np.ma.masked

    return ParticleDataset(
        iteration=dataset_c.axes["iteration"],
        time=dataset_c.axes["time"],
        name=dataset_c.name,
        quantities=quants,
    )
