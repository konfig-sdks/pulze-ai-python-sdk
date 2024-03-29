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

from pulze_ai_python_sdk.pydantic.tool_choice_function import ToolChoiceFunction

class ToolChoice(BaseModel):
    # The definition of the function you would like the LLM to guess the parameters for.
    function: typing.Optional[ToolChoiceFunction] = Field(None, alias='function')

    # (Note: Not supported by all models yet) // `json_object`: If you instruct the model to return a JSON object, the model will respond in a valid JSON format. || `function`: If you set this to function, you must also pass the `function` parameter with extra information. || 
    type: typing.Optional[Literal["function", "json_object"]] = Field(None, alias='type')
    class Config:
        arbitrary_types_allowed = True
