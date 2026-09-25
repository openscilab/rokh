# -*- coding: utf-8 -*-
"""Rokh errors."""


class RokhError(Exception):
    """Base exception for all Rokh errors."""


class RokhValidationError(RokhError, ValueError):
    """Raised when input validation fails."""
