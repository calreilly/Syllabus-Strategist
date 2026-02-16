import os
from pydantic_ai import Agent
from dotenv import load_dotenv

load_dotenv()

def main():
    print("Project Environment Setup Complete!")
    try:
        import pydantic_ai
        import lancedb
        import pypdf
        import streamlit
        print("All key dependencies installed successfully.")
    except ImportError as e:
        print(f"Error importing dependencies: {e}")

if __name__ == "__main__":
    main()
