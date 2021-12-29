import "./App.css";
import Header from "./components/header/Header";
import { useEffect } from "react";
import Home from "./pages/home/Home";
import { Routes, Route, BrowserRouter } from "react-router-dom";
import Login from "./pages/login/Login";
import PrivateRoute from "./routes/PrivateRoute";
import useAuth from "./hooks/useAuth";
import { domain } from "./.env";
import useData from "./hooks/useData";
import axios from "axios";

import "react-toastify/dist/ReactToastify.css";
import { toast } from "react-toastify";

toast.configure();

const App = () => {

  const{user} = useAuth();
  const{setFavouriteList}=useData();

  useEffect(()=>{
    const getData = async()=>{
      const res = await axios.get(`${domain}/favourite_list`,{
        headers:{Authorization:`Bearer ${localStorage.getItem('token')}`}
      })
      if (res.status==200){
        setFavouriteList(res.data)
      }
    }
    getData()
  },[user])
 
  return (
    <div>
      <BrowserRouter>
        <Header />
        <Routes>
          <Route
            path="/"
            element={
              <PrivateRoute>
                <Home />
              </PrivateRoute>
            }
          />
          <Route path="/login" element={<Login />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
};

export default App;
