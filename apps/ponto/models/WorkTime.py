import datetime

from django.db import models

from apps.ponto.models.TimeBlock import TimeBlock


class WorkTime(TimeBlock):
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-day', '-start']

    @property
    def time_span(self):
        if not self.end: return 0
        return self.end - self.start

    def save(self, *args, **kwargs):
        self.day = self.start.date()
        starting_date = self.day
        ending_date = self.end.date()

        if starting_date != ending_date:
            start_next_day = datetime.datetime.combine(self.start.date() + datetime.timedelta(days=1), datetime.time.min)
            new_work_time = WorkTime(start=start_next_day, end=ending_date, day=start_next_day.date())
            self.next_time_block = new_work_time
            new_work_time.save()
            
        super(WorkTime, self).save(*args, **kwargs)
