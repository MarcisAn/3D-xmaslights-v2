import {createServer} from "http";
import {Server, Socket} from "socket.io";
import telegramData from "../../telegram.json"
import * as https from "https";
import * as cron from 'node-cron';
import express from "express"
import cors from "cors";

const app = express();

function sendMessage(text) {
    const url = "https://api.telegram.org/bot"+telegramData.key+"/sendMessage?chat_id="+telegramData.id+"&text="+text
    https.get(url)
}

let currentAnim = "axis"
app.use(cors())
app.get("/currentAnim", (_req, res) =>{
    res.send(JSON.stringify({anim: currentAnim}))
})

app.post("/setAnim", (req,res) =>{
    currentAnim = req.params.anim
    res.send(JSON.stringify({anim: currentAnim}))
})
app.listen(3000)