import React, { useState, useEffect } from "react";

function Name(){
    const [data, setdata] = useState({name:""});
    useEffect(() => {fetch("/welcome").then((res) =>
        res.json().then((data) => {
            // Setting a data from api
            setdata({
                name: data.Name
            });
        })
    );
    }, []);

    return <h1>{data.name}</h1>
}