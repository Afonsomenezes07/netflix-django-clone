import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";
import "./Login.css";

function Login() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const navigate = useNavigate();

    const handleLogin = async () => {
        try {
            const response = await api.post("auth/token/", {
                username,
                password,
            });

        localStorage.setItem("token", response.data.access);
        window.location.href = "/home";
        } catch (err) {
            setError("Invalid username or password.");
        }
    };

    return (
        <div className="login-page">
            <div className="login-box">
                <h1 className="login-title">StreamVault</h1>
                <h2 className="login-subtitle">Sign in</h2>

                {error && <p className="login-error">{error}</p>}

                <input
                    className="login-input"
                    placeholder="Username"
                    onChange={(e) => setUsername(e.target.value)}
                />

                <input
                    className="login-input"
                    type="password"
                    placeholder="Password"
                    onChange={(e) => setPassword(e.target.value)}
                />

                <button className="login-button" onClick={handleLogin}>Sign in</button>

                <p className="login-switch">
                    Don't have an account?{" "}
                    <span onClick={() => navigate("/register")}>Sign up</span>
                </p>
            </div>
        </div>
    );
}

export default Login;