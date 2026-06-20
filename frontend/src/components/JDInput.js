import React, { useState } from "react";
function JDInput() {
  const [jobDescription, setJobDescription] =
    useState("");
  const [analysis, setAnalysis] =
    useState(null);
  const analyzeJD = () => {
    const result = {
      role: "Backend Developer",
      skills: [
        "Python",
        "Flask",
        "MongoDB",
        "Docker"
      ],
      experience: "3+ Years"
    };
    setAnalysis(result);
  };
  return (
    <div>
      <h2>
        Job Description Analyzer
      </h2>
      <textarea
        rows="10"
        cols="80"
        placeholder="Paste Job Description Here..."
        value={jobDescription}
        onChange={(e) =>
          setJobDescription(
            e.target.value
          )
        }
      />
      <br />
      <button
        onClick={analyzeJD}
      >
        Analyze JD
      </button>

      {analysis && (
        <div>

          <h3>Extracted Requirements</h3>

          <p>
            <strong>Role:</strong>
            {analysis.role}
          </p>

          <p>
            <strong>Experience:</strong>
            {analysis.experience}
          </p>

          <p>
            <strong>Skills:</strong>
            {analysis.skills.join(", ")}
          </p>

        </div>
      )}

    </div>
  );
}

export default JDInput;