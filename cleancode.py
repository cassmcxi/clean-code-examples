

# my code after cleaning it up --------------------
# 'not' in place of '==' to minimize redundancy 

distance_mi = 12
is_raining = True
has_bike = False
has_car = True
has_ride_share_app = True

if not distance_mi:
    print(False)
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)
elif 1 < distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)
elif distance_mi > 6:
    if has_ride_share_app:
        print(True)
    elif has_car:
        print(True)
    else:
        print(False)


# previous code -----------------------------------
# too many '==' making it more difficult to read

distance_mi = 12
is_raining = True
has_bike = False
has_car = True
has_ride_share_app = True

if not distance_mi:
    print(False)
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)
elif distance_mi > 1 and distance_mi <= 6:
    if is_raining == True and has_bike == False:
        print(False) 
    elif is_raining == False and has_bike == False:
        print(False)
    else:
        print(True)
elif distance_mi > 6:
    if has_ride_share_app == True:
        print(True)
    elif has_car == True:
        print(True)
    else:
        print(False)