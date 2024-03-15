import typing_extensions

from pulze_ai_python_sdk.paths import PathValues
from pulze_ai_python_sdk.apis.paths.v1_chat_completions import V1ChatCompletions
from pulze_ai_python_sdk.apis.paths.v1_completions import V1Completions
from pulze_ai_python_sdk.apis.paths.v1_models_rank import V1ModelsRank
from pulze_ai_python_sdk.apis.paths.v1_logs_log_id import V1LogsLogId
from pulze_ai_python_sdk.apis.paths.v1_logs_log_id_rating import V1LogsLogIdRating
from pulze_ai_python_sdk.apis.paths.v1_apps_self import V1AppsSelf
from pulze_ai_python_sdk.apis.paths.v1_apps_update import V1AppsUpdate
from pulze_ai_python_sdk.apis.paths.v1_models_active import V1ModelsActive
from pulze_ai_python_sdk.apis.paths.v1_models_all import V1ModelsAll
from pulze_ai_python_sdk.apis.paths.v1_models_model_id_toggle import V1ModelsModelIdToggle
from pulze_ai_python_sdk.apis.paths.v1_logs import V1Logs

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_CHAT_COMPLETIONS: V1ChatCompletions,
        PathValues.V1_COMPLETIONS: V1Completions,
        PathValues.V1_MODELS_RANK: V1ModelsRank,
        PathValues.V1_LOGS_LOG_ID: V1LogsLogId,
        PathValues.V1_LOGS_LOG_ID_RATING: V1LogsLogIdRating,
        PathValues.V1_APPS_SELF: V1AppsSelf,
        PathValues.V1_APPS_UPDATE: V1AppsUpdate,
        PathValues.V1_MODELS_ACTIVE: V1ModelsActive,
        PathValues.V1_MODELS_ALL: V1ModelsAll,
        PathValues.V1_MODELS_MODEL_ID_TOGGLE: V1ModelsModelIdToggle,
        PathValues.V1_LOGS: V1Logs,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_CHAT_COMPLETIONS: V1ChatCompletions,
        PathValues.V1_COMPLETIONS: V1Completions,
        PathValues.V1_MODELS_RANK: V1ModelsRank,
        PathValues.V1_LOGS_LOG_ID: V1LogsLogId,
        PathValues.V1_LOGS_LOG_ID_RATING: V1LogsLogIdRating,
        PathValues.V1_APPS_SELF: V1AppsSelf,
        PathValues.V1_APPS_UPDATE: V1AppsUpdate,
        PathValues.V1_MODELS_ACTIVE: V1ModelsActive,
        PathValues.V1_MODELS_ALL: V1ModelsAll,
        PathValues.V1_MODELS_MODEL_ID_TOGGLE: V1ModelsModelIdToggle,
        PathValues.V1_LOGS: V1Logs,
    }
)
