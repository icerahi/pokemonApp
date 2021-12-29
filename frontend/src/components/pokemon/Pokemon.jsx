import axios from "axios";
import React, { useEffect, useState } from "react";
import { domain, token } from "../../.env";
import useData from "../../hooks/useData";
import notify from "../../utils/notify";
import "./Pokemon.css";
const Pokemon = ({ pokemon }) => {
  const {favouriteList,setFavouriteList} = useData()
  const {  name, sprites, types } = pokemon;
  const image = sprites?.other?.dream_world?.front_default
  const type = types[0].type.name

  const addToFavourite=async()=>{
    const data ={name,image,type}
    const res=await axios.post(`${domain}/add`,data,{
      headers:{Authorization:`Bearer ${localStorage.getItem('token')}`}
    })
    
    if (res.status==201){

      setFavouriteList([res.data,...favouriteList])
      notify(' Added Successfully!','success')
    }
    else{
      notify(' Something went wrong!','error')
    }
  }

  
  return (
    <div className="col">
      <div   className="card h-100 task-card glass">
 
        <button onClick={()=>addToFavourite()} className="add-to-fav bg-dark">
          <i className="fas fa-fav"></i> Add to Favourite
        </button>

        <div className="card-body text-center">
          <img className="img-fluid " src={image} alt={name} />
         <div>
           <p className="lead text-center">{name}</p>
           <small className="fw-light" >Type: {type}</small>
         </div>
        </div>
      </div>
    </div>
  );
};

export default Pokemon;
