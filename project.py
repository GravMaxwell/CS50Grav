# Welcome to CaddiePy! !!!!!
# Select a club based on distance to the hole, surface/lie type, and swing type

# Function 1 - Get Yardage
import math

def get_user_input():
    yardage = math.ceil(float(input("Distance to Hole (yds): ")))
    surface = input("Lie Surface (Sand, Rough, Fairway, or Tee): ")
    swing = input("Swing Type (Full, 3/4, Half, or Quarter): ")
    return yardage, surface, swing

# Function 2 - Adjust yardage based on surface
def adjust_lie(yardage, surface):
    if surface.lower() == "sand":
        return yardage - 5
    elif surface.lower() == "rough":
        return yardage - 10
    elif surface.lower() == "fairway":
        return yardage
    elif surface.lower() == "tee":
        return yardage + 5
    else:
        return yardage

# Function 3 - Adjust yardage based on swing type
def adjust_swing(yardage, swing):
    if swing.lower() == "full":
        return yardage * 1.0
    elif swing.lower() == "3/4":
        return yardage * 0.75
    elif swing.lower() == "half":
        return yardage * 0.5
    elif swing.lower() == "quarter":
        return yardage * 0.25
    else:
        return yardage

# Function 4 - Select club based on yardage
def select_club(yardage, surface, swing):
    clubs = {
        "Driver": 300.0,
        "3-Wood": 275.0,
        "3-Hybrid": 250.0,
        "4-Iron": 215.0,
        "5-Iron": 210.0,
        "6-Iron": 190.0,
        "7-Iron": 175.0,
        "8-Iron": 165.0,
        "9-Iron": 155.0,
        "Pitching Wedge": 135.0,
        "Gap Wedge": 120.0,
        "Sand Wedge": 110.0,
        "Lob Wedge": 100.0,
    }
    # Store the average yardage before adjustments
    average_yardages = clubs.copy()
    # Adjust each club's yardage based on surface and swing type
    adjusted_clubs = {club: adjust_swing(adjust_lie(distance, surface), swing) for club, distance in clubs.items()}
    # Select the club that gets closest to the yardage without going past it
    suitable_clubs = {club: distance for club, distance in adjusted_clubs.items() if distance <= yardage}
    if not suitable_clubs:
        return "No suitable club... Mulligan, perhaps?", 0, average_yardages
    closest_club = max(suitable_clubs, key=suitable_clubs.get)
    return closest_club, adjusted_clubs[closest_club], average_yardages[closest_club], adjusted_clubs

# Main Function
def main():
    yardage, surface, swing = get_user_input()
    selected_club, adjusted_yardage, average_yardage, adjusted_clubs = select_club(yardage, surface, swing)
    if selected_club == "No suitable club... Mulligan, perhaps?":
        print("No suitable club found for the given yardage.")
    else:
        print(f"On average, your {selected_club} goes {average_yardage} yds.")
        print(f"Adjusted for lie and swing, it should go {adjusted_yardage} yds.")
        if abs(adjusted_yardage - yardage) <= 5:
            print(f"I'd recommend hitting your {selected_club}.... Send it!")
        else:
            print(f"I'd recommend laying up with your {selected_club}.")

if __name__ == "__main__":
    main()

