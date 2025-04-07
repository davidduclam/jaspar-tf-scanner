# JASPAR Transcription Factor Binding Site Scanner

This project is a Streamlit web application that allows users to search for transcription factors from the JASPAR database and scan DNA sequences for potential binding sites.

## Features

- **Search Transcription Factors**: Enter the name of a transcription factor to search the JASPAR database.
- **Select Transcription Factor**: Choose from a list of matching transcription factors.
- **Fetch Motif Data**: Retrieve motif data for the selected transcription factor.
- **Enter DNA Sequence**: Input a DNA sequence to scan for binding sites.
- **Find Binding Sites**: Identify potential binding sites within the DNA sequence.

## Demonstration

Watch the demonstration of the app on YouTube:

[https://youtu.be/k1zaJC9YX-g](https://youtu.be/k1zaJC9YX-g)

## Usage

The deployed application can be accessed through the following link:

[https://jaspar-tf-scanner.streamlit.app/](https://jaspar-tf-scanner.streamlit.app/)

## Running Locally

Alternatively, it can also be run locally on your own PC by following both the [Installation](#installation) and [Run](#run-locally) sections, in order.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/davidduclam/jaspar-tf-scanner.git
   cd jaspar-tf-scanner
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Run

1. Navigate to the project folder:

   ```bash
   cd jaspar-tf-scanner
   ```

2. Navigate to the `src` folder:

   ```bash
   cd src
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

4. Open your web browser and go to `http://localhost:8501`.

5. Enter the name of a transcription factor (e.g., "CTCF") and click "Search Transcription Factors".

6. Select a transcription factor binding profile from the dropdown list.

7. Click "Find Transcription Factor", which redirects you to a new page containing information about the transcription factor binding profile

8. Enter a DNA sequence in the text box on the right hand side of the screen and click "Find Binding Sites" to see the results shown in an interactive scatter plot.

## Project Structure

- `src/`: Contains all the source code for the project.
  - `app.py`: The main Streamlit application file.
  - `constants.py`: Contains constants used throughout the project.
  - `modules/`: Contains all the modules related to the project.
    - `jaspar_api.py`: Module for interacting with the JASPAR database.
    - `pfm_pwm_converter.py`: Module for converting Position Frequency Matrices (PFM) to Position Weight Matrices (PWM).
    - `binding_site_finder.py`: Module for scanning DNA sequences for binding sites.
    - `results_viewer.py`: Module for displaying results in the Streamlit app.
  - `pages/`: Contains all the pages of the application.
    - `binding_site_score.py`: Module for showing general information about the transcription factor, as well as finding binding sites based on a user-given DNA sequence.
- `tests/`: Contains unit tests for the modules.
- `requirements.txt`: Lists the dependencies.
- `README.md`: Contains the project documentation.

## Dependencies

- Streamlit
- Requests
- Pandas
- NumPy
