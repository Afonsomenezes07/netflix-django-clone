import React, { useState } from "react";
import api from "../services/api";
import { useNavigate } from "react-router-dom";
import "./Login.css"; // reutiliza o mesmo CSS

function Register() {
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [success, setSuccess] = useState("");
    const navigate = useNavigate();

    const handleRegister = async () => {
        setError("");
        setSuccess("");

        if (!username || !password) {
            setError("Username and password are required.");
            return;
        }

        try {
            await api.post("auth/register/", { username, email, password });
            setSuccess("Account created! Redirecting to login...");
            setTimeout(() => navigate("/"), 2000);
        } catch (err) {
            setError(err.response?.data?.error || "Error creating account.");
        }
    };

    return (
        <div className="login-page">
            <div className="login-box">
                <h1 className="login-title">StreamVault</h1>
                <h2 className="login-subtitle">Create Account</h2>

                {error && <p className="login-error">{error}</p>}
                {success && <p className="login-success">{success}</p>}

                <input
                    className="login-input"
                    placeholder="Username"
                    onChange={(e) => setUsername(e.target.value)}
                />
                <input
                    className="login-input"
                    placeholder="Email (optional)"
                    onChange={(e) => setEmail(e.target.value)}
                />
                <input
                    className="login-input"
                    type="password"
                    placeholder="Password"
                    onChange={(e) => setPassword(e.target.value)}
                />
                <button className="login-button" onClick={handleRegister}>
                    Create Account
                </button>

                <p className="login-switch">
                    Already have an account?{" "}
                    <span onClick={() => navigate("/")}>Sign in</span>
                </p>
            </div>
        </div>
    );
}

export default Register;