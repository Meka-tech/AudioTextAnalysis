import React, { useState } from "react";
import "./styles.css";
import Login from "./login";
import Register from "./register";

const Auth = () => {
  const [activeState, setActiveState] = useState("login");
  return (
    <div className="main">
      <div className="mainheader">
        <div
          className="headerButton"
          onClick={() => {
            setActiveState("login");
          }}
          style={{
            borderBottom: activeState === "login" ? "2px solid white" : "none"
          }}
        >
          <h2>SIGN IN</h2>
        </div>
        <div
          className="headerButton"
          onClick={() => {
            setActiveState("signup");
          }}
          style={{
            borderBottom: activeState === "signup" ? "2px solid white" : "none"
          }}
        >
          <h2>SIGN UP</h2>
        </div>
      </div>
      <form className="body">
        {activeState === "login" ? (
          <Login />
        ) : (
          <Register
            onSignIn={() => {
              setActiveState("login");
            }}
          />
        )}
      </form>
    </div>
  );
};

export default Auth;
