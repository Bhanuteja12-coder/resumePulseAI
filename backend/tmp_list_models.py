import sys
import os
from dotenv import load_dotenv
load_dotenv('.env')

sys.path.insert(0, os.path.abspath('.'))

from google.ai.generativelanguage_v1beta import ModelServiceClient

api_key = os.getenv('GOOGLE_API_KEY')
print('API key present:', bool(api_key))
if not api_key:
    raise SystemExit('Missing GOOGLE_API_KEY')

client = ModelServiceClient(client_options={'api_key': api_key})
try:
    response = client.list_models()
    for i, model in enumerate(response):
        print(i+1, model.name)
        if i >= 49:
            break
except Exception as e:
    import traceback
    traceback.print_exc()
