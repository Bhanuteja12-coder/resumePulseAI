import sys
import os
from dotenv import load_dotenv
load_dotenv('.env')

sys.path.insert(0, os.path.abspath('.'))
from google.ai.generativelanguage_v1beta import GenerativeServiceClient
from google.ai.generativelanguage_v1beta.types import content

api_key = os.getenv('GOOGLE_API_KEY')
print('api key present:', bool(api_key))
client = GenerativeServiceClient(client_options={'api_key': api_key})
prompt_text = 'Write exactly 2 concise resume improvement suggestions in JSON with key suggestions.'

try:
    prompt_content = content.Content(parts=[content.Part(text=prompt_text)], role='user')
    print('prompt_content', prompt_content)
    response = client.generate_content(model='models/gemini-2.5-flash', contents=[prompt_content], temperature=0.2)
    print('response type', type(response))
    print('response attrs', [a for a in dir(response) if not a.startswith('_')])
    print('candidates attr', getattr(response, 'candidates', None))
    if getattr(response, 'candidates', None):
        for i, candidate in enumerate(response.candidates):
            print('candidate', i, 'type', type(candidate))
            print('candidate dir', [a for a in dir(candidate) if not a.startswith('_')][:100])
            print('candidate repr', repr(candidate)[:3000])
            print('candidate content getattr', getattr(candidate, 'content', None))
            content_items = getattr(candidate, 'content', None)
            if content_items is not None:
                for j, item in enumerate(content_items):
                    print('item', j, 'type', type(item))
                    print('item dir', [a for a in dir(item) if not a.startswith('_')][:100])
                    print('item repr', repr(item)[:3000])
                    print('item text', getattr(item, 'text', None))
except Exception as exc:
    print('exception', type(exc).__name__, exc)
