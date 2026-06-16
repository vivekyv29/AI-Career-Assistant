import { useEffect, useState } from "react";

function InterviewHistory() {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    const loadHistory = async () => {
      try {
        const response = await fetch(
          "http://127.0.0.1:8000/interview-history"
        );

        const data = await response.json();
        setHistory(data);
      } catch (error) {
        console.log(error);
      }
    };

    loadHistory();
  }, []);

  return (
    <div
      style={{
        padding: "30px",
        maxWidth: "1000px",
        margin: "auto",
      }}
    >
      <h1>Interview History</h1>

      {history.length === 0 ? (
        <p>No interview history found.</p>
      ) : (
        history.map((item) => (
          <div
            key={item.id}
            style={{
              border: "1px solid gray",
              padding: "15px",
              marginBottom: "20px",
            }}
          >
            <h3>Question</h3>
            <p>{item.question}</p>

            <h3>Answer</h3>
            <p>{item.answer}</p>

            <h3>Score</h3>
            <p>{item.score}/10</p>
          </div>
        ))
      )}
    </div>
  );
}

export default InterviewHistory;