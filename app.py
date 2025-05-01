import streamlit as st
from io import BytesIO
from docx import Document

# Placeholder: In a full version, these would be dynamically mapped based on subject, grade, and state
STANDARDS = {
    "Common Core": {
        "Science": [
            "HS-ETS1-1: Analyze a major global challenge...",
            "HS-PS1-3: Plan and conduct an investigation..."
        ],
        "Language Arts": [
            "CCSS.ELA-LITERACY.RI.11-12.1: Cite strong textual evidence...",
            "CCSS.ELA-LITERACY.W.11-12.7: Conduct sustained research projects..."
        ],
        "Humanities": [
            "CCSS.ELA-LITERACY.RH.11-12.1: Cite specific textual evidence to support analysis of primary and secondary sources...",
            "CCSS.ELA-LITERACY.RH.11-12.9: Integrate information from diverse sources..."
        ]
    },
    "Common Core": {
        "Science": [
            "HS-ETS1-1: Analyze a major global challenge...",
            "HS-PS1-3: Plan and conduct an investigation..."
        ],
        "Language Arts": [
            "CCSS.ELA-LITERACY.RI.11-12.1: Cite strong textual evidence...",
            "CCSS.ELA-LITERACY.W.11-12.7: Conduct sustained research projects..."
        ]
    },
    "CA": {
        "Science": ["CA NGSS HS-ETS1-2", "CA NGSS HS-PS1-4"],
        "Language Arts": ["CA CCSS.ELA-LITERACY.W.11-12.3", "CA CCSS.ELA-LITERACY.SL.11-12.4"],
        "Humanities": ["CA HSS.11.1: Analyze the effects of WWII on domestic policies", "CA HSS.11.11: Evaluate postwar economic and social changes"]
    },
    "TX": {
        "Science": ["TEKS SCI.11.B", "TEKS SCI.12.A"],
        "Language Arts": ["TEKS ELA.11.11A", "TEKS ELA.12.10C"],
        "Humanities": ["TEKS SS.11.24A: Analyze historical and contemporary policies", "TEKS SS.12.16B: Explain civic engagement through the lens of federal policy"]
    },
    "NY": {
        "Science": ["NYSSLS HS-LS2-3", "NYSSLS HS-ESS3-4"],
        "Language Arts": ["NYS ELA.11.R.1", "NYS ELA.12.W.2"],
        "Humanities": ["NYSS.11.2a: Examine key historical ideas of reform movements", "NYSS.12.G3a: Evaluate civic responsibilities through policy"]
    },
    "Other": {
        "Science": ["Local Standard SCI.1"],
        "Language Arts": ["Local Standard ELA.1"],
        "Humanities": ["Local Standard HUM.1"]
    }
}

def create_docx_export(content, title):
    doc = Document()
    doc.add_heading("Learning Production Unit Plan", 0)
    doc.add_paragraph(f"Unit Title: {title}")
    doc.add_paragraph("\n")
    doc.add_page_break()
    for section in content:
        doc.add_heading(section["title"], level=1)
        doc.add_paragraph(section["body"])
    doc.add_page_break()
    doc.add_heading("Appendices", level=1)
    doc.add_paragraph("Rubric and Exhibition Checklist available upon request or will be added dynamically.")
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer

def generate_lesson(day, week, theme, subject, tools, sel_skill, standard, selected_additional):
    # Select up to two complementary standards
    additional_standards_pool = [
        "National Core Arts Standards: Creating – Anchor Standard 1",
        "ISTE Standard for Students 6: Creative Communicator",
        "NAfME Music Standard MU:Cr1.1.HS",
        "Entrepreneurship Standard ES.01: Recognize characteristics of successful entrepreneurs"
    ]
    selected_additional = []
    for area in selected_additional:
        try:
            std_list = STANDARDS.get(state, {}).get(area, [])
            if std_list:
                selected_additional.append(std_list[0])
        except:
            continue
    if len(selected_additional) < 2:
        selected_additional += ["Local interdisciplinary standard"] * (2 - len(selected_additional))
    # Expand with interdisciplinary standards
    art_std = "National Core Arts Standards: Creating – Anchor Standard 1"
    tech_std = "ISTE Standard for Students 6: Creative Communicator"
    music_std = "NAfME Music Standard MU:Cr1.1.HS"  # Example for music
    entr_std = "Entrepreneurship Standard ES.01: Recognize characteristics of successful entrepreneurs"
    extra_standards = [art_std, tech_std, music_std, entr_std]
    return {
        "title": f"Lesson Plan – Week {week}, Day {day}",
        "body": f"""
Essential Question: How does {theme} impact our local and global communities?

Standards Addressed:
- [{standard}](https://www.google.com/search?q={standard.replace(' ', '+')})
- [{selected_additional[0]}](https://www.google.com/search?q={selected_additional[0].replace(' ', '+')})
- [{selected_additional[1]}](https://www.google.com/search?q={selected_additional[1].replace(' ', '+')})})
- [{extra_standards[0]}](https://www.google.com/search?q={extra_standards[0].replace(' ', '+')})
- [{extra_standards[1]}](https://www.google.com/search?q={extra_standards[1].replace(' ', '+')})
- [{extra_standards[2]}](https://www.google.com/search?q={extra_standards[2].replace(' ', '+')})
- [{extra_standards[3]}](https://www.google.com/search?q={extra_standards[3].replace(' ', '+')})})

Learning Objectives:
- Students will understand {theme.lower()} through applied {subject.lower()} concepts.
- Students will develop technical fluency using {', '.join(tools)}.
- Students will build {sel_skill} skills by collaborating and reflecting.

Hook:
- Begin with a short podcast clip about a personal story related to {theme}.

Activities:
- Interactive mini-lesson introducing a core concept
- Collaborative research or recording session using {', '.join(tools)}
- Guided group reflection on both process and product
- Exhibition prep activity: {['Identify authentic audience & brainstorm event concepts ([Run-of-Show Template](https://docs.google.com/document/d/1P-RUNSHOW-LINK))', 'Develop storytelling arc and create preliminary assets ([Storyboarding Template](https://docs.google.com/document/d/1P-STORYBOARD-LINK))', 'Finalize production roles and schedule rehearsal times ([Role Assignment Tool](https://docs.google.com/spreadsheets/d/1P-ROLESHEET-LINK))', 'Run dress rehearsals and collect peer feedback ([Rehearsal Checklist](https://docs.google.com/document/d/1P-REHEARSAL-CHECKLIST-LINK))', 'Refine final deliverables and promote the event ([Promotion Plan Template](https://docs.google.com/document/d/1P-PROMOTION-PLAN-LINK))'][(week - 1) % 5]}

Assessment:
- Formative: Exit ticket reflecting on technical, social, and content goals
- Summative: Artifact captured from recording or design process

Closure:
- Week {week} reflection prompt: “{['What challenged your perspective today?', 'How did today’s work deepen your understanding of the community issue?', 'What part of your identity influenced your work today?', 'How did your collaboration shape the outcome?', 'What connection can you draw between your technical work and your civic goals?'][(week - 1) % 5]}”

UDL & EDI:
- Multiple means of engagement: visual/audio prompts, written templates, peer modeling
- Materials reflect diverse cultural perspectives
"""
    }

def generate_unit(theme, subject, weeks, grade, identity, state, environment, selected_complements):
    title = f"{theme.title()} Through {subject}"
    tools = ["microphones", "audio software", "cameras"] if subject == "Science" else ["notebooks", "digital editors", "storyboarding tools"]
    standards = STANDARDS.get(state, STANDARDS["Other"]).get(subject, ["Local Standards TBD"])
    plan = []

    # Unit overview
    plan.append({"title": "Unit Overview", "body": f"This unit engages students in the theme of {theme} with a focus on civic application and production in a {subject} context. Students will work within a {environment.lower()} using professional tools to develop their project. The unit scaffolds learning toward a final public-facing product and lasts {weeks} weeks, targeting {grade} students."})

    # Daily lessons
    for week in range(1, weeks + 1):
        sel_focus = ["Self-awareness", "Self-management", "Social awareness", "Relationship skills", "Responsible decision-making"][(week - 1) % 5]
        standard = standards[(week - 1) % len(standards)]
        for day in range(1, 6):
            plan.append(generate_lesson(day, week, theme, subject, tools, sel_focus, standard, selected_complements))

    # Culmination & Rubric
    plan.append({
        "title": "Culminating Project & Rubric",
        "body": "Students will present a final product addressing the driving question through public exhibition.

**Rubric**
| Category | Exemplary (4) | Proficient (3) | Developing (2) | Beginning (1) |
|----------|----------------|----------------|----------------|---------------|
| Content Accuracy | Thorough, fact-based and insightful | Mostly accurate with some depth | Basic understanding shown | Limited accuracy or detail |
| Production Quality | Polished, professional, creatively executed | Clear and functional, some flair | Understandable but rough | Disorganized or incomplete |
| Civic Impact | Strong, authentic audience engagement and relevance | Audience-aware and relevant | Limited civic context | Minimal/no civic consideration |
| SEL Reflection | Deep, personal insights; strong connection to project | Honest reflection with meaningful connections | Surface-level insights | Lacks reflection or connection |"
    })
    plan.append({
        "title": "Exhibition Checklist",
        "body": "✔ A clearly defined public audience is identified and confirmed to receive student work
✔ A detailed run-of-show is created, outlining all roles and presentation moments
✔ Each student has a defined production role and is prepared to carry it out
✔ Students have participated in rehearsals or practice sessions
✔ All venue-related logistics (location, permissions, equipment needs) are confirmed
✔ Media documentation plans (video, audio, photo) are in place
✔ Accessibility and community outreach efforts are integrated where appropriate"
    })
    return title, plan

st.title("📘 Learning Production Generator")

with st.form("unit_form"):
    selected_complements = st.multiselect("Select up to TWO complementary subject areas to integrate standards from:", ["Art", "Technology", "Music", "Entrepreneurship"], max_selections=2)
    environment = st.selectbox("Production Environment", [
        "Recording Studio",
        "Photo/Video Studio",
        "Podcasting Studio",
        "Mobile Recording Studio",
        "Other tools (e.g., cameras, tripods, lighting kits, backdrops)"
    ])
    theme = st.text_input("Theme (e.g. Housing Insecurity)")
    subject = st.selectbox("Subject Area", ["Science", "Language Arts", "Humanities"])
    grade = st.text_input("Grade Level (e.g. 11th grade)")
    identity = st.text_input("Identity Focus (e.g. Black youth, Indigenous students, LGBTQIA+)")
    weeks = st.slider("Unit Length (weeks)", 2, 6, 4)
    state = st.selectbox("Standards Framework", ["Common Core", "CA", "TX", "NY", "Other"])
    submitted = st.form_submit_button("Generate Full Unit Plan")

if submitted:
    # Include environment in unit generation
    title, content = generate_unit(theme, subject, weeks, grade, identity, state, environment, selected_complements)
    st.subheader("📄 Unit Title: " + title)
    for section in content:
        st.markdown(f"### {section['title']}")
        st.markdown(section['body'])
    buffer = create_docx_export(content, title)
    st.download_button("📥 Download Unit Plan (DOCX)", data=buffer, file_name=f"{title.replace(' ', '_')}.docx")
