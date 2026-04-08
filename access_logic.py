def generate_username(user):
    """
    Generate a username in the format:
    firstname.lastname
    """

    first_name = user.get("first_name", "").strip().lower()
    last_name = user.get("last_name", "").strip().lower()

    if not first_name or not last_name:
        return None

    return f"{first_name}.{last_name}"

def process_access_request(req):
    """
    Handle a single user access request.
    Generates a username instead of reading it from ServiceNow.
    """

    user = req.get("requested_for", {})
    roles = req.get("requested_roles", [])

    username = generate_username(user)

    print("Processing access request:", req.get("number"))
    print("Generated username:", username)
    print("Email:", user.get("email"))
    print("Requested roles:", roles)
    print("-" * 50)