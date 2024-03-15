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

from pulze_ai_python_sdk.model.request_normalized import RequestNormalized as RequestNormalizedSchema
from pulze_ai_python_sdk.model.log_response_rating_request import LogResponseRatingRequest as LogResponseRatingRequestSchema
from pulze_ai_python_sdk.model.http_validation_error import HTTPValidationError as HTTPValidationErrorSchema

from pulze_ai_python_sdk.type.log_response_rating_request import LogResponseRatingRequest
from pulze_ai_python_sdk.type.http_validation_error import HTTPValidationError
from pulze_ai_python_sdk.type.request_normalized import RequestNormalized

from ...api_client import Dictionary
from pulze_ai_python_sdk.pydantic.log_response_rating_request import LogResponseRatingRequest as LogResponseRatingRequestPydantic
from pulze_ai_python_sdk.pydantic.request_normalized import RequestNormalized as RequestNormalizedPydantic
from pulze_ai_python_sdk.pydantic.http_validation_error import HTTPValidationError as HTTPValidationErrorPydantic

# Path params
LogIdSchema = schemas.UUIDSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'log_id': typing.Union[LogIdSchema, str, uuid.UUID, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_log_id = api_client.PathParameter(
    name="log_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=LogIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = LogResponseRatingRequestSchema


request_body_log_response_rating_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = RequestNormalizedSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: RequestNormalized


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: RequestNormalized


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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _rate_by_id_mapped_args(
        self,
        log_id: str,
        feedback: typing.Optional[str] = None,
        good_answer: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if feedback is not None:
            _body["feedback"] = feedback
        if good_answer is not None:
            _body["good_answer"] = good_answer
        args.body = _body
        if log_id is not None:
            _path_params["log_id"] = log_id
        args.path = _path_params
        return args

    async def _arate_by_id_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Rate Log By Id
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_log_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
            path_template='/v1/logs/{log_id}/rating',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_log_response_rating_request.serialize(body, content_type)
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


    def _rate_by_id_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Rate Log By Id
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_log_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
            path_template='/v1/logs/{log_id}/rating',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_log_response_rating_request.serialize(body, content_type)
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


class RateByIdRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def arate_by_id(
        self,
        log_id: str,
        feedback: typing.Optional[str] = None,
        good_answer: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._rate_by_id_mapped_args(
            log_id=log_id,
            feedback=feedback,
            good_answer=good_answer,
        )
        return await self._arate_by_id_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def rate_by_id(
        self,
        log_id: str,
        feedback: typing.Optional[str] = None,
        good_answer: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._rate_by_id_mapped_args(
            log_id=log_id,
            feedback=feedback,
            good_answer=good_answer,
        )
        return self._rate_by_id_oapg(
            body=args.body,
            path_params=args.path,
        )

class RateById(BaseApi):

    async def arate_by_id(
        self,
        log_id: str,
        feedback: typing.Optional[str] = None,
        good_answer: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> RequestNormalizedPydantic:
        raw_response = await self.raw.arate_by_id(
            log_id=log_id,
            feedback=feedback,
            good_answer=good_answer,
            **kwargs,
        )
        if validate:
            return RequestNormalizedPydantic(**raw_response.body)
        return api_client.construct_model_instance(RequestNormalizedPydantic, raw_response.body)
    
    
    def rate_by_id(
        self,
        log_id: str,
        feedback: typing.Optional[str] = None,
        good_answer: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> RequestNormalizedPydantic:
        raw_response = self.raw.rate_by_id(
            log_id=log_id,
            feedback=feedback,
            good_answer=good_answer,
        )
        if validate:
            return RequestNormalizedPydantic(**raw_response.body)
        return api_client.construct_model_instance(RequestNormalizedPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        log_id: str,
        feedback: typing.Optional[str] = None,
        good_answer: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._rate_by_id_mapped_args(
            log_id=log_id,
            feedback=feedback,
            good_answer=good_answer,
        )
        return await self._arate_by_id_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        log_id: str,
        feedback: typing.Optional[str] = None,
        good_answer: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._rate_by_id_mapped_args(
            log_id=log_id,
            feedback=feedback,
            good_answer=good_answer,
        )
        return self._rate_by_id_oapg(
            body=args.body,
            path_params=args.path,
        )

