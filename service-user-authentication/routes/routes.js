require("dotenv").config();
const router = require("express").Router();
const jwt = require("jsonwebtoken");

const User = require("../models/user");

// signup endpoint
router.post("/signup", async (req, res) => {
  try {
    let email = req.body.email;
    let username = req.body.username;

    let find = await User.findOne({ email });
    if (find)
      return res.status(400).send({ message: "Email already registered." });

    find = await User.findOne({ username });
    if (find)
      return res.status(400).send({ message: "Username already registered." });

    let createdDate = Date.now();

    const user = new User({
      name: req.body.name,
      email: req.body.email,
      username: req.body.username,
      password: req.body.password,
      role: req.body.role,
      createdDate: Date.now(),
    });

    const result = await user.save();
    const { password, ...data } = await result.toJSON();
    res.send(data);
  } catch (e) {
    console.log(e);
    res.status(500).send("Something went wrong");
  }
});

// login endpoint
router.post("/login", async (req, res) => {
  const user = await User.findOne({ username: req.body.username });

  if (!user) {
    return res.status(404).send({
      message: "User not found",
    });
  }

  if (!(await user.isValidPassword(req.body.password, user.password))) {
    return res.status(400).send({
      message: "Invalid password",
    });
  }

  const updatedLogin = await User.findOneAndUpdate(
    { username: req.body.username },
    { $set: { lastLoginDate: Date.now() } }
  );

  const token = jwt.sign(
    { _id: user._id, username: user.username, role: user.role },
    process.env.JWT_TOKEN_SECRET
  );

  res.cookie("jwt", token, {
    httpOnly: true,
    maxAge: 24 * 60 * 60 * 1000, // 1 day
  });

  res.send({
    message: "login success",
  });
});

// get current user info
router.get("/user", async (req, res) => {
  try {
    const cookie = req.cookies["jwt"];

    const claims = jwt.verify(cookie, process.env.JWT_TOKEN_SECRET);

    if (!claims) {
      return res.status(401).send({
        message: "unauthenticated",
      });
    }

    const user = await User.findOne({ username: claims.username });
    const { password, ...data } = await user.toJSON();

    res.send(data);
  } catch (e) {
    return res.status(401).send({
      message: "unauthenticated",
    });
  }
});

// get user by username
router.get("/user/:username", async (req, res) => {
  try {
    const cookie = req.cookies["jwt"];

    const claims = jwt.verify(cookie, process.env.JWT_TOKEN_SECRET);

    if (!claims) {
      return res.status(401).send({
        message: "unauthenticated",
      });
    }

    const user = await User.findOne({ username: req.params.username });

    if (!user) {
      return res.status(404).send({
        message: "user not found",
      });
    }

    const { password, ...data } = await user.toJSON();
    res.send(data);
  } catch (e) {
    return res.status(401).send({
      message: "unauthenticated",
    });
  }
});

// logout endpoint
router.post("/logout", (req, res) => {
  res.cookie("jwt", "", { maxAge: 0 });

  res.send();
});

// get useres (for admin role)
router.get("/users", async (req, res) => {
  let data;
  if (req.query.role) {
    const users = await User.find(
      { role: req.query.role },
      { username: 1, role: 1, hosting: 1, subscribed: 1, lastLoginDate: 1 }
    );

    if (!users) {
      return res.status(404).send({
        message: "users not found",
      });
    }

    const data = await users;
    res.send(data);
  } else {
    const users = await User.find(
      {},
      { username: 1, role: 1, hosting: 1, subscribed: 1, lastLoginDate: 1 }
    );

    if (!users) {
      return res.status(404).send({
        message: "users not found",
      });
    }

    const data = await users;
    res.send(data);
  }
  res.send(data);
});

// add hosted monitoring
router.put("/host-add", async (req, res) => {
  try {
    const cookie = req.cookies["jwt"];

    const claims = jwt.verify(cookie, process.env.JWT_TOKEN_SECRET);

    if (!claims) {
      return res.status(401).send({
        message: "unauthenticated",
      });
    }

    if (claims.role == "pasien") {
      return res.status(403).send({
        message: "forbidden",
      });
    }

    const user = await User.findOneAndUpdate(
      { username: claims.username },
      {
        $addToSet: {
          hosting: req.body.code,
        },
      }
    );

    updateduser = await User.findOne({ username: claims.username });

    const { username, hosting, ...data } = await updateduser.toJSON();

    res.send({
      username: username,
      hosting: hosting,
    });
  } catch (e) {
    return res.status(401).send({
      message: "unauthenticated",
    });
  }
});

// remove hosted monitoring
router.put("/host-pull", async (req, res) => {
  try {
    const cookie = req.cookies["jwt"];

    const claims = jwt.verify(cookie, process.env.JWT_TOKEN_SECRET);

    if (!claims) {
      return res.status(401).send({
        message: "unauthenticated",
      });
    }

    if (claims.role == "pasien") {
      return res.status(403).send({
        message: "forbidden",
      });
    }

    const user = await User.findOneAndUpdate(
      { username: claims.username },
      {
        $pull: {
          hosting: req.body.code,
        },
      }
    );

    updateduser = await User.findOne({ username: claims.username });

    const { username, hosting, ...data } = await updateduser.toJSON();

    res.send({
      username: username,
      hosting: hosting,
    });
  } catch (e) {
    return res.status(401).send({
      message: "unauthenticated",
    });
  }
});

// get subscribe monitoring
router.get("/subs-list", async (req, res) => {
  try {
    const user = await User.findOne({ username: req.body.uname });

    const { username, subscribed, ...data } = await user.toJSON();

    res.send({
      username: username,
      subscribed: subscribed,
    });
  } catch (e) {
    console.log(e);
    return res.send({
      message: "unauthenticated",
    });
  }
});

// add subscribe monitoring
router.put("/subs-add", async (req, res) => {
  try {
    // const cookie = req.cookies["jwt"];

    // const claims = jwt.verify(cookie, process.env.JWT_TOKEN_SECRET);

    // if (!claims) {
    //   return res.status(401).send({
    //     message: "unauthenticated",
    //   });
    // }

    // if (claims.role == "dokter") {
    //   return res.status(403).send({
    //     message: "forbidden",
    //   });
    // }

    const user = await User.findOneAndUpdate(
      { username: req.body.uname },
      {
        $addToSet: {
          subscribed: req.body.code,
        },
      }
    );

    updateduser = await User.findOne({ username: req.body.uname });

    const { username, subscribed, ...data } = await updateduser.toJSON();

    res.send({
      username: username,
      subscribed: subscribed,
    });
  } catch (e) {
    console.log(e);
    return res.send({
      message: "unauthenticated",
    });
  }
});

// remove subscribed monitoring
router.put("/subs-pull", async (req, res) => {
  try {
    // const cookie = req.cookies["jwt"];

    // const claims = jwt.verify(cookie, process.env.JWT_TOKEN_SECRET);

    // if (!claims) {
    //   return res.status(401).send({
    //     message: "unauthenticated",
    //   });
    // }

    // if (claims.role == "dokter") {
    //   return res.status(403).send({
    //     message: "forbidden",
    //   });
    // }

    const user = await User.findOneAndUpdate(
      { username: req.body.uname },
      {
        $pull: {
          subscribed: req.body.code,
        },
      }
    );

    updateduser = await User.findOne({ username: req.body.uname });

    const { username, subscribed, ...data } = await updateduser.toJSON();

    res.send({
      username: username,
      subscribed: subscribed,
    });
  } catch (e) {
    return res.status(401).send({
      message: "unauthenticated",
    });
  }
});

// remove all occurences of monitoring in subscribed (when a doctor's account deleted a monitoring form)
router.put("/subs-pull-all", async (req, res) => {
  try {
    // console.log(req.headers);
    const user = await User.updateMany(
      {},
      {
        $pull: {
          subscribed: req.body.code,
        },
      }
    );
    res.send({
      message:
        "Monitoring with code " + req.body.code + " successfully deleted.",
    });
  } catch (e) {
    console.log(e);
    res.send({
      message: "Error",
    });
  }
});

module.exports = router;
