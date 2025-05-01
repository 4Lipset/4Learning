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
        ],
        "Art": [
            "CCSS.ART.11-12.CR.1: Generate and conceptualize artistic ideas and work",
            "CCSS.ART.11-12.CR.2: Organize and develop artistic ideas and work"
        ],
        "Technology": [
            "ISTE 6a: Students choose the appropriate platforms and tools...",
            "ISTE 6b: Students create original works..."
        ],
        "Music": [
            "NAfME MU:Cr1.1.HS1: Compose and arrange music...",
            "NAfME MU:Pr6.1.HS1: Evaluate and refine musical work..."
        ],
        "Entrepreneurship": [
            "ENT.C1.1: Recognize characteristics of successful entrepreneurs",
            "ENT.C2.2: Develop a business plan..."
        ]
    }
}

# The rest of your application continues below

# Utility to safely link standards

def generate_standard_links(standards):
    links = []
    for std in standards:
        url = std.replace(' ', '+')
        links.append(f"- [{std}](https://www.google.com/search?q={url})")
    return '\n'.join(links)  # Fixed newline join
def generate_lesson_standards(core, additional):
    all_standards = [core] + additional
    return generate_standard_links(all_standards)

def generate_lesson(day, week, theme, subject, tools, sel_skill, core_standard, additional_standards):
    standard_links = generate_lesson_standards(core_standard, additional_standards)
    return {
        "title": f"Lesson Plan – Week {week}, Day {day}",
        "body": f"""
Essential Question: How does {theme} impact our local and global communities?

Standards Addressed:
{standard_links}

Learning Objectives:
- Understand {theme.lower()} through applied {subject.lower()} concepts.
- Develop technical fluency using {', '.join(tools)}.
- Strengthen {sel_skill} through collaboration and reflection.

Hook:
- Start with a story, image, or audio clip related to {theme}.

Activities:
- Core concept mini-lesson
- Collaborative production or design work using {', '.join(tools)}
- Peer feedback or journaling
- Exhibition prep: {['Identify audience & brainstorm event ideas (Run-of-Show Template)', 'Draft narrative structure & create content (Storyboard Template)', 'Finalize roles & logistics (Role Assignment Tool)', 'Run full rehearsal & get feedback (Rehearsal Checklist)', 'Prepare promo & finalize output (Promotion Plan Template)'][(week - 1) % 5]}

Assessment:
- Exit ticket + product check-in

Closure:
- {['What challenged your thinking today?', 'What impact do you hope your work will have?', 'What do you need from peers or audience next?', 'How are you showing up in your role?', 'What surprised you about your process?'][(week - 1) % 5]}
"""
    }

def generate_unit(theme, subject, weeks, grade, identity, state, environment, selected_complements):
    title = f"{theme.title()} Through {subject}"
    tools = ["microphones", "audio software", "cameras"] if subject == "Science" else ["notebooks", "digital editors", "storyboarding tools"]
    core_standards = STANDARDS.get(state, {}).get(subject, ["Local Standards TBD"])

    # Pull first standards from selected complementary subjects
    complementary_standards = []
    for area in selected_complements:
        comp_std_list = STANDARDS.get(state, {}).get(area, [])
        if comp_std_list:
            complementary_standards.append(comp_std_list[0])

    plan = []
    plan.append({"title": "Unit Overview", "body": f"This unit engages students in the theme of {theme} with a focus on civic application and production in a {subject} context. Students will work within a {environment.lower()} using professional tools to develop their project. The unit scaffolds learning toward a final public-facing product and lasts {weeks} weeks, targeting {grade} students."})

    for week in range(1, weeks + 1):
        sel_focus = ["Self-awareness", "Self-management", "Social awareness", "Relationship skills", "Responsible decision-making"][(week - 1) % 5]
        core_std = core_standards[(week - 1) % len(core_standards)]
        for day in range(1, 6):
            lesson = generate_lesson(day, week, theme, subject, tools, sel_focus, core_std, complementary_standards)
            plan.append(lesson)

    plan.append({"title": "Culminating Project & Rubric", "body": "Students will present a final product addressing the driving question through public exhibition.

**Rubric**
| Category | Exemplary (4) | Proficient (3) | Developing (2) | Beginning (1) |
|----------|----------------|----------------|----------------|---------------|
| Content Accuracy | Thorough, fact-based and insightful | Mostly accurate with some depth | Basic understanding shown | Limited accuracy or detail |
| Production Quality | Polished, professional, creatively executed | Clear and functional, some flair | Understandable but rough | Disorganized or incomplete |
| Civic Impact | Strong, authentic audience engagement and relevance | Audience-aware and relevant | Limited civic context | Minimal/no civic consideration |
| SEL Reflection | Deep, personal insights; strong connection to project | Honest reflection with meaningful connections | Surface-level insights | Lacks reflection or connection |"})

    plan.append({"title": "Exhibition Checklist", "body": "✔ A clearly defined public audience is identified and confirmed to receive student work
✔ A detailed run-of-show is created, outlining all roles and presentation moments
✔ Each student has a defined production role and is prepared to carry it out
✔ Students have participated in rehearsals or practice sessions
✔ All venue-related logistics (location, permissions, equipment needs) are confirmed
✔ Media documentation plans (video, audio, photo) are in place
✔ Accessibility and community outreach efforts are integrated where appropriate"})

    return title, plan

st.title("✅ Learning Production GPT – Full Version")
st.markdown("This version includes SEL integration, state-aligned standards, public exhibition support, and more.")

with st.form("unit_form"):
    theme = st.text_input("Theme (e.g. Housing Insecurity)")
    subject = st.selectbox("Subject Area", ["Science", "Language Arts", "Humanities"])
    grade = st.text_input("Grade Level (e.g. 11th grade)")
    identity = st.text_input("Identity Focus (e.g. Black youth, Indigenous students, LGBTQIA+)")
    weeks = st.slider("Unit Length (weeks)", 2, 6, 4)
    state = st.selectbox("Standards Framework", list(STANDARDS.keys()))
    environment = st.selectbox("Production Environment", [
        "Recording Studio",
        "Photo/Video Studio",
        "Podcasting Studio",
        "Mobile Recording Studio",
        "Other tools (e.g., cameras, tripods, lighting kits, backdrops)"
    ])
    selected_complements = st.multiselect("Select up to TWO complementary subject areas to integrate standards from:", ["Art", "Technology", "Music", "Entrepreneurship"], max_selections=2)
    submitted = st.form_submit_button("Generate Unit Plan")

if submitted:
    title, plan = generate_unit(theme, subject, weeks, grade, identity, state, environment, selected_complements)
    st.subheader(f"📘 Unit Title: {title}")
    full_output = []
    for section in plan:
        st.markdown(f"### {section['title']}")
        st.markdown(section['body'])
        full_output.append(f"{section['title']}

{section['body']}
")

    # DOCX export
    doc = Document()
    doc.add_heading(title, 0)
    for section in plan:
        doc.add_heading(section['title'], level=1)
        for line in section['body'].split('
'):
            doc.add_paragraph(line)
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    st.download_button("📥 Download Unit Plan (DOCX)", data=buffer, file_name=f"{title.replace(' ', '_')}.docx")

    # TXT export
    txt_output = '

'.join([f"{section['title']}
{section['body']}" for section in plan])
    st.download_button("📄 Download Unit Plan (TXT)", data=txt_output, file_name=f"{title.replace(' ', '_')}.txt")

    # PDF export (via plain text buffer)
    from fpdf import FPDF
    pdf = FPDF()
pdf.set_creator("Learning Production GPT")
pdf.set_title(title)
pdf.set_font("Arial", size=12)
pdf.set_margins(left=15, top=20, right=15)

# Add a simple branded header
pdf.set_fill_color(220, 220, 220)
pdf.set_text_color(0)
pdf.set_draw_color(180, 180, 180)
pdf.set_line_width(0.3)
pdf.set_font("Arial", style="B", size=16)
pdf.cell(0, 10, txt="Learning Production Unit Plan", ln=True, align="C", fill=True)
pdf.ln(5)
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    for section in plan:
        pdf.set_font("Arial", style='B', size=14)
        pdf.cell(200, 10, txt=section['title'], ln=True)
        pdf.set_font("Arial", size=12)
        for line in section['body'].split('
'):
            pdf.multi_cell(0, 10, txt=line)
    pdf_buffer = BytesIO()
    pdf.output(pdf_buffer)
    pdf_buffer.seek(0)
    st.download_button("🖨️ Download Unit Plan (PDF)", data=pdf_buffer, file_name=f"{title.replace(' ', '_')}.pdf")}.docx")
