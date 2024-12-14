# Fulfillment Operations Dashboard

A powerful and intuitive dashboard built with **React**, **Next.js**, and **TailwindCSS**, providing visual insights into fulfillment operations such as inventory levels and defect statistics. The dashboard uses **Chart.js** for visualizing data in interactive charts.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [API Integration](#api-integration)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project is designed to provide actionable insights into inventory management and product defects through a user-friendly, real-time dashboard. The dashboard fetches inventory data from a backend API and visualizes it with interactive charts, providing an overview of stock quantities and defect rates for different products.

## Features

- **Real-time Data Fetching**: Fetch inventory and defect data from a backend API using Axios.
- **Interactive Charts**: Utilize **Chart.js** for rendering line charts that display inventory and defect statistics.
- **Responsive Layout**: Built with **TailwindCSS** to ensure the dashboard is fully responsive across all devices.
- **User-Friendly UI**: TailwindCSS ensures the design is clean, modern, and accessible.
- **Customizable Chart Configuration**: Charts are fully customizable to include different datasets and dynamic rendering.

## Tech Stack

- **Frontend**:
  - **React**: A JavaScript library for building user interfaces.
  - **Next.js**: A React framework that enables server-side rendering, static site generation, and routing.
  - **TailwindCSS**: A utility-first CSS framework used to style the dashboard.
  - **Chart.js**: A powerful and flexible charting library for rendering charts.
- **Backend**:
  - **FastAPI** (or any backend of your choice) for serving the inventory and defect data through REST APIs.

## Installation

To get started with the project, follow the instructions below.

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/fulfillment-dashboard.git
cd fulfillment-dashboard
```

### 2. Install dependencies
Make sure you have Node.js installed. Then, run the following command to install the project dependencies:
```bash
npm install
```

### 23. Start the development server
After installing the dependencies, you can start the development server by running:
```bash
npm run dev
```
This will start the application on http://localhost:3000

## Usage
Once the application is running, you can access the Fulfillment Operations Dashboard in your web browser.

- The dashboard will fetch data from the backend API (http://127.0.0.1:8000 for local development).
- Data will be displayed in interactive charts showing both the inventory stock and defective quantities of different products.
- You can hover over the chart to see the exact numbers for each product and dataset.
- The UI adapts to all screen sizes, ensuring optimal usage on both mobile and desktop devices.

##Chart Overview:
- Inventory Data: Displays the number of products in stock.
- Defective Data: Displays the number of defective products.
- Both datasets are shown on the same chart for easy comparison.

## API Integration
The dashboard fetches data from an API hosted at http://127.0.0.1:8000/inventory and http://127.0.0.1:8000/defects. The data should be returned in the following format:


### Inventory Data:
```json
[
  {
    "product_name": "Product 1",
    "quantity_in_stock": 100,
    "quantity_defective": 5
  },
  {
    "product_name": "Product 2",
    "quantity_in_stock": 50,
    "quantity_defective": 2
  }
]
```

### Defect Data:
```json
[
  {
    "product_name": "Product 1",
    "quantity_in_stock": 100,
    "quantity_defective": 5
  },
  {
    "product_name": "Product 2",
    "quantity_in_stock": 50,
    "quantity_defective": 2
  }
]
```
Ensure that the backend is up and running to serve this data, or modify the URLs in the frontend code to match your API endpoints.

## Contributing
We welcome contributions to improve the project. Here's how you can help:

- Fork the repository.
- Create a new branch (git checkout -b feature/your-feature).
- Make your changes and commit them (git commit -am 'Add new feature').
- Push to your branch (git push origin feature/your-feature).
- Create a pull request with a clear explanation of your changes.
