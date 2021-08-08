import React from "react";
import { useState } from "react";
import axios from "axios";

const Main = () => {
  const [source, setSource] = useState(
    "https://img.icons8.com/clouds/100/000000/upload.png"
  );

  const postData = (files) => {
    let form = new FormData();
    console.log("HI I am noth that coll");
    form.append("file", files[0]);
    console.log(form);
    console.log(files);
    axios.post("http://127.0.0.1:5000/upload", form, {
      headers: {
        "content-type": "multipart/form-data", // do not forget this
      },
    });
    setInterval(() => {
      setSource("http://127.0.0.1:5000/detcted_image/facedetect.jpg");
    }, 8000);
  };
  const dragover = (evt) => {
    evt.preventDefault();
    evt.stopPropagation();
    evt.dataTransfer.dropEffect = "copy";
  };
  const ondrop = (evt) => {
    evt.preventDefault();
    evt.stopPropagation();
    console.log("evt Triggerd");
    const files = evt.dataTransfer.files;
    console.log(evt.dataTransfer);
    console.log(files);
    postData(files);
  };

  return (
    <>
      <div
        className="container"
        onDragOver={(evt) => dragover(evt)}
        onDrop={(evt) => ondrop(evt)}
      >
        <div className="header">
          <h3>UPLOAD</h3>
          <i className="fas fa-times-circle" />
        </div>
        <div className="show-img main-img">
          <img src={`${source}`} alt="upload.png" />
        </div>
        <input type="file" name="file" className="custom-file-input" />
      </div>
    </>
  );
};
export default Main;
