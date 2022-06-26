const mongoose = require("mongoose");
const bcrypt = require("bcrypt");

const UserSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  username: {
    type: String,
    required: true,
    unique: true,
  },
  password: {
    type: String,
    required: true,
  },
  email: {
    type: String,
    required: true,
    unique: true,
  },
  role: {
    type: String,
    required: true,
  },
  hosting: [String],
  subscribed: [String],
});

UserSchema.pre("save", async function (next) {
  const user = this;
  const hashedPassword = await bcrypt.hash(this.password, 10);

  this.password = hashedPassword;
});

UserSchema.methods.isValidPassword = async function (input, hash) {
  const compare = await bcrypt.compare(input, hash);

  return compare;
};

module.exports = mongoose.model("User", UserSchema);
