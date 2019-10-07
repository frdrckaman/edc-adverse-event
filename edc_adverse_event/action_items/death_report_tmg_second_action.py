from edc_action_item.action_with_notification import ActionWithNotification
from edc_constants.constants import HIGH_PRIORITY, CLOSED
from django.utils.safestring import mark_safe

from ..constants import (
    ADVERSE_EVENT_ADMIN_SITE,
    ADVERSE_EVENT_APP_LABEL,
    DEATH_REPORT_TMG_SECOND_ACTION,
    DEATH_REPORT_TMG_ACTION,
)


class DeathReportTmgSecondAction(ActionWithNotification):
    name = DEATH_REPORT_TMG_SECOND_ACTION
    display_name = "TMG Death Report (2nd) pending"
    notification_display_name = "TMG Death Report (2nd)"
    parent_action_names = [DEATH_REPORT_TMG_ACTION]
    reference_model = f"{ADVERSE_EVENT_APP_LABEL}.deathreporttmgsecond"
    related_reference_model = f"{ADVERSE_EVENT_APP_LABEL}.deathreport"
    related_reference_fk_attr = "death_report"
    priority = HIGH_PRIORITY
    create_by_user = False
    color_style = "info"
    show_link_to_changelist = True
    admin_site_name = ADVERSE_EVENT_ADMIN_SITE
    singleton = True
    instructions = mark_safe(f"This report is to be completed by the TMG only.")

    def reopen_action_item_on_change(self):
        """Do not reopen if report status is CLOSED.
        """
        return self.reference_obj.report_status != CLOSED

    def close_action_item_on_save(self):
        """Close if report status is CLOSED.
        """
        return self.reference_obj.report_status == CLOSED