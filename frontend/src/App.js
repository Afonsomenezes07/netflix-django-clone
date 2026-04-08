import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Home from "./pages/Home";
import Watch from "./pages/Watch";
import Login from "./pages/Login";
import PrivateRoute from "./components/PrivateRoute";
import Register from "./pages/Register";

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
          element={
            <PrivateRoute>
              <Home />
            </PrivateRoute>
          }
        />

        {/* WATCH */}
        <Route
          path="/watch/:id"
          element={
            <PrivateRoute>
              <Watch />
            </PrivateRoute>
          }
        />
        <Route
          path="/register"
          element={
          <Register />
          }
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;