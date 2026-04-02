import React, { useEffect, useState } from "react";
import api from "../services/api";
import { useNavigate } from "react-router-dom";
import "./Home.css";

function Home() {
    const [data, setData] = useState({});
    const [continueWatching, setContinueWatching] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(false);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchData = async () => {
            try {
                const homeResponse = await api.get("home/");
                const historyResponse = await api.get("history/continue_watching/");
                setData(homeResponse.data);
                setContinueWatching(historyResponse.data);
            } catch (err) {
                console.error(err);
                setError(true);
            } finally {
                setLoading(false);
            }
        };
        fetchData();
    }, []);

    const addToFavorites = async (movieId) => {
        try {
            await api.post("favorites/", { movie: movieId });
            alert("Added to My List!");
        } catch (error) {
            alert("Error adding to favorites");
        }
    };

    if (loading) return <div className="home-loading">Loading...</div>;
    if (error) return <div className="home-error">Failed to load content.</div>;

    return (
        <div className="home-page">
            {/* NAVBAR */}
            <nav className="home-nav">
                <span className="home-nav-logo">StreamVault</span>
                <button className="home-nav-logout" onClick={() => {
                    localStorage.removeItem("token");
                    window.location.href = "/";
                }}>Logout</button>
            </nav>

            {/* CONTINUAR ASSISTINDO */}
            {continueWatching.length > 0 && (
                <section className="home-section">
                    <h2 className="home-section-title">Continue Watching</h2>
                    <div className="home-row">
                        {continueWatching.map((item) => (
                            <div key={item.id} className="home-card" onClick={() => navigate(`/watch/${item.movie.id}`)}>
                                <img src={item.movie.thumbnail} alt={item.movie.title} />
                                <div className="home-card-overlay">
                                    <span>▶ Play</span>
                                </div>
                            </div>
                        ))}
                    </div>
                </section>
            )}

            {/* CATEGORIAS */}
            {Object.keys(data).map((category) => (
                <section key={category} className="home-section">
                    <h2 className="home-section-title">{category}</h2>
                    <div className="home-row">
                        {data[category].map((movie) => (
                            <div key={movie.id} className="home-card">
                                <img
                                    src={movie.thumbnail}
                                    alt={movie.title}
                                    onClick={() => navigate(`/watch/${movie.id}`)}
                                />
                                <div className="home-card-overlay" onClick={() => navigate(`/watch/${movie.id}`)}>
                                    <span>▶ Play</span>
                                </div>
                                <button className="home-card-fav" onClick={() => addToFavorites(movie.id)}>
                                    + My List
                                </button>
                            </div>
                        ))}
                    </div>
                </section>
            ))}
        </div>
    );
}

export default Home;