#!/usr/bin/env python3
"""
Simple FastAPI application for testing Render deployment.
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import os
import platform
import sys

# Initialize FastAPI app
app = FastAPI(
    title="Render FastAPI Test",
    description="A simple FastAPI application for testing Render deployment",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class HealthResponse(BaseModel):
    status: str
    timestamp: str
    environment: str
    python_version: str
    platform: str

class MessageRequest(BaseModel):
    message: str

class MessageResponse(BaseModel):
    message: str
    timestamp: str
    echo_count: int

@app.get("/", response_class=HTMLResponse)
async def home_page():
    """Home page with deployment information"""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Render FastAPI Test</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: #ffffff;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
            }
            
            .header {
                background: rgba(0, 0, 0, 0.2);
                backdrop-filter: blur(10px);
                padding: 2rem 0;
                text-align: center;
                border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            }
            
            .header h1 {
                font-size: 3rem;
                font-weight: 700;
                margin-bottom: 1rem;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            }
            
            .header p {
                font-size: 1.2rem;
                opacity: 0.9;
            }
            
            .main-content {
                flex: 1;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                padding: 4rem 2rem;
            }
            
            .content-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 2rem;
                max-width: 1200px;
                width: 100%;
            }
            
            .card {
                background: rgba(255, 255, 255, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 15px;
                padding: 2rem;
                text-align: center;
                backdrop-filter: blur(10px);
                transition: all 0.3s ease;
            }
            
            .card:hover {
                transform: translateY(-5px);
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            }
            
            .card h2 {
                font-size: 1.8rem;
                margin-bottom: 1rem;
                color: #ffffff;
            }
            
            .card p {
                margin-bottom: 1.5rem;
                opacity: 0.9;
                line-height: 1.6;
            }
            
            .btn {
                background: linear-gradient(45deg, #667eea, #764ba2);
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 25px;
                font-size: 1rem;
                font-weight: 600;
                cursor: pointer;
                transition: all 0.3s ease;
                text-decoration: none;
                display: inline-block;
            }
            
            .btn:hover {
                transform: scale(1.05);
                box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
            }
            
            .status-indicator {
                display: inline-block;
                width: 12px;
                height: 12px;
                border-radius: 50%;
                margin-right: 8px;
            }
            
            .status-online {
                background: #4caf50;
                box-shadow: 0 0 10px rgba(76, 175, 80, 0.5);
            }
            
            .footer {
                text-align: center;
                padding: 2rem;
                background: rgba(0, 0, 0, 0.2);
                border-top: 1px solid rgba(255, 255, 255, 0.1);
            }
            
            .footer p {
                opacity: 0.8;
            }
            
            @media (max-width: 768px) {
                .header h1 {
                    font-size: 2rem;
                }
                
                .content-grid {
                    grid-template-columns: 1fr;
                }
                
                .card {
                    padding: 1.5rem;
                }
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🚀 Render FastAPI Test</h1>
            <p>Simple FastAPI application for testing Render deployment</p>
        </div>
        
        <div class="main-content">
            <div class="content-grid">
                <div class="card">
                    <h2>Health Check</h2>
                    <p>Check the application health and deployment status</p>
                    <a href="/health" class="btn">Check Health</a>
                </div>
                
                <div class="card">
                    <h2>API Documentation</h2>
                    <p>Interactive API documentation with Swagger UI</p>
                    <a href="/docs" class="btn">View Docs</a>
                </div>
                
                <div class="card">
                    <h2>Message Echo</h2>
                    <p>Test the API with a simple message echo endpoint</p>
                    <a href="/echo" class="btn">Try Echo</a>
                </div>
                
                <div class="card">
                    <h2>Environment Info</h2>
                    <p>View deployment environment information</p>
                    <a href="/info" class="btn">View Info</a>
                </div>
            </div>
        </div>
        
        <div class="footer">
            <p>&copy; 2025 Render FastAPI Test | Deployed on Render</p>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        timestamp=datetime.now().isoformat(),
        environment=os.getenv("RENDER_ENVIRONMENT", "development"),
        python_version=sys.version,
        platform=platform.platform()
    )

@app.get("/info")
async def get_info():
    """Get deployment information"""
    return {
        "app_name": "Render FastAPI Test",
        "version": "1.0.0",
        "deployment_time": datetime.now().isoformat(),
        "environment": {
            "render_environment": os.getenv("RENDER_ENVIRONMENT", "development"),
            "render_service_id": os.getenv("RENDER_SERVICE_ID", "not_set"),
            "render_service_name": os.getenv("RENDER_SERVICE_NAME", "not_set"),
            "render_service_type": os.getenv("RENDER_SERVICE_TYPE", "not_set"),
            "render_commit_id": os.getenv("RENDER_COMMIT_ID", "not_set"),
            "render_branch": os.getenv("RENDER_BRANCH", "not_set"),
        },
        "system": {
            "python_version": sys.version,
            "platform": platform.platform(),
            "architecture": platform.architecture()[0],
            "processor": platform.processor(),
        },
        "endpoints": [
            {"path": "/", "method": "GET", "description": "Home page"},
            {"path": "/health", "method": "GET", "description": "Health check"},
            {"path": "/info", "method": "GET", "description": "Deployment info"},
            {"path": "/echo", "method": "GET", "description": "Message echo form"},
            {"path": "/api/echo", "method": "POST", "description": "Echo API endpoint"},
            {"path": "/docs", "method": "GET", "description": "API documentation"},
        ]
    }

@app.get("/echo", response_class=HTMLResponse)
async def echo_form():
    """Simple form to test echo functionality"""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Echo Test - Render FastAPI</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: #ffffff;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                padding: 2rem;
            }
            
            .container {
                background: rgba(255, 255, 255, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 15px;
                padding: 2rem;
                backdrop-filter: blur(10px);
                max-width: 500px;
                width: 100%;
            }
            
            h1 {
                text-align: center;
                margin-bottom: 2rem;
            }
            
            .form-group {
                margin-bottom: 1.5rem;
            }
            
            label {
                display: block;
                margin-bottom: 0.5rem;
                font-weight: 600;
            }
            
            input[type="text"] {
                width: 100%;
                padding: 12px;
                border: 2px solid rgba(255, 255, 255, 0.2);
                border-radius: 8px;
                background: rgba(255, 255, 255, 0.1);
                color: #ffffff;
                font-size: 1rem;
            }
            
            input[type="text"]:focus {
                outline: none;
                border-color: #667eea;
            }
            
            button {
                background: linear-gradient(45deg, #667eea, #764ba2);
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 8px;
                font-size: 1rem;
                font-weight: 600;
                cursor: pointer;
                width: 100%;
                transition: all 0.3s ease;
            }
            
            button:hover {
                transform: scale(1.02);
            }
            
            .result {
                margin-top: 2rem;
                padding: 1rem;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 8px;
                display: none;
            }
            
            .back-link {
                text-align: center;
                margin-top: 2rem;
            }
            
            .back-link a {
                color: #ffffff;
                text-decoration: none;
                opacity: 0.8;
            }
            
            .back-link a:hover {
                opacity: 1;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔊 Echo Test</h1>
            <form id="echoForm">
                <div class="form-group">
                    <label for="message">Enter your message:</label>
                    <input type="text" id="message" name="message" placeholder="Hello, Render!" required>
                </div>
                <button type="submit">Send Message</button>
            </form>
            
            <div id="result" class="result">
                <h3>Response:</h3>
                <p id="responseText"></p>
            </div>
        </div>
        
        <div class="back-link">
            <a href="/">← Back to Home</a>
        </div>

        <script>
            document.getElementById('echoForm').addEventListener('submit', async function(e) {
                e.preventDefault();
                
                const message = document.getElementById('message').value;
                const resultDiv = document.getElementById('result');
                const responseText = document.getElementById('responseText');
                
                try {
                    const response = await fetch('/api/echo', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ message: message })
                    });
                    
                    const data = await response.json();
                    
                    responseText.innerHTML = `
                        <strong>Message:</strong> ${data.message}<br>
                        <strong>Timestamp:</strong> ${data.timestamp}<br>
                        <strong>Echo Count:</strong> ${data.echo_count}
                    `;
                    
                    resultDiv.style.display = 'block';
                } catch (error) {
                    responseText.innerHTML = `Error: ${error.message}`;
                    resultDiv.style.display = 'block';
                }
            });
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.post("/api/echo", response_model=MessageResponse)
async def echo_message(request: MessageRequest):
    """Echo the received message with timestamp and count"""
    return MessageResponse(
        message=request.message,
        timestamp=datetime.now().isoformat(),
        echo_count=len(request.message.split())
    )

@app.get("/api/echo/{message}")
async def echo_path(message: str):
    """Echo message from path parameter"""
    return {
        "message": message,
        "timestamp": datetime.now().isoformat(),
        "echo_count": len(message.split()),
        "method": "GET"
    }

@app.get("/test")
async def test_endpoint():
    """Simple test endpoint"""
    return {
        "message": "Hello from Render!",
        "status": "success",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/error-test")
async def error_test():
    """Test error handling"""
    raise HTTPException(status_code=500, detail="This is a test error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
