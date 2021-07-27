from typing import NamedTuple

PositionBase = NamedTuple('Position',
                          [
                              ('title', str),
                              ('company', str),
                              ('link', str),
                              ('location', str),
                              ('remote', bool),
                              ('remote_level', str),
                              ('experience', str),
                              ('time_type', str),
                              ('tags', str)
                          ])

JOB_REMOTE_OPTION = ['Remote', 'Partially Remote', 'Not Specified']
REMOTE = JOB_REMOTE_OPTION[0]
PARTIALLY_REMOTE = JOB_REMOTE_OPTION[1]
NA_REMOTE = JOB_REMOTE_OPTION[2]

JOB_EXPERIENCE_OPTION = ['Junior Level', 'Mid Level', 'Senior Level', 'Not Specified']
JUNIOR_LEVEL = JOB_EXPERIENCE_OPTION[0]
MID_LEVEL = JOB_EXPERIENCE_OPTION[1]
SENIOR_LEVEL = JOB_EXPERIENCE_OPTION[2]
NA_LEVEL = JOB_EXPERIENCE_OPTION[3]

JOB_TIME_TYPE = ['Full-time', 'Part-time', 'Not Specified']
FULLTIME_JOB = JOB_TIME_TYPE[0]
PARTTIME_JOB = JOB_TIME_TYPE[1]
NA_TIME_JOB = JOB_TIME_TYPE[2]


class PositionClass:
    base = PositionBase
    defaults: tuple

    def __init__(self, defaults: tuple):
        self.base.__new__.__defaults__ = defaults
        self.defaults = defaults

    def create_position(self, title=None, company=None, link=None, location=None, remote=None, remote_level=None,
                        experience=None, time_type=None, tags=None):
        if not title:
            title = self.defaults[0]
        if not company:
            company = self.defaults[1]
        if not link:
            link = self.defaults[2]
        if not location:
            location = self.defaults[3]
        if not remote:
            remote = self.defaults[4]
        if not remote_level:
            remote_level = self.defaults[5]
        if not experience:
            experience = self.defaults[6]
        if not time_type:
            time_type = self.defaults[7]
        if not tags:
            tags = self.defaults[8]
        lowered_title = title.lower()
        if location:
            lowered_location = location.lower()

        remote, remote_level = PositionClass.__is_remote(lowered_title, lowered_location, remote, remote_level)
        experience = PositionClass.check_experience(lowered_title, link)
        # tags = ';'.join(PositionClass.create_tags(lowered_title))
        return self.base(title, company, link, location, remote, remote_level, experience, time_type, tags)

    def __hash__(self):
        return self._hash

    def __eq__(self, other):
        return self.title == other.title \
               and self.company == other.company \
               and self.link == other.link \
               and self.location == other.location

    @staticmethod
    def __is_remote(title, location, remote, remote_level):
        fully_remote = ['remote', 'wfh', 'work from home', 'מהבית', 'anywhere', 'מרחוק', 'רחוק', 'מרוחק', 'global']
        semi_remote = ['גמיש', 'flexible', 'hybrid', 'היברידי']
        if remote and remote_level:
            return remote, remote_level
        is_fully_remote = any(w for w in fully_remote if w in title or w in location) or remote
        is_semi_remote = any(w for w in semi_remote if w in title or w in location)
        not_specified = not (is_fully_remote or is_semi_remote)
        remote_level = NA_REMOTE
        if is_fully_remote:
            remote_level = REMOTE
        elif is_semi_remote:
            remote_level = PARTIALLY_REMOTE
        return not not_specified, remote_level

    @staticmethod
    def check_experience(title, link):
        level = NA_LEVEL
        if any(w for w in ['senior', 'team leader', 'expert', 'project', 'experienced', 'specialist',
                           'officer', 'program manager', 'development manager', 'lead', 'manager', 'professional',
                           'director', 'head', 'בכיר', 'מנוסה', 'ראשי', 'ראש צוות', 'ר"צ', 'vice', 'president', 'vp',
                           'sr.', 'snr ']
               if w in title):
            level = SENIOR_LEVEL
        elif any(w for w in ['student', 'junior', 'intern', 'סטודנט', 'צעיר', 'מתחיל', 'jr.']
                 if w in title):
            level = JUNIOR_LEVEL
        # else:
        #     level = MID_LEVEL
        return level

    @staticmethod
    def check_job_time(title, link):
        if any(w for w in ['part time', 'חלקית', 'part-time', 'maternity', 'paternity'] if w in title):
            return PARTTIME_JOB
        return FULLTIME_JOB

#### TESTS
# if __name__ == '__main__':
#     title = 'Front-End Developer'
#     x = PositionClass.create_tags(title.split('-')[0].split('–')[0].strip().lower())
#     print(f"For title: {title}")
#     print("Best matches are:")
#     for p in x[:3]:
#         if p['ratio']:
#             print(p['title'])
#
