require("dotenv").config();
const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
const cookieParser = require("cookie-parser");

const connectDatabase = async () => {
  try {
    // mongoose.set("useNewUrlParser", true);
    await mongoose.connect(process.env.DB_URL);
    console.log("connected to database");
  } catch (e) {
    console.log(e);
    process.exit(1);
  }
};

connectDatabase();

const routes = require("./routes/routes");

app = express();

app.use(cookieParser());
app.use(express.json());
app.use(
  cors({
    credentials: true,
    origin: ["http://localhost:3000", "http://localhost:8080"],
    // origin: ["*"],
  })
);

app.use("/api", routes);

app.listen(8003);
