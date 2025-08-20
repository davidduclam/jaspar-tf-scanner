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

Alternatively, you can run the application locally by following the steps in either the [Installation](#installation) or [Installation Using a Virtual Environment (Recommended)](#installation-using-a-virtual-environment-recommended) section, and then the [Run](#run) section, in order.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/davidduclam/jaspar-tf-scanner.git
   cd jaspar-tf-scanner
   ```

2. (**Recommended**) Create and activate a Python virtual environment to keep dependencies isolated:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   To deactivate the virtual environment when finished:
   ```bash
   deactivate
   ```

3. Install the required dependencies:
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
   - `pages/`: Contains all the pages of the application.
      - `binding_site_score.py`: Module for showing general information about the transcription factor, as well as finding binding sites based on a user-given DNA sequence.
      - `results_viewer.py`: Module for displaying results in the Streamlit app.
- `tests/`: Contains unit tests for the modules.
    - `test_binding_site_finder.py`: Test for scanning sequence for binding sites
    - `test_jaspar_api.py`: Tests for the JASPAR API
    - `test_pfm_pwm_converter.py`: Test for conversion of PFM to PWM
- `requirements.txt`: Lists the dependencies.
- `pytest.ini`: Configuration file for pytest test runner.

## Dependencies

- Streamlit
- Requests
- Pandas
- NumPy
- Pytest
