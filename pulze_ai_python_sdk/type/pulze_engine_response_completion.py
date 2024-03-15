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

from pulze_ai_python_sdk.type.pulze_engine_response_metadata import PulzeEngineResponseMetadata
from pulze_ai_python_sdk.type.pulze_engine_tokens import PulzeEngineTokens
from pulze_ai_python_sdk.type.response_completion_choice import ResponseCompletionChoice

class RequiredPulzeEngineResponseCompletion(TypedDict):
    choices: typing.List[ResponseCompletionChoice]

    # The fully qualified model name used by PulzeEngine
    model: str

    # The type of response object
    object: str

class OptionalPulzeEngineResponseCompletion(TypedDict, total=False):
    # Creation timestamp
    created: int

    # This ID gets generated by the database when we save the request
    id: str

    # Metadata of the response
    metadata: PulzeEngineResponseMetadata

    # Tokens used
    usage: PulzeEngineTokens

class PulzeEngineResponseCompletion(RequiredPulzeEngineResponseCompletion, OptionalPulzeEngineResponseCompletion):
    pass
