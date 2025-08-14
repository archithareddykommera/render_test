# 🚀 Render FastAPI Test

A simple FastAPI application for testing deployment on Render.

## 📋 Features

- ✅ **Beautiful UI**: Modern, responsive web interface
- ✅ **Health Check**: Monitor application status
- ✅ **API Documentation**: Interactive Swagger UI
- ✅ **Message Echo**: Test API functionality
- ✅ **Environment Info**: View deployment details
- ✅ **Error Handling**: Test error scenarios

## 🏗️ Project Structure

```
render-fastapi-test/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 🚀 Quick Start

### Local Development

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```bash
   python main.py
   ```

3. **Access the application**:
   - Home page: http://localhost:8000
   - API docs: http://localhost:8000/docs
   - Health check: http://localhost:8000/health

### Render Deployment

1. **Connect to Render**:
   - Go to [render.com](https://render.com)
   - Create a new Web Service
   - Connect your GitHub repository

2. **Configure the service**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

3. **Deploy**:
   - Render will automatically deploy your application
   - Access your live URL from the Render dashboard

## 📡 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page with navigation |
| `/health` | GET | Health check and status |
| `/info` | GET | Deployment information |
| `/echo` | GET | Echo test form |
| `/api/echo` | POST | Echo API endpoint |
| `/api/echo/{message}` | GET | Echo with path parameter |
| `/test` | GET | Simple test endpoint |
| `/error-test` | GET | Test error handling |
| `/docs` | GET | Interactive API documentation |

## 🔧 Environment Variables

Render automatically provides these environment variables:

- `RENDER_ENVIRONMENT`: Deployment environment
- `RENDER_SERVICE_ID`: Service identifier
- `RENDER_SERVICE_NAME`: Service name
- `RENDER_SERVICE_TYPE`: Service type
- `RENDER_COMMIT_ID`: Git commit ID
- `RENDER_BRANCH`: Git branch name
- `PORT`: Port number (set by Render)

## 🧪 Testing

### Health Check
```bash
curl https://your-app.onrender.com/health
```

### Echo Test
```bash
curl -X POST https://your-app.onrender.com/api/echo \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, Render!"}'
```

### Environment Info
```bash
curl https://your-app.onrender.com/info
```

## 📊 Monitoring

### Health Endpoint Response
```json
{
  "status": "healthy",
  "timestamp": "2025-01-13T22:30:00.000000",
  "environment": "production",
  "python_version": "3.11.0",
  "platform": "Linux-5.15.0-x86_64"
}
```

### Info Endpoint Response
```json
{
  "app_name": "Render FastAPI Test",
  "version": "1.0.0",
  "deployment_time": "2025-01-13T22:30:00.000000",
  "environment": {
    "render_environment": "production",
    "render_service_id": "srv-abc123",
    "render_service_name": "fastapi-test",
    "render_service_type": "web",
    "render_commit_id": "abc123def456",
    "render_branch": "main"
  },
  "system": {
    "python_version": "3.11.0",
    "platform": "Linux-5.15.0-x86_64",
    "architecture": "64bit",
    "processor": "x86_64"
  }
}
```

## 🎯 Use Cases

This application is perfect for:

- **Testing Render deployment** workflows
- **Learning FastAPI** basics
- **Prototyping** new features
- **Monitoring** application health
- **Demonstrating** API functionality

## 🔍 Troubleshooting

### Common Issues

1. **Build fails**:
   - Check `requirements.txt` syntax
   - Verify Python version compatibility

2. **Application won't start**:
   - Ensure start command uses `$PORT` environment variable
   - Check logs in Render dashboard

3. **Health check fails**:
   - Verify all dependencies are installed
   - Check application logs for errors

### Debug Commands

```bash
# Check Python version
python --version

# Verify dependencies
pip list

# Test locally
uvicorn main:app --reload

# Check logs
tail -f logs/app.log
```

## 📈 Performance

- **Cold Start**: ~2-5 seconds
- **Response Time**: <100ms for simple endpoints
- **Memory Usage**: ~50-100MB
- **CPU Usage**: Minimal for basic operations

## 🔐 Security

- CORS enabled for all origins (development)
- Input validation with Pydantic
- Error handling without sensitive data exposure
- No authentication (for testing purposes)

## 📝 License

This project is open source and available under the MIT License.

---

**Happy deploying! 🚀**
