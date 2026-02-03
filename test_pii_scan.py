"""Tests for pii_scan"""
import unittest
import re
import os
from pii_scan import show_aggie_pride, analyze_text


class TestPIIScan(unittest.TestCase):
    """Tests for the pii_scan module"""
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_base_supported_entities(self):
        """Test to make sure the default supported entities are returned"""
        # read entities from team_entities.csv
        with open('team_entities.csv', encoding='utf-8') as f:
            entities = f.read().splitlines()
            # remove the header row
            entities = entities[1:]
        supported_entities = [entity.split(',')[0] for entity in entities]

        results = analyze_text('', [], show_supported=True)

        for entity in supported_entities:
            if entity:
                self.assertIn(entity, results)
            # Check to make sure recognizer actually loads the entity
                analyze_text('entity load test', entity_list=[entity])

    def test_starts_with_test(self):
        """Test to make sure all test methods start with test"""
        # In order to run as a test case the method name must start with test
        # This test checks to make sure all defines within test files start with test
        # This is a common mistake that can cause tests to be skipped
        for file in os.listdir('.'):
            if file.endswith('.py') and file.startswith('test_'):
                with open(file, encoding='utf-8') as f:
                    for line in f:
                        # make sure everything that looks like a method name starts with test
                        m = re.search(r'\s*def (\w+)', line)
                        if m:
                            err = 'Method name does not start with test: def '
                            err += m.group(1) + ' in ' + file
                            self.assertTrue(m.group(1).startswith('test'), err)
