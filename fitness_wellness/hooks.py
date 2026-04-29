app_name = "fitness_wellness"
app_title = "Fitness Wellness"
app_publisher = "Antigravity"
app_description = "Fitness & Wellness Management System"
app_email = "antigravity@google.com"
app_license = "mit"

# Apps
required_apps = ["frappe", "erpnext"]

# Fixtures
fixtures = [
    {"dt": "Custom Field", "filters": [["module", "=", "Fitness Wellness"]]},
    {"dt": "Property Setter", "filters": [["module", "=", "Fitness Wellness"]]},
    {"dt": "Workspace", "filters": [["name", "=", "Fitness Wellness"]]},
    {"dt": "Workflow", "filters": [["module", "=", "Fitness Wellness"]]},
    {"dt": "Workflow State", "filters": [["module", "=", "Fitness Wellness"]]},
    {"dt": "Workflow Action Master", "filters": [["module", "=", "Fitness Wellness"]]},
    {"dt": "Print Format", "filters": [["module", "=", "Fitness Wellness"]]},
    {"dt": "Report", "filters": [["module", "=", "Fitness Wellness"]]},
    {"dt": "Client Script", "filters": [["module", "=", "Fitness Wellness"]]},
    {"dt": "Server Script", "filters": [["module", "=", "Fitness Wellness"]]},
    {"dt": "Notification", "filters": [["module", "=", "Fitness Wellness"]]}
]

# Schedulers
scheduler_events = {
    "daily": [
        "fitness_wellness.member_management.doctype.member_subscription.member_subscription.send_membership_expiry_reminders",
        "fitness_wellness.billing.doctype.membership_invoice.membership_invoice.auto_generate_monthly_invoices",
        "fitness_wellness.facility_management.doctype.maintenance_schedule.maintenance_schedule.check_equipment_maintenance_due"
    ],
    "weekly": [
        "fitness_wellness.trainer_management.doctype.trainer_commission.trainer_commission.generate_trainer_commission_vouchers"
    ],
    "monthly": [
        "fitness_wellness.billing.doctype.emi_schedule.emi_schedule.process_emi_deductions"
    ]
}
