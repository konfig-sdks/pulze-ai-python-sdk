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


class App(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "key_end",
            "is_active",
            "hashed_key",
            "description",
            "id",
            "auth0_id",
        }
        
        class properties:
            description = schemas.StrSchema
            auth0_id = schemas.StrSchema
            hashed_key = schemas.StrSchema
            id = schemas.UUIDSchema
            is_active = schemas.BoolSchema
            key_end = schemas.StrSchema
            added_on = schemas.DateTimeSchema
            modified_on = schemas.DateTimeSchema
            org_id = schemas.UUIDSchema
        
            @staticmethod
            def policies() -> typing.Type['LLMModelPolicies']:
                return LLMModelPolicies
            prompt_id = schemas.UUIDSchema
            rate_limit = schemas.IntSchema
            settings = schemas.DictSchema
        
            @staticmethod
            def weights() -> typing.Type['LLMModelWeights']:
                return LLMModelWeights
            __annotations__ = {
                "description": description,
                "auth0_id": auth0_id,
                "hashed_key": hashed_key,
                "id": id,
                "is_active": is_active,
                "key_end": key_end,
                "added_on": added_on,
                "modified_on": modified_on,
                "org_id": org_id,
                "policies": policies,
                "prompt_id": prompt_id,
                "rate_limit": rate_limit,
                "settings": settings,
                "weights": weights,
            }
    
    key_end: MetaOapg.properties.key_end
    is_active: MetaOapg.properties.is_active
    hashed_key: MetaOapg.properties.hashed_key
    description: MetaOapg.properties.description
    id: MetaOapg.properties.id
    auth0_id: MetaOapg.properties.auth0_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auth0_id"]) -> MetaOapg.properties.auth0_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hashed_key"]) -> MetaOapg.properties.hashed_key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_active"]) -> MetaOapg.properties.is_active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key_end"]) -> MetaOapg.properties.key_end: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["added_on"]) -> MetaOapg.properties.added_on: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modified_on"]) -> MetaOapg.properties.modified_on: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["org_id"]) -> MetaOapg.properties.org_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["policies"]) -> 'LLMModelPolicies': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prompt_id"]) -> MetaOapg.properties.prompt_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rate_limit"]) -> MetaOapg.properties.rate_limit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["settings"]) -> MetaOapg.properties.settings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weights"]) -> 'LLMModelWeights': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "auth0_id", "hashed_key", "id", "is_active", "key_end", "added_on", "modified_on", "org_id", "policies", "prompt_id", "rate_limit", "settings", "weights", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auth0_id"]) -> MetaOapg.properties.auth0_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hashed_key"]) -> MetaOapg.properties.hashed_key: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_active"]) -> MetaOapg.properties.is_active: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key_end"]) -> MetaOapg.properties.key_end: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["added_on"]) -> typing.Union[MetaOapg.properties.added_on, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modified_on"]) -> typing.Union[MetaOapg.properties.modified_on, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["org_id"]) -> typing.Union[MetaOapg.properties.org_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["policies"]) -> typing.Union['LLMModelPolicies', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prompt_id"]) -> typing.Union[MetaOapg.properties.prompt_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rate_limit"]) -> typing.Union[MetaOapg.properties.rate_limit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["settings"]) -> typing.Union[MetaOapg.properties.settings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weights"]) -> typing.Union['LLMModelWeights', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "auth0_id", "hashed_key", "id", "is_active", "key_end", "added_on", "modified_on", "org_id", "policies", "prompt_id", "rate_limit", "settings", "weights", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        key_end: typing.Union[MetaOapg.properties.key_end, str, ],
        is_active: typing.Union[MetaOapg.properties.is_active, bool, ],
        hashed_key: typing.Union[MetaOapg.properties.hashed_key, str, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, ],
        auth0_id: typing.Union[MetaOapg.properties.auth0_id, str, ],
        added_on: typing.Union[MetaOapg.properties.added_on, str, datetime, schemas.Unset] = schemas.unset,
        modified_on: typing.Union[MetaOapg.properties.modified_on, str, datetime, schemas.Unset] = schemas.unset,
        org_id: typing.Union[MetaOapg.properties.org_id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        policies: typing.Union['LLMModelPolicies', schemas.Unset] = schemas.unset,
        prompt_id: typing.Union[MetaOapg.properties.prompt_id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        rate_limit: typing.Union[MetaOapg.properties.rate_limit, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        settings: typing.Union[MetaOapg.properties.settings, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        weights: typing.Union['LLMModelWeights', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'App':
        return super().__new__(
            cls,
            *args,
            key_end=key_end,
            is_active=is_active,
            hashed_key=hashed_key,
            description=description,
            id=id,
            auth0_id=auth0_id,
            added_on=added_on,
            modified_on=modified_on,
            org_id=org_id,
            policies=policies,
            prompt_id=prompt_id,
            rate_limit=rate_limit,
            settings=settings,
            weights=weights,
            _configuration=_configuration,
            **kwargs,
        )

from pulze_ai_python_sdk.model.llm_model_policies import LLMModelPolicies
from pulze_ai_python_sdk.model.llm_model_weights import LLMModelWeights