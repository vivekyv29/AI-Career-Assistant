import { useEffect, useState } from "react";

function Dashboard() {

  const [data, setData] = useState({});

  useEffect(() => {
    fetch("http://127.0.0.1:8000/dashboard")
      .then((res) => res.json())
      .then((data) => setData(data));
  }, []);

  return (
    <div style={{ textAlign: "center" }}>
      <h1>Dashboard</h1>

      <h3>Total Resumes: {data.total_resumes}</h3>

      <h3>
        Interview Attempts:
        {data.total_interviews}
      </h3>

      <h3>
        Average Score:
        {data.average_score}
      </h3>
    </div>
  );
}

export default Dashboard;