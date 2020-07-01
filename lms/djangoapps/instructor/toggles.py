"""
Waffle flags for instructor dashboard.
"""

from openedx.core.djangoapps.waffle_utils import CourseWaffleFlag, WaffleFlagNamespace

WAFFLE_NAMESPACE = 'instructor'

DATA_DOWNLOAD_V2 = CourseWaffleFlag(
    waffle_namespace=WaffleFlagNamespace(name=WAFFLE_NAMESPACE, log_prefix='instructor_dashboard: '),
    flag_name='enable_data_download_v2',
    flag_undefined_default=False
)


def data_download_v2_is_enabled(course_key):
    """
    check if data download v2 is enabled.
    """
    return DATA_DOWNLOAD_V2.is_enabled(course_key)
