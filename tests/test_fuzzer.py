"""Unit tests for agent-api-fuzz-test-synthesizer."""
import unittest
from agent_api_fuzz_test_synthesizer.fuzzer import APIFuzzSynthesizer

class TestAPIFuzzer(unittest.TestCase):
    def test_integer_fuzzing(self):
        payloads = APIFuzzSynthesizer.generate_fuzz_values_for_type("count", "integer")
        categories = [p.category for p in payloads]
        self.assertIn("INT_MAX_32", categories)
        self.assertIn("NEGATIVE", categories)

    def test_string_fuzzing(self):
        payloads = APIFuzzSynthesizer.generate_fuzz_values_for_type("name", "string")
        categories = [p.category for p in payloads]
        self.assertIn("EMPTY_STRING", categories)
        self.assertIn("OVERFLOW_LENGTH", categories)

if __name__ == "__main__":
    unittest.main()
