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


class FunctionParameters(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "properties",
        }
        
        class properties:
        
            @staticmethod
            def properties() -> typing.Type['FunctionParametersProperties']:
                return FunctionParametersProperties
        
            @staticmethod
            def required() -> typing.Type['FunctionParametersRequired']:
                return FunctionParametersRequired
            type = schemas.StrSchema
            __annotations__ = {
                "properties": properties,
                "required": required,
                "type": type,
            }
    
    properties: 'FunctionParametersProperties'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["properties"]) -> 'FunctionParametersProperties': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["required"]) -> 'FunctionParametersRequired': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["properties", "required", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["properties"]) -> 'FunctionParametersProperties': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["required"]) -> typing.Union['FunctionParametersRequired', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["properties", "required", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        properties: 'FunctionParametersProperties',
        required: typing.Union['FunctionParametersRequired', schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FunctionParameters':
        return super().__new__(
            cls,
            *args,
            properties=properties,
            required=required,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from pulze_ai_python_sdk.model.function_parameters_properties import FunctionParametersProperties
from pulze_ai_python_sdk.model.function_parameters_required import FunctionParametersRequired
