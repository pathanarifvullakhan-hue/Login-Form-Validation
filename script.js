const form = document.getElementById("loginForm");
const usernameInput = document.getElementById("username");
const passwordInput = document.getElementById("password");
const usernameError = document.getElementById("usernameError");
const passwordError = document.getElementById("passwordError");
const message = document.getElementById("message");

// Demonstration credentials only. This is client-side validation, not secure authentication.
const DEMO_USERNAME = "student";
const DEMO_PASSWORD = "Demo@123";

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const username = usernameInput.value.trim();
  const password = passwordInput.value;
  let valid = true;

  usernameError.textContent = "";
  passwordError.textContent = "";
  message.textContent = "";
  message.className = "message";

  if (!username) {
    usernameError.textContent = "Username is required.";
    valid = false;
  }

  if (!password) {
    passwordError.textContent = "Password is required.";
    valid = false;
  } else if (password.length < 6) {
    passwordError.textContent = "Password must be at least 6 characters.";
    valid = false;
  }

  if (!valid) return;

  if (username === DEMO_USERNAME && password === DEMO_PASSWORD) {
    message.textContent = "Login successful! Welcome, " + username + ".";
    message.classList.add("success");
  } else {
    message.textContent = "Invalid username or password.";
    message.classList.add("failure");
  }
});
