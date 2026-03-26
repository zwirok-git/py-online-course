from __future__ import annotations


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        return cls(name=course_dict["name"],
                   description=course_dict["description"],
                   weeks=cls.duration_in_weeks(course_dict))

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return days // 7 if days % 7 == 0 else days // 7 + 1

    @staticmethod
    def duration_in_weeks(course_info: dict) -> int:
        if "weeks" in course_info:
            return course_info["weeks"]

        return OnlineCourse.days_to_weeks(course_info["days"])
