import * as THREE from 'three';
import {OrbitControls} from "three/examples/jsm/controls/OrbitControls";
import {chords, lightData} from "./state";

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
    let lightColorData;
    const unsubscribe = lightData.subscribe((value) => (lightColorData = value));
    renderer = new THREE.WebGLRenderer({antialias: true, canvas: el});
    controls = new OrbitControls(camera, renderer.domElement);
    controls.enableZoom = false;
    controls.enablePan = false;
    //controls.minPolarAngle = -90;

    let lightIndex = 0;
    for (const light of chords) {
        const material = new THREE.MeshBasicMaterial({color: 0x000000});

        const cube = new THREE.Mesh(geometry, material);
        cube.position.x = light.x-0.5;
        cube.position.y = light.y-0.5;
        cube.position.z = light.z-0.5;
        cube.scale.x = 0.03;
        cube.scale.y = 0.03;
        cube.scale.z = 0.03;
        // @ts-ignore
        const color = lightColorData[lightIndex];
        cube.material.color.setHSL(map_range(color.r), map_range(color.g), map_range(color.b))
        scene.add(cube)

        lightIndex++;
    }
    resize();
    animate();
};

