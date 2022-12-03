<script>
    import io from 'socket.io-client'
    import {onMount} from 'svelte';
    import {createScene, renderVis} from '../lib/scene.ts';
    import "../global.scss"
    import {dev} from '$app/environment';
    import {lightData} from "../lib/state.ts";

    //const socket = io("http://localhost:3000", {autoConnect: false})
    let socket;
    if (dev) {
        socket = io("ws://localhost:4000", {autoConnect: false})
    } else {
        socket = io("wss://lampinas.cvgmerch.lv", {autoConnect: false, path: "/client", transports: ['websocket']})
    }
    let el;

    socket.on("connect", (data) => {
        console.log("connection")
        debugMessage("klientam izdevās pievienoties serverim")
        socket.emit("connectioninfo", "client")
    })

    socket.on("controllerStatus", (data) => {
        console.log(data)
    })

    socket.on("lightUpdate", (data) => {
        const prevState = $lightData
        data.forEach(light => {
            prevState[light[0]] = {r: light[1][0], g: light[1][2], b: light[1][2]}
        })
        renderVis(data)

    })


    socket.on("connect_error", (e) => {
        debugMessage("klientam neizdevās pievienoties serverim")
    })

    function debugMessage(text) {
        if (!dev) {
            fetch("http://localhost:5173/debug", {method: "POST", body: JSON.stringify({text: text})})
        }
    }

    onMount(() => {
        createScene(el);
        socket.connect()
    });

    let controllData = "";

    function sendData() {
        socket.emit("lightControll", controllData)
    }
</script>
<div class="vis">
    <canvas bind:this={el}></canvas>
</div>
<input type="text" bind:value={controllData}>
<button on:click={sendData}>Send</button>