http_status = 200

match http_status:
    case 200 | 201:
        print("Success")
    case 400:
        print("Bad request")
    case 404:
        print("Not found")
    case 500 | 501:
        print("Server Error")
    case _:
        print("Unknown")
