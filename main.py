#!/usr/bin/env python3
import asyncio
import python_weather

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
      end_line = start_line + 7
      desired_lines = lines[start_line:end_line]
      for line in desired_lines:
          phase.append("  "+line)

    return phase

async def weather(location):
    async with python_weather.Client() as client:
        # Fetch a weather forecast from a city
        weather = await client.get(location)

        n = True
        for daily in weather.daily_forecasts:
            while n:
                phase = daily.moon_phase
                n = False
        return phase

phase = asyncio.run(weather("raipur"))
phases = [phase for phase in python_weather.enums.Phase]

# Read moon phases from art.txt
display_phase = read_moon_phase("art.txt", phases.index(phase))


if __name__ == "__main__":
    print("\n" + "".join(display_phase), end="")
