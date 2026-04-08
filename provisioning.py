def provision_user_access(request):
    """
    Substitute API calls in later...
    """

    user = request["requested_for"]
    requested_roles = request["requested_roles"]

    # Step 1: Generate username
    base_username = generate_username(user)

    # Step 2: Decide create vs update (API call later)
    user_exists = check_user_exists_in_centric(base_username)

    if user_exists:
        handle_existing_user(user, requested_roles)
    else:
        handle_new_user(user, base_username, requested_roles)

        def check_user_exists_in_centric(username):
    """
    Substitute Centric API call in later.
    """
    raise NotImplementedError("Centric API not integrated yet")


def handle_new_user(user, username, roles):
    """
    Substitute API call later for centric user creation.
    """
    print(f"[PLAN] Create user {username} with roles {roles}")


def handle_existing_user(user, roles):
    """
    Substitute API call later for updating an existing user.
    """
    print(f"[PLAN] Update user {user.get('email')} with roles {roles}")
``