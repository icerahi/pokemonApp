import React, { createContext, useState } from "react";

const PokemonState = () => {
  const [favouriteList, setFavouriteList] = useState([]);


  return { favouriteList, setFavouriteList, };
};

export const DataContext = createContext();

const DataProvider = ({ children }) => {
  const contextData = PokemonState();
  return (
    <DataContext.Provider value={contextData}>
      {children}
    </DataContext.Provider>
  );
};

export default DataProvider;
