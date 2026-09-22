# -*- coding: utf-8 -*-
"""Rokh errors."""


class RokhError(Exception):
    """Base exception for all Rokh errors."""


class RokhValidationError(ValueError):
    """Base class for validation errors in Rokh."""

    pass
