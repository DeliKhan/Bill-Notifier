import React, { useState, useEffect } from "react";
import axios from "axios";
import "./index.css";

function Name(){
    const [data, setdata] = useState({name:""});
    /*
    console.log("hi");
    axios({
        method: "GET",
        url:"/welcome",
      }).then((res) => console.log(res)).catch(err => console.log(err));
    //fetch("/welcome").then((res) => console.log(res));
    */
    useEffect(() => {fetch("/welcome").then((res) =>
        res.json().then((data) => {
            // Setting a data from api
            setdata({
                name: data.Name + " hi"
            });
        })
    );
    }, []);

    return <h1>{data.name}</h1>
}

export default Name;