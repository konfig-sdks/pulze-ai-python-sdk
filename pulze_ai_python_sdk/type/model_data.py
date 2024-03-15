# coding: utf-8

"""
    Pulze.ai API

    At Pulze it's our mission to supercharge today's workforce with AI to maximize the world's prosperity. We are doing so by enabling companies of any size to securely leverage Large Language Models (LLM) and easily build AI features into their apps. Our enterprise platform has access to all best in class LLMs and can route user requests to the most relevant model to get the highest quality response at the best price thanks to our smart meta model. End users can leverage pre-built applications, such as our Marketing AI product, or build custom apps on top of the Pulze Platform.  We are a VC Funded, early stage startup based in San Francisco.

    The version of the OpenAPI document: 0.1.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredModelData(TypedDict):
    # A description of the model
    description: str

    # A (usually 0) cost added on top of a request. Some models charge per request, not only per token
    base_cost: typing.Union[int, float]

    # The cost of a completion token, in USD
    completion_token_cost: typing.Union[int, float]

    # The max_tokens for this model
    context_window: int

    # This determines if the model will be available + pre-selected when users create new apps.
    default_active: bool

    # True if the model is of type Chat Completions, False if it's a Text Completion model.
    is_chat: bool

    # Whether it's fine-tuned or not
    is_ft: bool

    # True if the model complies with GDPR
    is_gdpr: bool

    # True if the model is open source
    is_open_source: bool

    # True if the model is publicly accessible to all
    is_public: bool

    # Model has been created and shared by Pulze.ai
    is_pulze_owner: bool

    # Whether it's rag-tuned or not
    is_rag: bool

    # The name of the model. Can belong to many providers
    model: str

    # The fully qualified (namespaced) model name
    namespace: str

    # The cost of a prompt token, in USD
    prompt_token_cost: typing.Union[int, float]

    # True if the model supports `function`/`tool` call
    supports_functions: bool

    # True if the model supports `json`-formatted responses
    supports_json: bool

    # True if the model supports `n` and `best_of` -- i.e, multiple responses
    supports_n: bool

    # True if the model supports `frequency_penalty` and `presence_penalty`
    supports_penalties: bool

    # True if the model supports streaming responses
    supports_stream: bool

    # A URL to the model's page or more informatino
    url: str

class OptionalModelData(TypedDict, total=False):
    # The user (auth0_id) who created the model
    added_by: str

    # When the model was added. Auto-populated in DB
    added_on: datetime

    # The app_id that has access to this model (if only one)
    app_id: str

    # Extra model settings inferred from namespace
    at: str

    # The ID of this model
    id: str

    # When the model was updated. Auto-populated in DB
    modified_on: datetime

    # The org_id that has acccess to this model
    org_id: str

    # The owner of the model. Sometimes, for a provider/model combination, many instances exist, trained on different data
    owner: str

    # The provider for the model.
    provider: str

    # The most recent data this model has been trained with
    until: datetime

class ModelData(RequiredModelData, OptionalModelData):
    pass