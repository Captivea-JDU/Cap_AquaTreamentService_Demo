# Copyright © 2021 Novobi, LLC
# See LICENSE file for full copyright and licensing details.

from ...restful import request_builder

from .. import resource
from ..registry import register_model
from ..request_builder import WooCommercePaginated


@register_model('product_shipping_classes')
class WooCommerceProductShippingClassModel(
    resource.WooCommerceResourceModel,
    request_builder.RestfulGet,
    request_builder.RestfulPost,
    request_builder.RestfulPut,
    request_builder.RestfulDelete,
    request_builder.RestfulList,
    WooCommercePaginated,
):
    """
    An interface of WooCommerce product shipping class
    """
    prefix = 'products/'
    path = 'shipping_classes'
    primary_key = 'id'
