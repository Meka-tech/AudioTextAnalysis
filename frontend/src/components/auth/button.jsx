import React from "react";
import "./styles.css";

const Button = ({ text, onClick }) => {
  return (
    <div className="btn" onClick={onClick}>
      {text}
    </div>
  );
};

export default Button;
