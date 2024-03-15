<div align="left">

[![Visit Pulze.ai](./header.png)](https://www.pulze.ai&#x2F;)

# Pulze.ai<a id="pulzeai"></a>

At Pulze it's our mission to supercharge today's workforce with AI to maximize the world's prosperity. We are doing so by enabling companies of any size to securely leverage Large Language Models (LLM) and easily build AI features into their apps. Our enterprise platform has access to all best in class LLMs and can route user requests to the most relevant model to get the highest quality response at the best price thanks to our smart meta model. End users can leverage pre-built applications, such as our Marketing AI product, or build custom apps on top of the Pulze Platform.

We are a VC Funded, early stage startup based in San Francisco.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`pulzeai.apps.get_app_for_api_key`](#pulzeaiappsget_app_for_api_key)
  * [`pulzeai.apps.update_properties`](#pulzeaiappsupdate_properties)
  * [`pulzeai.chat.perform_completion_request`](#pulzeaichatperform_completion_request)
  * [`pulzeai.completions.perform_text_request`](#pulzeaicompletionsperform_text_request)
  * [`pulzeai.logs.get_by_id`](#pulzeailogsget_by_id)
  * [`pulzeai.logs.get_matching_logs`](#pulzeailogsget_matching_logs)
  * [`pulzeai.logs.rate_by_id`](#pulzeailogsrate_by_id)
  * [`pulzeai.models.get_all_models`](#pulzeaimodelsget_all_models)
  * [`pulzeai.models.get_rank_of_best`](#pulzeaimodelsget_rank_of_best)
  * [`pulzeai.models.list_active_models`](#pulzeaimodelslist_active_models)
  * [`pulzeai.models.toggle_model_for_app`](#pulzeaimodelstoggle_model_for_app)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Pulze.ai&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from pulze_ai_python_sdk import PulzeAi, ApiException

pulzeai = PulzeAi(access_token="YOUR_BEARER_TOKEN")

try:
    # Get App For Api Key
    get_app_for_api_key_response = pulzeai.apps.get_app_for_api_key()
    print(get_app_for_api_key_response)
except ApiException as e:
    print("Exception when calling AppsApi.get_app_for_api_key: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from pulze_ai_python_sdk import PulzeAi, ApiException

pulzeai = PulzeAi(access_token="YOUR_BEARER_TOKEN")


async def main():
    try:
        # Get App For Api Key
        get_app_for_api_key_response = await pulzeai.apps.aget_app_for_api_key()
        print(get_app_for_api_key_response)
    except ApiException as e:
        print("Exception when calling AppsApi.get_app_for_api_key: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from pulze_ai_python_sdk import PulzeAi, ApiException

pulzeai = PulzeAi(access_token="YOUR_BEARER_TOKEN")

try:
    # Get App For Api Key
    get_app_for_api_key_response = pulzeai.apps.raw.get_app_for_api_key()
    pprint(get_app_for_api_key_response.body)
    pprint(get_app_for_api_key_response.body["app"])
    pprint(get_app_for_api_key_response.body["model_settings"])
    pprint(get_app_for_api_key_response.body["files"])
    pprint(get_app_for_api_key_response.headers)
    pprint(get_app_for_api_key_response.status)
    pprint(get_app_for_api_key_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AppsApi.get_app_for_api_key: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `pulzeai.apps.get_app_for_api_key`<a id="pulzeaiappsget_app_for_api_key"></a>

Retrieves the App for the given API key.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_app_for_api_key_response = pulzeai.apps.get_app_for_api_key()
```

#### 🔄 Return<a id="🔄-return"></a>

[`AppWithModelUpdatesInfo`](./pulze_ai_python_sdk/pydantic/app_with_model_updates_info.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/apps/self` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `pulzeai.apps.update_properties`<a id="pulzeaiappsupdate_properties"></a>

Update an App's properties: description, weights and policies.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_properties_response = pulzeai.apps.update_properties(
    description="a",
    id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    policies={
        "max_cost": 0.02,
        "max_same_model_retries": 1,
        "max_switch_model_retries": 1,
        "optimize_internal_requests": 0,
        "privacy_level": 1,
    },
    weights={
        "cost": 0.4,
        "latency": 0.4,
        "quality": 0.4,
    },
    prompt_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

##### id: `str`<a id="id-str"></a>

##### policies: [`LLMModelPolicies`](./pulze_ai_python_sdk/type/llm_model_policies.py)<a id="policies-llmmodelpoliciespulze_ai_python_sdktypellm_model_policiespy"></a>


##### weights: [`LLMModelWeights`](./pulze_ai_python_sdk/type/llm_model_weights.py)<a id="weights-llmmodelweightspulze_ai_python_sdktypellm_model_weightspy"></a>


##### prompt_id: `str`<a id="prompt_id-str"></a>

Prompt ID that we will use for requests

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AppUpdate`](./pulze_ai_python_sdk/type/app_update.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AppWithModelUpdatesInfo`](./pulze_ai_python_sdk/pydantic/app_with_model_updates_info.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/apps/update` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `pulzeai.chat.perform_completion_request`<a id="pulzeaichatperform_completion_request"></a>

Perform a Chat Completion request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
perform_completion_request_response = pulzeai.chat.perform_completion_request(
    best_of=1,
    _false=1,
    frequency_penalty=0,
    logit_bias={},
    logprobs=1,
    max_tokens=1,
    messages=[],
    model="pulze",
    presence_penalty=0,
    prompt="string_example",
    stop="string_example",
    stream=False,
    suffix="",
    temperature=1,
    tool_choice="string_example",
    tools=[
        {
            "function": {
                "parameters": {
                    "properties": {
                        "key": {},
                    },
                    "type": "object",
                },
                "name": "name_example",
            },
            "type": "function",
        }
    ],
    top_p=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### best_of: `int`<a id="best_of-int"></a>

The number of responses to _generate_. Out of those, it will return the best `n`.

##### _false: `int`<a id="_false-int"></a>

How many completions to generate for each prompt. @default 1 

##### frequency_penalty: `Union[int, float]`<a id="frequency_penalty-unionint-float"></a>

https://platform.openai.com/docs/api-reference/completions/create#completions/create-frequency_penalty Increase the model's likelihood to not repeat tokens/words 

##### logit_bias: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="logit_bias-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

COMING SOON https://platform.openai.com/docs/api-reference/completions/create#completions/create-logit_bias Modify the likelihood of specified tokens appearing in the completion.  See here for a detailed explanation on how to use: https://help.openai.com/en/articles/5247780-using-logit-bias-to-define-token-probability 

##### logprobs: `int`<a id="logprobs-int"></a>

COMING SOON https://platform.openai.com/docs/api-reference/completions/create#completions/create-logprobs Include the log probabilities on the logprobs most likely tokens, as well the chosen tokens. 

##### max_tokens: `int`<a id="max_tokens-int"></a>

The maximum number of tokens that the response can contain.

##### messages: List[`RoleContentChatChoice`]<a id="messages-listrolecontentchatchoice"></a>

The conversation sent (with or without history) (for a /chat/completions request)

##### model: `str`<a id="model-str"></a>

https://docs.pulze.ai/overview/models Specify the model you'd like Pulze to use. (optional). Can be the full model name, or a subset for multi-matching.  Defaults to our dynamic routing, i.e. best model for this request. 

##### presence_penalty: `Union[int, float]`<a id="presence_penalty-unionint-float"></a>

https://platform.openai.com/docs/api-reference/completions/create#completions/create-presence_penalty Increase the model's likelihood to talk about new topics 

##### prompt: Union[`str`, `List[str]`]<a id="prompt-unionstr-liststr"></a>


The prompt text sent (for a /completions request)

##### stop: Union[`str`, `List[str]`]<a id="stop-unionstr-liststr"></a>


Stop responding when this sequence of characters is generated. Leave empty to allow the model to decide. 

##### stream: `bool`<a id="stream-bool"></a>

** COMING SOON ** Specify if you want the response to be streamed or to be returned as a standard HTTP request 

##### suffix: `str`<a id="suffix-str"></a>

COMING SOON

##### temperature: `Union[int, float]`<a id="temperature-unionint-float"></a>

Optionally specify the temperature for this request only. Leave empty to allow Pulze to guess it for you.

##### tool_choice: Union[`str`, `ToolChoice`]<a id="tool_choice-unionstr-toolchoice"></a>


##### tools: List[`ToolFunction`]<a id="tools-listtoolfunction"></a>

##### top_p: `Union[int, float]`<a id="top_p-unionint-float"></a>

https://platform.openai.com/docs/api-reference/completions/create#completions/create-top_p An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CompletionRequestPayload`](./pulze_ai_python_sdk/type/completion_request_payload.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PulzeEngineResponseChatCompletion`](./pulze_ai_python_sdk/pydantic/pulze_engine_response_chat_completion.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/chat/completions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `pulzeai.completions.perform_text_request`<a id="pulzeaicompletionsperform_text_request"></a>

Perform a text Completion request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
perform_text_request_response = pulzeai.completions.perform_text_request(
    best_of=1,
    _false=1,
    frequency_penalty=0,
    logit_bias={},
    logprobs=1,
    max_tokens=1,
    messages=[],
    model="pulze",
    presence_penalty=0,
    prompt="string_example",
    stop="string_example",
    stream=False,
    suffix="",
    temperature=1,
    tool_choice="string_example",
    tools=[
        {
            "function": {
                "parameters": {
                    "properties": {
                        "key": {},
                    },
                    "type": "object",
                },
                "name": "name_example",
            },
            "type": "function",
        }
    ],
    top_p=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### best_of: `int`<a id="best_of-int"></a>

The number of responses to _generate_. Out of those, it will return the best `n`.

##### _false: `int`<a id="_false-int"></a>

How many completions to generate for each prompt. @default 1 

##### frequency_penalty: `Union[int, float]`<a id="frequency_penalty-unionint-float"></a>

https://platform.openai.com/docs/api-reference/completions/create#completions/create-frequency_penalty Increase the model's likelihood to not repeat tokens/words 

##### logit_bias: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="logit_bias-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

COMING SOON https://platform.openai.com/docs/api-reference/completions/create#completions/create-logit_bias Modify the likelihood of specified tokens appearing in the completion.  See here for a detailed explanation on how to use: https://help.openai.com/en/articles/5247780-using-logit-bias-to-define-token-probability 

##### logprobs: `int`<a id="logprobs-int"></a>

COMING SOON https://platform.openai.com/docs/api-reference/completions/create#completions/create-logprobs Include the log probabilities on the logprobs most likely tokens, as well the chosen tokens. 

##### max_tokens: `int`<a id="max_tokens-int"></a>

The maximum number of tokens that the response can contain.

##### messages: List[`RoleContentChatChoice`]<a id="messages-listrolecontentchatchoice"></a>

The conversation sent (with or without history) (for a /chat/completions request)

##### model: `str`<a id="model-str"></a>

https://docs.pulze.ai/overview/models Specify the model you'd like Pulze to use. (optional). Can be the full model name, or a subset for multi-matching.  Defaults to our dynamic routing, i.e. best model for this request. 

##### presence_penalty: `Union[int, float]`<a id="presence_penalty-unionint-float"></a>

https://platform.openai.com/docs/api-reference/completions/create#completions/create-presence_penalty Increase the model's likelihood to talk about new topics 

##### prompt: Union[`str`, `List[str]`]<a id="prompt-unionstr-liststr"></a>


The prompt text sent (for a /completions request)

##### stop: Union[`str`, `List[str]`]<a id="stop-unionstr-liststr"></a>


Stop responding when this sequence of characters is generated. Leave empty to allow the model to decide. 

##### stream: `bool`<a id="stream-bool"></a>

** COMING SOON ** Specify if you want the response to be streamed or to be returned as a standard HTTP request 

##### suffix: `str`<a id="suffix-str"></a>

COMING SOON

##### temperature: `Union[int, float]`<a id="temperature-unionint-float"></a>

Optionally specify the temperature for this request only. Leave empty to allow Pulze to guess it for you.

##### tool_choice: Union[`str`, `ToolChoice`]<a id="tool_choice-unionstr-toolchoice"></a>


##### tools: List[`ToolFunction`]<a id="tools-listtoolfunction"></a>

##### top_p: `Union[int, float]`<a id="top_p-unionint-float"></a>

https://platform.openai.com/docs/api-reference/completions/create#completions/create-top_p An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CompletionRequestPayload`](./pulze_ai_python_sdk/type/completion_request_payload.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PulzeEngineResponseCompletion`](./pulze_ai_python_sdk/pydantic/pulze_engine_response_completion.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/completions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `pulzeai.logs.get_by_id`<a id="pulzeailogsget_by_id"></a>

Get a specific log by id. If accessing via API Key, this endpoint will only return a log if it belongs to that App.
If the log's App is disabled, this endpoint won't return it.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = pulzeai.logs.get_by_id(
    log_id="log_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### log_id: `str`<a id="log_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`RequestNormalized`](./pulze_ai_python_sdk/pydantic/request_normalized.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/logs/{log_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `pulzeai.logs.get_matching_logs`<a id="pulzeailogsget_matching_logs"></a>

Get the list of logs that match the specified filters. When accessing via an App's API Key, only logs for that
app will be returned.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_matching_logs_response = pulzeai.logs.get_matching_logs(
    date_from="1970-01-01T00:00:00.00Z",
    app_ids=[],
    date_to="1970-01-01T00:00:00.00Z",
    labels={
        "key": "string_example",
    },
    params=[],
    query="",
    page=1,
    size=50,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### date_from: `datetime`<a id="date_from-datetime"></a>

The earliest date we are searching for.

##### app_ids: [`FilterLogsRequestAppIds`](./pulze_ai_python_sdk/type/filter_logs_request_app_ids.py)<a id="app_ids-filterlogsrequestappidspulze_ai_python_sdktypefilter_logs_request_app_idspy"></a>

##### date_to: `datetime`<a id="date_to-datetime"></a>

The latest date we are searching for.

##### labels: [`FilterLogsRequestLabels`](./pulze_ai_python_sdk/type/filter_logs_request_labels.py)<a id="labels-filterlogsrequestlabelspulze_ai_python_sdktypefilter_logs_request_labelspy"></a>

##### params: List[`GetTableSortParams`]<a id="params-listgettablesortparams"></a>

The sorting parameters for the query

##### query: `str`<a id="query-str"></a>

Search for logs containing the `query` in their Request or Response.

##### page: `int`<a id="page-int"></a>

##### size: `int`<a id="size-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FilterLogsRequest`](./pulze_ai_python_sdk/type/filter_logs_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/logs` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `pulzeai.logs.rate_by_id`<a id="pulzeailogsrate_by_id"></a>

Rate a specific request by its ID. When accessing it via an App's API Key, this endpoint will only allow
rating a log of that specific app.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rate_by_id_response = pulzeai.logs.rate_by_id(
    log_id="log_id_example",
    feedback="",
    good_answer=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### log_id: `str`<a id="log_id-str"></a>

##### feedback: `str`<a id="feedback-str"></a>

An optional text with accompanies the feedback's rating

##### good_answer: `bool`<a id="good_answer-bool"></a>

The rating given to this request. It can be good (`True`), bad (`False`) or none (`None` == `null`)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LogResponseRatingRequest`](./pulze_ai_python_sdk/type/log_response_rating_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`RequestNormalized`](./pulze_ai_python_sdk/pydantic/request_normalized.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/logs/{log_id}/rating` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `pulzeai.models.get_all_models`<a id="pulzeaimodelsget_all_models"></a>

Get a list of all the Models which this App can potentially use.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_models_response = pulzeai.models.get_all_models()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ModelsGetAllModelsResponse`](./pulze_ai_python_sdk/pydantic/models_get_all_models_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/models/all` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `pulzeai.models.get_rank_of_best`<a id="pulzeaimodelsget_rank_of_best"></a>

Get Rank Of Best Models For Payload

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_rank_of_best_response = pulzeai.models.get_rank_of_best(
    best_of=1,
    _false=1,
    frequency_penalty=0,
    logit_bias={},
    logprobs=1,
    max_tokens=1,
    messages=[],
    model="pulze",
    presence_penalty=0,
    prompt="string_example",
    stop="string_example",
    stream=False,
    suffix="",
    temperature=1,
    tool_choice="string_example",
    tools=[
        {
            "function": {
                "parameters": {
                    "properties": {
                        "key": {},
                    },
                    "type": "object",
                },
                "name": "name_example",
            },
            "type": "function",
        }
    ],
    top_p=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### best_of: `int`<a id="best_of-int"></a>

The number of responses to _generate_. Out of those, it will return the best `n`.

##### _false: `int`<a id="_false-int"></a>

How many completions to generate for each prompt. @default 1 

##### frequency_penalty: `Union[int, float]`<a id="frequency_penalty-unionint-float"></a>

https://platform.openai.com/docs/api-reference/completions/create#completions/create-frequency_penalty Increase the model's likelihood to not repeat tokens/words 

##### logit_bias: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="logit_bias-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

COMING SOON https://platform.openai.com/docs/api-reference/completions/create#completions/create-logit_bias Modify the likelihood of specified tokens appearing in the completion.  See here for a detailed explanation on how to use: https://help.openai.com/en/articles/5247780-using-logit-bias-to-define-token-probability 

##### logprobs: `int`<a id="logprobs-int"></a>

COMING SOON https://platform.openai.com/docs/api-reference/completions/create#completions/create-logprobs Include the log probabilities on the logprobs most likely tokens, as well the chosen tokens. 

##### max_tokens: `int`<a id="max_tokens-int"></a>

The maximum number of tokens that the response can contain.

##### messages: List[`RoleContentChatChoice`]<a id="messages-listrolecontentchatchoice"></a>

The conversation sent (with or without history) (for a /chat/completions request)

##### model: `str`<a id="model-str"></a>

https://docs.pulze.ai/overview/models Specify the model you'd like Pulze to use. (optional). Can be the full model name, or a subset for multi-matching.  Defaults to our dynamic routing, i.e. best model for this request. 

##### presence_penalty: `Union[int, float]`<a id="presence_penalty-unionint-float"></a>

https://platform.openai.com/docs/api-reference/completions/create#completions/create-presence_penalty Increase the model's likelihood to talk about new topics 

##### prompt: Union[`str`, `List[str]`]<a id="prompt-unionstr-liststr"></a>


The prompt text sent (for a /completions request)

##### stop: Union[`str`, `List[str]`]<a id="stop-unionstr-liststr"></a>


Stop responding when this sequence of characters is generated. Leave empty to allow the model to decide. 

##### stream: `bool`<a id="stream-bool"></a>

** COMING SOON ** Specify if you want the response to be streamed or to be returned as a standard HTTP request 

##### suffix: `str`<a id="suffix-str"></a>

COMING SOON

##### temperature: `Union[int, float]`<a id="temperature-unionint-float"></a>

Optionally specify the temperature for this request only. Leave empty to allow Pulze to guess it for you.

##### tool_choice: Union[`str`, `ToolChoice`]<a id="tool_choice-unionstr-toolchoice"></a>


##### tools: List[`ToolFunction`]<a id="tools-listtoolfunction"></a>

##### top_p: `Union[int, float]`<a id="top_p-unionint-float"></a>

https://platform.openai.com/docs/api-reference/completions/create#completions/create-top_p An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CompletionRequestPayload`](./pulze_ai_python_sdk/type/completion_request_payload.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PulzeEngineModelRanking`](./pulze_ai_python_sdk/pydantic/pulze_engine_model_ranking.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/models/rank` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `pulzeai.models.list_active_models`<a id="pulzeaimodelslist_active_models"></a>

Get a list of the Models which are active for a specific App.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_active_models_response = pulzeai.models.list_active_models()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ModelsListActiveModelsResponse`](./pulze_ai_python_sdk/pydantic/models_list_active_models_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/models/active` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `pulzeai.models.toggle_model_for_app`<a id="pulzeaimodelstoggle_model_for_app"></a>

Enable or disable a model.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
toggle_model_for_app_response = pulzeai.models.toggle_model_for_app(
    model_id="model_id_example",
    enable=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### model_id: `str`<a id="model_id-str"></a>

##### enable: `bool`<a id="enable-bool"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PulzeToggleModelResponse`](./pulze_ai_python_sdk/pydantic/pulze_toggle_model_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/models/{model_id}/toggle` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
