import sys
import os
sys.path.insert(0, os.path.abspath('.'))
from dotenv import load_dotenv
load_dotenv('.env')
from google.ai.generativelanguage_v1beta.types import generative_service, content

req_type = generative_service.GenerateContentRequest
print('GenerateContentRequest type', req_type)
print('GenerateContentRequest dir sample', [a for a in dir(req_type) if not a.startswith('_')][:100])
print('GenerateContentRequest.meta.fields keys', list(req_type.meta.fields.keys()))
print('GenerateContentRequest.meta.fields_by_number', req_type.meta.fields_by_number)
for name, field in req_type.meta.fields.items():
    print('field', name, 'type', type(field), field)

print('\ncontent.Content.meta.fields keys', list(content.Content.meta.fields.keys()))
print('content.Part.meta.fields keys', list(content.Part.meta.fields.keys()))
print('content.Content.meta.fields["parts"] type', content.Content.meta.fields['parts'])
print('content.Content.meta.fields["role"] type', content.Content.meta.fields['role'])
