import { useState } from "react";

function Report() {
  const [message, setMessage] = useState("");

  const generateReport = async () => {
    try {
      const response = await fetch(
        "http://127.0.0.1:8000/career-report"
      );

      const data = await response.json();

      setMessage(data.message);
    } catch (error) {
      console.log(error);
      setMessage("Report generation failed");
    }
  };

  return (
    <div
      style={{
        textAlign: "center",
        padding: "30px",
      }}
    >
      <h1>Career Report</h1>

      <button onClick={generateReport}>
        Generate Report
      </button>

      <br />
      <br />

      <h3>{message}</h3>

      {message && (
        <>
          <p>
            Generated file:
            <b> career_report.pdf</b>
          </p>

          <a
            href="http://127.0.0.1:8000/download-report"
            target="_blank"
            rel="noreferrer"
          >
            Download PDF
          </a>
        </>
      )}
    </div>
  );
}

export default Report;