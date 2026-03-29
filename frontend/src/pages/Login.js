import React, { useState } from "react";
import api from "../services/api";

function Login() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleLogin = async () => {
        const response = await api.post("auth/token/", {
            username,
            password,
        });

        localStorage.setItem("token", response.data.access);

        window.location.href = "/";
    };

    return (
        <div>
            <h1>Login</h1>

            <input
            placeholder="Username"
            onChange={(e) => setUsername(e.target.value)}
            />

            <input
            type="password"
            placeholder="Password"
            onChange={(e) => setPassword(e.target.value)}
            />

            <button onClick={handleLogin}>Entrar</button>
        </div>
    );
}

export default Login;