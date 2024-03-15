# coding: utf-8

"""
    Pulze.ai API

    At Pulze it's our mission to supercharge today's workforce with AI to maximize the world's prosperity. We are doing so by enabling companies of any size to securely leverage Large Language Models (LLM) and easily build AI features into their apps. Our enterprise platform has access to all best in class LLMs and can route user requests to the most relevant model to get the highest quality response at the best price thanks to our smart meta model. End users can leverage pre-built applications, such as our Marketing AI product, or build custom apps on top of the Pulze Platform.  We are a VC Funded, early stage startup based in San Francisco.

    The version of the OpenAPI document: 0.1.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from pulze_ai_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from pulze_ai_python_sdk.api_response import AsyncGeneratorResponse
from pulze_ai_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from pulze_ai_python_sdk import schemas  # noqa: F401

from pulze_ai_python_sdk.model.role_content_chat_choice import RoleContentChatChoice as RoleContentChatChoiceSchema
from pulze_ai_python_sdk.model.tool_function import ToolFunction as ToolFunctionSchema
from pulze_ai_python_sdk.model.pulze_engine_response_completion import PulzeEngineResponseCompletion as PulzeEngineResponseCompletionSchema
from pulze_ai_python_sdk.model.tool_choice import ToolChoice as ToolChoiceSchema
from pulze_ai_python_sdk.model.http_validation_error import HTTPValidationError as HTTPValidationErrorSchema
from pulze_ai_python_sdk.model.completion_request_payload import CompletionRequestPayload as CompletionRequestPayloadSchema

from pulze_ai_python_sdk.type.pulze_engine_response_completion import PulzeEngineResponseCompletion
from pulze_ai_python_sdk.type.completion_request_payload import CompletionRequestPayload
from pulze_ai_python_sdk.type.tool_choice import ToolChoice
from pulze_ai_python_sdk.type.tool_function import ToolFunction
from pulze_ai_python_sdk.type.role_content_chat_choice import RoleContentChatChoice
from pulze_ai_python_sdk.type.http_validation_error import HTTPValidationError

from ...api_client import Dictionary
from pulze_ai_python_sdk.pydantic.role_content_chat_choice import RoleContentChatChoice as RoleContentChatChoicePydantic
from pulze_ai_python_sdk.pydantic.completion_request_payload import CompletionRequestPayload as CompletionRequestPayloadPydantic
from pulze_ai_python_sdk.pydantic.tool_function import ToolFunction as ToolFunctionPydantic
from pulze_ai_python_sdk.pydantic.tool_choice import ToolChoice as ToolChoicePydantic
from pulze_ai_python_sdk.pydantic.pulze_engine_response_completion import PulzeEngineResponseCompletion as PulzeEngineResponseCompletionPydantic
from pulze_ai_python_sdk.pydantic.http_validation_error import HTTPValidationError as HTTPValidationErrorPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = CompletionRequestPayloadSchema


request_body_completion_request_payload = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'HTTPBearer',
]
SchemaFor200ResponseBodyApplicationJson = PulzeEngineResponseCompletionSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PulzeEngineResponseCompletion


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PulzeEngineResponseCompletion


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = HTTPValidationErrorSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: HTTPValidationError


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: HTTPValidationError


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '422': _response_for_422,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _perform_text_request_mapped_args(
        self,
        best_of: typing.Optional[int] = None,
        _false: typing.Optional[int] = None,
        frequency_penalty: typing.Optional[typing.Union[int, float]] = None,
        logit_bias: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        logprobs: typing.Optional[int] = None,
        max_tokens: typing.Optional[int] = None,
        messages: typing.Optional[typing.List[RoleContentChatChoice]] = None,
        model: typing.Optional[str] = None,
        presence_penalty: typing.Optional[typing.Union[int, float]] = None,
        prompt: typing.Optional[typing.Union[str, typing.List[str]]] = None,
        stop: typing.Optional[typing.Union[str, typing.List[str]]] = None,
        stream: typing.Optional[bool] = None,
        suffix: typing.Optional[str] = None,
        temperature: typing.Optional[typing.Union[int, float]] = None,
        tool_choice: typing.Optional[typing.Union[str, ToolChoice]] = None,
        tools: typing.Optional[typing.List[ToolFunction]] = None,
        top_p: typing.Optional[typing.Union[int, float]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if best_of is not None:
            _body["best_of"] = best_of
        if _false is not None:
            _body["false"] = _false
        if frequency_penalty is not None:
            _body["frequency_penalty"] = frequency_penalty
        if logit_bias is not None:
            _body["logit_bias"] = logit_bias
        if logprobs is not None:
            _body["logprobs"] = logprobs
        if max_tokens is not None:
            _body["max_tokens"] = max_tokens
        if messages is not None:
            _body["messages"] = messages
        if model is not None:
            _body["model"] = model
        if presence_penalty is not None:
            _body["presence_penalty"] = presence_penalty
        if prompt is not None:
            _body["prompt"] = prompt
        if stop is not None:
            _body["stop"] = stop
        if stream is not None:
            _body["stream"] = stream
        if suffix is not None:
            _body["suffix"] = suffix
        if temperature is not None:
            _body["temperature"] = temperature
        if tool_choice is not None:
            _body["tool_choice"] = tool_choice
        if tools is not None:
            _body["tools"] = tools
        if top_p is not None:
            _body["top_p"] = top_p
        args.body = _body
        return args

    async def _aperform_text_request_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Completions
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/completions',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_completion_request_payload.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _perform_text_request_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Completions
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/completions',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_completion_request_payload.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class PerformTextRequestRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aperform_text_request(
        self,
        best_of: typing.Optional[int] = None,
        _false: typing.Optional[int] = None,
        frequency_penalty: typing.Optional[typing.Union[int, float]] = None,
        logit_bias: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        logprobs: typing.Optional[int] = None,
        max_tokens: typing.Optional[int] = None,
        messages: typing.Optional[typing.List[RoleContentChatChoice]] = None,
        model: typing.Optional[str] = None,
        presence_penalty: typing.Optional[typing.Union[int, float]] = None,
        prompt: typing.Optional[typing.Union[str, typing.List[str]]] = None,
        stop: typing.Optional[typing.Union[str, typing.List[str]]] = None,
        stream: typing.Optional[bool] = None,
        suffix: typing.Optional[str] = None,
        temperature: typing.Optional[typing.Union[int, float]] = None,
        tool_choice: typing.Optional[typing.Union[str, ToolChoice]] = None,
        tools: typing.Optional[typing.List[ToolFunction]] = None,
        top_p: typing.Optional[typing.Union[int, float]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._perform_text_request_mapped_args(
            best_of=best_of,
            _false=_false,
            frequency_penalty=frequency_penalty,
            logit_bias=logit_bias,
            logprobs=logprobs,
            max_tokens=max_tokens,
            messages=messages,
            model=model,
            presence_penalty=presence_penalty,
            prompt=prompt,
            stop=stop,
            stream=stream,
            suffix=suffix,
            temperature=temperature,
            tool_choice=tool_choice,
            tools=tools,
            top_p=top_p,
        )
        return await self._aperform_text_request_oapg(
            body=args.body,
            **kwargs,
        )
    
    def perform_text_request(
        self,
        best_of: typing.Optional[int] = None,
        _false: typing.Optional[int] = None,
        frequency_penalty: typing.Optional[typing.Union[int, float]] = None,
        logit_bias: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        logprobs: typing.Optional[int] = None,
        max_tokens: typing.Optional[int] = None,
        messages: typing.Optional[typing.List[RoleContentChatChoice]] = None,
        model: typing.Optional[str] = None,
        presence_penalty: typing.Optional[typing.Union[int, float]] = None,
        prompt: typing.Optional[typing.Union[str, typing.List[str]]] = None,
        stop: typing.Optional[typing.Union[str, typing.List[str]]] = None,
        stream: typing.Optional[bool] = None,
        suffix: typing.Optional[str] = None,
        temperature: typing.Optional[typing.Union[int, float]] = None,
        tool_choice: typing.Optional[typing.Union[str, ToolChoice]] = None,
        tools: typing.Optional[typing.List[ToolFunction]] = None,
        top_p: typing.Optional[typing.Union[int, float]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._perform_text_request_mapped_args(
            best_of=best_of,
            _false=_false,
            frequency_penalty=frequency_penalty,
            logit_bias=logit_bias,
            logprobs=logprobs,
            max_tokens=max_tokens,
            messages=messages,
            model=model,
            presence_penalty=presence_penalty,
            prompt=prompt,
            stop=stop,
            stream=stream,
            suffix=suffix,
            temperature=temperature,
            tool_choice=tool_choice,
            tools=tools,
            top_p=top_p,
        )
        return self._perform_text_request_oapg(
            body=args.body,
        )

class PerformTextRequest(BaseApi):

    async def aperform_text_request(
        self,
        best_of: typing.Optional[int] = None,
        _false: typing.Optional[int] = None,
        frequency_penalty: typing.Optional[typing.Union[int, float]] = None,
        logit_bias: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        logprobs: typing.Optional[int] = None,
        max_tokens: typing.Optional[int] = None,
        messages: typing.Optional[typing.List[RoleContentChatChoice]] = None,
        model: typing.Optional[str] = None,
        presence_penalty: typing.Optional[typing.Union[int, float]] = None,
        prompt: typing.Optional[typing.Union[str, typing.List[str]]] = None,
        stop: typing.Optional[typing.Union[str, typing.List[str]]] = None,
        stream: typing.Optional[bool] = None,
        suffix: typing.Optional[str] = None,
        temperature: typing.Optional[typing.Union[int, float]] = None,
        tool_choice: typing.Optional[typing.Union[str, ToolChoice]] = None,
        tools: typing.Optional[typing.List[ToolFunction]] = None,
        top_p: typing.Optional[typing.Union[int, float]] = None,
        validate: bool = False,
        **kwargs,
    ) -> PulzeEngineResponseCompletionPydantic:
        raw_response = await self.raw.aperform_text_request(
            best_of=best_of,
            _false=_false,
            frequency_penalty=frequency_penalty,
            logit_bias=logit_bias,
            logprobs=logprobs,
            max_tokens=max_tokens,
            messages=messages,
            model=model,
            presence_penalty=presence_penalty,
            prompt=prompt,
            stop=stop,
            stream=stream,
            suffix=suffix,
            temperature=temperature,
            tool_choice=tool_choice,
            tools=tools,
            top_p=top_p,
            **kwargs,
        )
        if validate:
            return PulzeEngineResponseCompletionPydantic(**raw_response.body)
        return api_client.construct_model_instance(PulzeEngineResponseCompletionPydantic, raw_response.body)
    
    
    def perform_text_request(
        self,
        best_of: typing.Optional[int] = None,
        _false: typing.Optional[int] = None,
        frequency_penalty: typing.Optional[typing.Union[int, float]] = None,
        logit_bias: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        logprobs: typing.Optional[int] = None,
        max_tokens: typing.Optional[int] = None,
        messages: typing.Optional[typing.List[RoleContentChatChoice]] = None,
        model: typing.Optional[str] = None,
        presence_penalty: typing.Optional[typing.Union[int, float]] = None,
        prompt: typing.Optional[typing.Union[str, typing.List[str]]] = None,
        stop: typing.Optional[typing.Union[str, typing.List[str]]] = None,
        stream: typing.Optional[bool] = None,
        suffix: typing.Optional[str] = None,
        temperature: typing.Optional[typing.Union[int, float]] = None,
        tool_choice: typing.Optional[typing.Union[str, ToolChoice]] = None,
        tools: typing.Optional[typing.List[ToolFunction]] = None,
        top_p: typing.Optional[typing.Union[int, float]] = None,
        validate: bool = False,
    ) -> PulzeEngineResponseCompletionPydantic:
        raw_response = self.raw.perform_text_request(
            best_of=best_of,
            _false=_false,
            frequency_penalty=frequency_penalty,
            logit_bias=logit_bias,
            logprobs=logprobs,
            max_tokens=max_tokens,
            messages=messages,
            model=model,
            presence_penalty=presence_penalty,
            prompt=prompt,
            stop=stop,
            stream=stream,
            suffix=suffix,
            temperature=temperature,
            tool_choice=tool_choice,
            tools=tools,
            top_p=top_p,
        )
        if validate:
            return PulzeEngineResponseCompletionPydantic(**raw_response.body)
        return api_client.construct_model_instance(PulzeEngineResponseCompletionPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        best_of: typing.Optional[int] = None,
        _false: typing.Optional[int] = None,
        frequency_penalty: typing.Optional[typing.Union[int, float]] = None,
        logit_bias: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        logprobs: typing.Optional[int] = None,
        max_tokens: typing.Optional[int] = None,
        messages: typing.Optional[typing.List[RoleContentChatChoice]] = None,
        model: typing.Optional[str] = None,
        presence_penalty: typing.Optional[typing.Union[int, float]] = None,
        prompt: typing.Optional[typing.Union[str, typing.List[str]]] = None,
        stop: typing.Optional[typing.Union[str, typing.List[str]]] = None,
        stream: typing.Optional[bool] = None,
        suffix: typing.Optional[str] = None,
        temperature: typing.Optional[typing.Union[int, float]] = None,
        tool_choice: typing.Optional[typing.Union[str, ToolChoice]] = None,
        tools: typing.Optional[typing.List[ToolFunction]] = None,
        top_p: typing.Optional[typing.Union[int, float]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._perform_text_request_mapped_args(
            best_of=best_of,
            _false=_false,
            frequency_penalty=frequency_penalty,
            logit_bias=logit_bias,
            logprobs=logprobs,
            max_tokens=max_tokens,
            messages=messages,
            model=model,
            presence_penalty=presence_penalty,
            prompt=prompt,
            stop=stop,
            stream=stream,
            suffix=suffix,
            temperature=temperature,
            tool_choice=tool_choice,
            tools=tools,
            top_p=top_p,
        )
        return await self._aperform_text_request_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        best_of: typing.Optional[int] = None,
        _false: typing.Optional[int] = None,
        frequency_penalty: typing.Optional[typing.Union[int, float]] = None,
        logit_bias: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        logprobs: typing.Optional[int] = None,
        max_tokens: typing.Optional[int] = None,
        messages: typing.Optional[typing.List[RoleContentChatChoice]] = None,
        model: typing.Optional[str] = None,
        presence_penalty: typing.Optional[typing.Union[int, float]] = None,
        prompt: typing.Optional[typing.Union[str, typing.List[str]]] = None,
        stop: typing.Optional[typing.Union[str, typing.List[str]]] = None,
        stream: typing.Optional[bool] = None,
        suffix: typing.Optional[str] = None,
        temperature: typing.Optional[typing.Union[int, float]] = None,
        tool_choice: typing.Optional[typing.Union[str, ToolChoice]] = None,
        tools: typing.Optional[typing.List[ToolFunction]] = None,
        top_p: typing.Optional[typing.Union[int, float]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._perform_text_request_mapped_args(
            best_of=best_of,
            _false=_false,
            frequency_penalty=frequency_penalty,
            logit_bias=logit_bias,
            logprobs=logprobs,
            max_tokens=max_tokens,
            messages=messages,
            model=model,
            presence_penalty=presence_penalty,
            prompt=prompt,
            stop=stop,
            stream=stream,
            suffix=suffix,
            temperature=temperature,
            tool_choice=tool_choice,
            tools=tools,
            top_p=top_p,
        )
        return self._perform_text_request_oapg(
            body=args.body,
        )

