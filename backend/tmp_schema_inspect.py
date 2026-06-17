import sys
import os
from dotenv import load_dotenv
load_dotenv('.env')

sys.path.insert(0, os.path.abspath('.'))

from google.ai.generativelanguage_v1beta.types import content, TextPrompt, GenerateContentRequest, GenerateTextRequest

print('TextPrompt type', TextPrompt)
print('TextPrompt init', TextPrompt.__init__.__code__.co_varnames)
print('TextPrompt dir', [a for a in dir(TextPrompt) if not a.startswith('_')][:80])
try:
    tp = TextPrompt(text='hello')
    print('TextPrompt instance', tp)
    print('tp dict', tp.to_dict() if hasattr(tp, 'to_dict') else 'no to_dict')
except Exception as e:
    print('TextPrompt init error', type(e).__name__, e)

print('Content type', content.Content)
print('Content dir', [a for a in dir(content.Content) if not a.startswith('_')][:80])
try:
    c = content.Content(text='hello')
    print('Content init ok', c)
    print('Content dict', c.to_dict() if hasattr(c, 'to_dict') else 'no to_dict')
except Exception as e:
    print('Content init error', type(e).__name__, e)

try:
    c2 = content.Content()
    setattr(c2, 'text', 'hello')
    print('setattr text ok', c2)
    print('c2 dict', c2.to_dict() if hasattr(c2, 'to_dict') else 'no to_dict')
except Exception as e:
    print('setattr text error', type(e).__name__, e)

print('GenerateContentRequest type', GenerateContentRequest)
print('GenerateContentRequest dir', [a for a in dir(GenerateContentRequest) if not a.startswith('_')][:80])
try:
    r = GenerateContentRequest(model='models/gemini-2.5-flash', contents=[])
    print('request ok', r)
    print('request dict', r.to_dict() if hasattr(r, 'to_dict') else 'no to_dict')
except Exception as e:
    print('request init error', type(e).__name__, e)
