// backend/controllers/taskController.js
const Task = require('../models/task');

exports.createTask = async (req, res) => {
    const { title, description } = req.body;
    try {
        const newTask = await Task.create({ title, description });
        res.status(201).json(newTask);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// Similar methods for getTasks, updateTask, and deleteTask
