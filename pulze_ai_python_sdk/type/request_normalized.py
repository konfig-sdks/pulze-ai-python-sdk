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

from pulze_ai_python_sdk.type.pulze_completion_request import PulzeCompletionRequest
from pulze_ai_python_sdk.type.pulze_engine_response import PulzeEngineResponse
from pulze_ai_python_sdk.type.request_in_db_base import RequestInDBBase

class RequiredRequestNormalized(TypedDict):
    # Number of tokens the response used
    completion_tokens: int

    # Cost (in $) of the response
    completion_tokens_cost: typing.Union[int, float]

    # Cost (in $) saved in the completion costs comparison to the benchmark model
    completion_tokens_cost_savings: typing.Union[int, float]

    # ID of the request
    id: str

    # The name of the model. Can belong to many providers
    model: str

    # The ID of the model used
    model_id: str

    # Number of tokens the request used
    prompt_tokens: int

    # Cost (in $) of the prompt
    prompt_tokens_cost: typing.Union[int, float]

    # Cost (in $) saved in the prompt costs comparison to the benchmark model
    prompt_tokens_cost_savings: typing.Union[int, float]

    # The response object
    response: PulzeEngineResponse

    # The timestamp of the request, in milliseconds
    timestamp: int

    # Number of tokens of (request + response)
    total_tokens: int

    # Cost (in $) of the (request + response)
    total_tokens_cost: typing.Union[int, float]

    # Cost (in $) saved in total, in comparison to the benchmark model
    total_tokens_cost_savings: typing.Union[int, float]

class OptionalRequestNormalized(TypedDict, total=False):
    # The ID of the app that performed the request
    app_id: str

    # Extra model settings inferred from namespace
    at: str

    # The children of the Request. Will equal None unless you use eager loading in the query
    children: typing.List[RequestInDBBase]

    # When a request requires multiple intermediate calls, they are stored as 'no costs incurred' -- that way we can store the costs, but don't charge the user
    costs_incurred: bool

    # When the request was performed
    created: datetime

    # A free text providing more detailed feedback
    feedback: str

    # The rating for the request
    good_answer: bool

    # Time it took for the LLM to respond
    latency: typing.Union[int, float]

    # The name of the provider's model which was used to answer the request
    namespace: str

    # The owner of the model. Sometimes, for a provider/model combination, many instances exist, trained on different data
    owner: str

    # The parent of the Request, if any. Requests which are part of a series of sub-requests (like multiple LLM calls, or RAG) will have the final, resulting Log as parent.
    parent: RequestInDBBase

    # Reference to the ID of the parent of this log. A log has a parent when it's a subrequest used to retrieve the final answer.
    parent_id: str

    # The payload sent with the request
    payload: PulzeCompletionRequest

    # How much is logged? 1: everything, 2: mask request+response (but show log), 3: Not visible, not retrievable, no information stored.
    privacy_level: int

    # The prompt in text format
    prompt: str

    # The provider for the model.
    provider: str

    # The type of request (text completion or chat) the user sends and expects back
    request_type: str

    # The response in text format
    response_text: str

    # The status code of the request to the AI model
    status_code: int

class RequestNormalized(RequiredRequestNormalized, OptionalRequestNormalized):
    pass
