import React from "react";

function RankingChart() {

  const data = [
    {
      candidate: "John",
      score: 96
    },
    {
      candidate: "Sarah",
      score: 92
    },
    {
      candidate: "David",
      score: 88
    },
    {
      candidate: "Alex",
      score: 84
    }
  ];

  return (
    <div>

      <h2>
        Candidate Ranking Overview
      </h2>

      {data.map((item) => (

        <div
          key={item.candidate}
          style={{
            marginBottom: "15px"
          }}
        >

          <div>

            {item.candidate}
            {" "}
            ({item.score}%)

          </div>

          <div
            style={{
              width: "100%",
              backgroundColor: "#ddd",
              height: "20px"
            }}
          >

            <div
              style={{
                width:
                  item.score + "%",
                backgroundColor:
                  "#4CAF50",
                height: "20px"
              }}
            />

          </div>

        </div>

      ))}
    </div>
  );
}

export default RankingChart;