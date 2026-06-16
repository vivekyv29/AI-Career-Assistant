import { useState } from "react";

function ATS() {
  const [resumeText, setResumeText] = useState("");
  const [file, setFile] = useState(null);
  const [result, setResult] = useState("");

  const analyzeResume = async () => {
    try {
      const formData = new FormData();

      if (file) {
        formData.append("file", file);
      } else {
        formData.append("resume_text", resumeText);
      }

      const response = await fetch(
        "http://127.0.0.1:8000/ats",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      setResult(data.analysis);
    } catch (error) {
      console.log(error);
      setResult("Analysis failed");
    }
  };

  return (
    <div style={{ textAlign: "center", padding: "30px" }}>
      <h1>ATS Resume Analyzer</h1>

      <textarea
        rows="10"
        cols="80"
        placeholder="Paste Resume Text Here"
        value={resumeText}
        onChange={(e) => setResumeText(e.target.value)}
      />

      <br />
      <br />

      <h3>OR</h3>

      <input
        type="file"
        accept=".pdf,.doc,.docx"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br />
      <br />

      <button onClick={analyzeResume}>
        Analyze Resume
      </button>

      <div style={{ marginTop: "20px" }}>
        <h3>ATS Analysis</h3>

        <pre
          style={{
            whiteSpace: "pre-wrap",
            textAlign: "left",
            maxWidth: "900px",
            margin: "auto",
          }}
        >
          {result}
        </pre>
      </div>
    </div>
  );
}

export default ATS;