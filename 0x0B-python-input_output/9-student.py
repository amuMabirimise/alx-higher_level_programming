#!/usr/bin/python3
"""Defines a class of Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """difines a new Student.

        Args:
            The first name of the student.
            The last name of the student.
            The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a rep of the Student."""
        return self.__dict__
