import sys
import os
sys.path.insert(0, os.path.abspath('.'))
from dotenv import load_dotenv
load_dotenv('.env')
from google.ai.generativelanguage_v1beta.types import content, TextPrompt, GenerateTextRequest, GenerateContentRequest

print('Content type', content.Content)
print('Content DIR sample', [a for a in dir(content.Content) if not a.startswith('_')])
print('Content pb', getattr(content.Content, 'pb', None))
if getattr(content.Content, 'pb', None) is not None:
    print('Content fields', [f.name for f in content.Content.pb.DESCRIPTOR.fields])

print('TextPrompt pb', getattr(TextPrompt, 'pb', None))
if getattr(TextPrompt, 'pb', None) is not None:
    print('TextPrompt fields', [f.name for f in TextPrompt.pb.DESCRIPTOR.fields])

print('GenerateContentRequest pb', getattr(GenerateContentRequest, 'pb', None))
if getattr(GenerateContentRequest, 'pb', None) is not None:
    print('GenerateContentRequest fields', [f.name for f in GenerateContentRequest.pb.DESCRIPTOR.fields])

print('available content module attrs', [a for a in dir(content) if not a.startswith('_')])
print('available top-level attrs', [a for a in dir(__import__("google.ai.generativelanguage_v1beta.types")) if 'Content' in a or 'Prompt' in a or 'Generate' in a][:120])
