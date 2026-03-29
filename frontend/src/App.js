import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Home from "./pages/Home";
import Watch from "./pages/Watch";
import Login from "./pages/Login";

function App() {
  const token = localStorage.getItem("token");

  return (
    <BrowserRouter>
      <Routes>
        {/* LOGIN */}
        <Route
          path="/"
          element={token ? <Navigate to="/home" /> : <Login />}
        />

        {/* HOME */}
        <Route
          path="/home"
          element={token ? <Home /> : <Navigate to="/" />}
        />

        {/* WATCH */}
        <Route
          path="/watch/:id"
          element={token ? <Watch /> : <Navigate to="/" />}
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;