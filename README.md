# Attendance Visualization Tool

## Overview
This tool fetches attendance data from an attendance system API and visualizes it in a bar graph format. It allows users to log in, fetch attendance data for different subjects, and visualize the attendance percentage.

## Features
1. **Login** : Users can log in using their email and password.
2. **Subject Selection** : Users can select a specific subject or track (Web Designing or Machine Learning).
3. **Data Visualization** : Attendance data is visualized using horizontal bar graphs. Colors indicate different attendance ranges (e.g., red for less than 70%, orange for 70-74%, etc.).
4. **Aggregate Attendance** : Total attendance and aggregate percentage are displayed at the top of the graph.
5. **Logout** : Users can log out after fetching attendance data.

## Usage
1. **Login**: Enter your email and password when prompted.
2. **Subject Selection**: Choose your preferred track (Web Designing or Machine Learning) by entering the corresponding number.
3. **Data Fetching**: Attendance data will be fetched from the API.
4. **Visualization**: Attendance data will be visualized in a bar graph.
5. **Attendance Recommendations**: Based on the visualization, users can determine which classes require attendance to maintain a minimum of 75% attendance in each subject. This helps users identify classes they must attend to meet attendance requirements.
6. **Logout**: After visualization, the tool automatically logs out.



## Dependencies
1. **requests**: For making HTTP requests to the API.
2. **pandas**: For data manipulation and organization.
3. **matplotlib**: For data visualization.

## Setup
1. **Install dependencies**: pip install requests pandas matplotlib.
2. **Run the script**.
3. Follow the on-screen instructions to log in, fetch data, and visualize attendance.

## Contributors
[Biswojit Mohapatra](https://www.linkedin.com/in/biswojit-mohapatra-282b64258/) - Project Lead
