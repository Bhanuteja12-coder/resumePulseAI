import json
import os
import re

import fitz
from docx import Document

DEFAULT_STOPWORDS = {
    'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and',
    'any', 'are', 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below',
    'between', 'both', 'but', 'by', 'could', 'did', 'do', 'does', 'doing', 'down',
    'during', 'each', 'few', 'for', 'from', 'further', 'had', 'has', 'have', 'having',
    'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'i',
    'if', 'in', 'into', 'is', 'it', 'its', 'itself', 'just', 'me', 'more', 'most',
    'my', 'myself', 'no', 'nor', 'not', 'now', 'of', 'off', 'on', 'once', 'only',
    'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 's', 'same',
    'she', 'should', 'so', 'some', 'such', 't', 'than', 'that', 'the', 'their',
    'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this',
    'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', 'we',
    'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will',
    'with', 'you', 'your', 'yours', 'yourself', 'yourselves'
}


def extract_text_from_pdf(file_path):
    text_lines = []
    with fitz.open(file_path) as doc:
        for page in doc:
            text_lines.append(page.get_text())
    return "\n".join(text_lines).strip()


def extract_text_from_docx(file_path):
    document = Document(file_path)
    text_lines = [paragraph.text for paragraph in document.paragraphs if paragraph.text.strip()]
    return "\n".join(text_lines).strip()


def extract_keywords(text, top_n=20):
    if not text:
        return []

    normalized_text = re.sub(r'[^a-z0-9\s]', ' ', text.lower())
    tokens = normalized_text.split()
    filtered_tokens = [token for token in tokens if token.isalpha() and token not in DEFAULT_STOPWORDS]
    if not filtered_tokens:
        return []

    from sklearn.feature_extraction.text import TfidfVectorizer

    document = ' '.join(filtered_tokens)
    vectorizer = TfidfVectorizer(token_pattern=r'(?u)\b\w+\b')
    tfidf_matrix = vectorizer.fit_transform([document])
    feature_names = vectorizer.get_feature_names_out()
    scores = tfidf_matrix.toarray()[0]
    keyword_scores = list(zip(feature_names, scores))
    keyword_scores.sort(key=lambda item: (-item[1], item[0]))
    return [keyword for keyword, _ in keyword_scores[:top_n]]


def extract_skill_keywords(text, top_n=20):
    return extract_keywords(text, top_n=top_n)


TOOL_KEYWORDS = {
    'aws', 'docker', 'kubernetes', 'git', 'github', 'gitlab', 'jira', 'jenkins',
    'terraform', 'ansible', 'bash', 'linux', 'ubuntu', 'windows', 'sql', 'nosql',
    'postgresql', 'mysql', 'mongodb', 'redis', 'elasticsearch', 'react', 'angular',
    'vue', 'django', 'flask', 'fastapi', 'tensorflow', 'pytorch', 'pandas', 'numpy',
    'spark', 'hadoop', 'aws', 'azure', 'gcp', 'docker', 'k8s', 'ci', 'cd', 'api',
    'rest', 'graphql', 'html', 'css', 'javascript', 'typescript', 'node', 'npm',
    'yarn', 'selenium', 'pytest', 'unittest', 'postgres', 'mysql', 'sqlserver',
    'oracle', 'redis', 'dockerfile', 'kafka', 'rabbitmq'
}

EXPERIENCE_KEYWORDS = {
    'experience', 'experienced', 'years', 'project', 'projects', 'lead', 'managed',
    'management', 'team', 'collaboration', 'collaborate', 'design', 'architecture',
    'production', 'deployed', 'deployment', 'support', 'maintenance', 'internship',
    'intern', 'research', 'analysis', 'analytics', 'customer', 'stakeholder',
    'interface', 'agile', 'scrum', 'kanban', 'mentor', 'training', 'quality',
    'optimization', 'performance', 'scale', 'scalable'
}

IGNORED_GAP_KEYWORDS = {
    'build', 'great', 'products', 'excellent', 'strong', 'good', 'best', 'skills',
    'responsible', 'responsibility', 'responsibilities', 'join', 'working', 'work',
    'ability', 'able', 'ensure', 'ensuring', 'help', 'helping', 'team', 'successful',
    'success', 'knowledge', 'understand', 'understanding', 'effective', 'efficient',
    'care', 'require', 'required', 'requirement', 'requirements', 'must', 'should'
}


def categorize_gap_keywords(keywords):
    gap = {
        'skills': [],
        'tools': [],
        'experience': [],
    }
    for keyword in keywords:
        if keyword in TOOL_KEYWORDS:
            gap['tools'].append(keyword)
        elif keyword in EXPERIENCE_KEYWORDS:
            gap['experience'].append(keyword)
        else:
            gap['skills'].append(keyword)
    return gap


def build_gemini_prompt(job_description_text, gap_analysis):
    return f"""You are a friendly resume coach.
Read the job description and the missing keyword gap analysis below.
Create exactly 4 concise, high-impact resume improvement suggestions that a candidate can apply.
Each suggestion should be written as a complete sentence and reference the job description or missing areas when useful.
Return only valid JSON with a single key named "suggestions" whose value is a list of strings.

Job Description:
{job_description_text}

Gap Analysis:
Skills: {', '.join(gap_analysis.get('skills', [])) or 'None'}
Tools: {', '.join(gap_analysis.get('tools', [])) or 'None'}
Experience: {', '.join(gap_analysis.get('experience', [])) or 'None'}
"""


def parse_gemini_response(response_text):
    if not response_text:
        return []

    json_text = None
    try:
        json_text = response_text.strip()
        return json.loads(json_text).get('suggestions', [])
    except json.JSONDecodeError:
        pass

    match = re.search(r"\{.*\}", response_text, re.S)
    if match:
        try:
            return json.loads(match.group(0)).get('suggestions', [])
        except json.JSONDecodeError:
            pass

    suggestions = []
    for line in response_text.splitlines():
        cleaned = line.strip().lstrip('-*').strip()
        if cleaned:
            suggestions.append(cleaned)
    return suggestions


def generate_gemini_suggestions(job_description_text, gap_analysis):

    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        return fallback_suggestions(gap_analysis)


    try:
        import google.generativeai as genai

        genai.configure(api_key=api_key)

        model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )


        prompt = build_gemini_prompt(
            job_description_text,
            gap_analysis
        )


        response = model.generate_content(prompt)

        return parse_gemini_response(
            response.text
        )


    except Exception as e:

        print("Gemini error:", e)

        return fallback_suggestions(
            gap_analysis
        )

def fallback_suggestions(gap):

    suggestions = []


    for skill in gap.get("skills", [])[:2]:
        suggestions.append(
            f"Add projects or experience demonstrating {skill} skills."
        )


    for tool in gap.get("tools", [])[:2]:
        suggestions.append(
            f"Include hands-on experience with {tool} in your resume."
        )


    for exp in gap.get("experience", [])[:1]:
        suggestions.append(
            f"Highlight your {exp} experience with measurable achievements."
        )


    if not suggestions:
        suggestions = [
            "Add more relevant technical projects.",
            "Improve your resume keywords based on the job description.",
            "Highlight measurable achievements.",
            "Tailor your experience section for this role."
        ]


    return suggestions[:4]


def extract_gap_analysis(resume_keywords, job_description_text, top_n=30):
    job_keywords = extract_keywords(job_description_text, top_n=top_n)
    resume_set = set(resume_keywords or [])
    missing = [
        keyword for keyword in job_keywords
        if keyword not in resume_set and keyword not in IGNORED_GAP_KEYWORDS
    ]
    return categorize_gap_keywords(missing)


def extract_text_from_file(file_path):
    extension = os.path.splitext(file_path)[1].lower()
    if extension == ".pdf":
        return extract_text_from_pdf(file_path)
    if extension == ".docx":
        return extract_text_from_docx(file_path)
    return ""
