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


class ModelParts(BaseModel):
    # The name of the model. Can belong to many providers
    model: str = Field(alias='model')

    # The fully qualified (namespaced) model name
    namespace: str = Field(alias='namespace')

    # Extra model settings inferred from namespace
    at: typing.Optional[str] = Field(None, alias='at')

    # The owner of the model. Sometimes, for a provider/model combination, many instances exist, trained on different data
    owner: typing.Optional[str] = Field(None, alias='owner')

    # The provider for the model.
    provider: typing.Optional[str] = Field(None, alias='provider')
    class Config:
        arbitrary_types_allowed = True
