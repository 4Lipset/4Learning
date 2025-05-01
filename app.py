
import streamlit as st

# Learning Production Designer Web App

def generate_learning_production(theme, subject, weeks, grade, identity=None):
    title = f"{theme.title()} Through {subject}"
    identity_phrase = f" from the lens of {identity}" if identity else ""
    question = f"How can {grade} students use {subject.lower()} to address {theme.lower()}{identity_phrase}?"

    plan = [
        f"Week 1: Research the roots of {theme}. Include perspectives from {identity or 'diverse student backgrounds'}.",
        f"Week 2: Explore tools in recording/media arts. Begin drafting concepts.",
        f"Week 3: Build the project with feedback.",
        f"Week 4: Finalize and present the production."
    ]

    assessment = {
        "Academic": "Aligned rubric and standards",
        "SEL": "HOPE Survey, journaling, peer review",
        "Civic Impact": "Partner feedback and presentation impact"
    }

    sel = {
        "Identity Work": "Self and community reflection",
        "Agency": "Student-driven design",
        "Community": "Involvement from local partners"
    }

    resources = {
        "Tech": "Studio tools, laptops",
        "People": "Facilitators, artists, mentors",
        "Materials": "Project supplies, creative tools"
    }

    prompts = [
        "What does this theme mean to you?",
        "How does your background inform your work?",
        "What message do you want to share?",
        "How have you grown through this process?"
    ]

    summary = f"""
TITLE: {title}
DRIVING QUESTION: {question}

WEEKLY OUTLINE:
{chr(10).join('- ' + p for p in plan)}

ASSESSMENTS:
Academic: {assessment['Academic']}
SEL: {assessment['SEL']}
Civic: {assessment['Civic Impact']}

SEL & CIVIC COMPONENTS:
{chr(10).join(f'{k}: {v}' for k, v in sel.items())}

RESOURCES:
{chr(10).join(f'{k}: {v}' for k, v in resources.items())}

STUDENT REFLECTION:
{chr(10).join('- ' + q for q in prompts)}
"""

    return summary

# Streamlit UI
st.title("Learning Production Designer")

with st.form("builder"):
    theme = st.text_input("Theme (e.g., Environmental Justice)")
    subject = st.selectbox("Subject Area", ["Science", "Language Arts", "Humanities"])
    weeks = st.slider("Project Duration (weeks)", 1, 12, 4)
    grade = st.text_input("Grade Level (e.g., 11th grade)")
    identity = st.text_input("Identity Focus (optional)")
    generate = st.form_submit_button("Create Learning Production")

if generate:
    plan = generate_learning_production(theme, subject, weeks, grade, identity)
    st.subheader("Learning Production Plan")
    st.text_area("Generated Plan", plan, height=500)
    st.download_button("Download Plan", plan, file_name="learning_production_plan.txt")
