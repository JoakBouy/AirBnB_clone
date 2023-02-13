import io
import sys
import unittest
from unittest.mock import patch

from console import Console


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = Console()

    def test_get_input_returns_valid_input(self):
        with patch("builtins.input", return_value="Hello, world!"):
            result = self.console.get_input("Prompt: ")
            self.assertEqual(result, "Hello, world!")

    def test_get_input_handles_KeyboardInterrupt(self):
        with patch("builtins.input", side_effect=KeyboardInterrupt):
            with self.assertRaises(SystemExit):
                self.console.get_input("Prompt: ")

    def test_get_input_handles_EOFError(self):
        with patch("builtins.input", side_effect=EOFError):
            with self.assertRaises(SystemExit):
                self.console.get_input("Prompt: ")

    def test_output_returns_valid_output(self):
        with patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            self.console.output("Hello, world!")
            self.assertEqual(fake_stdout.getvalue(), "Hello, world!\n")

    def test_output_handles_KeyboardInterrupt(self):
        with patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            with self.assertRaises(SystemExit):
                self.console.output("Hello, world!", raise_keyboard_interrupt=True)
            self.assertEqual(fake_stdout.getvalue(), "Hello, world!\n")

    def test_output_handles_EOFError(self):
        with patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            with self.assertRaises(SystemExit):
                self.console.output("Hello, world!", raise_EOFError=True)
            self.assertEqual(fake_stdout.getvalue(), "Hello, world!\n")


if __name__ == "__main__":
    unittest.main()
