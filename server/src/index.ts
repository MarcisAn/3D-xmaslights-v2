import {createServer} from "http";
import {Server, Socket} from "socket.io";
import telegramData from "../../telegram.json"
import * as https from "https";
import * as cron from 'node-cron';
import express from "express"

const app = express();

let controllerID = null;
let clientID = null;

let controllerSocket;
let clientSockets = [];

const httpServer = createServer(app);
const wsserver = new Server(httpServer, {
    cors: {
        origin: ["*","http://localhost:5173","https://lampinas.vercel.app/"],

    },
    transports: ['websocket', 'polling'],
    allowEIO3: true
});

wsserver.on("connection", (socket) => {
    console.log("connection")
    socket.on("connectioninfo", (data) =>{
        console.log(data)
        if(data = "client"){
            // @ts-ignore
            clientSockets.push(socket)
            if(controllerID == null){
                socket.emit("controllerStatus", 0)
            }
            else{
                socket.emit("controllerStatus", 1)
            }
        }
        if(data = "constroller"){
            //@ts-ignore
            controllerID = socket.id
            controllerSocket = socket
        }
    })
})

function sendMessage(text) {
    const url = "https://api.telegram.org/bot"+telegramData.key+"/sendMessage?chat_id="+telegramData.id+"&text="+text
    https.get(url)
}
//app.get("/status", (req,res) =>{
//    console.log("status")
//    res.send("hello world"+req.ip)
//})

wsserver.listen(3000);


//clientSocket.emit("lightdata", "cav")

//controllerServer.on("connection", (socket) => {
//    isControllerConnected = true
//    cron.schedule('* * * * *', () => {
//        sendMessage("kontrolieris nav sasniedzams no servera")
//        isControllerConnected = false
//    });
//    console.log("controller connected", socket.id)
//    socket.on("data", (data) => {
//        console.log(data)
//    });
//});
//
//clientServer.on("connection", (socket) => {
//    console.log("client connected", socket.id)
//    socket.emit("cav", "data")
//    socket.on("data", (data) => {
//        console.log(data)
//    });
//
//});
