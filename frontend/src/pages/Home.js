import React, { useEffect, useState } from "react";
import api from "../services/api";

function Home() {
    const [data, setData] = useState({});

    useEffect(() => {
      api.get("home/").then((response) => {
        setData(response.data);
    });
}, []);

    return (
        <div>
        {Object.keys(data).map((category) => (
            <div key={category}>
                <h2>{category}</h2>

                <div style={{ display: "flex", overflowX: "scroll"}}>
                    {data[category].map((movie) => (
                        <img
                        key={movie.id}
                        src={movie.thumbnail}
                        alt={movie.title}
                        width="200"
                        />
                    ))}
                </div>
            </div>
        ))}
    </div>
    );
}

export default Home;