import sys
import os
from dotenv import load_dotenv
load_dotenv('.env')

sys.path.insert(0, os.path.abspath('.'))
from google.ai.generativelanguage_v1beta import GenerativeServiceClient
from google.ai.generativelanguage_v1beta.types import content, generative_service

print('python probe start')
print('GOOGLE_API_KEY present', bool(os.getenv('GOOGLE_API_KEY')))
print('content attrs sample', [a for a in dir(content) if not a.startswith('_')][:80])
print('generative_service attrs sample', [a for a in dir(generative_service) if not a.startswith('_')][:80])
print('GenerateContentRequest fields', list(generative_service.GenerateContentRequest.meta.fields.keys()))
print('GenerateContentResponse fields', list(generative_service.GenerateContentResponse.meta.fields.keys()))

print('Content fields', list(content.Content.meta.fields.keys()))
print('Part fields', list(content.Part.meta.fields.keys()))

print('GenerationConfig type from module?')
for name in dir(content):
    if 'Generation' in name or 'generation' in name.lower():
        print('content module candidate', name)
for name in dir(generative_service):
    if 'Generation' in name or 'generation' in name.lower():
        print('generative_service candidate', name)

# inspect overall types module names as well
import google.ai.generativelanguage_v1beta.types as types_module
for name in dir(types_module):
    if 'Generation' in name or 'generation' in name.lower():
        print('types module candidate', name)

# show type of generation_config if available
if 'generation_config' in generative_service.GenerateContentRequest.meta.fields:
    field = generative_service.GenerateContentRequest.meta.fields['generation_config']
    print('generation_config field type', type(field), field)

# build a request object if possible
try:
    prompt_text = 'Write exactly 2 concise resume improvement suggestions in JSON with key suggestions.'
    prompt_content = content.Content(parts=[content.Part(text=prompt_text)], role='user')
    print('prompt_content repr:', repr(prompt_content))
    print('prompt_content to_dict', prompt_content.to_dict())
    request = generative_service.GenerateContentRequest(
        model='models/gemini-2.5-flash',
        contents=[prompt_content],
    )
    print('request repr', repr(request)[:2000])
    print('request to_dict', request.to_dict())
    print('request pb', request.pb)
except Exception as exc:
    print('request create exc', type(exc).__name__, exc)

# actual call with content only to inspect response shape
try:
    client = GenerativeServiceClient(client_options={'api_key': os.getenv('GOOGLE_API_KEY')})
    response = client.generate_content(model='models/gemini-2.5-flash', contents=[prompt_content])
    print('response type', type(response))
    print('response repr', repr(response)[:2000])
    print('response to_dict', response.to_dict())
    print('candidates', getattr(response, 'candidates', None))
    if getattr(response, 'candidates', None):
        for i, cand in enumerate(response.candidates):
            print('candidate', i, type(cand))
            print('candidate dir', [a for a in dir(cand) if not a.startswith('_')][:100])
            try:
                print('candidate to_dict', cand.to_dict())
            except Exception as exc:
                print('candidate to_dict exc', type(exc).__name__, exc)
            print('candidate content attr', getattr(cand, 'content', None))
            content_items = getattr(cand, 'content', None)
            if content_items is not None:
                for j, item in enumerate(content_items):
                    print('item', j, type(item))
                    print('item dir', [a for a in dir(item) if not a.startswith('_')][:100])
                    try:
                        print('item to_dict', item.to_dict())
                    except Exception as exc:
                        print('item to_dict exc', type(exc).__name__, exc)
                    print('item text', getattr(item, 'text', None))
                    print('item parts', getattr(item, 'parts', None))
except Exception as exc:
    print('generate_content exc', type(exc).__name__, exc)
