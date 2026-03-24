import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Home from "./pages/Home";
import Watch from "./pages/Watch";
import Login from "./pages/Login";

function App() {
  const token = localStorage.getItem("token");

  return (
    <BrowserRouter>
      <Routes>
        {/* Se NÃO estiver logado */}
        {!token && (
          <>
          <Route path="/" element={<Login />} />
          <Route path="*" element={<Navigate to="/" />} />
          </>
        )}

        {/* Se estiver logado */}
        {token && (
          <>
            <Route path="/" element={<Home />} />
            <Route path="/watch/:id" element={<Watch />} />
            <Route path="*" element={<Navigate to="/"/>} />
          </>
        )}
      </Routes>
    </BrowserRouter>
  );
}

export default App;
