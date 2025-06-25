# Cyvox-server

## Overview

Cyvox-Server is the backend server for CyVox, a voice authentication and voice platfor designed for law Enforcement Agencies (LEAs). It provides secure APIs for user enrollment, voiceprint management, and authentication workflows.

## Features 

- RESTful API for voice enrollment and verification.
- Secure user management and authentication
- Integration with voice recognition and anti-spoofing models
- Logging and audit trails for compliance
- Scable and modular architecture.

  ## Getting started

  ### Prerequisites
  - Python (3.10+)
  - MongoDB
  - FastAPI
  - SpeechBrain

   ### Installation

'''bash
- git clone : https://github.com/CodingPirates70/CyVox-Server.git
- cd CyVox-server
- pip install -r requirements.txt
'''

### Configuration

Copy '.env.example' to '.env' and update environment variables as needed.

### Running the server
 
uvicorn main:app -- reload

## API Endpoints

- 'POST/auth/register' - Enroll a new user and it's voice
-  'POST/Complaint/register' - Registers a user's complaints with necessary Metadata
-  'GET/user/:id' - Retrieve complaint details

  See API Documentation at '/docs' after running the server for full details.

  ## Security

- All endpoints require authentication (JWT)
- Voice fata is encrypted at rest and in transit
- Role- based access control for LEA personel

  ## License

  This project is license under the MIT license.
