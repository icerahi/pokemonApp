import axios from "axios";
import React, { useEffect, useState } from "react";
import { useForm } from "react-hook-form";
import { domain, token } from "../../.env";
import Loader from "../../components/loader/Loader";
import SideBar from "../../components/sideBar/SideBar";
import Pokemon from "../../components/pokemon/Pokemon";
import useAuth from "../../hooks/useAuth";
import useData from "../../hooks/useData";
import notify from "../../utils/notify";
import "./home.css";

const Home = () => {
  const [allPokemons, setAllPokemons] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  const [sideBar, setSideBar] = useState(false);
  const {favouriteList} = useData()

  const [loadMore, setLoadMore] = useState(
    "https://pokeapi.co/api/v2/pokemon?limit=20"
  );

  const getAllPokemons = async () => {
    const res = await fetch(loadMore);
    const data = await res.json();

    setLoadMore(data.next);

    function createPokemonObject(results) {
      results.forEach(async (pokemon) => {
        const res = await fetch(
          `https://pokeapi.co/api/v2/pokemon/${pokemon.name}`
        );
        const data = await res.json();
        setAllPokemons((currentList) => [...currentList, data]);
        setIsLoading(false)
      });
    }
    createPokemonObject(data.results);
  };



  const handleCloseSideBar = (e) => {
    sideBar && setSideBar(false);
  };

  useEffect(() => {
    getAllPokemons();
  }, []);

  if (isLoading) {
    return <Loader />;
  }

  return (
    <div className="container">
      <div className="row row-cols-1 row-cols-md-4 g-4 my-4">
        {allPokemons?.map((pokemon, index) => (
          <Pokemon key={index} pokemon={pokemon} />
        ))}
      </div>

      <button
        onClick={() => getAllPokemons()}
        className="btn btn-default py-2 px-4 d-block mx-auto "
      >
        Load More
      </button>

      <div onClick={handleCloseSideBar} className="container-fluid">
        <a
          onClick={() => setSideBar(true)}
          id="my-done"
          className="text-decoration-none fw-bolder"
        >
          My Favourite <sup>{favouriteList.length}</sup>{" "}
        </a>
      </div>
      {sideBar && <SideBar handleCloseSideBar={handleCloseSideBar} />}
    </div>
  );
};

export default Home;
