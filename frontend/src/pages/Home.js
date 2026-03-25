import React, { useEffect, useState } from "react";
import api from "../services/api";
import { useNavigate } from "react-router-dom";

function Home() {
    const [data, setData] = useState({});
    const [continueWatching, setContinueWatching] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
      // Categorias (home)
      api.get("home/").then((response) => {
        setData(response.data);
    });

    // Continue Watching
    api.get("history/continue_watching/").then((res) => {
        setContinueWatching(res.data);
    });
}, []);

    const addToFavorites = async (movieId) => {
        try {
            await api.post("favorites/", { movie: movieId });
            alert("Adicionado à Minha Lista!");
        } catch (error) {
            alert("Erro ao adicionar favorito");
        }
    };

    return (
        <div>

        {/* 🔥 CONTINUAR ASSISTINDO */}
        <h2>Continuar Assistindo</h2>
        <div style={{ display: "flex", overflowX: "scroll" }}>
            {continueWatching.map((item) => (
                <div key={item.id} style={{ marginRight: "10px" }}>
                    <img
                        src={item.movie.thumbnail}
                        alt={item.movie.title}
                        width="200"
                        style={{ cursor: "pointer" }}
                        onClick={() => navigate(`/watch/${item.movie.id}`)}
                    />
                </div>
            ))}
        </div>

        {/* 🎬 CATEGORIAS */}
        {Object.keys(data).map((category) => (
            <div key={category}>
                <h2>{category}</h2>

                <div style={{ display: "flex", overflowX: "scroll"}}>
                    {data[category].map((movie) => (
                        <div key={movie.id} style={{ marginRight: "10px" }}>

                            {/* CLICAR PARA ASSISTIR */}
                            <img
                                src={movie.thumbnail}
                                alt={movie.title}
                                width="200"
                                style={{ cursor: "pointer" }}
                                onClick={() => navigate(`/watch/${movie.id}`)}
                            />

                            {/* BOTÃO FAVORITO */}
                            <button onClick={() => addToFavorites(movie.id)}>
                                + Minha Lista
                            </button>

                        </div>
                    ))}
                </div>
            </div>
        ))}
    </div>
    );
}

export default Home;