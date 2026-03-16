import streamlit as st

from tools import (
    load_dataframe,
    read_issue,
    update_issue,
    search_kb
)
from main import (
    simple_rule_based_resolution,
    kb_enhanced_resolution
)

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Customer Support Agent", layout="centered")
st.title("📞 Customer Support Agent")
st.write("This UI allows you to retrieve issues, generate resolutions, and update Excel files.")


# Load issues
df = load_dataframe()
issue_ids = df["IssueId"].tolist()

selected_id = st.selectbox("Select an IssueId", issue_ids)

if selected_id:
    issue = read_issue(selected_id)

    st.subheader("Issue Details")
    st.write(f"**IssueId:** {issue['IssueId']}")
    st.write(f"**IssueText:** {issue['IssueText']}")
    st.write(f"**Current Status:** {issue['Status']}")
    st.write(f"**Existing Resolution:** {issue.get('AgentSuggestedResolution', '')}")

    st.divider()

    # Generate resolution
    if st.button("Generate Resolution"):
        st.session_state.resolution = kb_enhanced_resolution(issue["IssueText"])
        st.session_state.issue_id = selected_id

    if "resolution" in st.session_state:
        st.subheader("Suggested Resolution")
        st.write(st.session_state.resolution)

        # Confirm update
        if st.button("Apply Resolution to Excel"):
            st.write("Updating Excel file...")
            success = update_issue(st.session_state.issue_id, st.session_state.resolution, "Resolved")
            if success:
                st.success("Issue updated successfully in customer.xlsx")
            else:
                st.error("Failed to update issue.")