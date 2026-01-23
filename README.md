
# Client Side AI Authoring (CBAA) Demo

This repository demonstrates how to use BrowserStack's Cross Browser AI Authoring (CBAA) with Python and Selenium. It executes Gherkin-based feature scenarios on BrowserStack's infrastructure, leveraging AI to interpret and execute natural language steps.

## Prerequisites

*   **Python 3.x**: Ensure Python 3 is installed on your system.
*   **BrowserStack Account**: You need a BrowserStack username and access key. [Sign up for a free trial](https://www.browserstack.com/users/sign_up) if you don't have one, and connect with your Account Manager to enable Cross Browser AI Authoring.

## Setup

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd cbaa-demo
    ```

2.  **Create and activate a virtual environment (optional but recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3.  **Install dependencies:**

    This project requires `selenium`, `gherkin-official`, and `python-dotenv`.

    ```bash
    pip install -r requirements.txt
    pip install python-dotenv
    ```

4.  **Configure Environment Variables:**

    Create a `.env` file in the root directory of the project and add your BrowserStack credentials:

    ```bash
    BROWSERSTACK_USERNAME=your_username
    BROWSERSTACK_ACCESS_KEY=your_access_key
    ```

## Project Structure

*   **`cbaa.py`**: The main entry point script. It initializes the Selenium driver with BrowserStack options, parses feature files, and executes scenarios using a thread pool.
*   **`features/`**: Contains Gherkin `.feature` files defining the test scenarios.
    *   `purchase.feature`: A sample e-commerce purchase scenario.
*   **`utils/`**: Helper utilities.
    *   `parse_feature.py`: Parses Gherkin feature files and "hydrates" them with examples (replaces placeholders with actual data).
*   **`browserstack.yml`**: Configuration file for BrowserStack SDK (reference).
*   **`requirements.txt`**: List of Python dependencies.

## Running the Tests

To run the AI-authored tests, execute the `cbaa.py` script:

```bash
python cbaa.py
```

### What happens during execution:

1.  The script reads `features/purchase.feature`.
2.  It parses the scenarios and replaces placeholders (e.g., `<Category>`, `<Email>`) with the values from the `Examples` table.
3.  For each scenario iteration, it spawns a thread.
4.  Each thread starts a Selenium session on BrowserStack.
5.  Steps are executed using `browserstack_executor` with the `ai` action, allowing the AI to interpret natural language commands like "Click on the 'Men' category".
6.  Results are reported back to BrowserStack.

## Notes

*   Ensure your BrowserStack plan supports the number of parallel threads you intend to run.
*   The `aiAuthoring: "true"` capability is critical for enabling the AI features.