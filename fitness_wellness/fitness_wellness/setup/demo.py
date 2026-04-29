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
    plan1 = _make("Membership Plan", plan_name="Standard Monthly", monthly_rate=1500, benefits="Gym Access")
    plan2 = _make("Membership Plan", plan_name="Premium Yearly", monthly_rate=12000, benefits="Gym + Pool + Spa Access")

    # 2. Members
    member1 = _make("Member", first_name="Rahul", last_name="Sharma", email="rahul@example.com", phone="9876543210", join_date=today())
    member2 = _make("Member", first_name="Anjali", last_name="Verma", email="anjali@example.com", phone="9876543211", join_date=today())

    # 3. Member Subscriptions
    sub1 = _make("Member Subscription", member=member1.name, plan=plan1.name, start_date=today(), end_date=add_months(today(), 1), status="Active")
    sub2 = _make("Member Subscription", member=member2.name, plan=plan2.name, start_date=today(), end_date=add_months(today(), 12), status="Active")

    # 4. Trainer Profiles
    trainer1 = _make("Trainer Profile", trainer_name="Vikram Singh", email="vikram@example.com", specialization="Strength & Conditioning", status="Active")
    trainer2 = _make("Trainer Profile", trainer_name="Sneha Kapoor", email="sneha@example.com", specialization="Yoga & Flexibility", status="Active")

    # 5. Class Types
    class1 = _make("Class Type", class_name="Crossfit Basics", description="High intensity cross training")
    class2 = _make("Class Type", class_name="Power Yoga", description="Vinyasa based power yoga")

    # 6. Class Schedules
    _make("Class Schedule", class_type=class1.name, trainer=trainer1.name, schedule_date=add_days(today(), 1), start_time="07:00:00", end_time="08:00:00")
    _make("Class Schedule", class_type=class2.name, trainer=trainer2.name, schedule_date=add_days(today(), 1), start_time="18:00:00", end_time="19:00:00")

    # 7. Equipment Register
    _make("Equipment Register", equipment_name="Treadmill T100", equipment_type="Cardio", status="Operational")
    _make("Equipment Register", equipment_name="Bench Press Rack", equipment_type="Weights", status="Operational")

    # 8. Diet Plans
    _make("Diet Plan", plan_name="Keto Weight Loss", member=member1.name, status="Active")

    # 9. Membership Invoices
    _make("Membership Invoice", member=member1.name, plan=plan1.name, amount=1500, due_date=today(), status="Paid")

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
