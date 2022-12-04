import * as THREE from 'three';
import {OrbitControls} from "three/examples/jsm/controls/OrbitControls";
import {lightData} from "./state";
import chords from "../../../chords.json"

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(30, 1, 0.1, 1000);
const geometry = new THREE.BoxGeometry();
let renderer: THREE.WebGLRenderer;
let controls: OrbitControls;

camera.position.z = 5;


const animate = () => {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
    controls.update();
};

const resize = () => {
    renderer.setSize(300, 300);
    camera.aspect = 1;
    camera.updateProjectionMatrix();
};
function map_range(value: number) {
    return 0 + (1 - 0) * (value - 0) / (255 - 0);
}
export const createScene = (el: any) => {
    renderer = new THREE.WebGLRenderer({antialias: true, canvas: el});
    controls = new OrbitControls(camera, renderer.domElement);
    controls.enableZoom = false;
    controls.enablePan = false;
    //controls.minPolarAngle = -90;
    let lightIndex = 0;
    for (const light of chords) {
        const material = new THREE.MeshBasicMaterial({color: 0x000000});

        const cube = new THREE.Mesh(geometry, material);
        cube.position.x = light.x/900;
        cube.position.z = light.y/900;
        cube.position.y = light.z/900;
        cube.scale.x = 0.015;
        cube.scale.y = 0.015;
        cube.scale.z = 0.015;
        // @ts-ignore
        try {
            cube.material.color.setRGB(255,0,0)
            cube.name = lightIndex.toString()
            // @ts-ignore
            cube.changeColor = ((r: number, g: number, b: number) => {
                cube.material.color.setRGB(r,g,b)
            })
            scene.add(cube)
        }
        catch (e) {
            console.log(e)
        }
        lightIndex += 1;
    }

    resize();
    animate();
};

export async function renderVis(data:any){
    console.log(data)
    data.forEach((light: string[]) =>{
        const obj = scene.getObjectByName(light[0].toString());
        // @ts-ignore
        obj.changeColor(light[1][0],light[1][1],light[1][2])
    })
    //console.log(lightColorData)
}
