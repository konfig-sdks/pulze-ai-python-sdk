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


class RequiredPaymentDetailsBalance(TypedDict):
    # The Zipcode of the address of the Organization
    billing_zip: str

    # The datetime when the local balance (i.e. the value we keep track of) was synced with stripe (and the customer was billed)
    last_sync: datetime

class OptionalPaymentDetailsBalance(TypedDict, total=False):
    # The balance in the account. Synced with Stripe periodically
    balance: typing.Union[int, float]

    # This represents balance that's either gifted or earned, and non-redeemable for any cash.
    free_balance: typing.Union[int, float]

    # The usage your account had since it last synced with Stripe. Used for reference purposes, this is the amount we will charge Stripe for.  This value does not only contain the sum of all the log tokens, but it might also contain other expenses, like uptime for custom models or base subscription prices, premium features, etc (all of this might come in the future) 
    pending_expense: typing.Union[int, float]

    # When the balance crosses this value, a high-warning email will be sent informing the customer that services will be disrupted if the balance reaches 0
    spending_limit_hard: typing.Union[int, float]

    # When the balance crosses this value, a warning email will be sent informing the customer
    spending_limit_soft: typing.Union[int, float]

class PaymentDetailsBalance(RequiredPaymentDetailsBalance, OptionalPaymentDetailsBalance):
    pass
