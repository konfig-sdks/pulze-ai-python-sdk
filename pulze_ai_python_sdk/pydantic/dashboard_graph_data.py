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

from pulze_ai_python_sdk.pydantic.stats_populated_graph_result import StatsPopulatedGraphResult

class DashboardGraphData(BaseModel):
    color: str = Field(alias='color')

    data: typing.List[StatsPopulatedGraphResult] = Field(alias='data')

    id: str = Field(alias='id')

    interval: str = Field(alias='interval')

    label: str = Field(alias='label')

    max: typing.Union[int, float] = Field(alias='max')

    name: str = Field(alias='name')

    total: typing.Union[int, float] = Field(alias='total')

    cumulative: typing.Optional[bool] = Field(None, alias='cumulative')

    large: typing.Optional[bool] = Field(None, alias='large')
    class Config:
        arbitrary_types_allowed = True
