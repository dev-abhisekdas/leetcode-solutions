# config.py

"""
Global configuration and reusable constants for the leetcode_solutions package.
"""

# -------------------------------
# General Constants
# -------------------------------

INF = float("inf")
NEG_INF = float("-inf")

# Directions (useful for graph/grid problems)
DIRECTIONS_4 = [(0,1), (1,0), (0,-1), (-1,0)]
DIRECTIONS_8 = [
    (0,1), (1,0), (0,-1), (-1,0),
    (1,1), (1,-1), (-1,1), (-1,-1)
]

# -------------------------------
# Debug / Development Settings
# -------------------------------

DEBUG = False


# -------------------------------
# Default Test Settings
# -------------------------------

RUN_TESTS_ON_EXECUTION = True


# -------------------------------
# Naming Conventions (Optional)
# -------------------------------

REPO_NAME = "leetcode-solutions"
DEFAULT_PATTERN = "general"