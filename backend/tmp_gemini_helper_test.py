import sys
import os
from dotenv import load_dotenv
load_dotenv('.env')

sys.path.insert(0, os.path.abspath('.'))
from resumes.utils import generate_gemini_suggestions

job_desc = 'django python mongodb react'
gap_analysis = {'skills': [], 'tools': ['mongodb'], 'experience': []}
print('calling helper...')
res = generate_gemini_suggestions(job_desc, gap_analysis)
print('result type', type(res))
print('result', res)
