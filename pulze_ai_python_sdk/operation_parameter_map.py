operation_parameter_map = {
    '/v1/apps/self-GET': {
        'parameters': [
        ]
    },
    '/v1/apps/update-PUT': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'id'
            },
            {
                'name': 'policies'
            },
            {
                'name': 'weights'
            },
            {
                'name': 'prompt_id'
            },
        ]
    },
    '/v1/chat/completions-POST': {
        'parameters': [
            {
                'name': 'best_of'
            },
            {
                'name': 'false'
            },
            {
                'name': 'frequency_penalty'
            },
            {
                'name': 'logit_bias'
            },
            {
                'name': 'logprobs'
            },
            {
                'name': 'max_tokens'
            },
            {
                'name': 'messages'
            },
            {
                'name': 'model'
            },
            {
                'name': 'presence_penalty'
            },
            {
                'name': 'prompt'
            },
            {
                'name': 'stop'
            },
            {
                'name': 'stream'
            },
            {
                'name': 'suffix'
            },
            {
                'name': 'temperature'
            },
            {
                'name': 'tool_choice'
            },
            {
                'name': 'tools'
            },
            {
                'name': 'top_p'
            },
        ]
    },
    '/v1/completions-POST': {
        'parameters': [
            {
                'name': 'best_of'
            },
            {
                'name': 'false'
            },
            {
                'name': 'frequency_penalty'
            },
            {
                'name': 'logit_bias'
            },
            {
                'name': 'logprobs'
            },
            {
                'name': 'max_tokens'
            },
            {
                'name': 'messages'
            },
            {
                'name': 'model'
            },
            {
                'name': 'presence_penalty'
            },
            {
                'name': 'prompt'
            },
            {
                'name': 'stop'
            },
            {
                'name': 'stream'
            },
            {
                'name': 'suffix'
            },
            {
                'name': 'temperature'
            },
            {
                'name': 'tool_choice'
            },
            {
                'name': 'tools'
            },
            {
                'name': 'top_p'
            },
        ]
    },
    '/v1/logs/{log_id}-GET': {
        'parameters': [
            {
                'name': 'log_id'
            },
        ]
    },
    '/v1/logs-POST': {
        'parameters': [
            {
                'name': 'date_from'
            },
            {
                'name': 'app_ids'
            },
            {
                'name': 'date_to'
            },
            {
                'name': 'labels'
            },
            {
                'name': 'params'
            },
            {
                'name': 'query'
            },
            {
                'name': 'page'
            },
            {
                'name': 'size'
            },
        ]
    },
    '/v1/logs/{log_id}/rating-POST': {
        'parameters': [
            {
                'name': 'log_id'
            },
            {
                'name': 'feedback'
            },
            {
                'name': 'good_answer'
            },
        ]
    },
    '/v1/models/all-GET': {
        'parameters': [
        ]
    },
    '/v1/models/rank-POST': {
        'parameters': [
            {
                'name': 'best_of'
            },
            {
                'name': 'false'
            },
            {
                'name': 'frequency_penalty'
            },
            {
                'name': 'logit_bias'
            },
            {
                'name': 'logprobs'
            },
            {
                'name': 'max_tokens'
            },
            {
                'name': 'messages'
            },
            {
                'name': 'model'
            },
            {
                'name': 'presence_penalty'
            },
            {
                'name': 'prompt'
            },
            {
                'name': 'stop'
            },
            {
                'name': 'stream'
            },
            {
                'name': 'suffix'
            },
            {
                'name': 'temperature'
            },
            {
                'name': 'tool_choice'
            },
            {
                'name': 'tools'
            },
            {
                'name': 'top_p'
            },
        ]
    },
    '/v1/models/active-GET': {
        'parameters': [
        ]
    },
    '/v1/models/{model_id}/toggle-PUT': {
        'parameters': [
            {
                'name': 'model_id'
            },
            {
                'name': 'enable'
            },
        ]
    },
};