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

from pulze_ai_python_sdk.pydantic.app import App
from pulze_ai_python_sdk.pydantic.app_custom_data import AppCustomData
from pulze_ai_python_sdk.pydantic.app_with_model_updates_info_model_settings import AppWithModelUpdatesInfoModelSettings

class AppWithModelUpdatesInfo(BaseModel):
    app: App = Field(alias='app')

    model_settings_: AppWithModelUpdatesInfoModelSettings = Field(alias='model_settings')

    # List of files associated with the app.
    files: typing.Optional[typing.List[AppCustomData]] = Field(None, alias='files')
    class Config:
        arbitrary_types_allowed = True
