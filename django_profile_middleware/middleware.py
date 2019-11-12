from __future__ import with_statement

import pstats
from django.conf import settings

try:
    import cProfile
except ImportError:
    import profile

from io import StringIO


class ProfilerMiddleware(object):
    profiler = None

    def can(self):
        if settings.DEBUG and settings.PROFILER["enable"]:
            return True

    def process_view(self, *args, **kwargs):
        if self.can():
            self.profiler = cProfile.Profile()
            self.profiler.enable()

    def process_response(self, request, response):
        if self.can():
            self.profiler.disable()

            profile_stream = StringIO()

            sort_by = settings.PROFILER.get('sort', 'time')
            count = settings.PROFILER.get('count', None)

            pstats.Stats(self.profiler, stream=profile_stream).sort_stats(sort_by).print_stats(count)

            for output in settings.PROFILER.get('output', ['console', 'file']):

                if output == 'console':
                    print(profile_stream.getvalue())

                if output == 'file':
                    file_loc = settings.PROFILER.get('file_location', 'profiling_results.txt')
                    with open(file_loc, 'a+') as _file:
                        counter = str(profile_stream.getvalue())
                        file.write(counter)

        return response
