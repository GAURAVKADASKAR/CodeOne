# Django Backend Documentation - CodeOne

This document provides a comprehensive overview of the CodeOne Django backend, including its features, database schema, and API endpoints.

---

## 🚀 Features List

### 1. User Management & Authentication
- **User Registration**: Support for both standard users (Coders) and administrators.
- **Verification**: Email-based account activation system.
- **Authentication**: JWT-based login and session management.
- **Password Security**: Reset password (internal), forgot password (via email token).
- **Account Management**: Profile deletion with automatic backup of user data.

### 2. Coding Platform (Challenges)
- **Problem Management**: Admin-side tools to create coding questions with multiple test cases.
- **Dynamic Scoring**: Points automatically calculated based on test case weights.
- **Public/Private Test Cases**: Support for visible sample cases and hidden evaluation cases.
- **Code Execution**: Remote code compilation and execution via Judge0 API.
- **Submission Tracking**: Logs for solved and partially solved status with user code storage.

### 3. SQL Challenges
- **SQL Editor**: Execute SQL queries against a live database.
- **Automated Evaluation**: Compares user query output with JSON-defined expected output.
- **Table Support**: Pre-populated tables like `student` (SqlQuestions) and `employee`.

### 4. Quiz System
- **Quiz Creation**: Comprehensive quiz setup with multiple-choice questions.
- **Registration**: Users can register for upcoming/inactive quizzes.
- **Live Quizzes**: Access to active quizzes and automated timer-based submission logic.
- **Scoring**: Instant result generation and leaderboard calculation.

### 5. Hackathon Management
- **Event Lifecycle**: Creation, registration, and status management.
- **Team-based Participation**: Support for team registration with leaders and members.
- **Problem Statement Assignment**: Teams can select specific problem statements from a limited pool.
- **Communication**: Automated email notifications for registration and verification.
- **Judge Integration**: Framework for assigning judges to hackathons.

### 6. Ranking & Leaderboards
- **Global Ranking**: Real-time point-based ranking of all users.
- **Activity Specific Leaderboards**: Dedicated boards for quizzes and global coding points.

---

## 📊 Database Tables (Models)

| Table Name | Model Class | Purpose |
| :--- | :--- | :--- |
| `home_userregistraion` | `UserRegistraion` | Stores core user profile, role, and verification status. |
| `home_codingquestion` | `CodingQuestion` | Metadata for coding challenges (title, description, difficulty). |
| `home_sampletestcase` | `SampleTestCase` | Input/Output pairs for coding question validation. |
| `home_userscodingpoints`| `UsersCodingPoints` | User-level stats (total points, solved count per difficulty). |
| `home_solvedquestion` | `SolvedQuestion` | History of solved coding questions and submitted code. |
| `home_sqlquestions` | `SqlQuestions` | SQL-specific tasks with expected result sets. |
| `employee` | `EmployeeData` | Sample dataset for SQL problem execution. |
| `home_solvedsqlquestion`| `SolvedSqlQuestion` | History of solved SQL challenges. |
| `home_quiz` | `Quiz` | Container for quiz events, timing, and metadata. |
| `home_quizquestion` | `QuizQuestion` | Multiple-choice questions for specific quizzes. |
| `home_quizanswer` | `QuizAnswer` | Holds the correct option mapping for quiz questions. |
| `home_quizresult` | `QuizResult` | Individual performance records for quiz attempts. |
| `home_quizregistration` | `QuizRegistration` | Tracks which users are registered for which quizzes. |
| `home_hackathon` | `HackaThon` | Master record for hackathon events. |
| `home_hackathonproblemstatement` | `hackathonProblemStatement` | Available tracks/problems for a hackathon. |
| `home_hackathonregistration` | `HackaThonRegistration` | Team members and roles for hackathon events. |
| `home_hackathonproblemteam` | `HackathonProblemTeam` | Mapping of selected problem statements to teams. |
| `home_backupuserregistraion` | `BackUpUserRegistraion` | Archive of deleted user accounts. |

---

## 🔌 API Documentation

### 🔑 Authentication & User Management

#### `POST /UserRegistration/`
- **Purpose**: Registers a new standard user.
- **Payload**:
  ```json
  {
    "username": "coder123",
    "firstname": "John",
    "lastname": "Doe",
    "email": "john@example.com",
    "password": "strongpassword"
  }
  ```

#### `POST /AdminRegistration/`
- **Purpose**: Registers a new administrator.
- **Payload**: Same as User Registration.

#### `GET /verify/?token=<token>`
- **Purpose**: Activates a user account via email token.

#### `POST /login/`
- **Purpose**: Authenticates user and returns a JWT token.
- **Payload**:
  ```json
  {
    "username": "coder123",
    "password": "strongpassword"
  }
  ```

#### `POST /RestPassword/`
- **Purpose**: Resets password while logged in.
- **Payload**:
  ```json
  {
    "token": "jwt_token",
    "currentpassword": "old_password",
    "newpassword": "new_password"
  }
  ```

#### `POST /ForgotPassword/`
- **Purpose**: Updates password using a verification token from email.
- **Payload**:
  ```json
  {
    "newpassword": "new_password"
  }
  ```
- **Query Param**: `token` (Verification token).

---

### 💻 Coding Challenges

#### `POST /EnterQuestion/`
- **Purpose**: (Admin) Create a new coding question.
- **Payload**:
  ```json
  {
    "coding_question": "QU001",
    "title": "Reverse Array",
    "description": "Write a function to reverse an array.",
    "difficulty": "Easy",
    "constraints": "O(n) time",
    "sample_test_cases": [
      {
        "input_data": "[1,2,3]",
        "expected_output": "[3,2,1]",
        "is_public": true,
        "testcasepoint": 10
      }
    ]
  }
  ```

#### `GET /GetAllQuestions/`
- **Purpose**: Fetch all available coding challenges.

#### `POST /GetQuestionById/`
- **Purpose**: Fetch details of a specific question.
- **Payload**: `{"id": 1}`

#### `POST /VerifyCodeForTestCase/`
- **Purpose**: Execute user code against all test cases.
- **Payload**:
  ```json
  {
    "token": "jwt_token",
    "question_id": 1,
    "user_code": "def solve()...",
    "language_id": 71
  }
  ```

---

### 🗄️ SQL Challenges

#### `POST /NewsqlQuestion/`
- **Purpose**: (Admin) Insert a new SQL challenge.
- **Payload**:
  ```json
  {
    "Sql_question": "SQL001",
    "title": "Select All Employees",
    "description": "Write a query to select all data from employee table.",
    "difficulty": "Easy",
    "points": 20,
    "expected_output": "[{\"id\":1, \"name\":\"John\"}, ...]"
  }
  ```

#### `POST /ExecuteUserSql/`
- **Purpose**: Run user's SQL query and validate results.
- **Payload**:
  ```json
  {
    "token": "jwt_token",
    "question_id": 1,
    "user_sql": "SELECT * FROM employee;"
  }
  ```

---

### 📝 Quiz System

#### `POST /CreateQuiz/`
- **Purpose**: (Admin) Create a quiz with questions.
- **Payload**:
  ```json
  {
    "quiz_name": "Python Basics",
    "title": "Introduction to Python",
    "description": "A beginner quiz",
    "total_questions": 2,
    "total_marks": 20,
    "start_time": "2023-12-01T10:00:00Z",
    "quiz_questions": [
      {
        "question": "What is 2+2?",
        "option1": "3", "option2": "4", "option3": "5", "option4": "6",
        "correct_option": "option2"
      }
    ]
  }
  ```

#### `POST /RegisterForQuiz/`
- **Purpose**: Registers a user for a specific quiz.
- **Payload**: `{"token": "jwt_token", "quiz_id": 1}`

#### `POST /SubmitQuizAnswer/`
- **Purpose**: Submit answers for an active quiz.
- **Payload**:
  ```json
  {
    "token": "jwt_token",
    "quiz_id": 1,
    "answers": [
      {"question_id": 1, "selected_option": "option2"}
    ]
  }
  ```

---

### 🏆 Hackathon Management

#### `POST /CreateHackaThon/`
- **Purpose**: (Admin) Initialize a hackathon event.
- **Payload**: `HackaThon model fields`.

#### `POST /HackRegistrations/`
- **Purpose**: Register a team for a hackathon.
- **Payload**:
  ```json
  [
    {
      "hackathon_id": 1,
      "team_name": "Alpha",
      "member_name": "Lead",
      "member_email": "lead@mail.com",
      "member_type": "leader",
      "college_name": "ABC University",
      "phone_number": "1234567890"
    }
  ]
  ```

#### `POST /SelectProblemStatement/`
- **Purpose**: Assign a problem statement to a team.
- **Payload**:
  ```json
  {
    "problem_statement_id": 1,
    "team_id": "alpha-1-12",
    "hackathon_id": 1
  }
  ```

---

## 📈 Leaderboards

- **Global Leaderboard**: `GET /GlobalLeaderBoard/` - Overall ranking.
- **Quiz Leaderboard**: `POST /QuizLeaderBoard/` - Ranking for a specific quiz (Payload: `{"quiz_id": 1}`).
