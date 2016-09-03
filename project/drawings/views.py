from django.shortcuts import render
from django.views import generic
from .models import Notebook

# Create your views here.

class HomepageView(generic.TemplateView):


    """Deluxe Nation homepage"""

    template_name = "drawings/homepage.html"
    # queryset = Cohort.published FIXME

    #
    # def get_object(self, queryset=None):
    #     """Get cohort to show.
    #
    #     Optionally, a cohort id can be given in the URL---if so, that will be
    #     the cohort shown. Otherwise, we'll use the one added by
    #     `frodo.middleware.AddCohortMiddleware`.
    #     """
    #
    #     return self.get_cohort(self.kwargs.get('pk'))
    #
    #

    def get_context_data(self, **kwargs):
        """Add data."""

        max_num = 5
        #
        context = super(HomepageView, self).get_context_data()
        #
        context['notebooks'] = \
            (Notebook
             .objects
             # .select_related('drawing')
             .order_by('-drawn_at')
             )[:max_num]

        # # We want enough labsessions for 3 exercise sessions to show up---so we'll ask for
        # # 3x as many lab sessions as we need here, and we filter this down to the 3 actual
        # # exercisesessions in the template using |slice
        #
        # context['exercise_labsessions'] = \
        #     (ExerciseLabSession
        #      .objects  # CORRECT: do not change to 'published'; ELSs are not published
        #      .filter(exercise_session__status='published',
        #              exercise_session__cohort=self.object,
        #              end_at__gt=now())
        #      .select_related('exercise_session', 'exercise_session__exercise')
        #      .order_by('start_at')
        #      )[:max_num * 3]
        #
        # context['homeworksession'] = \
        #     (HomeworkSession
        #      .published
        #      .filter(cohort=self.object, end_at__gt=now())
        #      .select_related('homework')
        #      .order_by('start_at')
        #      ).first()
        #
        # context['lightningtalks'] = \
        #     (LightningTalk
        #      .objects  # CORRECT FOR NOW -- since we show the sched of not-yet-published talks
        #      .filter(student__cohort=self.object,
        #              end_at__gt=now(),
        #              status='published')
        #      .select_related('student')
        #      .order_by('start_at')
        #      )[:max_num]
        #
        # context['events'] = \
        #     (Event
        #      .published
        #      .filter(cohort=self.object, end_at__gt=now())
        #      .order_by('start_at')
        #      )[:max_num]
        #
        # context['announcements'] = \
        #     (Announcement
        #      .published
        #      .filter(cohort=self.object, start_at__lt=now(), end_at__gt=now())
        #      .order_by('-start_at')
        #      )



        return context

