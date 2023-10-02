from main import CREATE, add_user, READ, UPDATE, DELETE, DROP  # import DROP

def test_CREATE():
    print("Running test_CREATE...")
    CREATE()
    users = READ()
    assert users == [], "Expected empty table after creation"
    print("test_CREATE passed!")

def test_add_user():
    print("Running test_add_user...")
    add_user("Charlie")
    users = READ()
    assert any(u[1] == "Charlie" for u in users), "Expected to find 'Charlie' in users after addition"
    print("test_add_user passed!")

def test_READ():
    print("Running test_READ...")
    # Ensure we have a clean state
    users_before = READ()
    add_user("Alice")
    users_after = READ()
    assert len(users_after) == len(users_before) + 1, "Expected one more user after addition"
    assert any(u[1] == "Alice" for u in users_after), "Expected to find 'Alice' in users after addition"
    print("test_READ passed!")

def test_UPDATE():
    print("Running test_UPDATE...")
    charlie_id = next(u[0] for u in READ() if u[1] == "Charlie")
    UPDATE(charlie_id, "Chuck")
    users = READ()
    assert any(u[1] == "Chuck" for u in users), "Expected name to be updated to 'Chuck'"
    print("test_UPDATE passed!")

def test_DELETE():
    print("Running test_DELETE...")
    chuck_id = next(u[0] for u in READ() if u[1] == "Chuck")
    DELETE(chuck_id)
    users = READ()
    assert all(u[1] != "Chuck" for u in users), "Expected 'Chuck' to be deleted from users"
    print("test_DELETE passed!")

if __name__ == "__main__":
    try:
        DROP()  # Drop the table before running tests
        test_CREATE()
        test_add_user()
        test_READ()
        test_UPDATE()
        test_DELETE()
        print("All tests passed!")
    except AssertionError as e:
        print(f"Test failed with assertion error: {e}")
    except Exception as e:
        print(f"Test failed with error: {e}")
