import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:5000/api",
  timeout: 10000,
  headers: {
    "Content-Type": "application/json"
  }
});

// Analyze Job Description
export const analyzeJD = async (jobDescription) => {
  try {

    const response = await API.post(
      "/jd/analyze",
      {
        job_description: jobDescription
      }
    );

    return response.data;

  } catch (error) {

    console.error(
      "JD Analysis Error:",
      error
    );

    return {
      success: false
    };
  }
};

// Add Candidate
export const addCandidate = async (
  candidateData
) => {

  try {

    const response = await API.post(
      "/candidates/add",
      candidateData
    );

    return response.data;

  } catch (error) {

    console.error(
      "Candidate Error:",
      error
    );

    return {
      success: false
    };
  }
};

// Get All Candidates
export const getCandidates = async () => {

  try {

    const response = await API.get(
      "/candidates/all"
    );

    return response.data;

  } catch (error) {

    console.error(
      "Fetch Error:",
      error
    );

    return [];
  }
};

// Rank Candidates
export const rankCandidates = async (
  jobDescription,
  candidates
) => {

  try {

    const response = await API.post(
      "/ranking/match",
      {
        job_description:
          jobDescription,

        candidates:
          candidates
      }
    );

    return response.data;

  } catch (error) {

    console.error(
      "Ranking Error:",
      error
    );

    return {
      success: false
    };
  }
};

export default API;