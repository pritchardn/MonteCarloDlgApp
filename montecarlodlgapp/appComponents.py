"""
montecarlodlgapp appComponent module.

This is the module of montecarlodlgapp containing DALiuGE application components.
Here you put your main application classes and objects.

Typically a component project will contain multiple components and will
then result in a single EAGLE palette.

Be creative! do whatever you need to do!
"""
import logging

from dlg.drop import BarrierAppDROP
from dlg.meta import (
    dlg_batch_input,
    dlg_batch_output,
    dlg_component,
    dlg_int_param,
    dlg_streaming_input,
)

logger = logging.getLogger(__name__)

##
# @brief MyApp
# @details Template app for demonstration only!
# Replace the documentation with whatever you want/need to show in the DALiuGE
# workflow editor. The appclass parameter should contain the relative Pythonpath
# to import MyApp.
#
# @par EAGLE_START
# @param category PythonApp
# @param[in] param/appclass Application Class/montecarlodlgapp.MyApp/String/readonly/
#     \~English Import direction for application class
# @param[in] param/dummy Dummy parameter/ /String/readwrite/
#     \~English Dummy modifyable parameter
# @param[in] port/dummy Dummy in/float/
#     \~English Dummy input port
# @param[out] port/dummy Dummy out/float/
#     \~English Dummy output port
# @par EAGLE_END

# Application components can inherit from BarrierAppDROP or BranchAppDrop.
# It is also possible to inherit directly from the AbstractDROP class. Please
# refer to the Developer Guide for more information.

import random


class MonteCarloAppDrop(BarrierAppDROP):
    """A template BarrierAppDrop that doesn't do anything at all
    Add your functionality in the run method and optional additional
    methods.
    """

    compontent_meta = dlg_component(
        "MyApp",
        "My Application",
        [dlg_batch_input("binary/*", [])],
        [dlg_batch_output("binary/*", [])],
        [dlg_streaming_input("binary/*")],
    )

    numIterations = dlg_int_param("Iterations", 100)
    randomSeed = dlg_int_param("Random", 42)

    def initialize(self, **kwargs):
        random.seed(self.randomSeed)
        super(MonteCarloAppDrop, self).initialize(**kwargs)

    def run(self):
        """
        The run method is mandatory for DALiuGE application components.
        """
        inside = 0
        outside = 0
        for _ in range(self.numIterations*self.numIterations):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            origin_dist = x ** 2 + y ** 2
            if origin_dist <= 1:
                inside += 1
            else:
                outside += 1
        pi = inside/outside
        return pi
