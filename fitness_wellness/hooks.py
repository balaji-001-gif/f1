app_name = "fitness_wellness"
app_title = "Fitness Wellness"
app_publisher = "Antigravity"
app_description = "Fitness & Wellness Management System"
app_email = "antigravity@google.com"
app_license = "mit"

# Apps
required_apps = ["frappe", "erpnext"]

# Module registration
app_include_js = []
app_include_css = []

# This registers the module
modules = {
    "Fitness Wellness": {
        "color": "#00BFA5",
        "icon": "octicon octicon-heart",
        "type": "module",
        "label": "Fitness Wellness"
    }
}


# DocType Class
# override_doctype_class = {
# 	"Todo": "custom_app.overrides.CustomTodo"
# }

# Document Events
# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Fixtures
fixtures = [
    {"dt": "Module Def"},
    {"dt": "Custom Field"},
    {"dt": "Property Setter"},
    {"dt": "Workspace"},
    {"dt": "Workflow"},
    {"dt": "Workflow State"},
    {"dt": "Workflow Action Master"},
    {"dt": "Print Format"},
    {"dt": "Report"},
    {"dt": "Client Script"},
    {"dt": "Server Script"},
    {"dt": "Notification"},
    {"dt": "Auto Repeat"},
    {"dt": "Assignment Rule"}
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
