inboundsms_data = {"type": "object",
                   "properties": {
                       "username": {"type":"string", "required":True},
                       "auth_id": {"type":"integer", "required":True},
                       "from": {"type":"integer", "required":True, "minLength":6, "maxLength":16},
                       "to": {"type":"integer", "required":True, "minLength":6, "maxLength":16},
                       "text": {"type":"string", "required":True, "minLength":1, "maxLength":120}
                   }
                   }

outboundsms_data = {"type": "object",
                   "properties": {
                       "username": {"type":"string", "required":True},
                       "auth_id": {"type":"integer", "required":True},
                       "from": {"type":"integer", "required":True, "minLength":6, "maxLength":16},
                       "to": {"type":"integer", "required":True, "minLength":6, "maxLength":16},
                       "text": {"type":"string", "required":True, "minLength":1, "maxLength":120},
                   }
                   }