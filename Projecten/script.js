import gradient from "gradient-string";
import chalkAnimation from "chalk-animation";
import figlet from "figlet";
import mongoose from "mongoose";

main().catch((err) => console.log(err));
async function main() {
  await mongoose.connect("mongodb://127.0.0.1:27017/test");
}

import { projectModel } from "./models/project.js";

const sleep = (ms = 100) => new Promise((r) => setTimeout(r, ms));
const welcome = async () => {
  const rainbowTitle = chalkAnimation.rainbow("\nHey there, I am Projecten!\n");
  await sleep();
  rainbowTitle.stop();
};

const createProject = (project) => {
  projectModel.create(project).then((project) => {
    figlet(`successfully created`, (err, data) => {
      console.log(gradient.pastel.multiline(data) + "\n");
    });
    mongoose.connection.close();
  });
};

const readProject = (projectName) => {
  const search = new RegExp(projectName, "i");
  projectModel.find({ projectName: search }).then((project) => {
    console.info(project);
    figlet(`${project.length} matches`, (err, data) => {
      console.log(gradient.pastel.multiline(data) + "\n");
    });
    mongoose.connection.close();
  });
};

const readChoice = (choice) => {
  const search = new RegExp(choice, "i");
  projectModel.find({ choice: search }).then((project) => {
    console.info(project);
    figlet(`${project.length} matches`, (err, data) => {
      console.log(gradient.pastel.multiline(data) + "\n");
    });
    mongoose.connection.close();
  });
};

const readAllProject = () => {
  projectModel.find().then((projects) => {
    console.info(projects);
    figlet(`${projects.length} tasks or issues`, (err, data) => {
      console.log(gradient.pastel.multiline(data) + "\n");
    });
    mongoose.connection.close();
  });
};

const updateProject = (_id, project) => {
  projectModel.updateOne({ _id }, project).then((project) => {
    figlet(`successfully updated`, (err, data) => {
      console.log(gradient.pastel.multiline(data) + "\n");
    });
    mongoose.connection.close();
  });
};

const deleteProject = (_id) => {
  projectModel.deleteOne({ _id }).then((project) => {
    figlet(`successfully deleted`, (err, data) => {
      console.log(gradient.pastel.multiline(data) + "\n");
    });
    mongoose.connection.close();
  });
};

const deleteAllProject = () => {
  projectModel.deleteMany().then(() => {
    figlet(`successfully deleted all`, (err, data) => {
      console.log(gradient.pastel.multiline(data) + "\n");
    });
    mongoose.connection.close();
  });
};

export {
  welcome,
  createProject,
  readProject,
  readChoice,
  readAllProject,
  updateProject,
  deleteProject,
  deleteAllProject,
};
