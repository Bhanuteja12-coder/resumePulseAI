import sys
import os
from dotenv import load_dotenv
load_dotenv('.env')

sys.path.insert(0, os.path.abspath('.'))

from google.ai.generativelanguage_v1beta.types import content, TextPrompt, GenerateContentRequest
import inspect

print('TextPrompt init:', inspect.signature(TextPrompt))
print('TextPrompt attrs:', [a for a in dir(TextPrompt) if not a.startswith('_')][:50])
print('Content init:', inspect.signature(content.Content))
print('Content attrs:', [a for a in dir(content.Content) if not a.startswith('_')][:50])
print('GenerateContentRequest init:', inspect.signature(GenerateContentRequest))
print('GenerateContentRequest attrs:', [a for a in dir(GenerateContentRequest) if not a.startswith('_')][:80])
try:
    print('TextPrompt SOURCE:\n', inspect.getsource(TextPrompt)[:1000])
except Exception as e:
    print('TextPrompt source error', e)
try:
    print('Content SOURCE:\n', inspect.getsource(content.Content)[:1000])
except Exception as e:
    print('Content source error', e)
