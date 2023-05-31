# Flask XML to HTML Converter

This application is a simple Flask web server that allows users to upload XML and XSL files. It then transforms the XML to HTML using the provided XSL and serves the resulting HTML. Demo can be found [here](https://xml.rajsingh.info).

## Prerequisites

- Docker
- Docker Compose

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installation

1. Clone the repository or download the source code.
2. Navigate to the directory containing the source code.

### Running the Application

1. To start the server, run the following command in your terminal:

2. Open your web browser and visit `http://localhost:8080`. 

3. Upload the XML and XSL files using the form on the webpage. The server will transform the XML to HTML using the XSL, save the HTML file, and redirect your browser to the newly created HTML file.

## Built With

- [Flask](https://flask.palletsprojects.com/en/2.1.x/) - The web framework used
- [lxml](https://lxml.de/) - Library for processing XML and HTML
- [Docker](https://www.docker.com/) - Used for containerization

