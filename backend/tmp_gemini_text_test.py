import sys
import os
from dotenv import load_dotenv
load_dotenv('.env')

sys.path.insert(0, os.path.abspath('.'))
from google.ai.generativelanguage_v1beta import ModelServiceClient, TextServiceClient
from google.ai.generativelanguage_v1beta.types import TextPrompt

api_key = os.getenv('GOOGLE_API_KEY')
print('API key present:', bool(api_key))
if not api_key:
    raise SystemExit('Missing GOOGLE_API_KEY')

model_names = [
    'models/gemini-2.5-flash',
    'models/gemini-flash-latest',
    'models/gemini-pro-latest',
    'models/gemini-3.5-flash',
]

client = ModelServiceClient(client_options={'api_key': api_key})
for model_name in model_names:
    try:
        model = client.get_model(name=model_name)
        print('MODEL FOUND:', model_name, model)
    except Exception as exc:
        print('MODEL ERROR', model_name, type(exc).__name__, exc)

prompt_text = 'Write exactly 2 concise resume improvement suggestions in JSON with key suggestions.'
text_client = TextServiceClient(client_options={'api_key': api_key})
for model_name in model_names:
    print('\n--- trying', model_name)
    try:
        prompt = TextPrompt(text=prompt_text)
        response = text_client.generate_text(model=model_name, prompt=prompt, temperature=0.2, max_output_tokens=120)
        print('RESPONSE TYPE', type(response))
        print('TEXT attr:', getattr(response, 'text', None))
        print('CANDIDATES attr:', getattr(response, 'candidates', None))
        if getattr(response, 'candidates', None):
            for i, candidate in enumerate(response.candidates):
                print('candidate', i, 'type', type(candidate))
                print('candidate attrs', [a for a in dir(candidate) if not a.startswith('_')])
                print('candidate repr', repr(candidate)[:1000])
    except Exception as exc:
        print('generate_text error', model_name, type(exc).__name__, exc)
