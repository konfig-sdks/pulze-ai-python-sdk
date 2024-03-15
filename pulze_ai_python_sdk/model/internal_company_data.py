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


class InternalCompanyData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "creator",
            "billing_email",
            "name",
            "id",
            "email",
            "slug",
        }
        
        class properties:
            billing_email = schemas.StrSchema
            creator = schemas.StrSchema
            email = schemas.StrSchema
            id = schemas.UUIDSchema
            name = schemas.StrSchema
            slug = schemas.StrSchema
            city = schemas.StrSchema
            country = schemas.StrSchema
            hubspot_id = schemas.StrSchema
            __annotations__ = {
                "billing_email": billing_email,
                "creator": creator,
                "email": email,
                "id": id,
                "name": name,
                "slug": slug,
                "city": city,
                "country": country,
                "hubspot_id": hubspot_id,
            }
    
    creator: MetaOapg.properties.creator
    billing_email: MetaOapg.properties.billing_email
    name: MetaOapg.properties.name
    id: MetaOapg.properties.id
    email: MetaOapg.properties.email
    slug: MetaOapg.properties.slug
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billing_email"]) -> MetaOapg.properties.billing_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creator"]) -> MetaOapg.properties.creator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["slug"]) -> MetaOapg.properties.slug: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hubspot_id"]) -> MetaOapg.properties.hubspot_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["billing_email", "creator", "email", "id", "name", "slug", "city", "country", "hubspot_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billing_email"]) -> MetaOapg.properties.billing_email: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creator"]) -> MetaOapg.properties.creator: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["slug"]) -> MetaOapg.properties.slug: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> typing.Union[MetaOapg.properties.city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hubspot_id"]) -> typing.Union[MetaOapg.properties.hubspot_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["billing_email", "creator", "email", "id", "name", "slug", "city", "country", "hubspot_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        creator: typing.Union[MetaOapg.properties.creator, str, ],
        billing_email: typing.Union[MetaOapg.properties.billing_email, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, ],
        email: typing.Union[MetaOapg.properties.email, str, ],
        slug: typing.Union[MetaOapg.properties.slug, str, ],
        city: typing.Union[MetaOapg.properties.city, str, schemas.Unset] = schemas.unset,
        country: typing.Union[MetaOapg.properties.country, str, schemas.Unset] = schemas.unset,
        hubspot_id: typing.Union[MetaOapg.properties.hubspot_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InternalCompanyData':
        return super().__new__(
            cls,
            *args,
            creator=creator,
            billing_email=billing_email,
            name=name,
            id=id,
            email=email,
            slug=slug,
            city=city,
            country=country,
            hubspot_id=hubspot_id,
            _configuration=_configuration,
            **kwargs,
        )