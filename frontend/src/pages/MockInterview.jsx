import { useState } from "react";

function MockInterview() {
  const [role, setRole] = useState("");
  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState([]);
  const [score, setScore] = useState(null);

  const startInterview = async () => {
    try {
      const response = await fetch(
        "http://127.0.0.1:8000/start-mock-interview",
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
      setAnswers(new Array(data.questions.length).fill(""));
      setScore(null);
    } catch (error) {
      console.log(error);
    }
  };

  const handleAnswerChange = (index, value) => {
    const updatedAnswers = [...answers];
    updatedAnswers[index] = value;
    setAnswers(updatedAnswers);
  };

  const submitInterview = async () => {
    try {
      const response = await fetch(
        "http://127.0.0.1:8000/submit-mock-interview",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            answers: answers,
          }),
        }
      );

      const data = await response.json();

      setScore(data.score);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div
      style={{
        padding: "30px",
        textAlign: "center",
      }}
    >
      <h1>Mock Interview</h1>

      <input
        type="text"
        placeholder="Enter Role"
        value={role}
        onChange={(e) => setRole(e.target.value)}
        style={{
          padding: "10px",
          width: "300px",
        }}
      />

      <br />
      <br />

      <button onClick={startInterview}>
        Start Interview
      </button>

      <div style={{ marginTop: "30px" }}>
        {questions.map((q, index) => (
          <div key={index}>
            <h2>Question {index + 1}</h2>

            <p>{q}</p>

            <textarea
              rows="5"
              cols="80"
              value={answers[index] || ""}
              onChange={(e) =>
                handleAnswerChange(index, e.target.value)
              }
              placeholder="Write your answer..."
            />

            <br />
            <br />
            <hr />
          </div>
        ))}
      </div>

      {questions.length > 0 && (
        <>
          <button onClick={submitInterview}>
            Submit Interview
          </button>

          <br />
          <br />

          {score !== null && (
            <h2>
              Final Score: {score}/10
            </h2>
          )}
        </>
      )}
    </div>
  );
}

export default MockInterview;