import streamlit as st
import base64
from io import BytesIO
from docx import Document

"""
Purpose:
Support educators in designing interdisciplinary, social justice-oriented learning productions aligned with academic standards, CASEL-based SEL, civic engagement, and identity development.
"""

CASEL_CORE_COMPETENCIES = [
    "Self-awareness",
    "Self-management",
    "Social awareness",
    "Relationship skills",
    "Responsible decision-making"
]

STATE_STANDARDS_EXAMPLES = {
    "CA": "Aligned with A-G requirements & CA CTE Pathways",
    "NY": "NYS Standards and CDOS",
    "TX": "TEKS + CTE standards",
    "MN": "Minnesota Academic Standards",
    "Common Core": "CCSS-aligned skills and interdisciplinary anchor standards",
    "Other": "Locally defined learning outcomes"
}

def create_docx_export(content, title):
    doc = Document()
    doc.add_heading(title, 0)
    for line in content.strip().split('\n'):
        doc.add_paragraph(line)
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer

def design_learning_production(theme, subject_area, duration_weeks, grade_level, student_identity_focus=None, state_code="Other"):
    title = f"{theme.title()} Through {subject_area}"
    identity_phrase = f" from the lens of {student_identity_focus}" if student_identity_focus else ""
    driving_question = f"How can {grade_level} students use {subject_area.lower()} to understand and impact the issue of {theme.lower()}{identity_phrase}?"

    weekly_breakdown = []
    for week in range(1, duration_weeks + 1):
        weekly_breakdown.append(
            f"Week {week}: Engage in {theme}-based exploration via research, media tools, and collaborative production. Emphasize CASEL SEL focus: {CASEL_CORE_COMPETENCIES[week % len(CASEL_CORE_COMPETENCIES)]}."
        )

    reflection_prompts = [
        f"Post-Week {i+1}: How did this week's activity affect your understanding of self and your community?"
        for i in range(duration_weeks)
    ]

    assessment = {
        "Academic": STATE_STANDARDS_EXAMPLES.get(state_code, STATE_STANDARDS_EXAMPLES["Other"]),
        "SEL": f"Aligned with CASEL: {', '.join(CASEL_CORE_COMPETENCIES)}",
        "Civic Impact": "Real-world presentation, feedback, and social engagement"
    }

    sel_and_civic = {
        "Identity Work": "Cultural storytelling, identity mapping, expressive media",
        "Voice & Agency": "Student-driven content and role selection",
        "Community Engagement": "Authentic partner dialogue and event facilitation"
    }

    resources = {
        "Tech": "Studio equipment, editing tools",
        "People": "Facilitators, creatives, collaborators",
        "Materials": "Mixed media, journaling supplies, event tools"
    }

    summary = f"""
TITLE: {title}
DRIVING QUESTION: {driving_question}

WEEKLY BREAKDOWN:
{chr(10).join(f'- {week}' for week in weekly_breakdown)}

ASSESSMENT OVERVIEW:
Academic: {assessment['Academic']}
SEL: {assessment['SEL']}
Civic Impact: {assessment['Civic Impact']}

SEL & CIVIC INTEGRATION:
Identity Work: {sel_and_civic['Identity Work']}
Voice & Agency: {sel_and_civic['Voice & Agency']}
Community Engagement: {sel_and_civic['Community Engagement']}

RESOURCES:
Tech: {resources['Tech']}
People: {resources['People']}
Materials: {resources['Materials']}

STUDENT REFLECTION OPPORTUNITIES:
{chr(10).join(f'- {prompt}' for prompt in reflection_prompts)}
"""

    return summary, title

st.title("🎓 Learning Production Designer")

with st.form("learning_production_form"):
    theme = st.text_input("Theme (e.g. Climate Justice)")
    subject_area = st.selectbox("Subject Area", ["Science", "Language Arts", "Humanities"])
    duration_weeks = st.slider("Duration (weeks)", min_value=1, max_value=12, value=4)
    grade_level = st.text_input("Grade Level (e.g. 11th grade)")
    identity = st.text_input("Student Identity Focus (optional)")
    state_code = st.selectbox("Standards Alignment", ["CA", "NY", "TX", "MN", "Common Core", "Other"])
    submitted = st.form_submit_button("Generate Plan")

if submitted:
    output, plan_title = design_learning_production(theme, subject_area, duration_weeks, grade_level, identity, state_code)
    st.subheader("📄 Generated Learning Production Plan")
    st.text_area("Plan Output", output, height=600)
    st.download_button("📄 Download as TXT", output, file_name="learning_production_plan.txt")

    # Microsoft Word export
    docx_buffer = create_docx_export(output, plan_title)
    st.download_button("📄 Download as DOCX", data=docx_buffer, file_name="learning_production_plan.docx")
