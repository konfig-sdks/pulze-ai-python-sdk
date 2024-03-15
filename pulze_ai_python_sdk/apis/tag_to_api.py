import typing_extensions

from pulze_ai_python_sdk.apis.tags import TagValues
from pulze_ai_python_sdk.apis.tags.models_api import ModelsApi
from pulze_ai_python_sdk.apis.tags.logs_api import LogsApi
from pulze_ai_python_sdk.apis.tags.apps_api import AppsApi
from pulze_ai_python_sdk.apis.tags.chat_api import ChatApi
from pulze_ai_python_sdk.apis.tags.completions_api import CompletionsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.MODELS: ModelsApi,
        TagValues.LOGS: LogsApi,
        TagValues.APPS: AppsApi,
        TagValues.CHAT: ChatApi,
        TagValues.COMPLETIONS: CompletionsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.MODELS: ModelsApi,
        TagValues.LOGS: LogsApi,
        TagValues.APPS: AppsApi,
        TagValues.CHAT: ChatApi,
        TagValues.COMPLETIONS: CompletionsApi,
    }
)
