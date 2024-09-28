# project.py aka "CADDIEPY"

## Video Demo: [Watch here](https://youtu.be/VDNcKes3yHc)

## Description

Welcome to **CaddiePy**! CaddiePy is my final project for HarvardX's CS50P Intro to Python Programming with instructor David J Malan. I designed CaddiePy to help golfers (and new coders!) choose the appropriate club based on the distance to the hole, the surface/lie type, and the golfer's desired swing type. This program takes golfer's input for these parameters and recommends the best club to use, considering the golfer's average carry distances for each club and adjustments based on the surface type and swing type. This project was extremely fun to put together, despite several challenges and hiccups along the way. I cannot thank David Malan and his team enough for their time and efforts in putting this course on.

THIS WAS CS50!

Now, let's dive into the ins and outs of CaddiePy!

## Project Structure

- `project.py`: The main script containing the logic for club selection.
- `test_project.py`: The test script containing unit tests for the functions in `project.py`.

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.

### Running the Project

To run the project, execute the following command in your terminal:

```bash
python project.py
```

### CaddiePy Features

- **User Input Prompts**: The program prompts the user to enter the distance to the hole in yards, the surface type (Tee, Fairway, Rough, or Sand), and the swing type (full, 3/4, half, or quarter).

- **Yardage Adjustment**: The program adjusts the yardage based on the surface type:
  - Tee: Adds 5 yds
  - Fairway: No adjustment
  - Sand: Deducts 5 yards
  - Rough: Deducts 10 yards

- **Swing Adjustment**: The program adjusts the yardage based on the swing type:
  - Full Swing: No Adjustment
  - 3/4 Swing: 75% of Avg Carry Distance
  - Half Swing: 50% of Avg Carry Distance
  - Quarter Swing: 25% of Avg Carry Distance

- **Club Selection**: The program selects the club whose average carry distance is closest to the adjusted yardage.

### Newest Improvements

- Club Selection optimization taking adjusted carry distance after swing selection.

### Future Improvements

- Further refinement of club selection when in specific lie cases (i.e., not hitting driver out of rough).
- Suggested alternate club with different swing type if distance to the hole is within 5 yds with swing/club/lie combination.
- Added cases where final output will return "hitting" or "laying up" if the adjusted club carry distance is over or short of the hole, respectively.

### How It Works

1. **Get User Input**: The program prompts the user to enter the distance to the hole, the type of surface/lie, and the swing type.
2. **Adjust Yardage Based on Surface**: The program adjusts the yardage based on the type of surface.
3. **Adjust Yardage Based on Swing Type**: The program further adjusts the yardage based on the swing type.
4. **Select Club**: The program selects the most suitable club based on the adjusted yardage.

### Example

```plaintext
Distance to Hole (yds): 150
Lie Surface (Sand, Rough, Fairway, or Tee): Fairway
Swing Type (Full, 3/4, Half, or Quarter): Full

Distance to Hole: 150 yds
Lie Surface: Fairway
Swing Type: Full
On average, your Pitching Wedge goes 135 yds.
Adjusted for lie and swing, it should go 135 yds.
I'd recommend hitting your Pitching Wedge.
```

## Testing

We use `pytest` for testing the functions in `project.py`. The test cases are defined in `test_project.py`.

## Test File Overview

The test_project.py code is testing the functionality of various functions in my project.py file. Here’s a breakdown of what each test is doing:

test_adjust_lie():
This function tests the adjust_lie function to ensure it correctly adjusts the yardage based on the surface type.
It checks:
Sand reduces the yardage by 5.
Rough reduces the yardage by 10.
Fairway keeps the yardage the same.
Tee increases the yardage by 5.
An unknown surface keeps the yardage the same.
test_adjust_swing():
This function tests the adjust_swing function to ensure it correctly adjusts the yardage based on the swing type.
It checks:
Full swing keeps the yardage the same.
3/4 swing reduces the yardage to 75% of the original.
Half swing reduces the yardage to 50% of the original.
Quarter swing reduces the yardage to 25% of the original.
An unknown swing type keeps the yardage the same.
test_select_club():
This function tests the select_club function to ensure it correctly selects the appropriate club based on the adjusted yardage.
It checks:
For a yardage of 150 on Fairway with a Full swing, the selected club should be a Pitching Wedge, with both adjusted and average yardages being 135.0.
For a yardage of 90 in Sand with a Half swing, the selected club should be a 7-Iron, with an adjusted yardage of 85.0 and an average yardage of 175.0.
test_get_user_input():
This function tests the get_user_input function using the unittest.mock.patch to simulate user input.
It checks:
The function correctly converts the input distance to an integer (rounding up).
The surface and swing type inputs are correctly captured.
These tests ensure that your functions behave as expected under various conditions.

### Running Tests

To run the tests, execute the following command in your terminal:

```bash
pytest test_project.py
```

### Test Cases

1. **test_adjust_lie**: Tests the `adjust_lie` function with different surface types.
2. **test_adjust_swing**: Tests the `adjust_swing` function with different swing types.
3. **test_select_club**: Tests the `select_club` function with different yardages, surfaces, and swing types.
4. **test_get_user_input**: Tests the `get_user_input` function using mock inputs.

### Example Output

```plaintext
============================= test session starts ==============================
collected 4 items

test_project.py ....                                                      [100%]

============================== 4 passed in 0.03s ===============================
```

## Acknowledgments

- Thanks to the Harvard CS50 Team and python community for their valuable resources and support.

Happy golfing with CaddiePy!
