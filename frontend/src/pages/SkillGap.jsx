import { useState } from "react";

function SkillGap() {
  const [role, setRole] = useState("");
  const [result, setResult] = useState(null);

  const analyze = async () => {
    const response = await fetch(
      "http://127.0.0.1:8000/skill-gap",
      {
        method: "POST",
        headers: {
          "Content-Type":
            "application/json",
        },
        body: JSON.stringify({
          resume_skills: [
            "Python",
            "SQL",
            "Machine Learning",
            "Pandas"
          ],
          target_role: role,
        }),
      }
    );

    const data = await response.json();

    setResult(data);
  };

  return (
    <div
      style={{
        padding: "30px",
        textAlign: "center",
      }}
    >
      <h1>Skill Gap Analyzer</h1>

      <input
        type="text"
        placeholder="Target Role"
        value={role}
        onChange={(e) =>
          setRole(e.target.value)
        }
      />

      <br /><br />

      <button onClick={analyze}>
        Analyze
      </button>

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h3>
            Match:
            {result.match_percentage}%
          </h3>

          <h4>Matched Skills</h4>
          <ul>
            {result.matched_skills.map(
              (skill) => (
                <li key={skill}>
                  {skill}
                </li>
              )
            )}
          </ul>

          <h4>Missing Skills</h4>
          <ul>
            {result.missing_skills.map(
              (skill) => (
                <li key={skill}>
                  {skill}
                </li>
              )
            )}
          </ul>
        </div>
      )}
    </div>
  );
}

export default SkillGap;