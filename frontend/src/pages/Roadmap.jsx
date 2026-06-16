import { useState } from "react";

function Roadmap() {
  const [role, setRole] = useState("");
  const [roadmap, setRoadmap] = useState([]);

  const generateRoadmap = async () => {
    try {
      const response = await fetch(
        "http://127.0.0.1:8000/roadmap",
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

      setRoadmap(data.roadmap);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div style={{ textAlign: "center", padding: "30px" }}>
      <h1>Career Roadmap</h1>

      <input
        type="text"
        placeholder="Enter Role"
        value={role}
        onChange={(e) => setRole(e.target.value)}
      />

      <br />
      <br />

      <button onClick={generateRoadmap}>
        Generate Roadmap
      </button>

      <div style={{ marginTop: "20px" }}>
        <h3>Roadmap</h3>

        <ol
        style={{
            display: "inline-block",
            textAlign: "left",
        }}
        >
        {roadmap.map((step, index) => (
            <li key={index}>{step}</li>
        ))}
        </ol>
      </div>
    </div>
  );
}

export default Roadmap;