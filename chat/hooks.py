from . import __version__ as app_version
from frappe import __version__ as frappe_version

app_name = "chat"
app_title = "Consti Helpdesk"
app_publisher = "Frappe Technologies"
app_description = "Chat application for frappe"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "developers@frappe.io"
app_license = "MIT"
guest_title = app_title
is_frappe_above_v13 = int(frappe_version.split('.')[0]) > 13

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = ['chat.bundle.css'] if is_frappe_above_v13 else [
    '/assets/css/chat.css']
app_include_js = ['chat.bundle.js'] if is_frappe_above_v13 else [
    '/assets/js/chat.js']

# include js, css files in header of web template
web_include_css = ['chat.bundle.css'] if is_frappe_above_v13 else [
    '/assets/css/chat.css']
web_include_js = ['chat.bundle.js'] if is_frappe_above_v13 else [
    '/assets/js/chat.js']

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "chat/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "chat.utils.jinja_methods",
# 	"filters": "chat.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "chat.install.before_install"
after_install = "chat.patches.migrate_chat_data.execute"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "chat.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"chat.tasks.all"
# 	],
# 	"daily": [
# 		"chat.tasks.daily"
# 	],
# 	"hourly": [
# 		"chat.tasks.hourly"
# 	],
# 	"weekly": [
# 		"chat.tasks.weekly"
# 	],
# 	"monthly": [
# 		"chat.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "chat.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "chat.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "chat.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"chat.auth.validate"
# ]

sounds = [
    {'name': 'chat-notification', 'src': '/assets/chat/sounds/chat-notification.mp3', 'volume': 0.2},
    {'name': 'chat-message-send', 'src': '/assets/chat/sounds/chat-message-send.mp3', 'volume': 0.2},
    {'name': 'chat-message-receive', 'src': '/assets/chat/sounds/chat-message-receive.mp3', 'volume': 0.5}
]