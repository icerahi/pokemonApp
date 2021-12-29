import React, { useEffect, useState } from "react";
import Pokemon from "../pokemon/Pokemon";
import Home from "../../pages/home/Home";
import "./SideBar.css";
import axios from "axios";
import { domain } from "../../.env";
import useData from "../../hooks/useData";
import FavPokemon from "./FavPokemon";
const SideBar = ({ handleCloseSideBar }) => {
  const {favouriteList} = useData()

  return (
    <aside className="">
      <div className="p-3 mb-2 border-bottom d-flex justify-center-center align-items-center sticky-top bg-white">
        <button
          className="border-2 border-dark me-2 rounded-circle p-2 fw-bolder px-3 text-center bg-dark text-white"
          onClick={handleCloseSideBar}
        >
          X
        </button>
        <h5 className="fw-bolder">Your Favourites</h5>
      </div>

      <div className="row row-cols-2 g-4 p-2">
        {favouriteList.map((pokemon, index) => (
          <FavPokemon key={index} pokemon={pokemon} />
        ))}
      </div>
      {favouriteList.length ===0&& <p className="text-center text-secondary">No Pokemon added in favourite list yet !!</p> }
    </aside>
  );
};

export default SideBar;
