import pytest
from data_structures.hashtable.hashtable import Hashtable


'''
test_set_key_value: Test that setting a key-value pair to the hashtable results in the value being in the data structure
test_retrieve_by_key: Test that retrieving a value based on a key returns the value stored in the hashtable
test_retrieve_nonexistent_key: Test that retrieving a key that does not exist in the hashtable returns null
test_list_unique_keys: Test that getting a list of all unique keys in the hashtable returns a list of all the unique keys
test_handle_collision: Test that the hashtable can successfully handle a collision within the data structure
test_retrieve_value_from_collision_bucket: Test that the hashtable can successfully retrieve a value from a bucket within the data structure that has a collision
test_hash_key: Test that the hashtable can successfully hash a key to an in-range value
'''



def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()  # Initialize hashtable
    hashtable.set("apple", "Used for apple sauce")  # Add key/value to hashtable
    actual = hashtable.get("apple")  # Retrieve value by key
    expected = "Used for apple sauce"
    assert actual == expected


# def test_get_apple():
#     hashtable = Hashtable()  # Create a new instance of the Hashtable class
#     hashtable.set("apple", "Used for apple sauce")  # Add a key-value pair to the Hashtable
#     actual = hashtable.get("apple")  # Retrieve the value associated with the 'apple' key
#     expected = "Used for apple sauce"  # Define the expected value for the 'apple' key
#     assert actual == expected  # Compare the actual and expected values, and raise an AssertionError if they don't match


def test_retrieve_nonexistent_key():
    # Initialize hashtable
    hashtable = Hashtable()

    # Attempt to retrieve value for nonexistent key
    assert hashtable.get("pear") is None



# @pytest.mark.skip("TODO") # test unique keys Add key/value pairs to hashtable
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    # Sort the key-value pairs in each inner list of the actual output
    # actual_sorted = [[sorted(pair, key=lambda x: str(x)) for pair in lst] for lst in actual]


    expected = [[['ahmad', 30]], [['silent', True], ['listen', 'to me']]]

    # Check that the contents of each inner list match
    assert actual == expected


def test_handle_collision():
    # Initialize hashtable
    hashtable = Hashtable(size=2)

    # Add key/value pairs that will result in a collision
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("pear", "Sweet fruit")
    hashtable.set("banana", "Yellow fruit")

    # Retrieve values for keys that collided
    assert hashtable.get("apple") == "Used for apple sauce"
    assert hashtable.get("pear") == "Sweet fruit"
    assert hashtable.get("banana") == "Yellow fruit"


def test_retrieve_value_from_collision_bucket():
    # Initialize hashtable
    hashtable = Hashtable(size=2)

    # Add key/value pairs that will result in a collision
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("pear", "Sweet fruit")
    hashtable.set("banana", "Yellow fruit")

    # Retrieve value from collision bucket
    node = hashtable._buckets[0]
    assert node.get("pear") == "Sweet fruit"


def test_hash_key():
    # Initialize hashtable
    hashtable = Hashtable()

    # Hash key using hash method
    hashed_key = hashtable.hash("apple")

    # Check if hashed key is in range
    assert hashed_key >= 0 and hashed_key < hashtable._size


