import streamlit as st
import requests
import base64

def main():
    st.title("GeoSpy AI Predictor")

    # Input: API Key
    api_key = st.text_input("Enter your API Key", type="password")

    # Input: Image upload
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Encode image to base64
        encoded_string = base64.b64encode(uploaded_file.read()).decode('utf-8')
        
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Input: Top K results
        top_k = st.number_input("Enter the number of top predictions (top_k):", min_value=1, max_value=20, value=5)

        # Predict button
        if st.button("Predict"):
            if not api_key:
                st.error("Please provide your API key.")
                return

            # API call
            url = f"https://dev.geospy.ai/predict?image={encoded_string}&top_k={top_k}"
            headers = {"Authorization": f"Bearer {api_key}"}
            
            try:
                response = requests.post(url, headers=headers)

                # Handle the response
                if response.status_code == 200:
                    st.success("Prediction successful!")
                    st.json(response.json())
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
