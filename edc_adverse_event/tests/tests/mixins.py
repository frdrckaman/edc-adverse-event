from edc_action_item.models import ActionItem
from edc_constants.constants import OTHER, YES
from model_mommy import mommy
from random import choice

from ...models import CauseOfDeath


class DeathReportTestMixin:

    def get_death_report(self, cause_of_death=None, cause_of_death_other=None):

        causes_qs = CauseOfDeath.objects.exclude(short_name=OTHER)
        cause_of_death = (
            cause_of_death or causes_qs[choice(
                [x for x in range(0, len(causes_qs))])]
        )

        # create ae initial
        ae_initial = mommy.make_recipe(
            "adverse_event_app.aeinitial",
            subject_identifier=self.subject_identifier,
            susar=YES,
            susar_reported=YES,
            ae_grade=5,
            user_created="erikvw",
        )

        action_item = ActionItem.objects.get(
            subject_identifier=self.subject_identifier,
            parent_action_item=ae_initial.action_item,
            reference_model="adverse_event_app.deathreport",
        )

        # create death report
        death_report = mommy.make_recipe(
            "adverse_event_app.deathreport",
            subject_identifier=self.subject_identifier,
            action_identifier=action_item.action_identifier,
            cause_of_death=cause_of_death,
            cause_of_death_other=cause_of_death_other,
            user_created="erikvw",
        )
        return death_report