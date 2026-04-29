"""
Fitness Wellness Demo Data Setup
=================================
Populates a realistic fitness and wellness scenario for demonstration.

Usage:
    bench --site <your-site> execute fitness_wellness.setup.demo.run
"""

import frappe
from frappe.utils import today, add_months, add_days

DEMO_TAG = "__fitness_wellness_demo__"

def run():
    """Main entry point. Run via: bench execute fitness_wellness.setup.demo.run"""
    frappe.set_user("Administrator")

    print("🚀 Fitness Wellness: Loading demo data...")

    # 1. Membership Plans
    plan1 = _make("Membership Plan", plan_name="Standard Monthly", plan_type="Gym", duration_months=1, total_amount=1500)
    plan2 = _make("Membership Plan", plan_name="Premium Yearly", plan_type="Gym", duration_months=12, total_amount=12000)

    # 2. Members
    member1 = _make("Member", first_name="Rahul", last_name="Sharma", email="rahul@example.com", contact_number="+91-9876543210", joining_date=today())
    member2 = _make("Member", first_name="Anjali", last_name="Verma", email="anjali@example.com", contact_number="+91-9876543211", joining_date=today())

    # 3. Member Subscriptions
    sub1 = _make("Member Subscription", member=member1.name, membership_plan=plan1.name, start_date=today(), status="Active")
    sub2 = _make("Member Subscription", member=member2.name, membership_plan=plan2.name, start_date=today(), status="Active")

    # 4. Trainer Profiles
    trainer1 = _make("Trainer Profile", trainer_name="Vikram Singh", email="vikram@example.com", status="Active")
    trainer2 = _make("Trainer Profile", trainer_name="Sneha Kapoor", email="sneha@example.com", status="Active")

    # 5. Class Types
    class1 = _make("Class Type", class_type_name="Crossfit Basics", duration_minutes=60)
    class2 = _make("Class Type", class_type_name="Power Yoga", duration_minutes=45)

    # 6. Diet Plans
    _make("Diet Plan", member=member1.name, plan_name="Keto Weight Loss", status="Active", start_date=today())
    _make("Diet Plan", member=member2.name, plan_name="Vegetarian Bulk", status="Active", start_date=today())

    frappe.db.commit()
    print("✅ Demo data loaded successfully!")


def _make(doctype, **kwargs):
    """Create and insert a document, return its name."""
    # Avoid duplicates
    if doctype == "Membership Plan" and frappe.db.exists("Membership Plan", {"plan_name": kwargs.get("plan_name")}):
        return frappe.get_doc("Membership Plan", {"plan_name": kwargs.get("plan_name")})
    if doctype == "Member" and frappe.db.exists("Member", {"email": kwargs.get("email")}):
        return frappe.get_doc("Member", {"email": kwargs.get("email")})
    if doctype == "Trainer Profile" and frappe.db.exists("Trainer Profile", {"email": kwargs.get("email")}):
        return frappe.get_doc("Trainer Profile", {"email": kwargs.get("email")})
    if doctype == "Class Type" and frappe.db.exists("Class Type", {"class_name": kwargs.get("class_name")}):
        return frappe.get_doc("Class Type", {"class_name": kwargs.get("class_name")})
    if doctype == "Equipment Register" and frappe.db.exists("Equipment Register", {"equipment_name": kwargs.get("equipment_name")}):
        return frappe.get_doc("Equipment Register", {"equipment_name": kwargs.get("equipment_name")})
    if doctype == "Diet Plan" and frappe.db.exists("Diet Plan", {"plan_name": kwargs.get("plan_name")}):
        return frappe.get_doc("Diet Plan", {"plan_name": kwargs.get("plan_name")})

    doc = frappe.new_doc(doctype)
    doc.update(kwargs)
    doc.insert(ignore_permissions=True, ignore_mandatory=True)
    return doc
