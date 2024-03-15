# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from pulze_ai_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_CHAT_COMPLETIONS = "/v1/chat/completions"
    V1_COMPLETIONS = "/v1/completions"
    V1_MODELS_RANK = "/v1/models/rank"
    V1_LOGS_LOG_ID = "/v1/logs/{log_id}"
    V1_LOGS_LOG_ID_RATING = "/v1/logs/{log_id}/rating"
    V1_APPS_SELF = "/v1/apps/self"
    V1_APPS_UPDATE = "/v1/apps/update"
    V1_MODELS_ACTIVE = "/v1/models/active"
    V1_MODELS_ALL = "/v1/models/all"
    V1_MODELS_MODEL_ID_TOGGLE = "/v1/models/{model_id}/toggle"
    V1_LOGS = "/v1/logs"
