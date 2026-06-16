import { useState } from "react";

function Interview() {
  const [role, setRole] = useState("");
  const [questions, setQuestions] = useState([]);
  const [answer, setAnswer] = useState("");
  const [feedback, setFeedback] = useState("");

  const generateQuestions = async () => {
    try {
      const response = await fetch(
        "http://127.0.0.1:8000/generate-question",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            role: role,
          }),
        }
      );

      const data = await response.json();

      setQuestions(data.questions);
    } catch (error) {
      console.log(error);
      setQuestions([]);
    }
  };

  const evaluateAnswer = async () => {
    try {
      const response = await fetch(
        "http://127.0.0.1:8000/evaluate-answer",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            question: questions[0],
            answer: answer,
          }),
        }
      );

      const data = await response.json();

      setFeedback(data.feedback);
    } catch (error) {
      console.log(error);
      setFeedback("Evaluation Failed");
    }
  };

  return (
    <div
      style={{
        textAlign: "center",
        padding: "30px",
      }}
    >
      <h1>Mock Interview</h1>

      <input
        type="text"
        placeholder="Enter Role"
        value={role}
        onChange={(e) =>
          setRole(e.target.value)
        }
      />

      <br />
      <br />

      <button onClick={generateQuestions}>
        Generate Questions
      </button>

      <div style={{ marginTop: "20px" }}>
        <h3>Questions</h3>

        <div
          style={{
            textAlign: "left",
            maxWidth: "800px",
            margin: "auto",
          }}
        >
          {questions.map((q, index) => (
            <p key={index}>
              {index + 1}. {q}
            </p>
          ))}
        </div>
      </div>

      <h3>Your Answer</h3>

      <textarea
        rows="8"
        cols="70"
        value={answer}
        onChange={(e) =>
          setAnswer(e.target.value)
        }
        placeholder="Write your answer here..."
      />

      <br />
      <br />

      <button onClick={evaluateAnswer}>
        Evaluate Answer
      </button>

      <div style={{ marginTop: "20px" }}>
        <h3>Feedback</h3>

        <pre
          style={{
            whiteSpace: "pre-wrap",
            textAlign: "left",
            maxWidth: "800px",
            margin: "auto",
          }}
        >
          {feedback}
        </pre>
      </div>
    </div>
  );
}

export default Interview;