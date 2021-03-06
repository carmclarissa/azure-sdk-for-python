# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ResourceSku
    from ._models_py3 import ResourceSkuCapabilities
    from ._models_py3 import ResourceSkuCapacity
    from ._models_py3 import ResourceSkuCosts
    from ._models_py3 import ResourceSkuLocationInfo
    from ._models_py3 import ResourceSkuRestrictionInfo
    from ._models_py3 import ResourceSkuRestrictions
    from ._models_py3 import ResourceSkusResult
except (SyntaxError, ImportError):
    from ._models import ResourceSku  # type: ignore
    from ._models import ResourceSkuCapabilities  # type: ignore
    from ._models import ResourceSkuCapacity  # type: ignore
    from ._models import ResourceSkuCosts  # type: ignore
    from ._models import ResourceSkuLocationInfo  # type: ignore
    from ._models import ResourceSkuRestrictionInfo  # type: ignore
    from ._models import ResourceSkuRestrictions  # type: ignore
    from ._models import ResourceSkusResult  # type: ignore

from ._compute_management_client_enums import (
    ResourceSkuCapacityScaleType,
    ResourceSkuRestrictionsReasonCode,
    ResourceSkuRestrictionsType,
)

__all__ = [
    'ResourceSku',
    'ResourceSkuCapabilities',
    'ResourceSkuCapacity',
    'ResourceSkuCosts',
    'ResourceSkuLocationInfo',
    'ResourceSkuRestrictionInfo',
    'ResourceSkuRestrictions',
    'ResourceSkusResult',
    'ResourceSkuCapacityScaleType',
    'ResourceSkuRestrictionsReasonCode',
    'ResourceSkuRestrictionsType',
]
