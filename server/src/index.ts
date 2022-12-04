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
let clientSocket;

const httpServer = createServer(app);
const controllerServer = new Server(httpServer, {
    cors: {
        origin: ["*","http://localhost:5173","https://lampinas.vercel.app"],

    },
    transports: ['websocket', 'polling'],
    allowEIO3: true
});
const clientServer = new Server(httpServer, {
    cors: {
        origin: ["*","http://localhost:5173","https://lampinas.vercel.app"],
    },
    transports: ['websocket', 'polling'],
    allowEIO3: true,
    path: "/client"
});
let sendTOVis;
let sendToController;
controllerServer.on("connection", (socket) => {
    console.log("connection")

    socket.on("lightUpdate", async (data)=>{
        sendTOVis(data);
    })
    sendToController= ((data)=>{
        socket.emit("lightControll", data)
    })
})
clientServer.on("connection", (socket) => {
    console.log("connectionClient")
    sendTOVis = ((data) => {
        socket.emit("lightUpdate", data)
    })
    socket.on("lightControll", async (data)=>{
        try{
            sendToController(data)
        }
        catch (e){
            console.log(e)
            //sendMessage("kontrolieris nav pievienojies")
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

controllerServer.listen(3000);
clientServer.listen(4000);