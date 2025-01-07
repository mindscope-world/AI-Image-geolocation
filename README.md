# GeoSpy AI Predictor

GeoSpy AI Predictor is a Streamlit application that allows users to upload images and interact with the GeoSpy AI API to get predictions. The app encodes the uploaded image in base64, sends it to the API, and displays the predictions.

## Features

- Upload an image in `.jpg`, `.jpeg`, or `.png` format.
- Provide your API key securely.
- Specify the number of top predictions to retrieve.
- View predictions in a user-friendly interface.

## Requirements

- Python 3.7 or later
- Streamlit
- Requests

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/GeoSpy-Predictor.git
   cd GeoSpy-Predictor
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Open the application in your browser (usually at `http://localhost:8501`).
2. Enter your API key in the provided field.
3. Upload an image by dragging and dropping it or selecting it from your file system.
4. Specify the number of top predictions you want (default is 5).
5. Click the **Predict** button to see the results.

## Example

1. Upload an image:
   ![Upload Example](./assets/upload_example.png)

2. View predictions:
   ![Prediction Example](./assets/prediction_example.png)

## API Details

The application interacts with the GeoSpy AI API:
- **Endpoint**: `https://dev.geospy.ai/predict`
- **Method**: POST
- **Parameters**:
  - `image`: Base64-encoded image string
  - `top_k`: Number of top predictions to retrieve
- **Headers**:
  - `Authorization`: `Bearer YOUR_API_KEY`

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/) for providing an easy-to-use Python web app framework.
- GeoSpy AI for their prediction API.
