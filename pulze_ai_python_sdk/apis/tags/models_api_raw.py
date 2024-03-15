# coding: utf-8

"""
    Pulze.ai API

    At Pulze it's our mission to supercharge today's workforce with AI to maximize the world's prosperity. We are doing so by enabling companies of any size to securely leverage Large Language Models (LLM) and easily build AI features into their apps. Our enterprise platform has access to all best in class LLMs and can route user requests to the most relevant model to get the highest quality response at the best price thanks to our smart meta model. End users can leverage pre-built applications, such as our Marketing AI product, or build custom apps on top of the Pulze Platform.  We are a VC Funded, early stage startup based in San Francisco.

    The version of the OpenAPI document: 0.1.0
    Generated by: https://konfigthis.com
"""

from pulze_ai_python_sdk.paths.v1_models_all.get import GetAllModelsRaw
from pulze_ai_python_sdk.paths.v1_models_rank.post import GetRankOfBestRaw
from pulze_ai_python_sdk.paths.v1_models_active.get import ListActiveModelsRaw
from pulze_ai_python_sdk.paths.v1_models_model_id_toggle.put import ToggleModelForAppRaw


class ModelsApiRaw(
    GetAllModelsRaw,
    GetRankOfBestRaw,
    ListActiveModelsRaw,
    ToggleModelForAppRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
