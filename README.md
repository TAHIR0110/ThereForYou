# ThereForYou

![GSSoC Logo Light](https://user-images.githubusercontent.com/63473496/213306239-9e8fc317-ce2f-4127-8bfe-17f5df06ee99.png#gh-light-mode-only)
![GSSoC Logo Dark](https://user-images.githubusercontent.com/63473496/213306279-338f7ce9-9a9f-4427-8c2a-3e344874498f.png#gh-dark-mode-only)

<div align="center">
  <img src="https://socialify.git.ci/TAHIR0110/ThereForYou/image?language=1&name=1&pattern=Plus&theme=Auto" alt="ThereForYou" width="640" height="320" />
</div> 

# Enhanced Public Safety: ThereForYou
**ThereForYou** is a groundbreaking solution aimed at enhancing public safety, particularly focusing on mental health support and suicide prevention. Leveraging cutting-edge technologies such as artificial intelligence (AI), machine learning (ML), natural language processing (NLP), and blockchain, our project offers accessible and empathetic assistance to individuals facing mental health challenges.

## Key Features
### Part 1: AI Psychologist
- Dynamic Voice Adjustment: Our AI assistant dynamically adjusts its voice to match the user's gender, enhancing engagement and personalization.
- Emotion Detection: Utilizing algorithms, the assistant detects signs of sadness or depression in user speech, securely storing this data using blockchain technology for potential future counseling sessions.
- Empathetic Support: In moments of distress, sadness, or depression, the AI psychologist offers empathetic support and practical advice to encourage users towards positive steps forward.

### Part 2: Suicide Prevention Model
- Choking Detection: We have developed an API powered by advanced machine learning models that can detect signs of choking in users. Upon detection, it immediately sends alerts with location data of the victim to nearby users and authorities, including police officers, ensuring prompt assistance in critical situations.
- Reward System: Users who assist individuals in choking incidents are rewarded with HealthTokens, redeemable at hospitals. This incentivizes community involvement in assisting those in need.

### Part 3: Voice-Activated Safety Alert System
- NLP-Based Danger Detection: Our advanced NLP model detects danger signals from user speech. Upon detection, nearby users and authorities such as police officers are alerted through push notifications about the location and condition of the victim.
- Reward Mechanism: Similar to Part 2, individuals who respond to safety alerts and assist those in danger are rewarded with HealthTokens.
- Link to safety system => https://vhelp.onrender.com/
- App link could not be shared because of security reasons

## Videos:
### PART 1:
https://github.com/Atharv714/nationalhackathon/assets/142321494/f8e68f17-ec9b-46f5-94c1-f09af9d5afa3

### PART 2:
https://github.com/Atharv714/nationalhackathon/assets/142321494/8de7ae5d-30b6-48f8-a58c-c4c9c1ce8bf4

### PART 3 (MUST WATCH):
https://github.com/Atharv714/nationalhackathon/assets/142321494/c13cde81-8ab2-4999-aa0c-916c5551d54d

## Tech Stack
### Frontend
- HTML/CSS
- JavaScript
- Flutter

## Machine Learning 
- TensorFlow
- Natural language processing
- Scikit-learn 
- SpaCy
- NLTK
- OpenCV

## Backend
- Flask
- OpenAPI
- Google Web Speech API
- PyAudio
- Node.js
- Firebase

## Forking Steps for New Contributors

To contribute to the ThereForYou project as part of GSSoC'24, follow these steps to fork the repository and set up your local development environment:

### Step 1: Fork the Repository
1. Navigate to the [ThereForYou GitHub repository].
2. Click the **Fork** button at the top-right corner of the page. This will create a copy of the repository under your GitHub account.

### Step 2: Clone Your Fork
1. Go to your GitHub profile and find the forked repository under your repositories list.
2. Click on the repository name to open it.
3. Click the **Code** button and copy the URL.
4. Open your terminal or command prompt.
5. Run the following command to clone the repository to your local machine:
   
          git clone https://github.com/yourusername/ThereForYou.git
7. Change into the project directory:
   
          cd ThereForYou

### Step 3: Set Up the Upstream Remote
1. Add the original repository as a remote to keep your fork up to date with the latest changes:
   
          git remote add upstream https://github.com/originalusername/ThereForYou.git
3. Verify the new remote named upstream:
   
          git remote -v

### Step 4: Create a Branch
1. Before starting work on a new feature or bug fix, create a new branch:
   
          git checkout -b feature-branch-name

### Step 5: Make Your Changes
1. Develop your feature or fix the bug.
2. Stage your changes:
   
          git add .
4. Commit your changes:
   
          git commit -m "Description of the feature or fix"

### Step 6: Push Your Changes
1. Push your changes to your forked repository:
   
          git push origin feature-branch-name

### Step 7: Create a Pull Request
1. Go to your forked repository on GitHub.
2. Click on the Compare & pull request button.
3. Provide a descriptive title and detailed description of your changes.
4. Click Create pull request.

### Step 8: Sync Your Fork
1. Keep your fork up to date with the upstream repository:
   
          git fetch upstream
          git checkout main
          git merge upstream/main
3. Push the updated main branch to your fork:

         git push origin main

### I'm participating in GSSoC'24 (GirlScript Summer of Code 2024).

## Note: Pull Request may take some time to be merged into the repository. If there are any issues, we will inform you; otherwise, it will be merged eventually. Please don't worry.
