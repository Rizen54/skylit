import sys
import time
import random
from termcolor import colored


def clear_screen():
    sys.stdout.write("\x1b[2J\x1b[H")
    sys.stdout.flush()


def read_moon_phase(filename, start):
    """
    Reads moon phases from a text file.

    Args:
      filename: The name of the text file containing moon phases.

    Returns:
      A list of strings, where each element represents a single moon phase
      consisting of 6 lines of ASCII art and a blank line.
    """

    phase = []

    with open(filename, 'r') as f:
      current_phase = []

      lines = f.readlines()
      start_line = start*7  # Starting line (0-based index)
      end_line = start_line + 6
      desired_lines = lines[start_line:end_line]
      for line in desired_lines:
          phase.append("  "+line)

    return phase


# Read moon phases from art.txt
phases = []
for i in range(0, 8):
    phases.append(read_moon_phase("prt.txt", i))


if __name__ == "__main__":
    clear_screen()
    while True:
      for phase in phases:
          print("\n"+"".join(phase), end="")
          time.sleep(0.3)
          clear_screen()
