import React, { useEffect, useState } from "react";
import api from "../services/api";
import { useParams } from "react-router-dom";

function Watch() {
    const { id } = useParams();
    const [movie, setMovie] = useState(null);

    useEffect(() => {
        api.get(`watch/${id}/`).then((response) => {
            setMovie(response.data);
        });
    }, [id]);

    if (!movie) return <div>Loading...</div>;

    return (
        <div>
            <h1>{movie.title}</h1>

            <video width="800" controls>
                <source src={movie.video} type="video/mp4" />
            </video>
        </div>
    );
}

export default Watch;