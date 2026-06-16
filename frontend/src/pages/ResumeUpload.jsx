import { useState } from "react";

function ResumeUpload() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState("");

  const uploadResume = async () => {
    if (!file) {
      alert("Please select a resume");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    const token = localStorage.getItem("token");

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/upload-resume",
        {
          method: "POST",
          headers: {
            Authorization: `Bearer ${token}`,
          },
          body: formData,
        }
      );

      const data = await response.json();

      setResult(JSON.stringify(data, null, 2));
    } catch (error) {
      console.error(error);
      setResult("Upload failed");
    }
  };

  return (
    <div style={{ padding: "30px", textAlign: "center" }}>
      <h1>Resume Upload</h1>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br />
      <br />

      <button onClick={uploadResume}>
        Upload Resume
      </button>

      <div style={{ marginTop: "20px" }}>
        <pre>{result}</pre>
      </div>
    </div>
  );
}

export default ResumeUpload;