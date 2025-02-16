#!/usr/bin/env python3
import unittest
import logging
import importlib
import random
import pytest

from unittest.mock import patch, MagicMock, mock_open

recon = importlib.import_module('ciftify.bin.cifti_vis_recon_all')

logging.disable(logging.CRITICAL)

class TestUserSettings(unittest.TestCase):

    def test_exits_gracefully_when_user_supplies_undefined_qc_mode(self):
        arguments = {'<subject>': 'some_subject',
                     '<QCmode>': 'new_mode',
                     '--temp-dir': None}
        with pytest.raises(SystemExit):
            recon.UserSettings(arguments)

class TestModifyTemplateContents(unittest.TestCase):

    original_vals = ['HCPDATA_ABSPATH', 'HCPDATA_RELPATH', 'SUBJID']
    scene_file = '/path/to/scene/file'

    def test_expected_strings_are_replaced(self):
        settings = self.get_settings()
        template_contents = get_template_contents(self.original_vals)
        modified_text = recon.modify_template_contents(template_contents,
                settings, self.scene_file)
        for val in self.original_vals:
            assert val not in modified_text

    def get_settings(self):
        class SettingsStub(object):
            def __init__(self):
                self.work_dir = '/path/num1'
                self.subject = 'subject_id'
        return SettingsStub()

def get_template_contents(keys):
    # Not a stroke, just randomly generated text
    mock_contents = ['Behind sooner dining so window excuse he summer.',
            ' Breakfast met certainty and fulfilled propriety led. ',
            ' Waited get either are wooded little her. Contrasted ',
            'unreserved as mr particular collecting it everything as ',
            'indulgence. Seems ask meant merry could put. Age old begin ',
            'had boy noisy table front whole given.']
    mock_contents.extend(keys)
    random.shuffle(mock_contents)
    template_contents = ' '.join(mock_contents)
    return template_contents
