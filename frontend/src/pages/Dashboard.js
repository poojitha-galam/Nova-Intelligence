import React from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import AnalyticsCards from
"../components/AnalyticsCards";
import JDInput from
"../components/JDInput";
import CandidateTable from
"../components/CandidateTable";
import RankingChart from
"../components/RankingChart";
function Dashboard() {
  return (
    <div>
      <Navbar />
      <Sidebar />
      <AnalyticsCards />
      <JDInput />
      <RankingChart />
      <CandidateTable />
    </div>
  );
}

export default Dashboard;