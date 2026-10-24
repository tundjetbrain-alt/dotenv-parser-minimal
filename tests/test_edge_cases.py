# Edge-case unit test suite for minimal dotenv parser (Rev #2 - 2026-10-24T10:20:51Z)
import unittest

def parse_line(line: str):
    s = line.strip()
    if not s or s.startswith('#') or '=' not in s:
        return None
    k, v = s.split('=', 1)
    return k.strip(), v.strip().strip('"\'')

class TestDotenvEdgeCases(unittest.TestCase):
    def test_quoted_value_rev_2(self):
        self.assertEqual(parse_line('API_URL="https://example.com"'), ('API_URL', 'https://example.com'))

if __name__ == '__main__':
    unittest.main()
