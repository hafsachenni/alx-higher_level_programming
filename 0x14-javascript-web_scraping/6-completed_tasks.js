ii/usr/bin/node
// script that computes the num of tasks completed by user
const request = require('request');
const url = process.argv[2];
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  // convert body to json format
  const todos = JSON.parse(body);

  // creation of object to store count of completed tasks
  const completedTasks = {};

  // iterating through each task
  for (const task of todos) {
    if (task.completed) {
      // if count already exists it takes current count
      // if not, it uses 0 as default value, and increments count by 1
      completedTasks[task.userId] = (completedTasks[task.userId] || 0) + 1;
    }
  }

  console.log(completedTasks);
}
);
