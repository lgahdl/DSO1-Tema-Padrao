from datetime import date

users = [{"id_user": 1,
          "user_name": "Luiz",
          "user_birthday": date(1996,3,19),
          "user_role": 2,
          "user_phone": 49984172756,
          "cars": []
          },
         {"id_user":2,
          "user_name": "Pedro",
          "user_birthday": date(2000,5,26),
          "user_role": 3,
          "user_phone": 47988583680,
          "cars":[]
         },
         {"id_user": 3,
          "user_name": "Jeremias",
          "user_birthday": date(1990, 2, 11),
          "user_role": 1,
          "user_phone": 49999992222,
          "cars": []
          },
         {"id_user": 3,
          "user_name": "Haroldo",
          "user_birthday": date(1999, 4, 25),
          "user_role": 0,
          "user_phone": 49987873535,
          "cars": []
          },
         ]
cars = [{"id_car":1,
         "car_plate":"XYZ9955",
         "car_model":"GOL",
         "car_brand":"VOLKSWAGEN",
         "car_year":2000,
         "car_kilometer":128984,
         "car_tier":1
        },
        {"id_car": 2,
         "car_plate": "QWE5544",
         "car_model": "ENZO",
         "car_brand": "FERRARI",
         "car_year": 2008,
         "car_kilometer": 2298,
         "car_tier": 3
         },
        {"id_car": 3,
         "car_plate": "IUY1996",
         "car_model": "KOMBI",
         "car_brand": "VOLKSWAGEN",
         "car_year": 1998,
         "car_kilometer": 304598,
         "car_tier": 2
         }]
keys = [{"id_key":1,
         "car": cars[0]},
        {"id_key": 2,
         "car": cars[1]},
        {"id_key": 3,
         "car": cars[2]}]

requests = [{"id_request": 1,
             "user": users[0],
             "key": keys[0],
             "created_date":date(2019, 9, 19),
             "devolution_date":date(2019,9,21),
             "accepted": True,
             "reason": ""}]
