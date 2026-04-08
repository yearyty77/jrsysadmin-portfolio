def get_requests():
    """
    Simulated ServiceNow user access requests.
    """

    simulated_response = {
        "result": [
            {
                "sys_id": "u123",
                "number": "RITM0012345",
                "requested_for": {
                    "user_name": "jdoe",
                    "email": "jdoe@company.com",
                    "first_name": "John",
                    "last_name": "Doe"
                },
                "system": "Centric PLM",
                "requested_roles": [
                    "Designer",
                    "Material Viewer"
                ],
                "request_type": "New Access",
                "state": "Approved"
            }
        ]
    }

    return simulated_response["result"]