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


class PulzeEngineResponseCompletion(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The response returned to the user by the (text) Completions endpoint
    """


    class MetaOapg:
        required = {
            "model",
            "choices",
            "object",
        }
        
        class properties:
            
            
            class choices(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ResponseCompletionChoice']:
                        return ResponseCompletionChoice
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ResponseCompletionChoice'], typing.List['ResponseCompletionChoice']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'choices':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ResponseCompletionChoice':
                    return super().__getitem__(i)
            model = schemas.StrSchema
            
            
            class object(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def TEXT_COMPLETION(cls):
                    return cls("text_completion")
                
                @schemas.classproperty
                def CHAT_COMPLETION(cls):
                    return cls("chat.completion")
            created = schemas.IntSchema
            id = schemas.StrSchema
        
            @staticmethod
            def metadata() -> typing.Type['PulzeEngineResponseMetadata']:
                return PulzeEngineResponseMetadata
        
            @staticmethod
            def usage() -> typing.Type['PulzeEngineTokens']:
                return PulzeEngineTokens
            __annotations__ = {
                "choices": choices,
                "model": model,
                "object": object,
                "created": created,
                "id": id,
                "metadata": metadata,
                "usage": usage,
            }
    
    model: MetaOapg.properties.model
    choices: MetaOapg.properties.choices
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["choices"]) -> MetaOapg.properties.choices: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model"]) -> MetaOapg.properties.model: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'PulzeEngineResponseMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["usage"]) -> 'PulzeEngineTokens': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["choices", "model", "object", "created", "id", "metadata", "usage", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["choices"]) -> MetaOapg.properties.choices: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model"]) -> MetaOapg.properties.model: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> typing.Union[MetaOapg.properties.created, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['PulzeEngineResponseMetadata', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["usage"]) -> typing.Union['PulzeEngineTokens', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["choices", "model", "object", "created", "id", "metadata", "usage", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        model: typing.Union[MetaOapg.properties.model, str, ],
        choices: typing.Union[MetaOapg.properties.choices, list, tuple, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        created: typing.Union[MetaOapg.properties.created, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union['PulzeEngineResponseMetadata', schemas.Unset] = schemas.unset,
        usage: typing.Union['PulzeEngineTokens', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PulzeEngineResponseCompletion':
        return super().__new__(
            cls,
            *args,
            model=model,
            choices=choices,
            object=object,
            created=created,
            id=id,
            metadata=metadata,
            usage=usage,
            _configuration=_configuration,
            **kwargs,
        )

from pulze_ai_python_sdk.model.pulze_engine_response_metadata import PulzeEngineResponseMetadata
from pulze_ai_python_sdk.model.pulze_engine_tokens import PulzeEngineTokens
from pulze_ai_python_sdk.model.response_completion_choice import ResponseCompletionChoice
