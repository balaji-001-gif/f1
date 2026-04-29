import frappe
from frappe import _

def get_context(context):
    if frappe.session.user == "Guest":
        frappe.local.flags.redirect_location = "/login"
        raise frappe.Redirect

    member_email = frappe.session.user
    
    # Fetch linked member
    member = frappe.db.get_value("Member", {"email": member_email}, ["name", "first_name", "last_name", "status"], as_dict=True)
    
    if not member:
        context.no_member_record = True
        return context

    context.member = member
    context.no_member_record = False

    # Fetch active subscription
    context.subscription = frappe.db.get_all(
        "Member Subscription",
        filters={"member": member.name, "status": "Active"},
        fields=["name", "membership_plan", "start_date", "end_date"]
    )

    # Fetch Diet Plans
    context.diet_plans = frappe.db.get_all(
        "Diet Plan",
        filters={"member": member.name, "status": "Active"},
        fields=["name", "plan_name", "total_calories", "total_protein", "total_carbs", "total_fats"]
    )

    # Fetch Attendance logs
    context.attendance = frappe.db.get_all(
        "Member Attendance",
        filters={"member": member.name},
        fields=["attendance_date", "status"],
        order_by="attendance_date desc",
        limit=10
    )

    # Fetch Upcoming Classes
    context.classes = frappe.db.get_all(
        "Class Enrollment",
        filters={"member": member.name},
        fields=["class_schedule", "status"]
    )
    # Fetch Assigned Trainers
    context.trainers = frappe.db.get_all(
        "Trainer Assignment",
        filters={"member": member.name},
        fields=["trainer"]
    )
    # Fetch Body Metrics
    context.metrics = frappe.db.get_all(
        "Body Metric Log",
        filters={"member": member.name},
        fields=["date", "weight", "body_fat_percentage"],
        order_by="date desc",
        limit=5
    )

    return context
