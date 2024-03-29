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
from pydantic import BaseModel, Field, RootModel

from pulze_ai_python_sdk.pydantic.pulze_engine_response_metadata import PulzeEngineResponseMetadata
from pulze_ai_python_sdk.pydantic.pulze_engine_tokens import PulzeEngineTokens
from pulze_ai_python_sdk.pydantic.response_completion_chat_choice import ResponseCompletionChatChoice
from pulze_ai_python_sdk.pydantic.response_completion_choice import ResponseCompletionChoice

class PulzeEngineResponse(BaseModel):
    # The fully qualified model name used by PulzeEngine
    model: str = Field(alias='model')

    # The type of response object
    object: Literal["text_completion", "chat.completion"] = Field(alias='object')

    # The Response contains a list of choices. The role: *.message.role, and the content: *.message.content or, for text completions, the *.text attribute.
    choices: typing.Optional[typing.Union[typing.List[ResponseCompletionChatChoice], typing.List[ResponseCompletionChoice]]] = Field(None, alias='choices')

    # Creation timestamp
    created: typing.Optional[int] = Field(None, alias='created')

    # This ID gets generated by the database when we save the request
    id: typing.Optional[str] = Field(None, alias='id')

    # Metadata of the response
    metadata: typing.Optional[PulzeEngineResponseMetadata] = Field(None, alias='metadata')

    # Tokens used
    usage: typing.Optional[PulzeEngineTokens] = Field(None, alias='usage')
    class Config:
        arbitrary_types_allowed = True
