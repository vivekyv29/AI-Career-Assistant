import { BrowserRouter, Routes, Route } from "react-router-dom";

import ATS from "./pages/ATS";
import Chat from "./pages/Chat";
import CoverLetter from "./pages/CoverLetter";
import Dashboard from "./pages/Dashboard";
import Interview from "./pages/Interview";
import InterviewHistory from "./pages/InterviewHistory";
import Jobs from "./pages/Jobs";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Report from "./pages/Report";
import ResumeFeedback from "./pages/ResumeFeedback";
import ResumeUpload from "./pages/ResumeUpload";
import Roadmap from "./pages/Roadmap";
import SkillGap from "./pages/SkillGap";
import MockInterview from "./pages/MockInterview";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
        <Route path="/upload" element={<ResumeUpload />} />
        <Route path="/skill-gap" element={<SkillGap />} />
        <Route path="/interview" element={<Interview />} />
        <Route
          path="/interview-history"
          element={<InterviewHistory />}
        />
        <Route path="/roadmap" element={<Roadmap />} />
        <Route path="/chat" element={<Chat />} />
        <Route path="/jobs" element={<Jobs />} />
        <Route path="/feedback" element={<ResumeFeedback />} />
        <Route path="/cover-letter" element={<CoverLetter />} />
        <Route path="/report" element={<Report />} />
        <Route path="/ats" element={<ATS />} />
        <Route
          path="/mock-interview"
          element={<MockInterview />}
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;