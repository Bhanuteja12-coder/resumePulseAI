import sys
import os
from dotenv import load_dotenv
load_dotenv('.env')

sys.path.insert(0, os.path.abspath('.'))
from google.ai.generativelanguage_v1beta.types import content

print('Part type:', content.Part)
print('Part dir sample:', [a for a in dir(content.Part) if not a.startswith('_')][:100])
print('Part.meta fields:', content.Part.meta.fields)
print('Part.meta fields_by_number:', content.Part.meta.fields_by_number)
for k,v in content.Part.meta.fields.items():
    print('field', k, type(v), v)

print('\nContent.meta.fields keys', list(content.Content.meta.fields.keys()))
print('Content.meta.fields_by_number', content.Content.meta.fields_by_number)

# inspect response classes
import google.ai.generativelanguage_v1beta as gal
from google.ai.generativelanguage_v1beta.types import generative_service
print('\nGenerateContentResponse type:', generative_service.GenerateContentResponse)
print('GenerateContentResponse dir sample:', [a for a in dir(generative_service.GenerateContentResponse) if not a.startswith('_')][:100])
print('GenerateContentResponse meta fields', generative_service.GenerateContentResponse.meta.fields)
print('GenerateContentResponse fields keys', list(generative_service.GenerateContentResponse.meta.fields.keys()))

print('\nCandidate type in response?')
print('GenerateContentResponse.candidates type maybe', type(getattr(generative_service.GenerateContentResponse, 'candidates', None)))

# inspect candidate class if available
if hasattr(generative_service, 'GenerateContentResponse'):
    for name in dir(generative_service):
        if 'Candidate' in name or 'Content' in name:
            print('generative_service attr', name)
