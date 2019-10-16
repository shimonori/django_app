from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
import subprocess

from . import mixins




class MonthCalendar(mixins.MonthCalendarMixin, generic.TemplateView):
    template_name = 'calendar/month.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context
