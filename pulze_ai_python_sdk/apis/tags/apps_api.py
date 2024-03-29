# coding: utf-8

"""
    Pulze.ai API

    At Pulze it's our mission to supercharge today's workforce with AI to maximize the world's prosperity. We are doing so by enabling companies of any size to securely leverage Large Language Models (LLM) and easily build AI features into their apps. Our enterprise platform has access to all best in class LLMs and can route user requests to the most relevant model to get the highest quality response at the best price thanks to our smart meta model. End users can leverage pre-built applications, such as our Marketing AI product, or build custom apps on top of the Pulze Platform.  We are a VC Funded, early stage startup based in San Francisco.

    The version of the OpenAPI document: 0.1.0
    Generated by: https://konfigthis.com
"""

from pulze_ai_python_sdk.paths.v1_apps_self.get import GetAppForApiKey
from pulze_ai_python_sdk.paths.v1_apps_update.put import UpdateProperties
from pulze_ai_python_sdk.apis.tags.apps_api_raw import AppsApiRaw


class AppsApi(
    GetAppForApiKey,
    UpdateProperties,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AppsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AppsApiRaw(api_client)
