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


class AppCustomData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "file_mime",
            "file_name",
            "data_type",
            "app_id",
        }
        
        class properties:
            app_id = schemas.UUIDSchema
            
            
            class data_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def FILE(cls):
                    return cls("file")
            file_mime = schemas.StrSchema
            file_name = schemas.StrSchema
            added_on = schemas.DateTimeSchema
            file_content = schemas.BinarySchema
            file_size = schemas.IntSchema
            id = schemas.UUIDSchema
            __annotations__ = {
                "app_id": app_id,
                "data_type": data_type,
                "file_mime": file_mime,
                "file_name": file_name,
                "added_on": added_on,
                "file_content": file_content,
                "file_size": file_size,
                "id": id,
            }
    
    file_mime: MetaOapg.properties.file_mime
    file_name: MetaOapg.properties.file_name
    data_type: MetaOapg.properties.data_type
    app_id: MetaOapg.properties.app_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["app_id"]) -> MetaOapg.properties.app_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data_type"]) -> MetaOapg.properties.data_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_mime"]) -> MetaOapg.properties.file_mime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_name"]) -> MetaOapg.properties.file_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["added_on"]) -> MetaOapg.properties.added_on: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_content"]) -> MetaOapg.properties.file_content: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_size"]) -> MetaOapg.properties.file_size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["app_id", "data_type", "file_mime", "file_name", "added_on", "file_content", "file_size", "id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["app_id"]) -> MetaOapg.properties.app_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data_type"]) -> MetaOapg.properties.data_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_mime"]) -> MetaOapg.properties.file_mime: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_name"]) -> MetaOapg.properties.file_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["added_on"]) -> typing.Union[MetaOapg.properties.added_on, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_content"]) -> typing.Union[MetaOapg.properties.file_content, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_size"]) -> typing.Union[MetaOapg.properties.file_size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["app_id", "data_type", "file_mime", "file_name", "added_on", "file_content", "file_size", "id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        file_mime: typing.Union[MetaOapg.properties.file_mime, str, ],
        file_name: typing.Union[MetaOapg.properties.file_name, str, ],
        data_type: typing.Union[MetaOapg.properties.data_type, str, ],
        app_id: typing.Union[MetaOapg.properties.app_id, str, uuid.UUID, ],
        added_on: typing.Union[MetaOapg.properties.added_on, str, datetime, schemas.Unset] = schemas.unset,
        file_content: typing.Union[MetaOapg.properties.file_content, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        file_size: typing.Union[MetaOapg.properties.file_size, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AppCustomData':
        return super().__new__(
            cls,
            *args,
            file_mime=file_mime,
            file_name=file_name,
            data_type=data_type,
            app_id=app_id,
            added_on=added_on,
            file_content=file_content,
            file_size=file_size,
            id=id,
            _configuration=_configuration,
            **kwargs,
        )
