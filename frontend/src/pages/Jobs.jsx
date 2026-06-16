import { useState } from "react";

function Jobs() {

  const [jobs, setJobs] = useState([]);

  const getJobs = async () => {

    const token = localStorage.getItem("token");

    const response = await fetch(
      "http://127.0.0.1:8000/job-recommendations",
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );

    const data = await response.json();

    setJobs(data.jobs);
  };

  return (
    <div style={{ textAlign: "center" }}>

      <h1>Job Recommendations</h1>

      <button onClick={getJobs}>
        Get Jobs
      </button>

      <ul>
        {jobs.map((job, index) => (
          <li key={index}>
            {job}
          </li>
        ))}
      </ul>

    </div>
  );
}

export default Jobs;