import dotenv
import os
import anthropic


dotenv.load_dotenv()
client = anthropic.Anthropic(api_key = os.getenv("ANTHROPIC_API_KEY"))
    

def summarise_papers(abstract):
    client = anthropic.Anthropic(
        api_key = os.getenv("ANTHROPIC_API_KEY")
    )
    
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens = 1024,
        messages=[
            {
                "role": "user",
                "content": f"Summarise this research paper abstract in 2-3 plain sentences for a technical ML engineer. No headers, no bullet points, no markdown: {abstract}"
            }
        ]
    )
 
    return message.content[0].text
    
if __name__ == "__main__":
    abstract = "In this paper, we propose a novel approach to natural language processing using deep learning techniques. We demonstrate the effectiveness of our method on several benchmark datasets, achieving state-of-the-art results. Our approach leverages transformer architectures and attention mechanisms to capture long-range dependencies in text data. We also provide an analysis of the model's performance and discuss potential applications in various domains."
    summary = summarise_papers(abstract)
    print(summary)