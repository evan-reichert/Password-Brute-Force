# Password Generator & Strength Analyzer

A Python-based cybersecurity application that generates secure passwords, evaluates their strength using entropy, and demonstrates how vulnerable weak passwords are to brute-force attacks.

---

## Overview

This project is a command-line password security tool designed to demonstrate secure password generation, entropy-based strength analysis, and brute-force attack simulation.

The application allows users to:

* Generate secure passwords
* Analyze password strength using entropy
* Validate password security criteria
* Estimate or simulate brute-force attacks
* Regenerate passwords until satisfied

The application is built entirely in Python and focuses on applying core cybersecurity concepts in a practical, interactive environment.

---

## Key Features

### Secure Password Generation

* Utilizes Python’s `secrets` module for cryptographically secure randomness
* Supports customizable password lengths
* Generates passwords using:

  * Uppercase letters
  * Lowercase letters
  * Numbers
  * Special characters

### Brute Force Simulation

* If password length is less than 8 characters:

  * Simulates a brute-force attack using `itertools`
  * Displays progress using `tqdm`
  * Demonstrates how quickly weak passwords can be cracked

### Brute Force Time Estimation

* For passwords 8+ characters:

  * Calculates total possible combinations
  * Estimates cracking time assuming 1 million attempts per second
  * Converts time into human-readable format (years, days, hours, etc.)

### Password Validation

* Ensures generated passwords meet security criteria:

  * Minimum length of 8 characters
  * Contains uppercase and lowercase letters
  * Includes numbers
  * Includes special characters

### Entropy Calculation

* Computes password entropy using:

Entropy = length × log₂(character set size)

* Dynamically adjusts character set size based on password composition
* Provides a mathematical measure of password unpredictability

### Strength Classification

* Categorizes passwords based on entropy:

| Entropy (bits) | Strength Level |
| -------------- | -------------- |
| < 28           | Very Weak      |
| 28 – 35        | Weak           |
| 36 – 59        | Reasonable     |
| 60 – 127       | Strong         |
| 128+           | Very Strong    |

### Interactive User Loop

* Displays:

  * Generated password
  * Entropy score
  * Strength classification
  * Validation result
  * Crack time estimate or simulation
* Allows users to regenerate passwords until satisfied

---

## Technologies Used

* Python
* secrets
* math
* string
* itertools
* time
* tqdm
* Git / GitHub

---

## Application Structure

|----- pass.py

---

## How to Run

### 1. Clone the repository

```python
git clone https://github.com/evan-reichert/Password-Brute-Force.git
```
### 2. Navigate into the project directory
```python
cd password-generator
```
### 3. (Optional but recommended) Create a virtual environment
```python
python3 -m venv venv
source venv/bin/activate (Mac/Linux)
venv\Scripts\activate (Windows)
```
### 4. Install Dependencies
```python
python3 -m pip install tqdm
```
### 5. Run the Application
```python
python3 pass.py
```
---

## Example Output

Generated Password: A9$kL2!qZ
Brute Force Time Estimate: 12y 45d 3h 20m 10s
Password Entropy: 59.87 bits
Password Validation: Meets criteria
Password Strength: Strong

---

## Skills Demonstrated

* Secure password generation
* Entropy-based security analysis
* Brute-force attack simulation
* Algorithmic problem solving
* Input validation and defensive programming
* CLI application development

---

## Future Improvements

* Add dictionary attack simulation
* Integrate password blacklist checking
* Build a graphical user interface (GUI)
* Allow custom character sets
* Improve attack modeling with hardware-based estimates
* Deploy as a web application
