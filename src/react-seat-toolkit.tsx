import SeatToolkit from "@mezh-hq/react-seat-toolkit";
import "@mezh-hq/react-seat-toolkit/styles";
import seats from "./seats.json";
import { Armchair } from "lucide-react";

const ReactToolKitSeat = () => {

    return (
        <div style={{ width: "1000px", height: "1000px" }}>
            <SeatToolkit
                mode={"designer"}
                data={{
                    name: "Categorized Example",
                    categories: [
                        { id: "b26fffc7-1e54-43b8-8e29-5077541ee637", name: "Standard", color: "#000000", textColor: "#f7f7f7" },
                        { id: "6267c38d-e1ee-433a-9bda-8be0cab0b062", name: "Premium", color: "#ff0000", textColor: "#f7f7f7" },
                        { id: "fe1a1eb0-1f30-4014-ae49-ee8438b720a3", name: "VIP", color: "#e5e5ff", textColor: "#000000" }
                    ],
                    sections: [
                        {
                            id: "1636dd75-ea0a-48d6-b14c-05ac9db08f5c",
                            name: "Section 1",
                            color: "#000000",
                            stroke: "#000000",
                            freeSeating: false
                        },
                        {
                            id: "65dfc91f-f7aa-407a-ae55-b31f1ee3a41c",
                            name: "Section 2",
                            color: "#FF0000",
                            stroke: "#FF0000",
                            freeSeating: false
                        },
                        {
                            id: "6975d973-5a37-4490-bf13-85c156cbb6b3",
                            name: "Section 3",
                            color: "#0000FF",
                            stroke: "#0000FF",
                            freeSeating: false
                        }
                    ],
                    seats: seats ,
                    text: [
                        {
                            "id": "116a57ac-9bc2-4f0c-a9fc-e1a57448bda7",
                            "x": 481.1094970703125,
                            "y": 93.39669311523437,
                            "label": "STAGE",
                            "fontSize": 35,
                            "fontWeight": 200,
                            "letterSpacing": 5,
                            "color": "#ffffff",
                            "embraceOffset": false,
                            "rotation": 0
                        },
                        {
                            "id": "5fbe906b-3f2b-4537-9dec-f0d29f10c8a8",
                            "x": 528.3535459175631,
                            "y": 224.05520045184514,
                            "label": "A",
                            "fontSize": 35,
                            "fontWeight": 200,
                            "letterSpacing": 3,
                            "color": "#000000",
                            "embraceOffset": false,
                            "rotation": 0
                        },
                        {
                            "id": "345f6da8-0679-46f7-8826-66a3c03888fc",
                            "x": 528.3535459175631,
                            "y": 267.460260276369,
                            "label": "B",
                            "fontSize": 35,
                            "fontWeight": 200,
                            "letterSpacing": 3,
                            "color": "#000000",
                            "embraceOffset": false,
                            "rotation": 0
                        },
                        {
                            "id": "aabd4361-106b-4b44-9125-4d99c831dfc7",
                            "x": 528.3535459175631,
                            "y": 306.3751414983559,
                            "label": "C",
                            "fontSize": 35,
                            "fontWeight": 200,
                            "letterSpacing": 3,
                            "color": "#000000",
                            "embraceOffset": false,
                            "rotation": 0
                        },
                        {
                            "id": "c7460dc4-2fe6-4d94-b083-244128806afb",
                            "x": 528.3535459175631,
                            "y": 345.29002272034285,
                            "label": "D",
                            "fontSize": 35,
                            "fontWeight": 200,
                            "letterSpacing": 3,
                            "color": "#000000",
                            "embraceOffset": false,
                            "rotation": 0
                        },
                        {
                            "id": "d1e10ba1-7d1d-486a-bc43-b9eca7dc272e",
                            "x": 528.3535459175631,
                            "y": 386.4499932435982,
                            "label": "E",
                            "fontSize": 35,
                            "fontWeight": 200,
                            "letterSpacing": 3,
                            "color": "#000000",
                            "embraceOffset": false,
                            "rotation": 0
                        },
                        {
                            "id": "be3acc20-f4dc-4546-8fc5-080b593b146e",
                            "x": 528.3535459175631,
                            "y": 425.3648744655852,
                            "label": "F",
                            "fontSize": 35,
                            "fontWeight": 200,
                            "letterSpacing": 3,
                            "color": "#000000",
                            "embraceOffset": false,
                            "rotation": 0
                        },
                        {
                            "id": "7d152956-7c75-4e9c-bdf5-ec504c79e82a",
                            "x": 528.3535459175631,
                            "y": 467.27320808926345,
                            "label": "G",
                            "fontSize": 35,
                            "fontWeight": 200,
                            "letterSpacing": 3,
                            "color": "#000000",
                            "embraceOffset": false,
                            "rotation": 0
                        },
                        {
                            "id": "c84c6f4b-a8a0-4df8-a872-912bc72e7081",
                            "x": 528.3535459175631,
                            "y": 506.18808931125034,
                            "label": "H",
                            "fontSize": 35,
                            "fontWeight": 200,
                            "letterSpacing": 3,
                            "color": "#000000",
                            "embraceOffset": false,
                            "rotation": 0
                        },
                        {
                            "id": "adb97ee0-9d84-4b33-b349-b7241b767c10",
                            "x": 528.3535459175631,
                            "y": 546.599696734083,
                            "label": "I",
                            "fontSize": 35,
                            "fontWeight": 200,
                            "letterSpacing": 3,
                            "color": "#000000",
                            "embraceOffset": false,
                            "rotation": 0
                        },
                        {
                            "id": "5bc66365-4e61-4285-8994-1d995913f666",
                            "x": 528.3535459175631,
                            "y": 586.2629410564927,
                            "label": "J",
                            "fontSize": 35,
                            "fontWeight": 200,
                            "letterSpacing": 3,
                            "color": "#000000",
                            "embraceOffset": false,
                            "rotation": 0
                        },
                        {
                            "id": "5dd4c2e3-25fd-47b9-8940-811b0c670a34",
                            "x": 528.3535459175631,
                            "y": 626.6745484793253,
                            "label": "K",
                            "fontSize": 35,
                            "fontWeight": 200,
                            "letterSpacing": 3,
                            "color": "#000000",
                            "embraceOffset": false,
                            "rotation": 0
                        }
                    ],
                    shapes: [
                        {
                            id: "60a1c8d8-efd1-4506-a5a8-59ef16571836",
                            name: "RectangleHorizontal",
                            x:-23.00061798095703,
                            y:  33.35831665039062,
                            width: 1100,
                            height: 100,
                            rx: 10,
                            color: "#000000",
                            stroke: "#000000"
                        }
                    ],
                    polylines: [],
                    images: [],
                    workspace: { initialViewBoxScale: 0.605909115101895, initialViewBoxScaleForWidth: 1386, visibilityOffset: 0 }

                }}
                options={{
                    shapes: {
                        icons: [
                            Armchair
                        ],
                        overrideDefaultIconset: true
                    }
                }}
            />
        </div>);
};
export default ReactToolKitSeat;