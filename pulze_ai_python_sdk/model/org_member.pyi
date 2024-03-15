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


class OrgMember(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "is_active",
            "last_login",
            "org_id",
            "permissions",
            "id",
            "auth0_id",
            "added_on",
        }
        
        class properties:
            added_on = schemas.DateTimeSchema
            auth0_id = schemas.StrSchema
            id = schemas.UUIDSchema
            is_active = schemas.BoolSchema
            last_login = schemas.DateTimeSchema
            org_id = schemas.UUIDSchema
            permissions = schemas.StrSchema
            __annotations__ = {
                "added_on": added_on,
                "auth0_id": auth0_id,
                "id": id,
                "is_active": is_active,
                "last_login": last_login,
                "org_id": org_id,
                "permissions": permissions,
            }
    
    is_active: MetaOapg.properties.is_active
    last_login: MetaOapg.properties.last_login
    org_id: MetaOapg.properties.org_id
    permissions: MetaOapg.properties.permissions
    id: MetaOapg.properties.id
    auth0_id: MetaOapg.properties.auth0_id
    added_on: MetaOapg.properties.added_on
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["added_on"]) -> MetaOapg.properties.added_on: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auth0_id"]) -> MetaOapg.properties.auth0_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_active"]) -> MetaOapg.properties.is_active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_login"]) -> MetaOapg.properties.last_login: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["org_id"]) -> MetaOapg.properties.org_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["permissions"]) -> MetaOapg.properties.permissions: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["added_on", "auth0_id", "id", "is_active", "last_login", "org_id", "permissions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["added_on"]) -> MetaOapg.properties.added_on: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auth0_id"]) -> MetaOapg.properties.auth0_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_active"]) -> MetaOapg.properties.is_active: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_login"]) -> MetaOapg.properties.last_login: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["org_id"]) -> MetaOapg.properties.org_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["permissions"]) -> MetaOapg.properties.permissions: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["added_on", "auth0_id", "id", "is_active", "last_login", "org_id", "permissions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        is_active: typing.Union[MetaOapg.properties.is_active, bool, ],
        last_login: typing.Union[MetaOapg.properties.last_login, str, datetime, ],
        org_id: typing.Union[MetaOapg.properties.org_id, str, uuid.UUID, ],
        permissions: typing.Union[MetaOapg.properties.permissions, str, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, ],
        auth0_id: typing.Union[MetaOapg.properties.auth0_id, str, ],
        added_on: typing.Union[MetaOapg.properties.added_on, str, datetime, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OrgMember':
        return super().__new__(
            cls,
            *args,
            is_active=is_active,
            last_login=last_login,
            org_id=org_id,
            permissions=permissions,
            id=id,
            auth0_id=auth0_id,
            added_on=added_on,
            _configuration=_configuration,
            **kwargs,
        )
