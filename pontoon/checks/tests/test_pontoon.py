# -*- coding: utf-8 -*-
from __future__ import absolute_import
import pytest

from mock import MagicMock

from pontoon.checks.libraries.pontoon import (
    get_max_length,
    run_checks
)


@pytest.fixture()
def get_entity_mock():
    """
    Create an entity mock with comment, resource.path and extension.
    """
    def _f(extension, comment='', string='', allows_empty_translations=False):
        entity = MagicMock()
        entity.comment = comment
        entity.string = string
        entity.resource.format = extension
        entity.resource.path = 'test.' + extension
        entity.resource.allows_empty_translations = allows_empty_translations
        return entity
    yield _f


@pytest.mark.parametrize(
    'comment, expected',
    (
        ('MAX_LENGTH: 24', 24),
        ('MAX_LENGTH: 4', 4),
        ('MAX_LENGTH:  4', 4),
        ('MAX_LENGTH:4 ', 4),
        ('MAX_LENGTH:  42  ', 42),
        ('MAX_LENGTH:  42\n MAX_LENGTH: 10 ', 42),
        ('MAX_LENGTH: 123 characters', 123),
        ('MAX_LENGTH: 4\naaaa', 4),
        ('bbbb \n MAX_LENGTH: 4\naaaa', 4),
        ('MAX_LENGTH: 4 characters\naaaa', 4),
        ('bbbb\nMAX_xLENGTH: 4 characters\naaaa', None),
        ('bbbb\nMAX_LENGTH: z characters\naaaa', None),
        ('bbbb\nMAX_LENGTH:\n 4 characters\naaaa', None),
    )
)
def test_too_long_translation_max_length(comment, expected):
    """
    Checks should return an error if a translation is too long.
    """
    assert get_max_length(comment) == expected


def test_too_long_translation_valid_length(get_entity_mock):
    """
    Checks shouldn't return an error if a translation isn't too long.
    """
    assert run_checks(
        get_entity_mock('lang', 'MAX_LENGTH: 4'),
        '0123'
    ) == {}


def test_too_long_translation_html_tags(get_entity_mock):
    """
    HTML tags can't be included in the MAX_LENGTH check.
    """
    assert run_checks(
        get_entity_mock('lang', 'MAX_LENGTH: 4'),
        '<a href="pontoon.mozilla.org">01</a><i>23</i>'
    ) == {}

    assert run_checks(
        get_entity_mock('lang', 'MAX_LENGTH: 4'),
        '<a href="pontoon.mozilla.org">012</a><i>23</i>'
    ) == {
        'pErrors': ['Translation too long']
    }

    # Check if entities are causing false errors
    assert run_checks(
        get_entity_mock('lang', 'MAX_LENGTH: 4'),
        '<a href="pontoon.mozilla.org">??&nbsp;</a><i>??&nbsp;</i>'
    ) == {}

    assert run_checks(
        get_entity_mock('lang', 'MAX_LENGTH: 4'),
        '<a href="pontoon.mozilla.org">??&nbsp;&nbsp;</a><i>??&nbsp;</i>'
    ) == {
        'pErrors': ['Translation too long']
    }


def test_too_long_translation_invalid_length(get_entity_mock):
    """
    Checks should return an error if a translation is too long.
    """
    assert run_checks(
        get_entity_mock('lang', 'MAX_LENGTH: 2'),
        '0123'
    ) == {'pErrors': ['Translation too long']}


def test_empty_translations(get_entity_mock):
    """
    Empty translations shouldn't be allowed for some extensions.
    """
    assert run_checks(
        get_entity_mock('po'),
        ''
    ) == {
        'pErrors': [u'Empty translations are not allowed']
    }

    assert run_checks(
        get_entity_mock('properties', allows_empty_translations=True),
        ''
    ) == {}


def test_lang_newlines(get_entity_mock):
    """Newlines aren't allowed in lang files"""
    assert run_checks(
        get_entity_mock('lang'),
        'aaa\nbbb'
    ) == {
        'pErrors': [u'Newline characters are not allowed']
    }

    assert run_checks(
        get_entity_mock('po'),
        'aaa\nbbb'
    ) == {}


def test_ftl_parse_error(get_entity_mock):
    """Invalid FTL strings are not allowed"""
    assert run_checks(
        get_entity_mock('ftl', string='key = value'),
        'key'
    ) == {
        'pErrors': [u'Expected message "key" to have a value or attributes']
    }

    assert run_checks(
        get_entity_mock('ftl', string='key = value'),
        'key = translation'
    ) == {}


def test_ftl_non_localizable_entries(get_entity_mock):
    """Non-localizable entries are not allowed"""
    assert run_checks(
        get_entity_mock('ftl', string='key = value'),
        '[[foo]]'
    ) == {
        'pErrors': [u'Translation needs to be a valid localizable entry']
    }


def test_ftl_id_missmatch(get_entity_mock):
    """ID of the source string and translation must be the same"""
    assert run_checks(
        get_entity_mock('ftl', string='key = value'),
        'key1 = translation'
    ) == {
        'pErrors': [u'Translation key needs to match source string key']
    }
