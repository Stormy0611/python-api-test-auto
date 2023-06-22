# /review/{review_id}
# /appointment/{appointment_id}/review
review = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/Review",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
    },
    "appointment_id": {
      "type": "string",
    },
    "rating": {
      "type": "integer",
    },
    "review": {
      "type": "string",
    },
    "client_id": {
      "type": "string",
    },
    "listing_id": {
      "type": "string",
    },
    "provider_id": {
      "type": "string",
    },
    "created_at": {
      "type": "string",
    },
  },
  "required": [
        "id",
        "appointment_id",
        "rating",
        "client_id",
        "listing_id", 
        "provider_id",
        "created_at"
  ]
}

# /user/review
# /provider/{provider_id}/review
# /listing/{listing_id}/review
get_x_all_review = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/",
  "type": "array",
  "items": [
      review
  ],
}

# 
card = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/Card",
  "type": "object",
  "properties": {
      "brand": {
          "type": "string",
      },
      "exp_month": {
          "type": "integer",
      },
      "exp_year": {
          "type": "integer",
      },
      "last4": {
          "type": "string",
      },
  },
  "required": [
      "brand",
      "exp_month",
      "exp_year",
      "last4"
  ]
}

# 
payment_method = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/PaymentMethod",
  "type": "object",
  "properties": {
      "id": {
          "type": "string",
      },
      "card": {
        card    
      }
  },
  "required": [
      "id"
  ]
}

# /user/payment_method
get_x_all_payment_method = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/",
  "type": "array",
  "items": [
      payment_method
  ],
}

# /provider/account_status
account_status = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/AccountStatus",
  "type": "object",
  "properties": {
      "account_status": {
          "type": "boolean"
      },
  },
  "required": [
          "account_status"
      ]
}

# /provider/account_link
account_link = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/AccountLink",
  "type": "object",
  "properties": {
      "object": {
          "type": "string"
      },
      "created": {
          "type": "integer"
      },
      "expires_at": {
          "type": "integer"
      },
      "url": {
          "type": "string"
      },
  } ,
  "required": [
          "object",
          "created",
          "expires_at",
          "url",
      ]
}

# /user/{user_id}
# /user
user = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/User",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
    },
    "username": {
      "type": "string",
    },
    "email": {
      "type": "integer",
    },
    "user_type": {
      "type": "string",
    },
    "description": {
      "type": "string",
    },
    "phone": {
      "type": "string",
    },
    "lat": {
      "type": "number",
    },
    "lng": {
      "type": "number",
    },
    "img_url": {
      "type": "string",
    },
    "created_at": {
      "type": "string",
    },
  },
  "required": [
        "id",
        "user_type",
        "created_at",
  ]
}

# /
# /check
empty_response = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/EmptyResponse",
  "type": "object",
  "properties": {
  }
}

# 
listing_tag = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/ListingTag",  
  "type": "object",
  "properties": {
      "id": {
          "type": "string"
      },
      "listing_id": {
          "type": "string"
      },
      "tag": {
          "type": "string"
      },
      "tag_id": {
          "type": "string"
      },
      "created_at": {
          "type": "string"
      },
  },
  "required": [
      "id",
      "listing_id",
      "tag",
      "tag_id",
      "created_at",
  ]
}

#
appointment_provider = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/AppointmentProvider",    
  "type": "object",
  "properties": {
      "id": {
          "type": "string"
      },
      "username": {
          "type": "string"
      },
      "distance": {
          "type": "integer"
      },
      "img_url": {
          "type": "string"
      },
  },
  "required": [
      "id",
      "username",
  ]
}

#
listing = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/Listing",  
  "type": "object",
  "properties": {
      "id": {
          "type": "string"
      },
      "user_id": {
          "type": "string"
      },
      "title": {
          "type": "string"
      },
      "description": {
          "type": "string"
      },
      "appointment_per_timeslot": {
          "type": "string"
      },
      "timeslot_minutes": {
          "type": "string"
      },
      "tags": {
          "type": "array",
          "items": [
              listing_tag
          ]
      },
      "provider": {
          "type": "array",
          "items": [
              appointment_provider
          ]
      },
      "rating": {
          "type": "number"
      },
      "review_count": {
          "type": "integer"
      },
      "distance": {
          "type": "integer"
      },
      "created_at": {
          "type": "string"
      },
  },
  "required": [
      "id",
      "user_id",
      "title",
      "description",
      "appointment_per_timeslot",
      "timeslot_minutes",
      "created_at",
  ]
}

# 
appointment_item = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/AppointmentItem",  
  "type": "object",
  "properties": {
      "id": {
          "type": "string"
      },
      "appointment_id": {
          "type": "string"
      },
      "listing_item_id": {
          "type": "string"
      },
  }
}

# /appointment/{id}
appointment = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/Appointment",
  "type": "object",
  "properties": {
      "id": {
          "type": "string"
      },
      "provider_id": {
          "type": "string"
      },
      "provider_username": {
          "type": "string"
      },
      "client_id": {
          "type": "string"
      },
      "status": {
          "type": "string"
      },
      "price": {
          "type": "integer"
      },
      "time": {
          "type": "string"
      },
      "description": {
          "type": "string"
      },
      "lat": {
          "type": "number"
      },
      "lng": {
          "type": "number"
      },
      "listing": listing,
      "items": {
          "type": "array",
          "items": [
              appointment_item
          ]
      },
  }
}

# 
validation_error = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/ValidationError",
  "type": "object",
  "properties": {
      "loc": {
          "type": "array",
          "items": [
              {
                  "type": "string" | "integer",
              }
          ]
      },
      "msg": {
          "type": "string"
      },
      "type": {
          "type": "string"
      },
  } ,
  "required": [
          'loc',
          'msg',
          'type'
      ]
}

# HTTP Validation Error - 422
http_validation_error = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/HTTPValidationError",
  "type": "object",
  "properties": {
      "detail": {
          "type": "array",
          "items": [
              validation_error
          ]
      },
  } 
}