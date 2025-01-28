import React, { useState } from "react";
import Authinput from "./input";
import Button from "./button";

const Register = ({ onSignIn }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const OnRegister = () => {
    if (password !== confirmPassword) {
      alert("Passwords do not match");
      return;
    }
    const accountsData = localStorage.getItem("accounts");
    const accounts = JSON.parse(accountsData) || [];
    const newAccount = { email, password };
    if (accounts.some((acc) => acc.email === email)) {
      alert("Email already exists");
      return;
    } else {
      accounts.push(newAccount);
      localStorage.setItem("accounts", JSON.stringify(accounts));
      alert("Account created successfully");
      setEmail("");
      setPassword("");
      setConfirmPassword("");
      onSignIn();
    }
  };
  return (
    <div>
      <Authinput
        label="EMAIL"
        value={email}
        onchange={(text) => setEmail(text)}
      />
      <Authinput
        label="PASSWORD"
        type="password"
        value={password}
        onchange={(text) => setPassword(text)}
      />
      <Authinput
        label="CONFIRM PASSWORD"
        type="password"
        value={confirmPassword}
        onchange={(text) => setConfirmPassword(text)}
      />
      <Button text={"SIGN UP"} onClick={OnRegister} />
    </div>
  );
};

export default Register;
