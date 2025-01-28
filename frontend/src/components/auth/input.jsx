import React from "react";
import "./styles.css";

const Authinput = ({ label, value, onchange, type = "text" }) => {
  return (
    <div className="inputItem">
      <label className="inputLabel">{label}</label>
      <input
        className="input"
        type={type}
        value={value}
        onChange={(e) => onchange(e.target.value)}
      />
    </div>
  );
};

export default Authinput;
