import React, { useState } from "react";

function CandidateTable() {

  const [candidates] = useState([
    {
      id: "C001",
      name: "John Doe",
      role: "Backend Developer",
      score: 96,
      experience: "4 Years",
      status: "Shortlisted"
    },
    {
      id: "C002",
      name: "Sarah Smith",
      role: "ML Engineer",
      score: 92,
      experience: "3 Years",
      status: "Interview"
    },
    {
      id: "C003",
      name: "David Lee",
      role: "Full Stack Developer",
      score: 88,
      experience: "2 Years",
      status: "Review"
    }
  ]);

  return (
    <div>
      <h2>Top Ranked Candidates</h2>

      <table border="1" width="100%">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Role</th>
            <th>Experience</th>
            <th>Match Score</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>
          {candidates.map((candidate) => (
            <tr key={candidate.id}>
              <td>{candidate.id}</td>
              <td>{candidate.name}</td>
              <td>{candidate.role}</td>
              <td>{candidate.experience}</td>
              <td>{candidate.score}%</td>
              <td>{candidate.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default CandidateTable;