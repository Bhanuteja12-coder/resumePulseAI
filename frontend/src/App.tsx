import { useEffect, useState } from 'react';
import { Route, Routes, Navigate } from 'react-router-dom';

import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import DashboardPage from './pages/DashboardPage';
import UploadResumePage from './pages/UploadResumePage';
import ReportPage from './pages/ReportPage';
import ReportsDashboard from "./pages/ReportsDashboard";

import MainLayout from './layouts/MainLayout';
import { getToken } from './utils/auth';

const App = () => {
  const [token, setToken] = useState(getToken());

  // 🔥 updates token when login/logout changes localStorage
  useEffect(() => {
    const syncToken = () => {
      setToken(getToken());
    };

    // storage event (works across tabs)
    window.addEventListener('storage', syncToken);

    // also check when tab becomes active
    window.addEventListener('focus', syncToken);

    return () => {
      window.removeEventListener('storage', syncToken);
      window.removeEventListener('focus', syncToken);
    };
  }, []);

  const isAuth = !!token;

  return (
    <div className="
      min-h-screen
      bg-gradient-to-br
      from-slate-950
      via-slate-900
      to-indigo-950
      text-slate-900
    ">

      <Routes>

        {/* pages with navbar + layout */}
        <Route element={<MainLayout />}>


          <Route
            path="/dashboard"
            element={
              isAuth
                ? <DashboardPage />
                : <Navigate to="/login" replace />
            }
          />

          <Route
            path="/upload"
            element={
              isAuth
                ? <UploadResumePage />
                : <Navigate to="/login" replace />
            }
          />

          <Route
            path="/reports"
            element={
              isAuth
                ? <ReportsDashboard />
                : <Navigate to="/login" replace />
            }
          />

          <Route
            path="/report/:id"
            element={
              isAuth
                ? <ReportPage />
                : <Navigate to="/login" replace />
            }
          />

        </Route>

        {/* auth routes */}
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />

        {/* fallback */}
        <Route
          path="*"
          element={
            <Navigate
              to={isAuth ? "/dashboard" : "/login"}
              replace
            />
          }
        />

      </Routes>
    </div>
  );
};

export default App;