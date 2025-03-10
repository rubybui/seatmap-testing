import SeatToolkit from "@mezh-hq/react-seat-toolkit";
import "@mezh-hq/react-seat-toolkit/styles";
import seats from "./seats.json";
import texts from "./texts.json";
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
                    text: texts,
                    shapes: [
                        {
                            id: "60a1c8d8-efd1-4506-a5a8-59ef16571836",
                            name: "RectangleHorizontal",
                            x: 117.017578125,
                            y:  -69.24331676483155,
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