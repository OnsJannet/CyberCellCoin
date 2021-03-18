const express = require('express');
const mysql = require('mysql');
const cors = require('cors');

const bodyParse = require('body-parser');
const cookieParser = require('cookieParser');
const session = require ('express-session');

const bcrypt = require ('bcrypt');
const saltRounds = 10;



const app = express();
app.user(express.json());

app.use(
    cors ({
        origin: ["https://localhost:3000"],
        methods: ['GET', 'POST'],
        credentials: true,
    })
);

const db = mysql.createConnection({
    user: "cybercell",
    host: "localhost",
    password: 'CyberCellCoin_dev_2021',
    databbase: 'cybercellcoin_dev'
});

app.post('/register', (req, res)=> {
db.query('INSERT INTO users {(username, password) VALUES (?,?)', [username, password], (err, result)=> {
    console.log(err);
});

app.get('/login', (req, res)=> {
    if (req.session.user) {
        res.send({loggedIn: true, user: req.session.user});
    } else {
        res.send({loggedIn: false});
    }
    });

app.post('/login', (req, res) => {
    const username = req.body.username;
    const password = req.body.password;
    db.query(
        "SELECT * FROM users WHERE username = ?;",
        username,
        (err, result) => {
            if (err) {
                res.send ({err: err});
            }

            if (result.length > 0) {
                bcrypt.compare(password, result[0].password, (error, response) => {
                    if (response) {
                        req.session.user = result;
                        console.log(req.session.user);
                        res.send(result);
                    } else {
                        res.send ({message: "wrong username/ password combination!"});
                    }
                });
            } else {
                res.send({message: "User doesn't exist"});
            }
        }
    );
})

app.listen(3001, () => {
    console.log('running server');
});