import frappe


@frappe.whitelist()
def get_member_stats():
    """
    Helper method to get member statistics for the dashboard
    """
    return {
        "active_members": frappe.db.count(
            "Member Subscription", {"status": "Active"}
        ),
        "total_trainers": frappe.db.count(
            "Trainer Profile", {"status": "Active"}
        ),
        "todays_attendance": frappe.db.count(
            "Member Attendance",
            {"attendance_date": ["=", frappe.utils.today()]}
        )
    }


@frappe.whitelist()
def get_onboarding_status():
    """
    Helper method to track onboarding progress
    """
    return {
        "has_members": frappe.db.count("Member") > 0,
        "has_plans": frappe.db.count("Membership Plan") > 0,
        "has_settings": frappe.db.count("Fitness Wellness Settings") > 0
    }
