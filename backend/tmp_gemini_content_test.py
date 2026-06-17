import sys
import os
from dotenv import load_dotenv
load_dotenv('.env')
sys.path.insert(0, os.path.abspath('.'))
from google.ai.generativelanguage_v1beta import GenerativeServiceClient
from google.ai.generativelanguage_v1beta.types import content

api_key = os.getenv('GOOGLE_API_KEY')
print('api_key present', bool(api_key))
client = GenerativeServiceClient(client_options={'api_key': api_key})
prompt_text = 'Write exactly 2 concise resume improvement suggestions in JSON with key suggestions.'

try:
    prompt_content = content.Content(text=prompt_text)
    response = client.generate_content(model='models/gemini-2.5-flash', contents=[prompt_content], temperature=0.2)
    print('response type', type(response))
    print('response attrs', [a for a in dir(response) if not a.startswith('_')])
    print('response repr', repr(response)[:3000])
    print('response candidates', getattr(response, 'candidates', None))
    if getattr(response, 'candidates', None):
        for i, cand in enumerate(response.candidates):
            print('candidate', i, 'type', type(cand))
            print('candidate attrs', [a for a in dir(cand) if not a.startswith('_')])
            print('candidate repr', repr(cand)[:2000])
except Exception as exc:
    print('exception', type(exc).__name__, exc)
