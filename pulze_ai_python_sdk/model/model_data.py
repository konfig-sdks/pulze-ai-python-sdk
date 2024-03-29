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


class ModelData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "is_gdpr",
            "prompt_token_cost",
            "is_pulze_owner",
            "completion_token_cost",
            "base_cost",
            "supports_json",
            "description",
            "is_rag",
            "url",
            "supports_penalties",
            "is_open_source",
            "is_public",
            "namespace",
            "is_chat",
            "supports_functions",
            "model",
            "supports_n",
            "context_window",
            "is_ft",
            "supports_stream",
            "default_active",
        }
        
        class properties:
            description = schemas.StrSchema
            base_cost = schemas.NumberSchema
            completion_token_cost = schemas.NumberSchema
            context_window = schemas.IntSchema
            default_active = schemas.BoolSchema
            is_chat = schemas.BoolSchema
            is_ft = schemas.BoolSchema
            is_gdpr = schemas.BoolSchema
            is_open_source = schemas.BoolSchema
            is_public = schemas.BoolSchema
            is_pulze_owner = schemas.BoolSchema
            is_rag = schemas.BoolSchema
            model = schemas.StrSchema
            namespace = schemas.StrSchema
            prompt_token_cost = schemas.NumberSchema
            supports_functions = schemas.BoolSchema
            supports_json = schemas.BoolSchema
            supports_n = schemas.BoolSchema
            supports_penalties = schemas.BoolSchema
            supports_stream = schemas.BoolSchema
            url = schemas.StrSchema
            added_by = schemas.StrSchema
            added_on = schemas.DateTimeSchema
            app_id = schemas.UUIDSchema
            at = schemas.StrSchema
            id = schemas.UUIDSchema
            modified_on = schemas.DateTimeSchema
            org_id = schemas.UUIDSchema
            owner = schemas.StrSchema
            provider = schemas.StrSchema
            until = schemas.DateTimeSchema
            __annotations__ = {
                "description": description,
                "base_cost": base_cost,
                "completion_token_cost": completion_token_cost,
                "context_window": context_window,
                "default_active": default_active,
                "is_chat": is_chat,
                "is_ft": is_ft,
                "is_gdpr": is_gdpr,
                "is_open_source": is_open_source,
                "is_public": is_public,
                "is_pulze_owner": is_pulze_owner,
                "is_rag": is_rag,
                "model": model,
                "namespace": namespace,
                "prompt_token_cost": prompt_token_cost,
                "supports_functions": supports_functions,
                "supports_json": supports_json,
                "supports_n": supports_n,
                "supports_penalties": supports_penalties,
                "supports_stream": supports_stream,
                "url": url,
                "added_by": added_by,
                "added_on": added_on,
                "app_id": app_id,
                "at": at,
                "id": id,
                "modified_on": modified_on,
                "org_id": org_id,
                "owner": owner,
                "provider": provider,
                "until": until,
            }
    
    is_gdpr: MetaOapg.properties.is_gdpr
    prompt_token_cost: MetaOapg.properties.prompt_token_cost
    is_pulze_owner: MetaOapg.properties.is_pulze_owner
    completion_token_cost: MetaOapg.properties.completion_token_cost
    base_cost: MetaOapg.properties.base_cost
    supports_json: MetaOapg.properties.supports_json
    description: MetaOapg.properties.description
    is_rag: MetaOapg.properties.is_rag
    url: MetaOapg.properties.url
    supports_penalties: MetaOapg.properties.supports_penalties
    is_open_source: MetaOapg.properties.is_open_source
    is_public: MetaOapg.properties.is_public
    namespace: MetaOapg.properties.namespace
    is_chat: MetaOapg.properties.is_chat
    supports_functions: MetaOapg.properties.supports_functions
    model: MetaOapg.properties.model
    supports_n: MetaOapg.properties.supports_n
    context_window: MetaOapg.properties.context_window
    is_ft: MetaOapg.properties.is_ft
    supports_stream: MetaOapg.properties.supports_stream
    default_active: MetaOapg.properties.default_active
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["base_cost"]) -> MetaOapg.properties.base_cost: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["completion_token_cost"]) -> MetaOapg.properties.completion_token_cost: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["context_window"]) -> MetaOapg.properties.context_window: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default_active"]) -> MetaOapg.properties.default_active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_chat"]) -> MetaOapg.properties.is_chat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_ft"]) -> MetaOapg.properties.is_ft: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_gdpr"]) -> MetaOapg.properties.is_gdpr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_open_source"]) -> MetaOapg.properties.is_open_source: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_public"]) -> MetaOapg.properties.is_public: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_pulze_owner"]) -> MetaOapg.properties.is_pulze_owner: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_rag"]) -> MetaOapg.properties.is_rag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model"]) -> MetaOapg.properties.model: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["namespace"]) -> MetaOapg.properties.namespace: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prompt_token_cost"]) -> MetaOapg.properties.prompt_token_cost: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supports_functions"]) -> MetaOapg.properties.supports_functions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supports_json"]) -> MetaOapg.properties.supports_json: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supports_n"]) -> MetaOapg.properties.supports_n: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supports_penalties"]) -> MetaOapg.properties.supports_penalties: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supports_stream"]) -> MetaOapg.properties.supports_stream: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["added_by"]) -> MetaOapg.properties.added_by: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["added_on"]) -> MetaOapg.properties.added_on: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["app_id"]) -> MetaOapg.properties.app_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["at"]) -> MetaOapg.properties.at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modified_on"]) -> MetaOapg.properties.modified_on: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["org_id"]) -> MetaOapg.properties.org_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner"]) -> MetaOapg.properties.owner: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider"]) -> MetaOapg.properties.provider: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["until"]) -> MetaOapg.properties.until: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "base_cost", "completion_token_cost", "context_window", "default_active", "is_chat", "is_ft", "is_gdpr", "is_open_source", "is_public", "is_pulze_owner", "is_rag", "model", "namespace", "prompt_token_cost", "supports_functions", "supports_json", "supports_n", "supports_penalties", "supports_stream", "url", "added_by", "added_on", "app_id", "at", "id", "modified_on", "org_id", "owner", "provider", "until", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["base_cost"]) -> MetaOapg.properties.base_cost: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["completion_token_cost"]) -> MetaOapg.properties.completion_token_cost: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["context_window"]) -> MetaOapg.properties.context_window: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default_active"]) -> MetaOapg.properties.default_active: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_chat"]) -> MetaOapg.properties.is_chat: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_ft"]) -> MetaOapg.properties.is_ft: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_gdpr"]) -> MetaOapg.properties.is_gdpr: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_open_source"]) -> MetaOapg.properties.is_open_source: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_public"]) -> MetaOapg.properties.is_public: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_pulze_owner"]) -> MetaOapg.properties.is_pulze_owner: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_rag"]) -> MetaOapg.properties.is_rag: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model"]) -> MetaOapg.properties.model: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["namespace"]) -> MetaOapg.properties.namespace: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prompt_token_cost"]) -> MetaOapg.properties.prompt_token_cost: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supports_functions"]) -> MetaOapg.properties.supports_functions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supports_json"]) -> MetaOapg.properties.supports_json: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supports_n"]) -> MetaOapg.properties.supports_n: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supports_penalties"]) -> MetaOapg.properties.supports_penalties: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supports_stream"]) -> MetaOapg.properties.supports_stream: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["added_by"]) -> typing.Union[MetaOapg.properties.added_by, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["added_on"]) -> typing.Union[MetaOapg.properties.added_on, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["app_id"]) -> typing.Union[MetaOapg.properties.app_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["at"]) -> typing.Union[MetaOapg.properties.at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modified_on"]) -> typing.Union[MetaOapg.properties.modified_on, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["org_id"]) -> typing.Union[MetaOapg.properties.org_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner"]) -> typing.Union[MetaOapg.properties.owner, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider"]) -> typing.Union[MetaOapg.properties.provider, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["until"]) -> typing.Union[MetaOapg.properties.until, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "base_cost", "completion_token_cost", "context_window", "default_active", "is_chat", "is_ft", "is_gdpr", "is_open_source", "is_public", "is_pulze_owner", "is_rag", "model", "namespace", "prompt_token_cost", "supports_functions", "supports_json", "supports_n", "supports_penalties", "supports_stream", "url", "added_by", "added_on", "app_id", "at", "id", "modified_on", "org_id", "owner", "provider", "until", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        is_gdpr: typing.Union[MetaOapg.properties.is_gdpr, bool, ],
        prompt_token_cost: typing.Union[MetaOapg.properties.prompt_token_cost, decimal.Decimal, int, float, ],
        is_pulze_owner: typing.Union[MetaOapg.properties.is_pulze_owner, bool, ],
        completion_token_cost: typing.Union[MetaOapg.properties.completion_token_cost, decimal.Decimal, int, float, ],
        base_cost: typing.Union[MetaOapg.properties.base_cost, decimal.Decimal, int, float, ],
        supports_json: typing.Union[MetaOapg.properties.supports_json, bool, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        is_rag: typing.Union[MetaOapg.properties.is_rag, bool, ],
        url: typing.Union[MetaOapg.properties.url, str, ],
        supports_penalties: typing.Union[MetaOapg.properties.supports_penalties, bool, ],
        is_open_source: typing.Union[MetaOapg.properties.is_open_source, bool, ],
        is_public: typing.Union[MetaOapg.properties.is_public, bool, ],
        namespace: typing.Union[MetaOapg.properties.namespace, str, ],
        is_chat: typing.Union[MetaOapg.properties.is_chat, bool, ],
        supports_functions: typing.Union[MetaOapg.properties.supports_functions, bool, ],
        model: typing.Union[MetaOapg.properties.model, str, ],
        supports_n: typing.Union[MetaOapg.properties.supports_n, bool, ],
        context_window: typing.Union[MetaOapg.properties.context_window, decimal.Decimal, int, ],
        is_ft: typing.Union[MetaOapg.properties.is_ft, bool, ],
        supports_stream: typing.Union[MetaOapg.properties.supports_stream, bool, ],
        default_active: typing.Union[MetaOapg.properties.default_active, bool, ],
        added_by: typing.Union[MetaOapg.properties.added_by, str, schemas.Unset] = schemas.unset,
        added_on: typing.Union[MetaOapg.properties.added_on, str, datetime, schemas.Unset] = schemas.unset,
        app_id: typing.Union[MetaOapg.properties.app_id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        at: typing.Union[MetaOapg.properties.at, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        modified_on: typing.Union[MetaOapg.properties.modified_on, str, datetime, schemas.Unset] = schemas.unset,
        org_id: typing.Union[MetaOapg.properties.org_id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        owner: typing.Union[MetaOapg.properties.owner, str, schemas.Unset] = schemas.unset,
        provider: typing.Union[MetaOapg.properties.provider, str, schemas.Unset] = schemas.unset,
        until: typing.Union[MetaOapg.properties.until, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ModelData':
        return super().__new__(
            cls,
            *args,
            is_gdpr=is_gdpr,
            prompt_token_cost=prompt_token_cost,
            is_pulze_owner=is_pulze_owner,
            completion_token_cost=completion_token_cost,
            base_cost=base_cost,
            supports_json=supports_json,
            description=description,
            is_rag=is_rag,
            url=url,
            supports_penalties=supports_penalties,
            is_open_source=is_open_source,
            is_public=is_public,
            namespace=namespace,
            is_chat=is_chat,
            supports_functions=supports_functions,
            model=model,
            supports_n=supports_n,
            context_window=context_window,
            is_ft=is_ft,
            supports_stream=supports_stream,
            default_active=default_active,
            added_by=added_by,
            added_on=added_on,
            app_id=app_id,
            at=at,
            id=id,
            modified_on=modified_on,
            org_id=org_id,
            owner=owner,
            provider=provider,
            until=until,
            _configuration=_configuration,
            **kwargs,
        )
