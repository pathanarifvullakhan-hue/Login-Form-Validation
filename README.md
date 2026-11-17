# Login Form Validation (5.a and 5.b)

A small HTML, CSS and JavaScript login form with field validation, Docker packaging, Git workflow and Selenium browser tests.

## Demo credentials

- Username: `student`
- Password: `Demo@123`

This is a classroom demonstration. Credentials are checked in browser-side JavaScript; do not use this pattern for a real website or real accounts.

## Requirements

- macOS / Windows / Linux
- Git
- Docker Desktop (running)

## 1. Run the application

Open Terminal in this project folder and run:

```bash
docker compose up --build -d app
```

Open http://localhost:3000 in your browser.

To stop the app:

```bash
docker compose down
```

## 2. Build the Docker image (5.b)

```bash
docker build -t login-validation:1.0 .
docker images
```

Run the image directly if you want to test it without Compose:

```bash
docker run --rm -d --name login-demo -p 3000:80 login-validation:1.0
```

Then open http://localhost:3000. Stop it with:

```bash
docker stop login-demo
```

## 3. Run Selenium tests (5.b)

Make sure Docker Desktop is running. From the project folder:

```bash
docker compose --profile test up --build --abort-on-container-exit --exit-code-from tests
```

The Selenium test suite checks:
1. Empty username and password
2. Password shorter than 6 characters
3. Successful login with demo credentials
4. Incorrect login credentials

After the test run:

```bash
docker compose down
```

## 4. Git operations (5.a)

Run these commands from this project folder. Replace the example remote URL with your own GitHub repository URL.

```bash
git init
git status
git add .
git commit -m "Initial commit: login form validation"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/login-form-validation.git
git push -u origin main
```

For later changes:

```bash
git status
git add .
git commit -m "Update login form"
git push
```

To download your project on another computer:

```bash
git clone https://github.com/YOUR-USERNAME/login-form-validation.git
```

## What each file does

- `index.html` - login form fields and page structure
- `style.css` - page design
- `script.js` - JavaScript validation and demo credential check
- `Dockerfile` - packages the website into an Nginx Docker image
- `docker-compose.yml` - starts the app, Selenium browser and test runner
- `tests/test_login.py` - Selenium test cases
- `tests/requirements.txt` - Python Selenium dependency
- `tests/Dockerfile` - creates the test-runner image

## Mapping to the question

- **5.a:** Username/password form, JavaScript validation, and Git commands.
- **5.b:** Docker image build and Selenium tests for valid, invalid and missing login details.
