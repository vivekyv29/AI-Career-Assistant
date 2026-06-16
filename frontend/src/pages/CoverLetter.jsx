import { useState } from "react";

function CoverLetter() {
  const [name, setName] = useState("");
  const [role, setRole] = useState("");
  const [skills, setSkills] = useState("");
  const [result, setResult] = useState("");

  const generateLetter = async () => {
    const response = await fetch(
      "http://127.0.0.1:8000/cover-letter",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: name,
          job_role: role,
          skills: skills.split(","),
        }),
      }
    );

    const data = await response.json();

    setResult(data.cover_letter);
  };

  return (
    <div style={{ textAlign: "center" }}>
      <h1>Cover Letter Generator</h1>

      <input
        placeholder="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <br /><br />

      <input
        placeholder="Job Role"
        value={role}
        onChange={(e) => setRole(e.target.value)}
      />

      <br /><br />

      <textarea
        rows="5"
        cols="50"
        placeholder="Python, Machine Learning, NLP"
        value={skills}
        onChange={(e) => setSkills(e.target.value)}
      />

      <br /><br />

      <button onClick={generateLetter}>
        Generate Cover Letter
      </button>

      <br /><br />

      <pre>{result}</pre>
    </div>
  );
}

export default CoverLetter;