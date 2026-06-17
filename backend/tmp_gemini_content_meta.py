import sys
import os
sys.path.insert(0, os.path.abspath('.'))
from dotenv import load_dotenv
load_dotenv('.env')
from google.ai.generativelanguage_v1beta.types import content

print('content module attrs sample:', [a for a in dir(content) if not a.startswith('_')])
print('\nContent class type:', content.Content)
print('Content class dir sample:', [a for a in dir(content.Content) if not a.startswith('_')][:100])
print('\nContent.meta:', getattr(content.Content, 'meta', None))
print('Content.meta dir:', [a for a in dir(content.Content.meta) if not a.startswith('_')])
print('Content.meta repr:', repr(content.Content.meta))
print('Content.meta type', type(content.Content.meta))

# try introspection on fields
if hasattr(content.Content.meta, 'fields'):
    print('Content.meta.fields:', content.Content.meta.fields)
    print('Content.meta.fields len', len(content.Content.meta.fields))
    for field in content.Content.meta.fields:
        print('field', field.name, field)

if hasattr(content.Content.meta, '_fields'):
    print('Content.meta._fields:', content.Content.meta._fields)

if hasattr(content.Content.meta, 'as_dict'):
    print('Content.meta.as_dict()', content.Content.meta.as_dict())

print('\nTrying to create raw Content with mapping:')
try:
    c = content.Content({'text': 'hello'})
    print('created raw', c)
    print('raw to_dict', c.to_dict())
except Exception as exc:
    print('raw create error', type(exc).__name__, exc)

print('\nTrying to create raw Content with value:')
for k in ['text', 'value', 'content', 'input', 'items', 'type']:
    try:
        c = content.Content({k: 'hello'})
        print('created raw', k, c)
        print('to_dict', c.to_dict())
    except Exception as exc:
        print('raw create', k, 'error', type(exc).__name__, exc)
