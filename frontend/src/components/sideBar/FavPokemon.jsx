import axios from "axios";
import React, { useEffect, useState } from "react";
import { domain, token } from "../../.env";
import useData from "../../hooks/useData";
import notify from "../../utils/notify";

const FavPokemon = ({ pokemon }) => {
  const { favouriteList, setFavouriteList } = useData();
  const { name, image, type, id } = pokemon;
   

  const removeFromFavourite = async () => {
    const res = await axios.delete(`${domain}/remove/${id}`, {
      headers: { Authorization: `Bearer ${localStorage.getItem("token")}` },
    });
   
    if (res.status == 204) {
        const resData = favouriteList.filter(pokemon => pokemon.id!=id)
        setFavouriteList(resData)
       notify(" Removed Successfully!", "success");
    } else {
      notify(" Something went wrong!", "error");
    }
  };

  return (
    <div className="col">
      <div className="card h-100 task-card glass">
        <button
          onClick={() => removeFromFavourite()}
          className="add-to-fav bg-dark"
        >
          <i className="fas fa-trash"></i> Remove
        </button>

        <div className="card-body text-center">
          <img className="img-fluid " src={image} alt={name} />
          <div>
            <p className="lead text-center">{name}</p>
            <small className="fw-light">Type: {type}</small>
          </div>
        </div>
      </div>
    </div>
  );
};

export default FavPokemon;
