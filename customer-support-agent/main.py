from tools import read_issue, update_issue, search_issues


def simple_rule_based_resolution(issue_text: str) -> str:
    """
    Very simple heuristic-based 'agent' to generate a suggested resolution.
    You will later replace this with an LLM call.
    """
    text = issue_text.lower()

    if "login" in text or "account" in text:
        return (
            "Please try resetting your password, ensure caps lock is off, and "
            "verify you are using the correct email. If the issue persists, "
            "we can manually verify your account."
        )
    if "password reset" in text:
        return (
            "Please check your spam/junk folder for the reset email. "
            "If you still don't see it, request another reset and ensure "
            "you are using the correct email address."
        )
    if "charged twice" in text or "double charge" in text:
        return (
            "We are sorry for the inconvenience. We will review your transaction "
            "and issue a refund for the duplicate charge within 3 to 5 business days."
        )
    if "payment failed" in text or "money deducted" in text:
        return (
            "Sometimes payments show as deducted but are reversed by the bank. "
            "Please allow 3 to 5 business days. If it does not reverse, share the "
            "transaction ID and we will investigate."
        )
    if "order not delivered" in text or "not delivered" in text or "delayed" in text:
        return (
            "We are sorry your order is delayed. We are checking with the courier. "
            "You will receive an update with a new delivery estimate shortly."
        )
    if "wrong item" in text:
        return (
            "We apologize for the mix-up. Please share a photo of the item you "
            "received and we will arrange a replacement or refund."
        )
    if "promo code" in text or "coupon" in text:
        return (
            "Please ensure the promo code is valid, not expired, and meets the "
            "minimum order value. If it still fails, share the code and we will "
            "check it on our side."
        )
    if "app crashes" in text or "crash" in text:
        return (
            "Please update the app to the latest version, clear cache, and restart "
            "your device. If the issue continues, share your device model and OS version."
        )
    if "account locked" in text or "locked" in text:
        return (
            "Your account may be temporarily locked for security reasons. "
            "Please wait 30 minutes and try again, or contact support to verify your identity."
        )

    # Fallback
    return (
        "Thank you for reaching out. We need a bit more information to assist you. "
        "Please describe the issue in more detail or share screenshots if possible."
    )


def handle_issue(issue_id: int) -> None:
    issue = read_issue(issue_id)
    if issue is None:
        print(f"IssueId {issue_id} not found.")
        return

    print(f"\n--- Issue {issue_id} ---")
    print(f"IssueText: {issue['IssueText']}")
    print(f"Current Status: {issue['Status']}")
    print(f"Current AgentSuggestedResolution: {issue.get('AgentSuggestedResolution', '')}\n")

    # Agent "reasoning"
    suggested_resolution = simple_rule_based_resolution(issue["IssueText"])
    new_status = "Resolved"

    print("=== Agent Suggested Resolution ===")
    print(suggested_resolution)
    print(f"\nNew Status: {new_status}")

    confirm = input("\nApply this resolution to the Excel file? (y/n): ").strip().lower()
    if confirm == "y":
        success = update_issue(issue_id, suggested_resolution, new_status)
        if success:
            print("✅ Issue updated in customer.xlsx")
        else:
            print("⚠️ Failed to update issue (IssueId not found).")
    else:
        print("No changes were made.")


def main():
    print("Customer Support Agent (POC)")
    print("----------------------------")

    while True:
        choice = input(
            "\nOptions:\n"
            "  1. Handle a specific IssueId\n"
            "  2. Search issues by keyword\n"
            "  3. Exit\n"
            "Enter choice (1/2/3): "
        ).strip()

        if choice == "1":
            try:
                issue_id = int(input("Enter IssueId: ").strip())
            except ValueError:
                print("Please enter a valid integer IssueId.")
                continue
            handle_issue(issue_id)

        elif choice == "2":
            keyword = input("Enter keyword to search in IssueText: ").strip()
            results = search_issues(keyword)
            if not results:
                print("No matching issues found.")
                continue
            print(f"\nFound {len(results)} issue(s):")
            for r in results:
                print(f"- IssueId {r['IssueId']}: {r['IssueText']} (Status: {r['Status']})")

        elif choice == "3":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
