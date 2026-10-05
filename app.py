import streamlit as st
import pandas as pd

# ----------------------------------------------------
# 1. PAGE CONFIGURATION
# ----------------------------------------------------
st.set_page_config(
    page_title="EEHC | Smart Grid Master Control",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------------------------------------------
# 2. CUSTOM CSS (Modern Executive Theme)
# ----------------------------------------------------
st.markdown("""
<style>
    .stApp {
        background-color: #0F172A;
        color: #E2E8F0;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 28px 36px;
        margin-bottom: 28px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
    }
    .main-header h1 {
        color: #F8FAFC;
        font-size: 2.3rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.5px;
    }
    .main-header p {
        color: #38BDF8;
        font-size: 1.05rem;
        margin-top: 6px;
        margin-bottom: 0;
        font-weight: 500;
    }

    .kpi-card {
        background-color: #1E293B;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 16px 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
    }
    .kpi-title {
        color: #94A3B8;
        font-size: 0.78rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }
    .kpi-value {
        color: #F8FAFC;
        font-size: 1.5rem;
        font-weight: 800;
        margin-top: 4px;
    }
    .kpi-sub {
        color: #38BDF8;
        font-size: 0.82rem;
        margin-top: 2px;
        font-weight: 600;
    }

    .domain-title {
        background: #1E293B;
        color: #F8FAFC;
        border: 1px solid #334155;
        border-bottom: 3px solid #0284C7;
        padding: 12px;
        border-radius: 10px 10px 0 0;
        text-align: center;
        font-weight: 700;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    div[data-testid="column"] > div {
        background-color: #1E293B;
        border-radius: 12px;
        border: 1px solid #334155;
        padding: 6px;
    }

    div.stButton > button {
        width: 100% !important;
        background-color: #0F172A !important;
        color: #CBD5E1 !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
        padding: 10px 12px !important;
        font-size: 0.85rem !important;
        font-weight: 500 !important;
        text-align: left !important;
        transition: all 0.2s ease !important;
        margin-bottom: 6px !important;
    }
    div.stButton > button:hover {
        background-color: #0284C7 !important;
        color: #FFFFFF !important;
        border-color: #38BDF8 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(2, 132, 199, 0.3) !important;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #1E293B;
        border-radius: 8px;
        color: #94A3B8;
        padding: 10px 20px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #0284C7 !important;
        color: #FFFFFF !important;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# 3. ROADMAP DATA MATRIX
# ----------------------------------------------------
PROJECTS = {
    "1. Policy & Regulatory": [
        ("PS1", "Policy and regulatory review"),
        ("PS2", "Technical standards & regulation"),
        ("PS3", "Privacy & customer data ownership"),
        ("PS4", "Cybersecurity")
    ],
    "2. Organizational": [
        ("OS1", "Business goals & use cases"),
        ("OS2", "Organizational KPIs"),
        ("OS3", "Asset management strategy"),
        ("OS4", "Smart grid governance")
    ],
    "3. Infrastructure": [
        ("IF1", "Smart meters: C&I"),
        ("IF2", "Asset Mgmt & GIS Implementation"),
        ("IF3", "Smart meters: Res >200 kWh/mo"),
        ("IF4", "Asset management & monitoring"),
        ("IF5", "Smart Meter Plus: Res <200 kWh/mo"),
        ("IF6", "Phasor measurement units")
    ],
    "4. Technology": [
        ("TE1", "Technology evaluation & selection"),
        ("TE2", "Integrated solution selection"),
        ("TE3", "Smart meter analytics"),
        ("TE4", "PV and EV monitoring"),
        ("TE5", "Demand response"),
        ("TE6", "DSM pilot"),
        ("TE7", "Energy storage pilots")
    ],
    "5. Customer Engagement": [
        ("C1", "Green DISCO"),
        ("C2", "AMI lessons learned"),
        ("C3", "Buy REN@DISCO"),
        ("C4", "Advanced meter analytics"),
        ("C5", "Interactive energy applications")
    ]
}

if "selected_project" not in st.session_state:
    st.session_state["selected_project"] = None

def select_project(code):
    st.session_state["selected_project"] = code

# Header
st.markdown("""
<div class="main-header">
    <h1>EEHC Smart Grid Command Center</h1>
    <p>Egyptian Electricity Holding Company & 9 Distribution Companies (DISCOs) Strategic Roadmap</p>
</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# 4. DASHBOARD VIEW
# ----------------------------------------------------
if st.session_state["selected_project"] is None:
    
    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.markdown('<div class="kpi-card"><div class="kpi-title">Portfolio Scope</div><div class="kpi-value">5 Domains</div><div class="kpi-sub">26 Total Projects</div></div>', unsafe_allow_html=True)
    with k2:
        st.markdown('<div class="kpi-card"><div class="kpi-title">Target Network</div><div class="kpi-value">9 DISCOs</div><div class="kpi-sub">Unified Architecture</div></div>', unsafe_allow_html=True)
    with k3:
        st.markdown('<div class="kpi-card"><div class="kpi-title">Active Flagship</div><div class="kpi-value">IF2 (GIS)</div><div class="kpi-sub">Short-Term Horizon</div></div>', unsafe_allow_html=True)
    with k4:
        st.markdown('<div class="kpi-card"><div class="kpi-title">Program Horizon</div><div class="kpi-value">2026 – 2030+</div><div class="kpi-sub">3 Phased Horizons</div></div>', unsafe_allow_html=True)

    st.markdown("###")
    st.markdown("#### ⚡ Smart Grid Portfolio Matrix — Click any project to open details")

    cols = st.columns(5)
    
    for idx, (domain_name, proj_list) in enumerate(PROJECTS.items()):
        with cols[idx]:
            st.markdown(f'<div class="domain-title">{domain_name}</div>', unsafe_allow_html=True)
            st.markdown("<div style='padding: 6px;'>", unsafe_allow_html=True)
            
            for code, name in proj_list:
                label = f"⭐ **{code}**: {name}" if code == "IF2" else f"🔹 **{code}**: {name}"
                    
                if st.button(label, key=f"btn_{code}"):
                    select_project(code)
                    st.rerun()
                    
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    
    st.markdown("#### 🎯 Portfolio Benefits Framework")
    b1, b2, b3, b4 = st.columns(4)
    b1.info("💰 **B1 / B2**: Deferred & Avoided Grid Investment")
    b2.warning("⚡ **B3 / B4**: Reduced Losses & Planned Outages")
    b3.success("🌱 **B5 / B6 / B7**: Customer Experience & CO₂ Reduction")
    b4.metric("B8 / B9", "Operational Efficiency", "EV Integration")

# ----------------------------------------------------
# 5. DETAILED PROJECT VIEWS
# ----------------------------------------------------
else:
    if st.button("← Return to Smart Grid Command Center"):
        st.session_state["selected_project"] = None
        st.rerun()

    proj_code = st.session_state["selected_project"]

    if proj_code == "IF2":
        st.markdown("## 🗺 IF2: Asset Management Design & Implementation (GIS Project)")
        st.caption("Central GIS Foundation, Network Digitization, and Strategic Asset Record")
        
        st.markdown("---")
        
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Short Term Target", "MV Network Coverage", "By June 2027")
        m2.metric("Medium Term Target", "LV Network & Apps", "2027 – 2030")
        m3.metric("Long Term Target", "ADMS Operations", "May 2030 Onward")
        m4.metric("Scope", "9 DISCOs", "1 Unified Model")

        st.markdown("###")

        tab1, tab2, tab3, tab4 = st.tabs([
            "🎯 Strategic Objectives", 
            "📅 3-Horizon Roadmap", 
            "🔄 Update Workflow & Acceptance", 
            "🔌 Connected Applications"
        ])

        with tab1:
            col_left, col_right = st.columns(2)
            with col_left:
                st.markdown("""
                ### Core Pillars
                * **Unified Network Record**: 9 Distribution Companies operating under one agreed data standard and schema.
                * **Trusted Network Data**: Verified asset locations, stable global asset IDs, and validated electrical topology.
                """)
            with col_right:
                st.markdown("""
                ### Deployment Principles
                * **Continuous Lifecycle**: *Capture → Verify → Approve → Publish* update workflow.
                * **Sector Applications**: Powering Asset Management, OMS, ADMS, and Loss Analysis.
                """)

        with tab2:
            st.subheader("Implementation Horizons Timeline")
            
            horizon_df = pd.DataFrame({
                "Horizon": ["Short Term", "Medium Term", "Long Term"],
                "Timeline": ["Jan 2026 – Jun 2027", "Jun 2027 – May 2030", "May 2030 Onward"],
                "Focus Area": [
                    "Central foundation; 9 DISCO pilots; full MV network coverage",
                    "LV network expansion; operating apps; RE/PQ/BESS pilots",
                    "Coordinated ADMS operations; voltage & peak optimization; AMI"
                ],
                "Gate Evidence": [
                    "Accepted MV network records in all 9 DISCOs",
                    "Measured value and validated electrical models",
                    "Approved investment cases and operating readiness"
                ]
            })
            st.table(horizon_df)

        with tab3:
            st.subheader("Continuous Update & Acceptance Workflow")
            st.code("""
[ Field Change / Survey ] ──> [ DISCO QA Check ] ──> [ Joint Acceptance ] ──> [ Central SQL / GIS Sync ]
            """, language="text")
            
            st.markdown("""
            * **EEHC GIS & R&D Team**: Common model, SQL integration, central platform maintenance, publication support.
            * **DISCO Teams**: Field locating, attribute verification, record ownership.
            * **Joint Acceptance Team**: QA checklist verification, coordinate matching, and approval workflow.
            """)

        with tab4:
            st.subheader("Connected Application Modules")
            app_select = st.selectbox("Select Application Domain to View Status:", [
                "Asset Management & Maintenance",
                "Fleet & Workforce Management",
                "Outage Management System (OMS)",
                "Loss Analysis & Cost Visibility",
                "Renewable Energy & EV Connection Screening",
                "Power Quality Assessment & Response",
                "Battery Energy Storage (BESS) Support"
            ])
            
            st.success(f"Configured View: **{app_select}**")
            st.json({
                "Project Code": "IF2-APP",
                "Integration Architecture": "ArcGIS Enterprise / Central SQL Link",
                "Primary Identifier": "Unified Global Asset ID",
                "Deployment Horizon": "Medium-Term (2027-2030)"
            })

    else:
        proj_name = "Selected Project"
        for domain in PROJECTS.values():
            for code, name in domain:
                if code == proj_code:
                    proj_name = name
                    break

        st.markdown(f"## ⚙ {proj_code}: {proj_name}")
        st.info("🔒 Dedicated workspace allocated within the Smart Grid Master Roadmap.")

        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Lead Department / Owner", value="EEHC Operations", disabled=True)
            st.selectbox("Implementation Status", ["Planning", "Pilot Phase", "Active Rollout", "Completed"])
        with col2:
            st.date_input("Target Start Date")
            st.number_input("Estimated Investment ($)", value=0)

        st.text_area("Scope Definition & Project Objectives", placeholder="Enter technical requirements, key deliverables, and target KPIs...")
        st.button("Save Workspace Configuration", disabled=True)
