from datetime import datetime

def complaint_serializer(complaint) -> dict:
    matched_results = []
    for result in complaint.get("matchedResults", []):
        matched_results.append({
            "matched_id": str(result["matched_id"]),
            "matched_score": result["matched_score"]
        })

    return {
        "_id": str(complaint["_id"]),
        "username": complaint.get("username"),
        "userId": str(complaint.get("userId")),
        "clerkUserId": complaint.get("clerkUserId"),
        "email": complaint.get("email"),
        "userPhoneNumber": complaint.get("userPhoneNumber"),
        "scammerPhoneNumber": complaint.get("scammerPhoneNumber"),
        "callFrequency": complaint.get("callFrequency"),
        "userConversationAudioUrl": complaint.get("userConversationAudioUrl"),
        "city": complaint.get("city"),
        "district": complaint.get("district"),
        "state": complaint.get("state"),
        "pincode": complaint.get("pincode"),
        "streetAddress": complaint.get("streetAddress"),
        "complainSubject": complaint.get("complainSubject"),
        "incidentDescription": complaint.get("incidentDescription"),
        "moneyScammed": complaint.get("moneyScammed"),
        "createdAt": complaint.get("createdAt").isoformat() if isinstance(complaint.get("createdAt"), datetime) else complaint.get("createdAt"),
        "updatedAt": complaint.get("updatedAt").isoformat() if isinstance(complaint.get("updatedAt"), datetime) else complaint.get("updatedAt"),
        "scammerAudioUrl": complaint.get("userScammerAudioUrl"),
        "matchedResults": matched_results
    }

    
def complaint_list_serializer(complaints) -> list:
    return [complaint_serializer(c) for c in complaints]
