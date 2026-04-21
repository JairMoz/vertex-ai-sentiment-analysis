import vertexai
from vertexai.language_models import TextGenerationModel

def generate_text(project_id: str, location: str):
    """Example of using Vertex AI to generate text."""
    vertexai.init(project=project_id, location=location)
    
    parameters = {
        "candidate_count": 1,
        "max_output_tokens": 1024,
        "temperature": 0.2,
        "top_p": 0.8,
        "top_k": 40
    }
    
    model = TextGenerationModel.from_pretrained("text-bison@002")
    
    # This prompt is based on the Generative AI Studio lab tasks
    prompt = "Summarize the following text in 3 bullet points: [INSERT TEXT HERE]"
    
    response = model.predict(prompt, **parameters)
    print(f"Response from Model: {response.text}")

if __name__ == "__main__":
    # Replace with your actual project ID
    # generate_text(project_id="your-project-id", location="us-central1")
    pass
