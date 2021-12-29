import React from "react";

const Loader = () => {
  return (
    <div className="d-flex mx-auto justify-content-center gx-5 align-item-center">
      <div className="spinner-grow m-2" role="status">
        <span className="visually-hidden">Loading...</span>
      </div>{" "}
      <div className="spinner-grow m-2" role="status">
        <span className="visually-hidden">Loading...</span>
      </div>{" "}
      <div className="spinner-grow m-2" role="status">
        <span className="visually-hidden">Loading...</span>
      </div>
    </div>
  );
};

export default Loader;
