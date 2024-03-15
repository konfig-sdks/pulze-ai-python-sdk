# coding: utf-8

"""
    Pulze.ai API

    At Pulze it's our mission to supercharge today's workforce with AI to maximize the world's prosperity. We are doing so by enabling companies of any size to securely leverage Large Language Models (LLM) and easily build AI features into their apps. Our enterprise platform has access to all best in class LLMs and can route user requests to the most relevant model to get the highest quality response at the best price thanks to our smart meta model. End users can leverage pre-built applications, such as our Marketing AI product, or build custom apps on top of the Pulze Platform.  We are a VC Funded, early stage startup based in San Francisco.

    The version of the OpenAPI document: 0.1.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from pulze_ai_python_sdk import schemas  # noqa: F401


class SubscriptionPricingTable(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "descriptions",
            "table",
        }
        
        class properties:
        
            @staticmethod
            def table() -> typing.Type['SubscriptionPricingTableTable']:
                return SubscriptionPricingTableTable
            subscription_price_id = schemas.StrSchema
            __annotations__ = {
                "table": table,
                "subscription_price_id": subscription_price_id,
            }
    
    descriptions: schemas.AnyTypeSchema
    table: 'SubscriptionPricingTableTable'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["table"]) -> 'SubscriptionPricingTableTable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscription_price_id"]) -> MetaOapg.properties.subscription_price_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["table", "subscription_price_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["table"]) -> 'SubscriptionPricingTableTable': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscription_price_id"]) -> typing.Union[MetaOapg.properties.subscription_price_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["table", "subscription_price_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        descriptions: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        table: 'SubscriptionPricingTableTable',
        subscription_price_id: typing.Union[MetaOapg.properties.subscription_price_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SubscriptionPricingTable':
        return super().__new__(
            cls,
            *args,
            descriptions=descriptions,
            table=table,
            subscription_price_id=subscription_price_id,
            _configuration=_configuration,
            **kwargs,
        )

from pulze_ai_python_sdk.model.subscription_pricing_table_table import SubscriptionPricingTableTable
