# Keymate API for GPT Integration

## Overview

This project leverages the Keymate SDK to build a REST API in Python, facilitating the use of GPT models with enhanced search capabilities and access to a knowledge base. The API is designed to be deployed on RENDER and can be called from custom GPT implementations to extend their functionality and knowledge.

## Features

- REST API built with FastAPI.
- Integration with Keymate SDK for advanced search and analysis.
- API Key Authentication for secure access.
- Deployable on RENDER for easy access and scalability.
- Designed to enhance GPT models with web search and knowledge base capabilities.

## Prerequisites

- Python 3.8 or higher
- FastAPI
- Uvicorn (for running the API locally)
- HTTPx (for making HTTP requests, may be used with Keymate SDK)
- A RENDER account for deployment

## Local Setup

1. **Clone the Repository**: 
   Clone this repository to your local machine.

2. **Install Dependencies**: 
   Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**: 
   Create a `.env` file in the project root and add your API keys and other necessary environment variables.

4. **Run the Application Locally**:
   Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Testing

Run the test suite to ensure everything is working as expected:
```bash
pytest /tests
```

## Deployment on RENDER

1. **Create a Docker Container**:
   Use the provided `Dockerfile` to build a Docker container for the API.

2. **Deploy on RENDER**: 
   Follow RENDER's documentation to deploy your Docker container.

## Usage

- The API provides a `/search` endpoint for conducting web searches and analysis.
- Secure access via API Key Authentication.

## Extending GPT Functionality

- This API can be called from custom GPT models to integrate web search and knowledge base features.
- Enhances GPT's ability to provide up-to-date and comprehensive responses.

## Support

For support and queries, [create an issue](https://github.com/your-github-repo/issues) in the GitHub repository.

---

This README provides a comprehensive guide for anyone looking to understand, set up, and use your API. You can modify and extend it as needed to fit the evolving details of your project.