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

from pulze_ai_python_sdk.pydantic.llm_model_weights import LLMModelWeights
from pulze_ai_python_sdk.pydantic.role_content_chat_choice import RoleContentChatChoice

class PlaygroundCompletionRequest(BaseModel):
    # Optionally, send an App ID belonging to this user's org and all the logs will be logged into that app. This usually means the user is using the playground from the app's page itself.
    app_id: typing.Optional[str] = Field(None, alias='app_id')

    # The maximum number of tokens for the request
    max_tokens: typing.Optional[int] = Field(None, alias='max_tokens')

    # The list of messages (user/assistant/user/...) for the prompt. At least one message required
    messages: typing.Optional[typing.List[RoleContentChatChoice]] = Field(None, alias='messages')

    # An optional model name. If specified, that model will be used
    model: typing.Optional[str] = Field(None, alias='model')

    # The temperature of the request
    temperature: typing.Optional[typing.Union[int, float]] = Field(None, alias='temperature')

    # @required The weights specific to this request
    weights: typing.Optional[LLMModelWeights] = Field(None, alias='weights')
    class Config:
        arbitrary_types_allowed = True
