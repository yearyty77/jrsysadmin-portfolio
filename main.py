from servicenow import get_requests
from access_logic import process_access_request

def main():
    for request in get_requests():
        process_access_request(request)

if __name__ == "__main__":
    main()