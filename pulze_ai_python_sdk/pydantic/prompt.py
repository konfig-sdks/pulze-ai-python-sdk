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


class Prompt(BaseModel):
    title: str = Field(alias='title')

    description: str = Field(alias='description')

    added_on: datetime = Field(alias='added_on')

    id: str = Field(alias='id')

    modified_on: datetime = Field(alias='modified_on')

    org_id: str = Field(alias='org_id')

    prompt: str = Field(alias='prompt')

    tokens: int = Field(alias='tokens')

    approved_on: typing.Optional[datetime] = Field(None, alias='approved_on')

    # Reason for decline
    decline_reason: typing.Optional[str] = Field(None, alias='decline_reason')

    published_on: typing.Optional[datetime] = Field(None, alias='published_on')

    reviewed_on: typing.Optional[datetime] = Field(None, alias='reviewed_on')
    class Config:
        arbitrary_types_allowed = True
