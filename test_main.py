"""
Test goes here

"""

import subprocess
import psutil
import os
import time


def test_extract():
    """tests extract()"""
    result = subprocess.run(
        ["python", "main.py", "extract"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Extracting data..." in result.stdout


def test_transform_load():
    """tests transfrom_load"""
    result = subprocess.run(
        ["python", "main.py", "transform_load"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Transforming data..." in result.stdout


def test_update_record():
    """tests update_record"""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "update_record",
            "100 Grand",
            "1",
            "1",
            "1",
            "0",
            "0",
            "1",
            "0",
            "1",
            "0",
            "0.4",
            "0.4",
            "90.0",
            "1",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_delete_record():
    """tests delete_record"""
    result = subprocess.run(
        ["python", "main.py", "delete_record", "1"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_create_record():
    """tests create_record"""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "create_record",
            "Jujube Cake",
            "0",
            "1",
            "0",
            "0",
            "0",
            "1",
            "1",
            "1",
            "0",
            "0.4",
            "0.4",
            "90.0",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_general_query():
    """tests general_query"""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "general_query",
            "SELECT * FROM candy_data_DB WHERE competitorname = 'Air Heads'",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_read_data():
    """tests read_data"""
    result = subprocess.run(
        ["python", "main.py", "read_data"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def get_memory_usage():
    """Return memory usage in kilobytes."""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024  # Convert bytes to kilobytes


def run_tests():
    initial_memory = get_memory_usage()
    print(f"Initial memory usage: {initial_memory:.2f} kB")

    start_time = time.time()  # Start timing

    try:
        test_extract()
        test_transform_load()
        test_create_record()
        test_read_data()
        test_update_record()
        test_delete_record()
        test_general_query()
    except subprocess.CalledProcessError as e:
        print(f"Test failed with error: {e}")

    end_time = time.time()  # End timing

    final_memory = get_memory_usage()
    print(f"Final memory usage: {final_memory:.2f} kB")
    print(f"Memory used for tests: {final_memory - initial_memory:.2f} kB")

    time_taken = (end_time - start_time) * 1000000  # Calculate time taken
    print(f"Total time taken for tests: {time_taken:.2f} microseconds")


if __name__ == "__main__":
    test_extract()
    test_transform_load()
    test_create_record()
    test_read_data()
    test_update_record()
    test_delete_record()
    test_general_query()
    run_tests()
