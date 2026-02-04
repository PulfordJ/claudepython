"""Sample module — run with: uv run src/hello.py"""

import numpy as np


def greet(name: str) -> str:
    return f"Hello, {name}!"


def quick_stats(values: list[float]) -> dict[str, float]:
    """Return basic descriptive stats for a list of numbers."""
    arr = np.array(values)
    return {
        "mean": float(arr.mean()),
        "std": float(arr.std()),
        "min": float(arr.min()),
        "max": float(arr.max()),
    }


if __name__ == "__main__":
    print(greet("Codespace"))

    data = [1.0, 2.5, 3.7, 4.2, 5.9]
    for k, v in quick_stats(data).items():
        print(f"  {k}: {v:.3f}")
