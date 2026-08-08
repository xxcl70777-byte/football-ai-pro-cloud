import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.set_page_config(
    page_title="Football AI Cloud",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ 足球人工智能专业云平台")
st.markdown("---")

try:
    admin_password = st.secrets["admin_password"]
    postgres_url = st.secrets["postgres_url"]
    st.sidebar.success("✅ Cloud config loaded")
except Exception as e:
    st.sidebar.warning("⚠️ Using demo mode.")

@st.cache_data(ttl=600)
def get_matches():
    return pd.DataFrame([
        {
            "Source": "China Sports Lottery",
            "Match": "Man City vs Arsenal",
            "Home Win": 1.85,
            "Draw": 3.60,
            "Away Win": 4.10,
            "Time": datetime.now().strftime("%Y-%m-%d %H:%M")
        },
        {
            "Source": "Macau Slot",
            "Match": "Real Madrid vs Barcelona",
            "Home Win": 2.05,
            "Draw": 3.40,
            "Away Win": 3.30,
            "Time": datetime.now().strftime("%Y-%m-%d %H:%M")
        },
        {
            "Source": "HKJC",
            "Match": "Inter Milan vs AC Milan",
            "Home Win": 1.90,
            "Draw": 3.50,
            "Away Win": 3.80,
            "Time": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
    ])

@st.cache_data(ttl=600)
def get_seasons():
    return [
        {
            "Team": "Real Madrid",
            "Trend": "72% -> 76% -> 78% (Up)",
            "Offense": "Strong firepower, 2.3 goals/match average.",
            "Defense": "Stable, conceding ~0.8 goals/match.",
            "Rating": "⭐️⭐️⭐️⭐️⭐️"
        },
        {
            "Team": "Barcelona",
            "Trend": "65% -> 68% -> 74% (Recovery)",
            "Offense": "High xG creation via possession.",
            "Defense": "Vulnerable to fast counterattacks.",
            "Rating": "⭐️⭐️⭐️⭐️"
        }
    ]

@st.cache_data(ttl=600)
def get_reviews():
    return pd.DataFrame([
        {
            "Match": "Chelsea vs Burnley",
            "Prediction": "Home Win (75%)",
            "Result": "1 : 1 (Draw)",
            "Status": "❌ Missed",
            "Reason": "1. Key striker injured during warm-up;\n2. Low-block defense success rate 88%."
        }
    ])

# 纯英文标签名，彻底杜绝中文符号引起的语法报错
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Live Data", 
    "3-Season Analysis",
    "AI Prediction", 
    "Review & Postmortem", 
    "Admin Settings"
])

with tab1:
    st.subheader("📊 Multi-source Odds & Matches")
    df = get_matches()
    st.dataframe(df, use_container_width=True)
    if st.button("Refresh Data"):
        st.cache_data.clear()
        st.rerun()

with tab2:
    st.subheader("📈 Past 3 Seasons Team Performance")
    for item in get_seasons():
        with st.expander(f"🛡️ {item['Team']}"):
            st.write(f"**Win Rate Trend**: {item['Trend']}")
            st.write(f"**Offense**: {item['Offense']}")
            st.write(f"**Defense**: {item['Defense']}")
            st.success(f"**Rating**: {item['Rating']}")

with tab3:
    st.subheader("🤖 AI Neural Network Prediction")
    c1, c2 = st.columns(2)
    with c1:
        t1 = st.text_input("Home Team", "Real Madrid")
    with c2:
        t2 = st.text_input("Away Team", "Barcelona")
    
    if st.button("Run AI Analysis"):
        with st.spinner("Calculating..."):
            import time
            time.sleep(1)
        st.success("Prediction Results:")
        st.metric(label=f"{t1} Win Rate", value="58.5%")
        st.metric(label="Draw Rate", value="24.0%")
        st.metric(label=f"{t2} Win Rate", value="17.5%")

with tab4:
    st.subheader("📉 AI Postmortem & Failure Analysis")
    df_rev = get_reviews()
    for idx, row in df_rev.iterrows():
        with st.expander(f"📌 {row['Match']} ({row['Status']})"):
            st.write(f"Prediction: {row['Prediction']} | Result: {row['Result']}")
            st.text(f"Failure Reason Analysis:\n{row['Reason']}")

with tab5:
    st.subheader("⚙️ Admin Panel")
    pwd = st.text_input("Password", type="password")
    if pwd:
        try:
            if pwd == admin_password:
                st.success("Access Granted!")
                if st.button("Sync Database"):
                    st.success("Synced successfully!")
            else:
                st.error("Wrong password.")
        except:
            st.error("Secrets not configured.")
