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


class BillingTransactionItem(BaseModel):
    amount: typing.Union[int, typing.Union[int, float]] = Field(alias='amount')

    created: typing.Union[int, datetime] = Field(alias='created')

    currency: Literal["USD"] = Field(alias='currency')

    id: str = Field(alias='id')

    type: str = Field(alias='type')

    description: typing.Optional[str] = Field(None, alias='description')

    balance: typing.Optional[typing.Union[int, typing.Union[int, float]]] = Field(None, alias='balance')

    invoice_status: typing.Optional[str] = Field(None, alias='invoice_status')

    link: typing.Optional[str] = Field(None, alias='link')

    link_pdf: typing.Optional[str] = Field(None, alias='link_pdf')

    metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='metadata')
    class Config:
        arbitrary_types_allowed = True