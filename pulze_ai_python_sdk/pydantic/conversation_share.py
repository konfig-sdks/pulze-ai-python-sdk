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


class ConversationShare(BaseModel):
    # A title for this conversation
    title: str = Field(alias='title')

    # The HASH that was shared. Used to fetch all the conversation items
    share_hash: str = Field(alias='share_hash')

    # Some extra information, like when was the conversation shared
    shared_on: datetime = Field(alias='shared_on')

    # The Auth0-ID of the user that shared this. Could be used by a user to share a conversation between their different organizations (as long as they open it themselves)
    auth0_id: typing.Optional[str] = Field(None, alias='auth0_id')

    # Will be used for analytics. We can know from which conversation this was shared.
    continuation_of: typing.Optional[str] = Field(None, alias='continuation_of')

    # To avoid creating duplicated shared links, we use this value as a quick way to verify that we are receiving new IDs
    hashed_ids: typing.Optional[str] = Field(None, alias='hashed_ids')

    # Whether the conversation is shared publicly or only members of your organization
    is_public: typing.Optional[bool] = Field(None, alias='is_public')

    # The organization that shared this. Important, as it can be used to filter users belonging to different organizations
    org_id: typing.Optional[str] = Field(None, alias='org_id')
    class Config:
        arbitrary_types_allowed = True
