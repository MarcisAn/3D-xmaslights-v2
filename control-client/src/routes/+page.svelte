<script>
    import io from 'socket.io-client'
    import {onMount} from 'svelte';
    import {createScene} from '../lib/scene.ts';
    import "../global.scss"
    import {dev} from '$app/environment';

    //const socket = io("http://localhost:3000", {autoConnect: false})
    let socket;
    if (dev) {
        socket = io("ws://localhost:3000", {autoConnect: false})
    }
    else{
        socket = io("wss://lampinas.cvgmerch.lv/", {autoConnect: false})
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
    function sendData(){
        socket.emit("lightControll", controllData)
    }
</script>
<div class="vis">
    <canvas bind:this={el}></canvas>
</div>
<input type="text" value={controllData}>
<button on:click={sendData}>Send</button>