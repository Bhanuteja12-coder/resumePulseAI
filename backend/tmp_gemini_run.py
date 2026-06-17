import sys
import os
from dotenv import load_dotenv
load_dotenv('.env')

sys.path.insert(0, os.path.abspath('.'))

from google.ai.generativelanguage_v1beta import TextServiceClient, GenerativeServiceClient
from google.ai.generativelanguage_v1beta.types import TextPrompt

api_key = os.getenv('GOOGLE_API_KEY')
print('API key present:', bool(api_key))
if not api_key:
    raise SystemExit('Missing GOOGLE_API_KEY')

prompt_text = 'Write exactly 4 concise resume improvement suggestions in JSON with key suggestions.'

print('\n== TextServiceClient.generate_text ==')
try:
    text_client = TextServiceClient(client_options={'api_key': api_key})
    prompt = TextPrompt(text=prompt_text)
    response = text_client.generate_text(model='models/gemini-2.5-flash', prompt=prompt, temperature=0.2, max_output_tokens=200)
    print('response type:', type(response))
    print('response attrs:', [a for a in dir(response) if not a.startswith('_')])
    print('response text:', getattr(response, 'text', None))
    print('response candidates:', getattr(response, 'candidates', None))
    if getattr(response, 'candidates', None):
        for i, candidate in enumerate(response.candidates):
            print('candidate', i, 'type', type(candidate))
            print('candidate attrs', [a for a in dir(candidate) if not a.startswith('_')])
            print('candidate repr:', repr(candidate)[:2000])
except Exception as exc:
    print('TextService error:', type(exc).__name__, exc)

print('\n== GenerativeServiceClient.generate_content ==')
try:
    from google.ai.generativelanguage_v1beta.types import content
    gen_client = GenerativeServiceClient(client_options={'api_key': api_key})
    prompt_content = content.Content(text=prompt_text)
    response2 = gen_client.generate_content(model='models/gemini-2.5-flash', contents=[prompt_content])
    print('response2 type:', type(response2))
    print('response2 attrs:', [a for a in dir(response2) if not a.startswith('_')])
    print('response2 repr:', repr(response2)[:2000])
    print('response2 candidates:', getattr(response2, 'candidates', None))
    if getattr(response2, 'candidates', None):
        for i, candidate in enumerate(response2.candidates):
            print('candidate', i, 'type', type(candidate))
            print('candidate attrs', [a for a in dir(candidate) if not a.startswith('_')])
            print('candidate repr:', repr(candidate)[:2000])
except Exception as exc:
    print('GenerateContent error:', type(exc).__name__, exc)
