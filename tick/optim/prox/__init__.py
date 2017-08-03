# License: BSD 3 clause

import tick.base

from .prox_zero import ProxZero
from .prox_positive import ProxPositive
from .prox_l2sq import ProxL2Sq
from .prox_l1 import ProxL1
from .prox_l1w import ProxL1w
from .prox_tv import ProxTV
from .prox_nuclear import ProxNuclear
from .prox_slope import ProxSlope
from .prox_oscar import ProxOscar
from .prox_elasticnet import ProxElasticNet
from .prox_multi import ProxMulti
from .prox_equality import ProxEquality
from .prox_binarsity import ProxBinarsity


__all__ = ["ProxZero",
           "ProxPositive",
           "ProxL1",
           "ProxL1w",
           "ProxL2Sq",
           "ProxTV",
           "ProxNuclear",
           "ProxSlope",
           "ProxOscar",
           "ProxElasticNet",
           "ProxMulti",
           "ProxEquality",
           "ProxBinarsity"]
