import streamlit as st
import pandas as pd
import plotly.express as px


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="European Bank Churn Analytics",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# THEME STATE
# ============================================================

if "theme" not in st.session_state:
    st.session_state.theme = "dark"

dark = st.session_state.theme == "dark"


# ============================================================
# COLORS
# ============================================================

if dark:
    BG = "#080B12"
    SIDEBAR = "#0D1119"
    CARD = "#111722"
    CARD_HOVER = "#151C29"
    BORDER = "#303A4A"

    WHITE = "#FFFFFF"
    TEXT = "#F4F7FB"
    MUTED = "#9AA5B5"

    PURPLE = "#6C63FF"
    PURPLE_LIGHT = "#8178FF"

    BLUE = "#35C9FF"
    GREEN = "#35D48A"
    RED = "#FF5C70"
    ORANGE = "#FFAD55"

    GRID = "#28313F"

else:
    BG = "#F4F6FA"
    SIDEBAR = "#FFFFFF"
    CARD = "#FFFFFF"
    CARD_HOVER = "#F8F9FC"
    BORDER = "#DCE2EA"

    WHITE = "#111827"
    TEXT = "#171A21"
    MUTED = "#667085"

    PURPLE = "#5B50E6"
    PURPLE_LIGHT = "#6C63FF"

    BLUE = "#009ED8"
    GREEN = "#159A63"
    RED = "#E5485D"
    ORANGE = "#E58A1F"

    GRID = "#E3E7ED"


# ============================================================
# CSS
# ============================================================

st.markdown(
f"""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap');


/* =========================================================
   GLOBAL
   ========================================================= */

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
}}

.stApp {{
    background: {BG};
    color: {TEXT};
}}

.block-container {{
    max-width: 1450px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}}

#MainMenu {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

header {{
    background: transparent !important;
}}


/* =========================================================
   SIDEBAR
   ========================================================= */

section[data-testid="stSidebar"] {{
    background: {SIDEBAR};
    border-right: 1px solid {BORDER};
}}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label {{
    color: {TEXT} !important;
}}

.brand {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 29px;
    font-weight: 700;
    color: {WHITE};
    letter-spacing: -1px;
}}

.brand-purple {{
    color: {PURPLE_LIGHT};
}}

.brand-sub {{
    color: {MUTED};
    font-size: 12px;
    margin-top: 3px;
    margin-bottom: 25px;
}}

.sidebar-heading {{
    color: {MUTED};
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.3px;
    text-transform: uppercase;
    margin-top: 15px;
    margin-bottom: 10px;
}}

.dashboard-button {{
    background: rgba(108,99,255,0.13);
    border: 1px solid {PURPLE};
    border-radius: 10px;
    padding: 11px 14px;
    color: {WHITE};
    font-size: 13px;
    font-weight: 600;
}}


/* =========================================================
   MAIN HEADER
   ========================================================= */

.eyebrow {{
    color: {PURPLE_LIGHT};
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.7px;
    text-transform: uppercase;
    margin-bottom: 5px;
}}

.main-title {{
    color: {WHITE};
    font-family: 'Space Grotesk', sans-serif;
    font-size: 34px;
    font-weight: 700;
    letter-spacing: -1px;
    line-height: 1.2;
}}

.main-subtitle {{
    color: {MUTED};
    font-size: 13px;
    line-height: 1.5;
    margin-top: 5px;
}}


/* =========================================================
   KPI CARDS
   ========================================================= */

.kpi-card {{
    height: 145px;
    box-sizing: border-box;

    background: linear-gradient(
        145deg,
        {CARD},
        {CARD_HOVER}
    );

    border: 1px solid {BORDER};
    border-radius: 16px;

    padding: 20px;

    box-shadow: 0 8px 28px rgba(0,0,0,0.18);
}}

.kpi-card:hover {{
    border-color: {PURPLE};
}}

.kpi-label {{
    color: {MUTED};
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 0.8px;
    text-transform: uppercase;
}}

.kpi-value {{
    color: {WHITE};
    font-family: 'Space Grotesk', sans-serif;
    font-size: 29px;
    font-weight: 700;
    margin-top: 10px;
}}

.kpi-description {{
    color: {MUTED};
    font-size: 11px;
    margin-top: 8px;
}}


/* =========================================================
   SECTION TITLES
   ========================================================= */

.section-title {{
    color: {WHITE};
    font-family: 'Space Grotesk', sans-serif;
    font-size: 17px;
    font-weight: 700;
}}

.section-subtitle {{
    color: {MUTED};
    font-size: 11px;
    margin-top: 3px;
}}


/* =========================================================
   INSIGHT CARDS
   ========================================================= */

.insight-card {{
    min-height: 145px;
    box-sizing: border-box;

    background: linear-gradient(
        145deg,
        {CARD},
        {CARD_HOVER}
    );

    border: 1px solid {BORDER};
    border-radius: 15px;

    padding: 18px;

    box-shadow: 0 8px 25px rgba(0,0,0,0.15);
}}

.insight-icon {{
    font-size: 20px;
    margin-bottom: 8px;
}}

.insight-title {{
    color: {WHITE};
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 7px;
}}

.insight-text {{
    color: {MUTED};
    font-size: 11px;
    line-height: 1.6;
}}


/* =========================================================
   SELECT BOXES
   ========================================================= */

div[data-baseweb="select"] > div {{
    background: {CARD} !important;
    border: 1px solid {BORDER} !important;
    border-radius: 9px !important;
}}

div[data-baseweb="select"] span {{
    color: {WHITE} !important;
}}

span[data-baseweb="tag"] {{
    background: {PURPLE} !important;
    color: #FFFFFF !important;
    border-radius: 6px !important;
}}

span[data-baseweb="tag"] span {{
    color: #FFFFFF !important;
}}


/* =========================================================
   RADIO
   ========================================================= */

div[data-testid="stRadio"] label {{
    color: {WHITE} !important;
}}

div[data-testid="stRadio"] p {{
    color: {WHITE} !important;
}}


/* =========================================================
   DOWNLOAD BUTTON
   ========================================================= */

.stDownloadButton button {{
    background: {PURPLE} !important;
    color: #FFFFFF !important;

    border: 1px solid {PURPLE_LIGHT} !important;
    border-radius: 9px !important;

    font-weight: 700 !important;
    padding: 10px 18px !important;

    box-shadow: 0 5px 18px rgba(108,99,255,0.25);
}}

.stDownloadButton button:hover {{
    background: {PURPLE_LIGHT} !important;
    color: #FFFFFF !important;
}}


/* =========================================================
   STREAMLIT BORDER CONTAINERS
   ========================================================= */

div[data-testid="stVerticalBlockBorderWrapper"] {{
    background: {CARD};
    border-color: {BORDER} !important;
    border-radius: 15px !important;
    box-shadow: 0 8px 25px rgba(0,0,0,0.12);
}}


/* =========================================================
   DATAFRAME
   ========================================================= */

div[data-testid="stDataFrame"] {{
    border-radius: 10px;
    overflow: hidden;
}}


/* =========================================================
   FOOTER
   ========================================================= */

.footer {{
    border-top: 1px solid {BORDER};
    margin-top: 35px;
    padding-top: 18px;
    text-align: center;
    color: {MUTED};
    font-size: 10px;
}}

</style>
""",
unsafe_allow_html=True
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    return pd.read_csv("European_Bank_segmentedDAY3.csv")


df = load_data()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="brand">European<span class="brand-purple"> Bank</span></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="brand-sub">Customer Intelligence Platform</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-heading">Navigation</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="dashboard-button">◈ &nbsp; Dashboard</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown(
        '<div class="sidebar-heading">Dashboard Filters</div>',
        unsafe_allow_html=True
    )

    geo_filter = st.multiselect(
        "Geography",
        sorted(df["Geography"].dropna().unique()),
        default=list(df["Geography"].dropna().unique())
    )

    gender_filter = st.multiselect(
        "Gender",
        sorted(df["Gender"].dropna().unique()),
        default=list(df["Gender"].dropna().unique())
    )

    age_filter = st.multiselect(
        "Age Band",
        sorted(df["AgeBand"].dropna().unique()),
        default=list(df["AgeBand"].dropna().unique())
    )

    st.markdown("---")

    st.markdown(
        '<div class="sidebar-heading">Appearance</div>',
        unsafe_allow_html=True
    )

    theme_choice = st.radio(
        "Theme",
        ["Dark", "Light"],
        index=0 if dark else 1,
        horizontal=True,
        label_visibility="collapsed"
    )

    if (theme_choice == "Dark") != dark:
        st.session_state.theme = (
            "dark" if theme_choice == "Dark" else "light"
        )
        st.rerun()

    st.markdown("---")

    st.caption("RetainIQ Analytics")
    st.caption("European Banking Dataset")


# ============================================================
# FILTER DATA
# ============================================================

filtered = df[
    df["Geography"].isin(geo_filter)
    & df["Gender"].isin(gender_filter)
    & df["AgeBand"].isin(age_filter)
].copy()


# ============================================================
# CALCULATIONS
# ============================================================

total_customers = len(filtered)

if total_customers > 0:
    overall_churn = filtered["Exited"].mean() * 100
else:
    overall_churn = 0


high_value_churn = filtered[
    (filtered["Balance"] > 100000)
    & (filtered["Exited"] == 1)
]

high_value_count = len(high_value_churn)

revenue_at_risk = high_value_churn["Balance"].sum()


active = filtered[
    filtered["IsActiveMember"] == 1
]

inactive = filtered[
    filtered["IsActiveMember"] == 0
]

if len(active) > 0:
    active_churn = active["Exited"].mean() * 100
else:
    active_churn = 0

if len(inactive) > 0:
    inactive_churn = inactive["Exited"].mean() * 100
else:
    inactive_churn = 0


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="eyebrow">CUSTOMER INTELLIGENCE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-title">Customer Churn Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-subtitle">European Bank — Customer Segmentation, Churn Analytics and High-Value Customer Risk Monitoring</div>',
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)


# ============================================================
# KPI CARDS
# ============================================================

k1, k2, k3, k4 = st.columns(4, gap="medium")


with k1:
    st.markdown(
        f'<div class="kpi-card">'
        f'<div class="kpi-label">Overall Churn Rate</div>'
        f'<div class="kpi-value">{overall_churn:.1f}%</div>'
        f'<div class="kpi-description">● Customer attrition rate</div>'
        f'</div>',
        unsafe_allow_html=True
    )


with k2:
    st.markdown(
        f'<div class="kpi-card">'
        f'<div class="kpi-label">Total Customers</div>'
        f'<div class="kpi-value">{total_customers:,}</div>'
        f'<div class="kpi-description">● Selected customer population</div>'
        f'</div>',
        unsafe_allow_html=True
    )


with k3:
    st.markdown(
        f'<div class="kpi-card">'
        f'<div class="kpi-label">High-Value Churners</div>'
        f'<div class="kpi-value">{high_value_count:,}</div>'
        f'<div class="kpi-description">Customers with balance above $100K</div>'
        f'</div>',
        unsafe_allow_html=True
    )


with k4:
    st.markdown(
        f'<div class="kpi-card">'
        f'<div class="kpi-label">Revenue at Risk</div>'
        f'<div class="kpi-value">${revenue_at_risk:,.0f}</div>'
        f'<div class="kpi-description">High-value churn exposure</div>'
        f'</div>',
        unsafe_allow_html=True
    )


st.markdown("<br>", unsafe_allow_html=True)


# ============================================================
# PLOTLY STYLE
# ============================================================

def style_chart(fig):

    fig.update_layout(
        height=310,
        paper_bgcolor=CARD,
        plot_bgcolor=CARD,

        font=dict(
            family="Inter",
            color=TEXT
        ),

        margin=dict(
            l=10,
            r=10,
            t=15,
            b=15
        ),

        xaxis=dict(
            gridcolor=GRID,
            zerolinecolor=GRID
        ),

        yaxis=dict(
            gridcolor=GRID,
            zerolinecolor=GRID
        ),

        hoverlabel=dict(
            bgcolor=CARD,
            font_color=TEXT
        )
    )

    return fig


# ============================================================
# ROW 1
# ============================================================

left, right = st.columns([1.35, 1], gap="medium")


# ------------------------------------------------------------
# GEOGRAPHY
# ------------------------------------------------------------

with left:

    with st.container(border=True):

        st.markdown(
            '<div class="section-title">Churn Rate by Geography</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-subtitle">Percentage of customers who exited by region</div>',
            unsafe_allow_html=True
        )

        geo_data = (
            filtered
            .groupby("Geography")["Exited"]
            .mean()
            .reset_index()
        )

        geo_data["Churn Rate"] = geo_data["Exited"] * 100

        fig_geo = px.bar(
            geo_data,
            x="Geography",
            y="Churn Rate",
            text="Churn Rate"
        )

        fig_geo.update_traces(
            marker_color=PURPLE,
            texttemplate="%{text:.1f}%",
            textposition="outside"
        )

        fig_geo.update_layout(
            showlegend=False
        )

        fig_geo.update_yaxes(
            title="Churn %",
            rangemode="tozero"
        )

        fig_geo.update_xaxes(
            title=""
        )

        style_chart(fig_geo)

        st.plotly_chart(
            fig_geo,
            use_container_width=True,
            config={"displayModeBar": False}
        )


# ------------------------------------------------------------
# ACTIVE VS INACTIVE
# ------------------------------------------------------------

with right:

    with st.container(border=True):

        st.markdown(
            '<div class="section-title">Active vs Inactive Churn</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-subtitle">Churn comparison based on customer activity</div>',
            unsafe_allow_html=True
        )

        active_data = (
            filtered
            .groupby("IsActiveMember")["Exited"]
            .mean()
            .reset_index()
        )

        active_data["Churn Rate"] = (
            active_data["Exited"] * 100
        )

        active_data["Status"] = active_data[
            "IsActiveMember"
        ].map({
            0: "Inactive",
            1: "Active"
        })

        fig_active = px.bar(
            active_data,
            x="Status",
            y="Churn Rate",
            text="Churn Rate"
        )

        fig_active.update_traces(
            marker_color=[
                RED if x == "Inactive"
                else GREEN
                for x in active_data["Status"]
            ],
            texttemplate="%{text:.1f}%",
            textposition="outside"
        )

        fig_active.update_layout(
            showlegend=False
        )

        fig_active.update_yaxes(
            title="Churn %",
            rangemode="tozero"
        )

        fig_active.update_xaxes(
            title=""
        )

        style_chart(fig_active)

        st.plotly_chart(
            fig_active,
            use_container_width=True,
            config={"displayModeBar": False}
        )


# ============================================================
# ROW 2
# ============================================================

left2, right2 = st.columns(2, gap="medium")


# ------------------------------------------------------------
# AGE BAND
# ------------------------------------------------------------

with left2:

    with st.container(border=True):

        st.markdown(
            '<div class="section-title">Churn by Age Band</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-subtitle">Identify age groups with higher customer attrition</div>',
            unsafe_allow_html=True
        )

        age_data = (
            filtered
            .groupby("AgeBand")["Exited"]
            .mean()
            .reset_index()
        )

        age_data["Churn Rate"] = (
            age_data["Exited"] * 100
        )

        fig_age = px.bar(
            age_data,
            x="AgeBand",
            y="Churn Rate",
            text="Churn Rate"
        )

        fig_age.update_traces(
            marker_color=BLUE,
            texttemplate="%{text:.1f}%",
            textposition="outside"
        )

        fig_age.update_layout(
            showlegend=False
        )

        fig_age.update_yaxes(
            title="Churn %",
            rangemode="tozero"
        )

        fig_age.update_xaxes(
            title=""
        )

        style_chart(fig_age)

        st.plotly_chart(
            fig_age,
            use_container_width=True,
            config={"displayModeBar": False}
        )


# ------------------------------------------------------------
# BALANCE
# ------------------------------------------------------------

with right2:

    with st.container(border=True):

        st.markdown(
            '<div class="section-title">Customer Balance Distribution</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-subtitle">Customer volume across balance segments</div>',
            unsafe_allow_html=True
        )

        balance_data = (
            filtered
            .groupby("BalanceSegment")
            .size()
            .reset_index(name="Customers")
        )

        fig_balance = px.pie(
            balance_data,
            names="BalanceSegment",
            values="Customers",
            hole=0.60
        )

        fig_balance.update_traces(
            textinfo="percent",
            hovertemplate=(
                "<b>%{label}</b><br>"
                "Customers: %{value}<br>"
                "Share: %{percent}"
                "<extra></extra>"
            )
        )

        fig_balance.update_layout(
            showlegend=True,
            legend=dict(
                orientation="h",
                y=-0.05
            )
        )

        style_chart(fig_balance)

        st.plotly_chart(
            fig_balance,
            use_container_width=True,
            config={"displayModeBar": False}
        )


# ============================================================
# BUSINESS INSIGHTS
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    '<div class="eyebrow">AUTOMATED ANALYSIS</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-title" style="font-size:24px;">Business Insights</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-subtitle">Key observations from the selected customer population.</div>',
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)


i1, i2, i3 = st.columns(3, gap="medium")


# ------------------------------------------------------------
# INSIGHT 1
# ------------------------------------------------------------

with i1:

    if len(geo_data) > 0:

        highest_geo = geo_data.loc[
            geo_data["Churn Rate"].idxmax()
        ]

        st.markdown(
            f'<div class="insight-card">'
            f'<div class="insight-icon">🌍</div>'
            f'<div class="insight-title">Geographic Churn Signal</div>'
            f'<div class="insight-text">'
            f'<b>{highest_geo["Geography"]}</b> records the highest '
            f'observed churn rate at '
            f'<b>{highest_geo["Churn Rate"]:.1f}%</b> among the selected regions.'
            f'</div>'
            f'</div>',
            unsafe_allow_html=True
        )


# ------------------------------------------------------------
# INSIGHT 2
# ------------------------------------------------------------

with i2:

    difference = inactive_churn - active_churn

    st.markdown(
        f'<div class="insight-card">'
        f'<div class="insight-icon">⚡</div>'
        f'<div class="insight-title">Customer Activity Signal</div>'
        f'<div class="insight-text">'
        f'Inactive customers show <b>{inactive_churn:.1f}%</b> churn, '
        f'compared with <b>{active_churn:.1f}%</b> for active customers. '
        f'Difference: <b>{difference:.1f} pp</b>.'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True
    )


# ------------------------------------------------------------
# INSIGHT 3
# ------------------------------------------------------------

with i3:

    st.markdown(
        f'<div class="insight-card">'
        f'<div class="insight-icon">💰</div>'
        f'<div class="insight-title">High-Value Exposure</div>'
        f'<div class="insight-text">'
        f'<b>{high_value_count:,}</b> high-value customers are classified '
        f'as churned, representing approximately '
        f'<b>${revenue_at_risk:,.0f}</b> in balance exposure.'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True
    )


# ============================================================
# CUSTOMER EXPLORER
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    '<div class="eyebrow">CUSTOMER EXPLORER</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-title" style="font-size:24px;">High-Value Customer Explorer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-subtitle">Customers with account balance above $100,000.</div>',
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)


explorer = filtered[
    filtered["Balance"] > 100000
][
    [
        "CustomerId",
        "Geography",
        "Gender",
        "Age",
        "Balance",
        "EstimatedSalary",
        "Exited"
    ]
].sort_values(
    "Balance",
    ascending=False
).copy()


explorer["Status"] = explorer["Exited"].map({
    0: "Retained",
    1: "Churned"
})

explorer = explorer.drop(
    columns=["Exited"]
)


with st.container(border=True):

    st.markdown(
        '<div class="section-title">High-Value Accounts</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Sorted by account balance</div>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.dataframe(
        explorer,
        use_container_width=True,
        height=350,
        hide_index=True
    )


# ============================================================
# DOWNLOAD
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

csv_data = filtered.to_csv(
    index=False
).encode("utf-8")


st.download_button(
    label="↓  Download Filtered Customer Data",
    data=csv_data,
    file_name="filtered_customers.csv",
    mime="text/csv"
)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    '<div class="footer">'
    '· Customer Intelligence Platform<br>'
    'European Bank Customer Churn Analytics'
    '</div>',
    unsafe_allow_html=True
)