#!/usr/bin/env node
import { program } from "commander";
import inquirer from "inquirer";
import chalk from "chalk";
import gradient from "gradient-string";

const prompt = inquirer.createPromptModule();

import {
  welcome,
  createProject,
  readProject,
  readChoice,
  readAllProject,
  updateProject,
  deleteProject,
  deleteAllProject,
} from "./script.js";

program
  .version(`${chalk.bgCyan("1.0.3")}`)
  .description(gradient.rainbow(`Project_Management_CLI`));

const questions = [
  {
    type: "input",
    name: "projectName",
    message: `What is the name of the ${chalk.bgCyan("PROJECT")}?`,
  },
  {
    type: "input",
    name: "employee",
    message: `Which ${chalk.bgRed("EMPLOYEE")} has been assigned?`,
  },
  {
    type: "list",
    name: "choice",
    message: `What is the ${chalk.bgGreen("TYPE")}? `,
    choices: ["", "Task", "Issue"],
  },
  {
    type: "input",
    name: "taskOrIssueName",
    message: `What is the ${chalk.bgBlue("TASK or ISSUE")}? `,
  },
  {
    type: "input",
    name: "description",
    message: `What is the ${chalk.bgRedBright("DESCRIPTION")}? `,
  },
  {
    type: "list",
    name: "language",
    message: `Which ${chalk.bgBlueBright("LANGUAGE")} is required to solve this? `,
    choices: [
      "",
      "Javascript",
      "Python",
      "C++",
      "Java",
      "HTML",
      "CSS",
      "Typescript",
      "Swift",
      "Kotlin",
      "C#",
      "Go",
      "Rust",
      "Bash",
      "SQL",
      "NoSQL",
      "Matlab",
      "PHP",
    ],
  },
  {
    type: "input",
    name: "githubLink",
    message: `What is the ${chalk.bgYellow("GITHUB LINK")}?`,
  },
  {
    type: "input",
    name: "assignDate",
    message: `What is ${chalk.bgRedBright(
      "ASSIGNED DATE"
    )} for the task or issue? `,
  },
  {
    type: "input",
    name: "deadline",
    message: `What is ${chalk.bgYellowBright("Dealine")}? `,
  },
];

program
  .command("create")
  .alias("c")
  .description(`${chalk.bgYellow("Create a task or issue")}`)
  .action(async () => {
    await welcome();
    prompt(questions).then((answers) => createProject(answers));
  });

program
  .command("read <projectName>")
  .alias("r")
  .description(`${chalk.bgBlue("Read a task or issue")}`)
  .action(async (projectName) => {
    await welcome();
    readProject(projectName);
  });

program
  .command("readChoice <choice>")
  .alias("rc")
  .description(`${chalk.bgBlue("Read a choice")}`)
  .action(async (choice) => {
    await welcome();
    readChoice(choice);
  });

program
  .command("readAll ")
  .alias("ra")
  .description(`${chalk.bgBlueBright("Read all tasks or issues")}`)
  .action(async () => {
    await welcome();
    readAllProject();
  });

program
  .command("update <_id>")
  .alias("u")
  .description(`${chalk.bgGreen("Update a task or issue")}`)
  .action(async (_id) => {
    await welcome();
    prompt(questions).then((answers) => updateProject(_id, answers));
  });

program
  .command("delete <_id>")
  .alias("d")
  .description(`${chalk.bgRed("Delete a task or issue")}`)
  .action(async (_id) => {
    await welcome();
    deleteProject(_id);
  });

program
  .command("deleteAll")
  .alias("da")
  .description(`${chalk.bgRedBright("Delete all tasks or issues")}`)
  .action(async () => {
    await welcome();
    deleteAllProject();
  });

program.parse(process.argv);
