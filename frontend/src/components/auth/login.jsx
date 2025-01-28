import React, { useState } from "react";
import Authinput from "./input";
import Button from "./button";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const OnLogin = () => {
    const accountsData = localStorage.getItem("accounts");
    const accounts = JSON.parse(accountsData) || [];
    const foundAccount = accounts.find(
      (acc) => acc.email === email && acc.password === password
    );
    if (foundAccount) {
      alert("Logged in successfully");
      setEmail("");
      setPassword("");
      window.open("http://127.0.0.1:7860");
    } else {
      alert("Invalid credentials");
    }
  };
  return (
    <div>
      <Authinput
        label="EMAIL"
        value={email}
        onchange={(value) => setEmail(value)}
      />
      <Authinput
        label="PASSWORD"
        type="password"
        value={password}
        onchange={(value) => setPassword(value)}
      />
      <Button text={"SIGN IN"} onClick={OnLogin} />
    </div>
  );
};

export default Login;
