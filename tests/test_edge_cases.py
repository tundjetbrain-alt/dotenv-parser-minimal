# Edge-case unit test suite for minimal dotenv parser (Rev #6 - 2026-10-31T00:53:58Z)
import unittest

def parse_line(line: str):
    s = line.strip()
    if not s or s.startswith('#') or '=' not in s:
        return None
    k, v = s.split('=', 1)
    return k.strip(), v.strip().strip('"\'')

class TestDotenvEdgeCases(unittest.TestCase):
    def test_quoted_value_rev_6(self):
        self.assertEqual(parse_line('API_URL="https://example.com"'), ('API_URL', 'https://example.com'))

if __name__ == '__main__':
    unittest.main()
