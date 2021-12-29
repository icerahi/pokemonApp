import React, { useEffect } from "react";
import { Navigate } from "react-router-dom";
import { token } from "../.env";
import Loader from "../components/loader/Loader";
import useAuth from "../hooks/useAuth";
import jwtDecode from "jwt-decode";
const PrivateRoute = ({ children }) => {
  const { user, setUser, isLoading, setIsLoading } = useAuth();
 

  if (isLoading) {
    return <Loader />;
  }

  return user ? children : <Navigate to="/login" />;
};

export default PrivateRoute;
