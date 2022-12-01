import https from "https";
import {json} from '@sveltejs/kit';
import type {RequestHandler} from './$types';

export const POST: RequestHandler = async ({request}) => {
    //const { text } = await request.json();
    let text = await request.json()
    text = text.text

    function sendMessage() {
        const url = "https://api.telegram.org/bot" + process.env.TG_KEY + "/sendMessage?chat_id=" + process.env.ID + "&text=" + text
        https.get(url)
    }

    sendMessage()
    return json(true);
}