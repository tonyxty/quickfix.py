#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `quickfix_py` package."""


import unittest
from pathlib import Path
from shlex import split

from quickfix_py import cli


class TestQuickfix_py(unittest.TestCase):
    """Tests for `quickfix_py` package."""

    @classmethod
    def setUpClass(cls):
        """Set up test fixtures, if any."""
        cls.here = Path(__file__).parent

    def test_cli(self):
        """Test something."""
        cli.main(split(str(self.here / "errors" / "div_by_zero.py")))
