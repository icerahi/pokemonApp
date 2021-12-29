import React, { useEffect, useState } from "react";
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import "./Login.css";
import axios from "axios";
import jwt_decode from "jwt-decode";
import useAuth from "../../hooks/useAuth";
import jwtDecode from "jwt-decode";
import notify from "../../utils/notify";
import { domain } from "../../.env";
import Loader from "../../components/loader/Loader";

const Login = () => {
  const [isLogin, setIsLogin] = useState(true);
  const[isLoading,setIsLoading]=useState(false)
  const{user,setUser} = useAuth()
   const navigate = useNavigate();
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm();

  const loginSubmit = (data) => {
    setIsLoading(true)

    axios
      .post(`${domain}/login`,data)
      .then((res) => {
        const token = res?.data?.access_token;
        localStorage.setItem("token", token);
        const decoded_token = jwtDecode(token);
       
        setUser(decoded_token);
        notify("You have been logged In!", "success");

        navigate("/");
      })
      .catch((error) =>
        notify(
          "Login fail !!! Please use correct username and password",
          "error"
        )
      )
      .finally(()=> setIsLoading(false))
  };

  const registerSubmit = (data) => {
    setIsLoading(true)
    if (data.password !== data.password2) {
      notify("Password not match!!", "error");
      return;
    }
    delete data.password2
    axios
      .post(`${domain}/signup`, data)
      .then((res) => {
      
  
        notify(
          "You have been registered Successfully, Please Login now!",
          "success"
        );
        setIsLogin(true);
         
      })
      .catch((error) =>{
        if (error.response.status==409){
          notify(
            "User already exists!",
            "error"
          );
        }
      })
      .finally(()=> setIsLoading(false))
  };

  const toggleLogin = () => {
    setIsLogin(true);
  };
  const toggleRegister = () => {
    setIsLogin(false);
  };

  return (
    <div className="container">
      {isLoading && <Loader/>}
      <div className="col-md-6 mx-auto  my-5 p-5">
        <h4 className="text-center">{isLogin ? "Login" : "Register"}</h4>
    <hr/>
         <form onSubmit={handleSubmit(isLogin ? loginSubmit : registerSubmit)}>
          {/* register your input into the hook by invoking the "register" function */}
          <div className="w-75  mx-auto  m-2">
            <input
              type="text"
              placeholder={`${isLogin?'username or email':'username'}`}
              className="form-control"
              defaultValue=""
              {...register("username", { required: true })}
            />
          </div>
          {!isLogin && (
            <div className="w-75  mx-auto  m-2">
              <input
                type="text"
                placeholder="Email"
                className="form-control"
                defaultValue=""
                {...register("email", { required: true })}
              />
            </div>
          )}
          {/* include validation with required or other standard HTML validation rules */}
          <div className="w-75  mx-auto py-2 m-2">
            <input
              type="password"
              placeholder="Your Password"
              className="form-control"
              {...register("password", { required: true })}
            />
          </div>

          {!isLogin && (
            <div className="w-75  mx-auto py-2 m-2">
              <input
                type="password"
                placeholder="Confirm Password"
                className="form-control"
                {...register("password2", { required: true })}
              />
            </div>
          )}
          {/* errors will return when field validation fails  */}
          {errors.exampleRequired && <span>This field is required</span>}
          <input
            className="btn btn-success d-block w-50 mx-auto fw-bolder py-2"
            type="submit"
            value={isLogin ? `Login` : "Register"}
          />
        </form>
        {isLogin ? (
          <p className="text-center my-2 lead">
            Haven't any account?{" "}
            <button onClick={toggleRegister} className="loginRegisterBtn">
            Register Now 
             
            </button>{" "}
          </p>
        ) : (
          <p className="text-center my-2 lead">
            Already have an account?{" "}
            <button onClick={toggleLogin} className="loginRegisterBtn  ">
             Login 
            </button>{" "}
          </p>
        )}
      </div>
    </div>
  );
};

export default Login;
