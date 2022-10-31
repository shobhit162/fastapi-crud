def userEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "name":item["name"],
        "email":item["email"],
        "mobile":item["mobile"],
        "address":item["address"],
        "project_name":item["project_name"],
        "deadline":item["deadline"],
        "budget":item["budget"],
        "amount_paid":item["amount_paid"]
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]