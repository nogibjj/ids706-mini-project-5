from main import CREATE, add_user, READ, UPDATE, DELETE

def test_CREATE():
    CREATE()
    users = READ()
    assert users == [], "Expected empty table after creation"

def test_add_user():
    add_user("Charlie")
    users = READ()
    assert any(u[1] == "Charlie" for u in users), "Expected to find 'Charlie' in users after addition"

def test_READ():
    # Ensure we have a clean state
    users_before = READ()
    add_user("Alice")
    users_after = READ()
    assert len(users_after) == len(users_before) + 1, "Expected one more user after addition"
    assert any(u[1] == "Alice" for u in users_after), "Expected to find 'Alice' in users after addition"

def test_UPDATE():
    charlie_id = next(u[0] for u in READ() if u[1] == "Charlie")
    UPDATE(charlie_id, "Chuck")
    users = READ()
    assert any(u[1] == "Chuck" for u in users), "Expected name to be updated to 'Chuck'"

def test_DELETE():
    chuck_id = next(u[0] for u in READ() if u[1] == "Chuck")
    DELETE(chuck_id)
    users = READ()
    assert all(u[1] != "Chuck" for u in users), "Expected 'Chuck' to be deleted from users"

if __name__ == "__main__":
    test_CREATE()
    test_add_user()
    test_READ()
    test_UPDATE()
    test_DELETE()
