import React, { useState } from "react";

function Results() {

  const [rankedCandidates] = useState([
    {
      rank: 1,
      name: "John Doe",
      score: 96,
      experience: "4 Years",
      skills: [
        "Python",
        "Flask",
        "MongoDB"
      ]
    },
    {
      rank: 2,
      name: "Sarah Smith",
      score: 92,
      experience: "3 Years",
      skills: [
        "Machine Learning",
        "Python",
        "TensorFlow"
      ]
    },
    {
      rank: 3,
      name: "David Lee",
      score: 88,
      experience: "2 Years",
      skills: [
        "React",
        "Node.js",
        "MongoDB"
      ]
    }
  ]);

  return (

    <div
      style={{
        padding: "20px"
      }}
    >

      <h1>
        TalentSphere Results
      </h1>

      <p>
        AI Ranked Candidate Recommendations
      </p>

      {

        rankedCandidates.map(
          (candidate) => (

            <div
              key={candidate.rank}

              style={{
                border:
                  "1px solid #ccc",

                borderRadius:
                  "10px",

                padding:
                  "15px",

                marginBottom:
                  "15px",

                boxShadow:
                  "0px 2px 5px rgba(0,0,0,0.1)"
              }}
            >

              <h2>

                #{candidate.rank}

                {" "}

                {candidate.name}

              </h2>

              <p>

                <strong>
                  Match Score:
                </strong>

                {" "}

                {candidate.score}%

              </p>

              <p>

                <strong>
                  Experience:
                </strong>

                {" "}

                {candidate.experience}

              </p>

              <p>

                <strong>
                  Skills:
                </strong>

                {" "}

                {
                  candidate.skills.join(
                    ", "
                  )
                }

              </p>

              <div>

                <strong>
                  AI Recommendation:
                </strong>

                <p>

                  {

                    candidate.score >= 90

                    ?

                    "Highly Recommended Candidate"

                    :

                    candidate.score >= 80

                    ?

                    "Recommended Candidate"

                    :

                    "Needs Further Review"

                  }

                </p>

              </div>

            </div>

          )
        )

      }

    </div>

  );

}

export default Results;