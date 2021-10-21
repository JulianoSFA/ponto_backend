import datetime

from django.db import models

from apps.ponto.models.TimeBlock import TimeBlock


class WorkTime(TimeBlock):
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-id']

    @property
    def time_span(self):
        if not self.end: return 0
        return self.end - self.start

    def save(self, *args, **kwargs):
        if not self.end:
            super(WorkTime, self).save(*args, **kwargs)
            return

        self.day = self.start.date()
        starting_date = self.day
        ending_date = self.end.date()

        if starting_date != ending_date:
            start_next_day = datetime.datetime.combine(self.start.date() + datetime.timedelta(days=1), datetime.time.min)
            new_work_time = WorkTime(start=start_next_day, end=self.end, day=start_next_day.date())
            self.next_time_block = new_work_time
            self.end = start_next_day - datetime.timedelta(seconds=1)
            new_work_time.save()

        super(WorkTime, self).save(*args, **kwargs)
