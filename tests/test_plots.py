# -*- coding: utf-8 -*-
import numpy as np
from pytest import fixture

from nata.containers import GridDataset
from nata.plots.axes import Axes
from nata.plots.figure import Figure
from nata.plots.types import BasePlot
from nata.plots.types import DefaultGridPlotTypes


@fixture(name="SampleGridDataset")
def _sample_grid_dataset():
    def grid_dataset(niters: int = 1, grid_shape: tuple = (10,)):
        arr = np.random.random_sample(grid_shape)
        ds = GridDataset.from_array(arr)
        return ds

    return grid_dataset


def test_default_grid_plot_types(SampleGridDataset):

    for i, grid_shape in enumerate([(10,), (2, 5,)]):
        ds = SampleGridDataset(grid_shape=grid_shape)

        fig = ds.plot()
        assert isinstance(fig, Figure)

        axes = next(iter(fig.axes.values()))
        assert isinstance(axes, Axes)

        plot = next(iter(axes.plots))
        assert isinstance(plot, BasePlot)
        assert isinstance(plot, DefaultGridPlotTypes[i + 1])


def test_invalid_grid_plot_dims():
    pass


def test_default_particle_plot_types():
    pass


def test_invalid_particle_plot_quants():
    pass


def test_PlotPlan_init():
    pass


def test_AxesPlan_init():
    pass


def test_FigurePlan_init():
    pass


def test_Axes_default_init():
    pass


def test_Figure_default_init():
    pass


def test_LinePlot_default_init():
    pass


def test_mpl_LinePlot_default_init():
    pass


def test_ColorPlot_default_init():
    pass


def test_mpl_ColorPlot_default_init():
    pass


def test_ScatterPlot_default_init():
    pass


def test_mpl_ScatterPlot_default_init():
    pass


# test default particle plot types
