import sys
import os
from dotenv import load_dotenv
load_dotenv('.env')
sys.path.insert(0, os.path.abspath('.'))
import google.ai.generativelanguage_v1beta as gal
from google.ai.generativelanguage_v1beta.types import TextPrompt, GenerateTextRequest

api_key = os.getenv('GOOGLE_API_KEY')
print('API_KEY_PRESENT', bool(api_key))
client = gal.TextServiceClient(client_options={'api_key': api_key})
prompt = TextPrompt(text='Write exactly 4 resume improvement suggestions in JSON with key suggestions.')
request = GenerateTextRequest(model='models/gemini-2.5-flash', prompt=prompt, temperature=0.2, max_output_tokens=120)
response = client.generate_text(request=request)
print('RESPONSE_TYPE', type(response))
print('RESPONSE_DIR', [a for a in dir(response) if not a.startswith('_')])
print('RESPONSE_REPR', repr(response)[:3000])
print('TEXT', getattr(response, 'text', None))
print('CANDIDATES', getattr(response, 'candidates', None))
if getattr(response, 'candidates', None):
    for i, candidate in enumerate(response.candidates):
        print(f'Candidate {i}', candidate)
        if hasattr(candidate, 'content'):
            print('content', candidate.content)
