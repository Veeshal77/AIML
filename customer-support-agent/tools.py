import pandas as pd
from pathlib import Path

EXCEL_PATH = Path(__file__).parent / "customer.xlsx"
SHEET_NAME = "Sheet1"  # change if your sheet has a different name


def load_dataframe() -> pd.DataFrame:
    """Load the Excel file into a DataFrame."""
    if not EXCEL_PATH.exists():
        raise FileNotFoundError(f"Excel file not found at {EXCEL_PATH}")
    df = pd.read_excel(EXCEL_PATH, sheet_name=SHEET_NAME)

    # Force text columns to be strings 
    df["AgentSuggestedResolution"] = df["AgentSuggestedResolution"].astype("string") 
    df["Status"] = df["Status"].astype("string")

    return df


def save_dataframe(df: pd.DataFrame) -> None:
    """Save the DataFrame back to the Excel file."""
    df.to_excel(EXCEL_PATH, sheet_name=SHEET_NAME, index=False)


def read_issue(issue_id: int) -> dict | None:
    """Return a single issue as a dict, or None if not found."""
    df = load_dataframe()
    row = df[df["IssueId"] == issue_id]
    if row.empty:
        return None
    return row.iloc[0].to_dict()


def search_issues(keyword: str, limit: int = 10) -> list[dict]:
    """
    Search issues whose IssueText contains the keyword (case-insensitive).
    Returns a list of dicts.
    """
    df = load_dataframe()
    mask = df["IssueText"].str.contains(keyword, case=False, na=False)
    results = df[mask].head(limit)
    return results.to_dict(orient="records")


def update_issue(issue_id: int, resolution: str, status: str = "Resolved") -> bool:
    """
    Update AgentSuggestedResolution and Status for a given IssueId.
    Returns True if updated, False if IssueId not found.
    """
    df = load_dataframe()
    idx = df.index[df["IssueId"] == issue_id]
    if len(idx) == 0:
        return False
    print(f"\n idx: {idx}\n")
    print(f"\n Data Types: {df.dtypes}\n")

    df.loc[idx,"AgentSuggestedResolution"] = resolution

    print("\n\n **HERE**\n\n")

    df.loc[idx,"Status"] = status
    print("\n\n **NOW HERE**\n\n")

    save_dataframe(df)
    return True
