# Nexvion — AI-Powered E-Commerce Platform

## Project Overview
Nexvion is a frontend e-commerce website designed to provide a simple shopping experience with product discovery, cart management, user account features, and checkout.

## Technologies Used
- HTML5
- CSS3
- JavaScript
- LocalStorage
- Docker
- Nginx
- Git and GitHub
- GitHub Actions

## Features
- Product catalogue containing 12 products
- Product image fallback placeholders
- Category, price, and stock filters
- Product search and sorting
- Shopping cart with quantity controls
- Login, registration, and logout
- LocalStorage persistence for demo accounts and cart data
- Separate checkout and payment page
- Input validation for phone number, PIN, card details, expiry, and UPI
- Cash on Delivery option
- Order confirmation

## Project Structure
- `index.html` — Home page
- `products.html` — Product catalogue
- `payment.html` — Checkout page
- `style.css`, `products.css`, `payment.css` — Styling
- `script.js`, `payment.js` — Client-side functionality
- `logo.png` — Website logo
- `Dockerfile` — Nginx-based container image configuration
- `.github/workflows/ci.yml` — Automated Docker image build workflow

## Run Locally
Run the following command from the project directory:

`py -m http.server 8000`

Open `http://localhost:8000` in your browser.

## Run with Docker
Build the image:

`docker build -t nexvion:latest .`

Start the container:

`docker run -d --name nexvion-web -p 8081:80 nexvion:latest`

Open `http://localhost:8081`.

## Continuous Integration
GitHub Actions automatically builds the Docker image when changes are pushed or pull requests target the `main` branch.

## Limitations
Authentication and payment are frontend demo features implemented using LocalStorage. The project does not process real payments or provide production-grade authentication. A production deployment would require a secure backend and a real payment gateway.
### Terraform Infrastructure as Code
Terraform provisions the local Nexvion Docker container using
the Docker provider. The application is exposed on port 8083.
This demonstrates local infrastructure automation, not cloud provisioning.