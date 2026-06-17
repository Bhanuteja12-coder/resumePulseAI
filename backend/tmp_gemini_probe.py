import sys
import os
import inspect
from dotenv import load_dotenv
load_dotenv('.env')
os.environ.setdefault('GOOGLE_API_KEY', os.getenv('GOOGLE_API_KEY', ''))

sys.path.insert(0, os.path.abspath('.'))

import google.ai.generativelanguage_v1beta as gal
from google.ai.generativelanguage_v1beta.types import TextPrompt, GenerateTextRequest, GenerateContentRequest

print('== Gemini SDK probe ==')
print('GOOGLE_API_KEY present:', bool(os.getenv('GOOGLE_API_KEY')))
print('gal attrs sample:', [a for a in dir(gal) if 'ServiceClient' in a or 'Request' in a or 'TextPrompt' in a or 'Generate' in a][:80])
print('has TextServiceClient:', hasattr(gal, 'TextServiceClient'))
print('has GenerativeServiceClient:', hasattr(gal, 'GenerativeServiceClient'))
print('TextServiceClient methods:', [m for m in dir(gal.TextServiceClient) if not m.startswith('_')] if hasattr(gal, 'TextServiceClient') else [])
print('GenerativeServiceClient methods:', [m for m in dir(gal.GenerativeServiceClient) if not m.startswith('_')] if hasattr(gal, 'GenerativeServiceClient') else [])
print('GenerateTextRequest init args:', GenerateTextRequest.__init__.__code__.co_varnames)
print('GenerateContentRequest init args:', GenerateContentRequest.__init__.__code__.co_varnames)
print('TextPrompt init args:', TextPrompt.__init__.__code__.co_varnames)
print('TextPrompt dir sample:', [a for a in dir(TextPrompt) if not a.startswith('_')][:40])
print('GenerateTextRequest dir sample:', [a for a in dir(GenerateTextRequest) if not a.startswith('_')][:40])

# Try constructing objects to see how they print
try:
    p = TextPrompt(text='hello')
    print('TextPrompt created:', p)
except Exception as e:
    print('TextPrompt create failed:', type(e).__name__, e)

try:
    r = GenerateTextRequest(model='models/gemini-2.5-flash', prompt=p, temperature=0.2, max_output_tokens=50)
    print('GenerateTextRequest created:', r)
except Exception as e:
    print('GenerateTextRequest create failed:', type(e).__name__, e)

try:
    c = GenerateContentRequest(model='models/gemini-2.5-flash', contents=[])
    print('GenerateContentRequest created:', c)
except Exception as e:
    print('GenerateContentRequest create failed:', type(e).__name__, e)

print('\n== service client signatures ==')
if hasattr(gal, 'TextServiceClient'):
    print('TextServiceClient.generate_text sig:', inspect.signature(gal.TextServiceClient.generate_text))
if hasattr(gal, 'GenerativeServiceClient'):
    print('GenerativeServiceClient.generate_content sig:', inspect.signature(gal.GenerativeServiceClient.generate_content))
print('== done ==')
